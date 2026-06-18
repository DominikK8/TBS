# ---------------------------------------------------------
# =========================================================
# TEXTDEFINITONS
# =========================================================
# ---------------------------------------------------------

# =========================================================
# GENERAL
# =========================================================

WELCOME = ( "\nDu bist mit einem Kompass in der Hand mitten in einem Labyrinth gelandet.\n" 
            "Es ist kalt, modrig, feucht und vor allem dunkel.\n" 
            "Du kannst nichts sehen, nichtmal die Hände vor deinen Augen,\n"
            "aber da ist ein Labyrinth, soviel musst du wissen,\n"
            "und du musst einen weg herausfinden.\n"
            "Es wäre eine Gute Idee sich umzuschauen, oder nach Hilfe zu Fragen.\n"
            "Viel Glück!")

GAME_OVER = ("Spiel beenden?\n"
             "Drücke 'Q' zum Beenden, 'Z' für zurück und 'N' für ein neues Spiel.")

WON = ("\nDu hast einen Ausgang gefunden! Herzlichen Glückwunsch!\n\n"
       "Drücke 'Q' zum Beenden oder 'N' für ein neues Spiel.")

GAME_OVER_BROWSER = ("Du hast einen Ausgang gefunden. Herzlichen Glückwunsch!\n"
                     "Drücke 'N' für ein neues Spiel.")

NEW_GAME = "Neues Spiel startet..."

END_GAME_INPUT_REPETITION = "Bitte 'Q', 'Z' oder 'N' eingeben."

END_GAME_INPUT_REPETITION_WON = "Bitte 'Q' oder 'N' eingeben."

HELP = ("Befehle: \n"
        "'umschauen' oder 'u' um ein Beschreibung des Abschnitts zu erhalten, in dem du dich befindest.\n \n"
        "gehe 'norden'; 'westen'; 'süden'; 'osten' oder gehe 'n'; 'w'; 's'; 'o' um dich zu bewegen. \n \n"
        "'inv', 'inventory' oder 'i' um dein Inventar anzuzeigen.\n\n"
        "'quit' oder 'q' um das Spiel zu beenden.")

INVENTORY_HEADER = "Inventar:"
INVENTORY_EMPTY = "Du hast derzeit keine Gegenstände."

INVALID_COMMAND1 = "Ich kenne die Bedeutung von"
# zwischendrin wird head in der main.py-Ausgabe eingesetzt
INVALID_COMMAND2 = "nicht."

GO_WHERE = "Wohin möchtest du gehen? Bitte gib eine Richtung an (z.B. 'gehe norden')."

WALL = ["**BOOF** Du läufst vor eine Wand!", 
        "BÄM! Du bist gegen eine Wand gelaufen!", 
        "Du stößt gegen eine Wand. Autsch!", 
        "Puh, du warst dieses Mal ganz vorsichtig und hast rechtzeitig gesehen, dass da eine Wand ist.",
        "Verd***t, genau mit dem großen Zeh zuerst mitten im Schritt gegen eine Wand.",
        "Tränen schießen dir in die Augen, eine Wand hat dich und vor allem deine Nase abrupt gebremst."]

QUIT_BROWSER = ("Das Labyrinth verschluckt dich erneut...")

QUIT = ("Du hast das Spiel beendet, so wirst du den Ausgang niemals finden.\n"
        "Mach's gut!")

END = ("Spiel Ende. Danke fürs Spielen!")

RESTART_BROWSER = ("Das war keine gute Entscheidung...")

NO_EXITS = ("Es gibt keine Ausgänge.")

ONE_EXIT = ["Es gibt einen Weg nach .",
            "Du kannst nach .",
            "Es führt ein Weg nach .",
            "{} ist der einzige Weg, den du gehen kannst."]

TWO_EXITS = ["Es gibt Wege nach {} und {}.",
              "Du kannst nach {} und {} gehen.",
              "Es führen Wege nach {} und {}.",
              "Es gibt zwei Wege, nach {} und {}.",
              "Es führen zwei Wege, nach {} und {}."]

THREE_EXITS = ["Es gibt Wege nach {}, {} und {}.",
                "Du kannst nach {}, {} und {} gehen.",
                "Es führen Wege nach {}, {} und {}.",
                "Es gibt drei Wege, nach {}, {} und {}.",
                "Es führen drei Wege, nach {}, {} und {}."]

