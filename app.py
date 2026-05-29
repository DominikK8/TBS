from flask import Flask, render_template, jsonify, request, session
from TBS import GameState
from Rooms import ROOMS
from main import VALID_DIRECTIONS, START_ROOM, normalize_dir, current_items_list, current_items_list_enumerate
import random
import text
from Items import ALL_ITEMS

app = Flask(__name__)
app.secret_key = 'secret-key'

@app.route('/')
def tbs():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    # Session komplett zurücksetzen
    session['current_room_id'] = START_ROOM
    session['flags'] = []
    session['dialog'] = None
    current_room = ROOMS[START_ROOM]
    output = [
        text.WELCOME,
        f"== {current_room.desc} ==",
        current_room.ldesc
    ]
    return jsonify(output=output)

@app.route('/eingabe', methods=['POST'])
def eingabe():
    data = request.json
    command = data.get('cmd', '').strip()
    current_room_id = session.get('current_room_id', START_ROOM)
    current_room = ROOMS[current_room_id]
    flags = set(session.get('flags', []))
    state = GameState(flags=flags)
    dialog = session.get('dialog', None)
    output = []

    # Spieler ist im j/n Dialog (blockierter Ausgang entdeckt)
    if dialog == "item_choice":
        if command.lower() in ("j", "ja"):
            current_items = current_items_list(state)
            if not current_items:
                output.append(text.NO_ITEMS)
                session['dialog'] = None
            else:
                # Itemliste ausgeben, Dialog-Zustand wechseln
                for line in current_items_list_enumerate(current_items):
                    output.append(line)
                output.append(text.ITEM_CHOICE)
                session['dialog'] = 'item_select'
        elif command.lower() in ("n", "nein"):
            output.append(text.LEAVE_DIALOG)
            session['dialog'] = None
        else:
            output.append(text.DIALOG_OPTIONS)
        
        session['flags'] = list(state.flags)
        return jsonify(output=output)

    # auswahl aus Liste
    elif dialog == "item_select":
        blocker_flag = session.get('blocker_flag', None)
        current_items = current_items_list(state)

        if command.lower() in ("z", "zurück", "zurueck"):
            output.append(text.LEAVE_DIALOG)
            session['dialog'] = None

        elif command.isdigit():
            index = int(command) - 1
            if not (0 <= index < len(current_items)):
                output.append(f"'{command}' {text.NOT_IN_CHOICE}")
            else:
                chosen_item = current_items[index]
                output.append(f"{text.GIVE_ITEM} {chosen_item.name}")
                output.append(chosen_item.item_reaktion)
                # Item als benutzt markieren
                if chosen_item.used_flag:
                    state.flags.add(chosen_item.used_flag)
                # Löst das Item die Blockade?
                if blocker_flag and blocker_flag in chosen_item.solves:
                    state.flags.add(blocker_flag)
                    output.append(text.REDBUG_UNBLOCK)
                    session['dialog'] = None
                else:
                    output.append(text.REDBUG_STAYS)
                    # Aktualisierte Liste anzeigen
                    current_items = current_items_list(state)
                    for line in current_items_list_enumerate(current_items):
                        output.append(line)
        else:
            output.append(text.ITEM_CHOICE)

        session['flags'] = list(state.flags)
        return jsonify(output=output)

    parts = command.split()
    if not parts:
        return jsonify(output=[])
    head = parts[0].lower()

    if head in ("look", "l", "umschauen", "u"):
        output.append(current_room.ldesc)
        # Item im Raum
        itemtext = current_room.find_item(state)
        if itemtext:
            output.append(itemtext)
        # Blockierter Ausgang
        blocker_flag = current_room.exit_blocked_flag(state)
        blocked_msg = current_room.exit_blocked_message(state)
        if blocked_msg:
            output.append(blocked_msg)
            # Dialog starten, blocker_flag merken
            session['dialog'] = 'item_choice'
            session['blocker_flag'] = blocker_flag

    elif head in ("help", "hilfe", "h", "?"):
        output.append(text.HELP)

    elif head in ("quit", "exit", "q"):
        session.clear()
        session['current_room_id'] = START_ROOM
        session['flags'] = []
        session['dialog'] = None
        output.append(text.QUIT_BROWSER)
        output.append(text.RESTART_BROWSER)
        current_room = ROOMS[START_ROOM]
        output.append(f"== {current_room.desc} ==")

    else:
        if head in ("go", "gehe") and len(parts) >= 2:
            direction = normalize_dir(parts[1])
        elif head in ("go", "gehe"):
            output.append(text.GO_WHERE)
            session['flags'] = list(state.flags)
            return jsonify(output=output)
        else:
            direction = normalize_dir(parts[0])

        if direction not in VALID_DIRECTIONS:
            output.append(text.INVALID_COMMAND1 + f" '{head}' " + text.INVALID_COMMAND2)
        else:
            result, status = current_room.try_move(state, direction)
            if status == "OK":
                current_room_id = result
                current_room = ROOMS[current_room_id]
                output.append(f"== {current_room.desc} ==")
                if current_room.action:
                    current_room.action(state, current_room, command)
            elif status == "BLOCKED":
                output.append(result.blocked_msg_general)
            else:
                output.append(random.choice(text.WALL))

    session['current_room_id'] = current_room_id
    session['flags'] = list(state.flags)
    return jsonify(output=output)

if __name__ == '__main__':
    app.run(debug=True)