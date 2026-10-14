import os
import urllib.request
import json
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)

SERVER_IP = "pace.mywire.org"

def get_minecraft_status():
    """Fragt den echten Server-Status über die mcstatus.io API ab"""
    try:
        url = f"https://api.mcstatus.io/v2/status/java/{SERVER_IP}"
        req = urllib.request.Request(url, headers={'User-Agent': 'KiiviSMP-Web'})
        with urllib.request.urlopen(req, timeout=2) as response:
            data = json.loads(response.read().decode())
            if data.get("online"):
                players_online = data["players"]["online"]
                players_max = data["players"]["max"]
                return {"online": True, "players": f"({players_online}/{players_max} Spieler)"}
    except Exception:
        pass
    return {"online": False, "players": "(Offline)"}

def get_background():
    """Prüft automatisch, ob MP4 oder MP3 im static-Ordner liegt"""
    if os.path.exists(os.path.join('static', 'background.mp4')):
        return {'type': 'video', 'filename': 'background.mp4'}
    elif os.path.exists(os.path.join('static', 'background.mp3')):
        return {'type': 'audio', 'filename': 'background.mp3'}
    return {'type': 'video', 'filename': 'background.mp4'}

@app.route('/')
def index():
    bg = get_background()
    status = get_minecraft_status()
    return render_template('index.html', bg=bg, status=status, server_ip=SERVER_IP)

@app.route('/about')
def about():
    return render_template('about.html', bg=get_background())

@app.route('/plugins')
def plugins():
    return render_template('plugins.html', bg=get_background())

@app.route('/team')
def team():
    return render_template('team.html', bg=get_background())

@app.route('/pakete')
def pakete():
    return render_template('pakete.html', bg=get_background())

@app.route('/blog')
def blog():
    return render_template('blog.html', bg=get_background())

@app.route('/status')
def status_page():
    return render_template('status.html', bg=get_background(), status=get_minecraft_status())

@app.route('/hilfe')
def hilfe():
    return render_template('hilfe.html', bg=get_background())

@app.route('/tickets')
def tickets():
    return render_template('tickets.html', bg=get_background())

@app.route('/eltern')
def eltern():
    return render_template('eltern.html', bg=get_background())

@app.route('/agb')
def agb():
    return render_template('agb.html', bg=get_background())

@app.route('/impressum')
def impressum():
    return render_template('impressum.html', bg=get_background())

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html', bg=get_background())

@app.route('/widerruf')
def widerruf():
    return render_template('widerruf.html', bg=get_background())

@app.route('/cookies')
def cookies():
    return render_template('cookies.html', bg=get_background())

if __name__ == '__main__':
    app.run(debug=True, port=5000)
