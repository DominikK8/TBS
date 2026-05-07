from flask import Flask, render_template, jsonify 

app = Flask(__name__)

@app.route('/')
def tbs():
    return render_template('index.html')

@app.route('/eingabe', methods=['POST'] )
def eingabe():
    return jsonify(output=["== ROOM1_3 ==", "Du bist in einer Kurve...", "[Exits: SOUTH, WEST]"])
   

if __name__ == '__main__':
    app.run()