FOUR_EXITS = ["Es gibt Wege nach {}, {}, {} und {}.",
              "Du kannst nach {}, {}, {} und {} gehen.",
              "Es führen Wege nach {}, {}, {} und {}.",
              "Es gibt vier Wege, nach {}, {}, {} und {}.",
              "Es führen vier Wege, nach {}, {}, {} und {}."]

# =========================================================
# BLOCKED EXITS
# =========================================================

NO_ITEMS = ("Du hast nichts, das du geben könntest.")

ITEM_CHOICE = ("Wähle ein Item (Zahl) oder 'z' für zurück.")

LEAVE_DIALOG = ("Du wendest dich ab.")

NOT_IN_CHOICE = ("ist nicht in der Auswahl.")

GIVE_ITEM = ("Du gibst der Gestalt:")

REDBUCK_BLOCKED_MSG = ("\nEine große Gestalt mit bunter Jacke, Brille und hochstehenden kurzen Haaren versperrt den Weg nach Osten.\nSie sagt: Buongiorno, äh, ich meine: sind noch alle da?\nHast du etwas für mich?")
REDBUCK_BLOCKED_MSG_GENERAL = ("Eine Gestalt versperrt den Weg.")
REDBUG_UNBLOCK = ("Die Gestalt verschwindet. Der Weg ist frei.")
REDBUG_STAYS = ("Die Gestalt rührt sich nicht und verperrt den Weg nach wie vor.")

DIALOG_OPTIONS = ("Antworte mit ja/nein")

# =========================================================
# ITEMS
# =========================================================

MATCHBOX_NAME = ("Matchbox-Auto")
MATCHBOX_DESC = ("Du findest ein Matchbox-Auto und nimmst es mit.")
MATCHBOX_REACT = ("Dieses Modell suche ich schon seit ich ein kleiner Mann war.\nIch werde es sofort meiner Sammlung hinzufügen.")

AIDA_NAME = ("AIDA Modell")
AIDA_DESC = ("In der Wand steckt etwas, ein kleines Schiff,\nes stand mal etwas darauf, irgendwas mit A..., du packst es ein.")
AIDA_REACT = ("Oh, ein kleines Kreuzfahrtschiff, wie schön,\nich mag Kreuzfahrten, ich behalte es.")

DOOR_NAME = ("Tür eines Straßen-Sicherungs-Kastens")
DOOR_DESC = ("An der Wand lehnt eine Tür von einem Straßen-Sicherungs-Kasten,\ndie Schaniere sind Defekt, du steckst sie trotzdem ein.")
DOOR_REACT = ("Ha, das erinnert mich an die doofe EAM, die meint, dass sie mich abziehen könnte.")

KEY_NAME = ("Schlüsselbund")
KEY_DESC = ("Du findest einen Schlüsselbund mit einem herausziehbaren Band.")
KEY_REACT = ("Du hast meinen Schlüssel gefunden, danke, den habe ich schon gesucht.")

DOCUMENT_NAME = ("Dokument")
DOCUMENT_DESC = ("Es liegen Blätter auf dem Boden, darauf sind unterstrichene Überschriften zu sehen.\nDu steckst es ein.")
DOCUMENT_REACT = ("Man unterschreicht keine Überschriften mehr, seit Jahrzenten nicht,\nDie Gestalt wird zornig.")

# ---------------------------------------------------------
# =========================================================
# ROOMS
# =========================================================
# ---------------------------------------------------------


# =========================================================
# MIDDLE
# =========================================================

MIDDLE_DESC = "Mitte"
MIDDLE_LDESC = (
    "Geräusche werden geschluckt,\n"
    "als hätte der Ort kein Interesse daran, sie weiterzutragen. \n"
    "Du kannst es kaum erkennen, aber nach Osten und nach Süden vermutest du Wege, die weiterführen könnten."
)

# =========================================================
# EBENE 1 – Myzel / Zersetzung
# =========================================================

ROOM1_1_DESC = "Rippengewölbe der Hyphen"
ROOM1_1_LDESC = (
    "Über dir spannt sich ein rippenartiges Gewölbe.\n"
)

ROOM1_2_DESC = "Fugenpassage mit Biofilm"
ROOM1_2_LDESC = (
    "Die Passage endet abrupt. Du fühlst glatte Fugen, die sich in der Dunkelheit über die Wände ziehen."
    "Du fährst die Fugen entlang und spürst plötzlich Kerben. \n"
    "Du tastest ruhig an den Kerben entlang. Es scheinen Buchstaben zu sein. \n"
    "Konzentriert ertasteste du sie. \n"
    "J...U...dann folgt...S...dann...T...I...\n"
    "Jetzt bist du dir sicher...da steht eindeutig 'KERSTIN'."
)

