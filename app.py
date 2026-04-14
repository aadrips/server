import os
from flask import Flask, jsonify

app = Flask(__name__)

action_queue = []

@app.route('/action/<action>')
def add_action(action):
    action_queue.append(action)
    print("ACCION:", action)
    return "OK"

@app.route('/getAction')
def get_action():
    if action_queue:
        return jsonify({"action": action_queue.pop(0)})
    return jsonify({"action": None})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print("SERVER ON PORT", port)
    app.run(host="0.0.0.0", port=port)
