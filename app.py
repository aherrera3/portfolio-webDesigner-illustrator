from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/portfolio/web-designer')
def web_designer():
    return render_template('web_designer.html')

@app.route('/portfolio/illustrator')
def illustrator():
    return render_template('illustrator.html')

@app.route('/contact-me')
def contact_me():
    return render_template('contact_me.html')

@app.route('/contact-me-successful-response', methods=["POST"])
def contact_me_successful_response():
    name = request.form.get("name-input");
    select_option = request.form.get("select-project");
    text_area = request.form.get("text-area");
    email = request.form.get("email-input");
    return render_template('contact_me_successful_response.html')

if __name__ == '__main__':
   app.run(debug = True)