ROOM1_3_DESC = "Nische der Sporen"
ROOM1_3_LDESC = (
    "Die Nische zwingt dich näher an die Wand. Du schmeckst feinen Staub, der in der Luft liegt.\n"
)

ROOM1_4_DESC = "Gang der Gärung"
ROOM1_4_LDESC = (
    "Der Gang teilt sich hier. Es fällt dir schwer das Gleichgewicht zu halten,\n"
    "der Boden ist uneben und es knirscht unter deinen Füßen. \n"
)

ROOM1_5_DESC = "Winkel des Schimmelflaums"
ROOM1_5_LDESC = (
    "Du fährst in der Dunkelheit die Wand ab und fühlst matten Flaum. \n"
    "Nach Norden führt der Weg zurück. \n"
)

ROOM1_6_DESC = "Bruchkante der Zersetzer"
ROOM1_6_LDESC = (
    "Es ist duster, deine Augen wollen sich an die Dunkelheit gewöhnen, \n"
    "aber du siehst trotzdem nur schemenhaft."
)

ROOM1_7_DESC = "Weg der Myzelspur"
ROOM1_7_LDESC = (
    "Mit dem Fuß spürst du Rillen im Boden, denen man folgen könnte \n"
    "Aber sie enden im Nichts."
)

ROOM1_8_DESC = "Echokammer des Faulholzes"
ROOM1_8_LDESC = (
    "Jeder Schritt hallt dumpf zurück, als würde der Raum ihn behalten wollen. \n"
)

# =========================================================
# EBENE 2 – Chitin / Larven
# =========================================================

ROOM2_1_DESC = "Flur der Chitinspur"
ROOM2_1_LDESC = (
    "Der Flur wirkt härter, geschlossener, fast gepanzert. \n"
    "Nach Süden führt der Weg weiter durch feste Strukturen. \n"
)

ROOM2_2_DESC = "Hof der Fühler"
ROOM2_2_LDESC = (
    "Der Hof ist klein und abgeschlossen. Auf dem Boden liegt etwas Kaputtes, \n"
    "daneben liegt ein Zettel, auf dem steht: Das war schon so, Grüße Maxi"
    "Ansonsten gibt es hier nichts zu sehen."
)

ROOM2_3_DESC = "Nische der Larvenhaut"
ROOM2_3_LDESC = (
    "Dünne Schichten liegen übereinander, wie abgestreift. \n"
    "Wege führen nach Osten und nach Westen. \n"
)

ROOM2_4_DESC = "Passage des Kokons"
ROOM2_4_LDESC = (
    "Die Passage ist gedämpft, fast umhüllt. \n"
    "Sie setzt sich nach Westen und nach Osten fort. \n"
)

ROOM2_5_DESC = "Steg der Tarsen"
ROOM2_5_LDESC = (
    "Der Steg verbindet mehrere Richtungen, schmal und fest zugleich. \n"
    "Nach Süden bleibt alles gedrungen, nach Westen führt der Weg zurück. \n"
)

ROOM2_6_DESC = "Gewölbe der Facetten"
ROOM2_6_LDESC = (
    "Das Gewölbe schließt sich hier vollständig. \n"
    "Die Dunkelheit ist unmittelbar und undurchdringlich. \n"
    "In der Ecke liegt ein Stein, komisch..."
    "egal, du musst umkehren."
)

ROOM2_7_DESC = "Gang der Puppenruhe"
ROOM2_7_LDESC = (
    "Der Gang endet still und unbewegt. \n"
    "Dich überkommt ein Gefühl des rapiden Alterns.\n"
    "Du fühlst dich als wäre das wichtigste im Leben ausreichend Schlaf zu bekommen. \n"
    "Du schüttelst dich und kommst wieder zu dir. \n"
    "Du bist wohl kurz weggenickt, karim ja mal passieren. \n"
    "Nach Süden führt der einzige Weg zurück."
)

ROOM2_8_DESC = "Hallwinkel der Panzerfuge"
ROOM2_8_LDESC = (
    "Die Wände stoßen in harten Winkeln aufeinander, ein leiser Hall liegt in der Luft. \n"
)

ROOM2_9_DESC = "Schwelle der Schwarmspur"
ROOM2_9_LDESC = (
    "Der Raum knickt ab, feine Spuren verlaufen dicht nebeneinander. \n"
)

