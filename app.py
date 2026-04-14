from flask import Flask, jsonify

app = Flask(__name__)

action_queue = []

@app.route('/action/<action>')
def add_action(action):
    action_queue.append(action)
    print("ACCION RECIBIDA:", action)
    return "OK"

@app.route('/getAction')
def get_action():
    if len(action_queue) > 0:
        action = action_queue.pop(0)
        print("ENVIANDO:", action)
        return jsonify({"action": action})

    return jsonify({"action": None})

if __name__ == "__main__":
    print("SERVER INICIADO")
    app.run(host="0.0.0.0", port=10000)
