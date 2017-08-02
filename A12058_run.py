from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
	print 'hello world'
    return render_template('A12058.html')

if __name__ == '__main__':
    app.run(debug = True)