ROOM2_10_DESC = "Schacht der Häutung"
ROOM2_10_LDESC = (
    "Der Schacht zieht sich gerade durch das Material. \n"
)

ROOM2_11_DESC = "Korridor der Antennenrillen"
ROOM2_11_LDESC = (
    "Feine Rillen ziehen sich längs über die Wände, als hätten sie etwas ertastet. \n"
)

ROOM2_12_DESC = "Engpass der Ocelli"
ROOM2_12_LDESC = (
    "Der Engpass zwingt dich dicht an die Wand. \n"
    "Nach Osten bleibt es schmal. \n"
)

ROOM2_13_DESC = "Durchlass der Segmentfuge"
ROOM2_13_LDESC = (
    "Der Durchlass wirkt wie ein Gelenk im Raum. \n"
    "Nach Norden bleibt alles fest gefügt. \n"
)

ROOM2_14_DESC = "Kammer der Mandibeln"
ROOM2_14_LDESC = (
    "Die Kammer ist kantig und geschlossen, als könnte sie sich jederzeit zusammenziehen. \n"
    "Wege führen nach Norden und nach Süden. \n"
)

ROOM2_15_DESC = "Bucht der Flügeldecken"
ROOM2_15_LDESC = (
    "Überlappende Flächen bilden eine langgezogene Bucht. \n"
)

ROOM2_16_DESC = "Rippe der Tracheenluft"
ROOM2_16_LDESC = (
    "Rippenartige Strukturen ziehen sich durch den Raum. \n"
)

# =========================================================
# EBENE 3 – Wedel / Schattenblatt
# =========================================================

ROOM3_1_DESC = "Flur der Wedel"
ROOM3_1_LDESC = (
    "Der Flur wirkt weicher in seinen Konturen. \n"
)

ROOM3_2_DESC = "Hof der Rhizome"
ROOM3_2_LDESC = (
    "Der Hof öffnet sich weit, Linien verzweigen sich unter deinen Füßen. \n"
    "Wege führen nach Norden, Süden, Osten und Westen. \n"
)

ROOM3_3_DESC = "Gang der Schattenblätter"
ROOM3_3_LDESC = (
    "Breite Formen legen sich wie Schatten über den Gang. \n"
)

ROOM3_4_DESC = "Kurve der Blattadern"
ROOM3_4_LDESC = (
    "Feine Muster ziehen sich entlang der Wand, als würden sie etwas leiten. \n"
)

ROOM3_5_DESC = "Kurve der Tauhaut"
ROOM3_5_LDESC = (
    "Die Oberfläche wirkt kühl und gespannt. \n"
    "Der Weg setzt sich nach Süden und nach Osten fort."
)

ROOM3_6_DESC = "Spaltung der Spaltöffnungen"
ROOM3_6_LDESC = (
    "Der Raum teilt sich in mehrere Richtungen. \n"
    "Wege öffnen sich nach Norden, nach Osten und nach Westen. \n"
)

ROOM3_7_DESC = "Gang der Knospenruhe"
ROOM3_7_LDESC = (
    "Der Gang liegt ruhig da, als würde er warten. \n"
    "Die Luft ist jetzt manchmal gefüllt von einem leichten Duft, der von Osten zu kommen scheint. \n"
    "Das Licht aus Osten ist stark, fast schon blendend."
)

ROOM3_8_DESC = "Kurve der Blattfalten"
ROOM3_8_LDESC = (
    "Der Weg legt sich in Falten. \n"
)

ROOM3_9_DESC = "Kurve der Wachsschicht"
ROOM3_9_LDESC = (
    "Die Kurve wirkt glatt und abgeschlossen. \n"
    "Grelles Licht fällt von Osten her ein."
)

ROOM3_10_DESC = "Sackgasse der Prothallien"
ROOM3_10_LDESC = (
    "Der Weg endet hier, flach und unscheinbar.\n"
    "An der Wand lehnt ein Stuhl, sieht aus, als wäre er umgekippt. \n"
    "Als du ihn dir genauer ansiehst erkennst du, dass ein großes Skelett kippelnd auf ihm sitzt.\n"
    "Der Geruch von Energy steigt dir in die Nase."
)

ROOM3_11_DESC = "Kammer der Blattstiele"
ROOM3_11_LDESC = (
    "Die Kammer wirkt tragend, als halte sie den Raum zusammen. \n"
    "Die Licht wirkt blass, verwunschen..."
)

