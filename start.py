from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index_page() -> str:
    return render_template('index.html')


app.run(debug=True,host='0.0.0.0')
