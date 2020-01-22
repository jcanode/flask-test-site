from flask import Flask, render_template
from testsite import app

@app.route('/')
def main():
	return render_template('index.html', title='main')

@app.route('/about')
def about():
	return render_template('about.html', title='about')

@app.route('/blog')
def blog():
	return render_template('blog.html', title='blog')

@app.route('/contact')
def contact():
	return render_template('contact.html', title='contact')
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html', title='dashboard')


# ##API Links
# @app.route('/api/contact/submit', methods=['POST'])
# # def contactSubmit():
# # if request.method == "POST":
# #