ROOM3_12_DESC = "Flur der Zellstruktur"
ROOM3_12_LDESC = (
    "Der Flur ist gleichmäßig gegliedert. \n"
)

ROOM3_13_DESC = "Gang der Wasseradern"
ROOM3_13_LDESC = (
    "Feine Linien ziehen sich wie Adern durch den Boden. \n"
)

ROOM3_14_DESC = "Gang der Schattenränder"
ROOM3_14_LDESC = (
    "Die Ränder des Ganges sind dunkler als sein Zentrum. \n"
    "Ein kalter Luftzug lässt dich frösteln, er tanzt um dich herum,\n"
    "so dass du nicht genau feststellen kannst, aus welcher Richtung er kommt."
)

ROOM3_15_DESC = "Kreuzung der Spaltöffnungen"
ROOM3_15_LDESC = (
    "Die Kreuzung liegt offen vor dir, ohne bevorzugte Richtung. \n"
)

ROOM3_16_DESC = "Kurve der Wurzelhaare"
ROOM3_16_LDESC = (
    "Der Weg knickt sanft ab, feine Strukturen ziehen sich entlang der Wand. \n"
)

ROOM3_17_DESC = "Kurve der Dämmerwedel"
ROOM3_17_LDESC = (
    "Die Kurve wirkt weich und nachgiebig. \n"
)

ROOM3_18_DESC = "Kurve der Blattnerven"
ROOM3_18_LDESC = (
    "Feine Linien bündeln sich und laufen wieder auseinander. \n"
)

ROOM3_19_DESC = "Kurve des Chlorophyllschimmers"
ROOM3_19_LDESC = (
    "Ein matter Schimmer liegt auf den Flächen. \n"
)

ROOM3_20_DESC = "Gang der Blattfalten"
ROOM3_20_LDESC = (
    "Der Gang zieht sich ruhig in die Länge. \n"
)

ROOM3_21_DESC = "Gang der Wachsschicht"
ROOM3_21_LDESC = (
    "Die Oberflächen wirken versiegelt, fast schützend. \n"
)

ROOM3_22_DESC = "Kurve der Knospenruhe"
ROOM3_22_LDESC = (
    "Der Weg biegt ab und verschwindet teilweise aus dem Blick. \n"
    "Die Luft aus Westen wirkt frisch, nicht mehr verbraucht, du kannst alles erkennen, da es es fast schon hell ist."
)

# =========================================================
# EBENE 4 – Pollen / Blüte / Samenflug
# (Texte vorbereitet für bestehende ROOM4-Struktur)
# =========================================================

ROOM4_1_DESC = "Flur des Nektars"
ROOM4_1_LDESC = (
    "Der Flur wirkt offen und weit, als würde er mehr Raum lassen als nötig. \n"
)

ROOM4_2_DESC = "Hof der Pollenfahne"
ROOM4_2_LDESC = (
    "Feine Partikel scheinen in der Luft zu hängen, ohne sich zu setzen. \n"
)

ROOM4_3_DESC = "Passage der Staubfäden"
ROOM4_3_LDESC = (
    "Die Passage ist von feinen Linien durchzogen, die sich kreuzen und lösen. \n"
)

ROOM4_4_DESC = "Steg der Blütenkrone"
ROOM4_4_LDESC = (
    "Der Steg spannt sich sanft durch den Raum, als wäre er Teil einer geöffneten Form. \n"
    "Endlich Licht, du siehst es deutlich, es brennt dir in den Augen. \n"
    "Nachdem sich die Augen an das grelle Licht gewöhnt haben, siehst du, es ist nur ein Loch in der Wand. \n"
    "Es ist zu hoch, du kommst nicht hin, es ist auch zu klein, du kommst nicht durch. \n"
    "Das Licht macht dir Hoffnung, aber es scheint unerreichbar, dir bleibt nichts übrig als nach Westen zurückzugehen."
)

ROOM4_5_DESC = "Gewölbe des Duftes"
ROOM4_5_LDESC = (
    "Der Raum wirkt weit und schwebend, als trüge er mehr als nur Luft. \n"
)

ROOM4_6_DESC = "Gang der Bestäubung"
ROOM4_6_LDESC = (
    "Der Gang ist von feinen Spuren durchzogen, die sich kreuzen und verlieren. \n"
)

ROOM4_7_DESC = "Hallwinkel der Lichtkrone"
ROOM4_7_LDESC = (
    "Der Winkel öffnet sich nach mehreren Seiten, Flächen scheinen das Licht zu sammeln. \n"
)

