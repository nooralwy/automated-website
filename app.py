from flask import Flask, render_template, request
from scraper import scrape_website
from email_sender import send_email

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')    
def about():
    return render_template('/about.html')

@app.route('/task', methods=['GET', 'POST'])    
def task():

    success_message = ""
    if request.method == 'POST':

        url = request.form['url']

        scrape_website(url)

        send_email()

        success_message = (
            "Websites scrapped and email sent successfully!"
      )
    
    return render_template('task.html', success_message=success_message)
 
if __name__ == '__main__':
    app.run(debug=True)    