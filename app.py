from flask import Flask, render_template, jsonify, request, session
from TBS import GameState
from Rooms import ROOMS
from main import DIR_ALIASES, VALID_DIRECTIONS, START_ROOM, WALL, show_room, looking_room, normalize_dir, game_loop
import random
import text 

app = Flask(__name__)
app.secret_key = 'secret-key'
@app.route('/')
def tbs():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    session['current_room_id'] = START_ROOM
    current_room = ROOMS[START_ROOM]
    output = [text.WELCOME,
        f"== {current_room.desc} ==",
        current_room.ldesc
    ]
    return jsonify(output=output)

@app.route('/eingabe', methods=['POST'] )
def eingabe():
    data = request.json
    command = data.get('cmd', '')
    current_room_id = session.get('current_room_id', 'MIDDLE')
    current_room = ROOMS[current_room_id]
    parts = command.split()
    head = parts[0].lower()
    output = []

    if head in ("look", "l", "umschauen", "u"):
        output.append(current_room.ldesc)
        session["current_room_id"] = current_room_id
        return jsonify(output=output)

    elif head in ("help", "hilfe", "h", "?"):
            output.append(text.HELP)
            session["current_room_id"] = current_room_id
            return jsonify(output=output)

    elif head in ("quit", "exit", "q"):
        session.pop('current_room_id', None)
        output.append(text.QUIT_BROWSER)
        # Neustart
        session['current_room_id'] = START_ROOM
        current_room = ROOMS[START_ROOM]
        output.append(text.RESTART_BROWSER)
        output.append(f"== {current_room.desc} ==")
        return jsonify(output=output)

    else:
        if head in ("go", "gehe") and len(parts) >= 2:
            direction = normalize_dir(parts[1])
        else:
            direction = normalize_dir(parts[0]) 

        if direction not in VALID_DIRECTIONS: 
            output.append(text.INVALID_COMMAND1 + f" '{head}' " + text.INVALID_COMMAND2)
        else:      
            target = current_room.try_move(GameState(), direction)
            if target and target in ROOMS:
                current_room_id = target
                current_room = ROOMS[current_room_id]
                output.append(f"== {current_room.desc} ==")
                if current_room.action:
                    current_room.action(GameState(), current_room, command)
                    session["current_room_id"] = current_room_id
                    return jsonify(output=output)
            else:
                output.append(random.choice(WALL)) 
            
        session["current_room_id"] = current_room_id
        return jsonify(output=output)

if __name__ == '__main__':
     app.run()