ROOM4_8_DESC = "Schwelle des Fruchtstands"
ROOM4_8_LDESC = (
    "Der Raum wirkt wie ein Übergang, nichts hier scheint endgültig. \n"
)

ROOM4_9_DESC = "Schacht des Samenflaums"
ROOM4_9_LDESC = (
    "Der Schacht wirkt leicht und offen, als würde er mehr tragen als halten. \n"
)

ROOM4_10_DESC = "Korridor des Griffels"
ROOM4_10_LDESC = (
    "Der Korridor ist langgezogen und klar gegliedert. \n"
)

ROOM4_11_DESC = "Kammer der Narbe"
ROOM4_11_LDESC = (
    "Die Kammer wirkt aufnahmebereit, ruhig und gesammelt. \n"
)

ROOM4_12_DESC = "Durchlass des Fruchtknotens"
ROOM4_12_LDESC = (
    "Der Durchlass ist rundlicher als die übrigen Räume, fast organisch geschlossen. \n"
)

ROOM4_13_DESC = "Bucht der Blütenröhre"
ROOM4_13_LDESC = (
    "Die Bucht zieht sich sanft in die Länge, ohne harte Kanten. \n"
)

ROOM4_14_DESC = "Engpass der Honigspur"
ROOM4_14_LDESC = (
    "Der Raum verengt sich kurz, bleibt aber durchlässig. \n"
)

ROOM4_15_DESC = "Rippe der Pollenkügelchen"
ROOM4_15_LDESC = (
    "Feine, runde Strukturen ziehen sich wie eine Rippe durch den Raum. \n"
    "Du siehst es ganz deutlich...\n"
    "41\n"
    "4...1\n"
    "Dir ist, als würdest du ein Lachen hören.\n"
    "4...1...\n"
    "Dann wird dir klar,...\n"
    "...hier geht es nicht weiter."
)

ROOM4_16_DESC = "Flur der Streufrucht"
ROOM4_16_LDESC = (
    "Der Flur wirkt weit und offen, als würde er Bewegung begünstigen. \n"
)

ROOM4_17_DESC = "Hof der Kapseln"
ROOM4_17_LDESC = (
    "Der Hof öffnet sich ruhig, mehrere Wege treffen hier aufeinander. \n"
)

ROOM4_18_DESC = "Nische der Flügelnüsse"
ROOM4_18_LDESC = (
    "Die Nische ist klein, aber nicht geschlossen, als wäre sie nur ein Rastpunkt. \n"
)

ROOM4_19_DESC = "Passage der Samenflügel"
ROOM4_19_LDESC = (
    "Die Passage wirkt leicht und gerichtet, als hätte sie eine bevorzugte Strömung. \n"
    "Irgenwann einmal war hier mal ein Weg, aber nun liegt hier bis zur Decke Geröll.\n"
    "Du denkst darüber nach, dass ein Lebenslauf und der Euro-Pass doch dasselbe sind."
)

ROOM4_20_DESC = "Steg der Keimruhe"
ROOM4_20_LDESC = (
    "Der Steg liegt ruhig da, fast erwartungsvoll. \n"
)

ROOM4_21_DESC = "Gewölbe der Lichtfenster"
ROOM4_21_LDESC = (
    "Über dir öffnet sich das Gewölbe in mehreren hellen Flächen. \n"
)

ROOM4_22_DESC = "Gang der Blütenstände"
ROOM4_22_LDESC = (
    "Der Gang ist von aufstrebenden Formen gesäumt. \n"
)

ROOM4_23_DESC = "Hallwinkel der Duftwolke"
ROOM4_23_LDESC = (
    "Der Winkel wirkt weich und ausgedehnt, als würde sich hier etwas sammeln. \n"
)

ROOM4_24_DESC = "Schwelle der Reife"
ROOM4_24_LDESC = (
    "Der Raum wirkt abgeschlossen und zugleich bereit. \n"
)

ROOM4_25_DESC = "Schacht der Sonnenflecken"
ROOM4_25_LDESC = (
    "Der Schacht ist unregelmäßig erhellt, als fiele Licht nur stellenweise ein. \n"
)

ROOM4_26_DESC = "Korridor der Farbzeichen"
ROOM4_26_LDESC = (
    "Der Korridor trägt feine Variationen in seinen Flächen. \n"
    "Du schaust dir dieses Spiel der Variationen eine Weile an,\n"
    "dann stellst du fest, dass es hier nicht weitergeht."
)