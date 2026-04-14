from flask import Flask, jsonify

app = Flask(__name__)

action_queue = []

@app.route('/action/<name>')
def action(name):
    action_queue.append(name)
    print("Acción:", name)
    return "OK"

@app.route('/getAction')
def get_action():
    if action_queue:
        return jsonify({"action": action_queue.pop(0)})
    return jsonify({"action": None})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)