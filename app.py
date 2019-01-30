from flask import Flask, render_template
from flask_wtf import  FlaskForm
from wtforms import StringField,PasswordField
app = Flask(__name__)
app.config['SECRET_KEY']='Thisisasecret!'

class contactform(FlaskForm):
    Name=StringField('Name')
    Email=StringField('Email')
    PhoneNumber=StringField('Phone Number')
    Message=StringField('Message')


@app.route('/', methods=['GET' ,'POST'])
def home():
    form=contactform()
    if form.validate_on_submit():
        return 'Your form has been submitted!'
    return render_template('home.html' , form=form)

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
