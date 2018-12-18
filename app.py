from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/company')
def company():
    return render_template('companyoverview.html')

@app.route('/ourservices')
def services():
    return render_template('ourservices.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/quote')
def quote():
    return render_template('quote.html')



if __name__ == '__main__':
    app.run()
