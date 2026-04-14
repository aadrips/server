from flask import Flask, jsonify, request
import os

app = Flask(__name__)

action_queue = []

@app.route('/')
def home():
    print("PING HOME")
    return "OK SERVER RUNNING"

@app.route('/action/<action>')
def add_action(action):
    print("🔥 ACTION RECIBIDA:", action)
    action_queue.append(action)
    return {"status": "ok", "action": action}

@app.route('/getAction')
def get_action():
    print("📡 ROBLOX PIDE ACTION")

    if action_queue:
        action = action_queue.pop(0)
        print("➡ ENVIANDO:", action)
        return jsonify({"action": action})

    return jsonify({"action": None})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    print("🚀 SERVER STARTED ON PORT", port)
    app.run(host="0.0.0.0", port=port)
