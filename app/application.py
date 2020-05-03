from flask import Flask, request, render_template, url_for, redirect
import requests
def get_audio():
    radio_url = "https://coderadio-admin.freecodecamp.org/api/live/nowplaying/coderadio"
    return requests.get(radio_url).json()['station']['listen_url']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data = get_audio())



if __name__=="__main__":
    #localhost:5000
    app.run(debug=True)