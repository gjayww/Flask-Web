#!flask/bin/python3
from flask import Flask,request

app = Flask(__name__)

@app.route('/hello/',methods=['get'])
def index():
	university = request.args.get('university', '')
	city = request.args.get('city', '')
	return f'Hello, {university} {city}'

if __name__ == '__main__':
	app.run(debug=True)