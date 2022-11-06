import json, socket, datetime
from flask import Flask, request, jsonify


app = Flask(__name__)

print(socket.gethostname())

@app.route('/api', methods=['GET'])
def list_all():
    return jsonify({'hostname': socket.gethostname(),'timestamp': datetime.datetime.now()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
