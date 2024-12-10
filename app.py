from flask import Flask, request, render_template, render_template_string, session
import subprocess, shlex
from waitress import serve
import uuid

app = Flask(__name__)
app.secret_key = 'REDACTED'

songs = [
    {
        "name": "Aishite Aishite Aishite (愛して愛して愛して)",
        "image": "/static/img/utaite.jpg",
        "audio": "/static/audio/aishite.mp3"
    },
    {
        "name": "New Genesis / 新時代",
        "image": "/static/img/new_genesis.jpg",
        "audio": "/static/audio/new_genesis.mp3"
    },
    {
        "name": "Odo (踊)",
        "image": "/static/img/odo.jpg",
        "audio": "/static/audio/odo.mp3"
    },
    {
        "name": "Readymade (レディメイド)",
        "image": "/static/img/readymade.jpg",
        "audio": "/static/audio/readymade.mp3"
    },
    {
        "name": "RuLe (ルル)",
        "image": "/static/img/rule.jpg",
        "audio": "/static/audio/rule.mp3"
    },
    {
        "name": "Shoka",
        "image": "/static/img/shoka.jpg",
        "audio": "/static/audio/shoka.mp3"
    },    
    {
        "name": "Show (唱)",
        "image": "/static/img/show.jpg",
        "audio": "/static/audio/show.mp3"
    },
    {
        "name": "Ussewa (うっせぇわ)",
        "image": "/static/img/ussewa.jpg",
        "audio": "/static/audio/ussewa.mp3"
    },
    {
        "name": "きらきら星",
        "image": "/static/img/twinkle.png",
        "audio": "/static/audio/twinkle.mp3"
    },
]

added_songs = {}

def show_playlist(uuid):
    songs_to_add = []
    if uuid in added_songs:
        songs_to_add = added_songs[uuid]
    
    playlist = songs + songs_to_add
    if request.remote_addr == "127.0.0.1":
        # adminbot can see flag
        playlist.append(
            {
                "name": "rwandiCTF{REDACTED}",
                "image": "/static/img/",
                "audio": "/static/audio/"
            }
        )
    
    playlist.sort(key=lambda song:song['name'])
    return render_template('index.html', playlist=playlist)

@app.route('/')
def index():
    if 'uuid' not in session:
        user = str(uuid.uuid4())
        session['uuid'] = user
        added_songs[user] = []
    return show_playlist(session['uuid'])
    
@app.route('/users/<uuid>')
def index_uuid(uuid):
    print(uuid)
    return show_playlist(uuid)

# no UI for the rest so make a request yourself

@app.route('/add', methods=['POST'])
def add_to_playlist():
    if 'uuid' not in session:
        return 'No uuid!'
        
    # Get data from the form
    name = request.form.get('name')
    image = request.form.get('image')
    audio = request.form.get('audio')

    # Create a new track
    new_track = {"name": name, "image": image, "audio": audio}

    # Add to session playlist
    user = session['uuid']
    if user not in added_songs:
        del session['uid']
    added_songs[user].append(new_track)

    return f'new track with name={name}, image={image}, audio={audio} added'

@app.route('/remove', methods=['POST'])
def remove_from_playlist():
    if 'uuid' not in session:
        return 'No uuid!'
        
    # Get data from the form
    name = request.form.get('name')

    # Remove from session playlist
    user = session['uuid']
    if user not in added_songs:
        del session['uid']
    
    new_list = [song for song in added_songs[user] if song.name != name]
    added_songs[user] = new_list

@app.route('/sess')
def send():
    return render_template_string('<h1>'+session['uuid']+'</h1>')

@app.route('/adminbot', methods=['POST'])
def adminbot():
    if 'uuid' not in session:
        return 'No uuid!'
    
    url = shlex.quote('http://127.0.0.1:8000/users/' + session['uuid'])
    print(url)
    # command = f"chromium --virtual-time-budget=10000 --no-sandbox --headless --disable-gpu --timeout=10000 {url}"
    command = f"node admin.js {url}"
    subprocess.Popen(command, shell=True)
    return "Admin bot will see your request soon"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)