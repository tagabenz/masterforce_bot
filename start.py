from flask import Flask, Response, render_template, request, session
import requests,redis
import hashlib


app = Flask(__name__)
app.secret_key='We Will Rock You'
cache = redis.StrictRedis( host='redis', port=6379, db=0 )


@app.route('/')
def welcome_page():
    return render_template('welcome.html', title='Welcome')


@app.route('/index', methods=['GET','POST'])
def index_page() -> str:
    if request.method=="POST":
        session['user']=request.form['name']
    return render_template('index.html', title='Masterforce')


@app.route('/monster/<name>')
def get_identicon(name):
    image=cache.get(name)
    if image is None:
        r = requests.get('http://dnmonster:8080/monster/' + name + '?size=32')
        image = r.content
        cache.set(name,image)
    return Response(image, mimetype='image/png')


@app.route('/test')
def test_page():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
