from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/welcome_page')
def welcome():
	return 'Welcome World.'
	
if __name__ == '__main__':
	app.run(debug=True)
