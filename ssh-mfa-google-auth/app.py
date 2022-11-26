import json, socket, subprocess
from pathlib import Path
from functools import wraps
from flask import Flask, request, jsonify, abort

storage_auth = '/opt/google_auth'
storage_qr = '/opt/google_qr'
app = Flask(__name__)

def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        with open('api.key', 'r') as apikey:
            key=apikey.read().replace('\n', '')
        if request.headers.get('x-api-key') and request.headers.get('x-api-key') == key:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

@app.route('/api/create_auth/<username>', methods=['POST'])
@require_appkey
def create_auth(username):
    user_check = Path(f"{storage_auth}/{username}_auth")
    if user_check.is_file():
        abort(400)
    else:
        generate = subprocess.check_output(f"google-authenticator -q -t -d -f -r 3 -R 30 -w 3 --secret={storage_auth}/{username}_auth", shell=True)
        return username

@app.route('/api/generate_qr/<username>', methods=['POST'])
@require_appkey
def generate_qr(username):
    secret = subprocess.check_output(f"cat {storage_auth}/{username}_auth|head -1", shell=True)
    qr = subprocess.check_output(f'qrencode -o- -d 300 -s 10 "otpauth://totp/{username}?secret={secret}&issuer=PGP-Bastion" > {storage_qr}/{username}.png', shell=True)
    return secret

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug="true")
