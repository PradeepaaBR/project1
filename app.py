from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    phone = request.form['phone']
    gender = request.form['gender']
    department = request.form['department']
    address = request.form['address']

    hobbies = request.form.getlist('hobbies')
    hobbies_str = ", ".join(hobbies)

    message = f"""Subject: Your Submitted Details

Hello {name},

Here are your submitted details:

Name: {name}
Email: {email}
Age: {age}
Phone: {phone}
Gender: {gender}
Department: {department}
Hobbies: {hobbies_str}
Address: {address}

Thank you!
"""

    sender_email = "pradeepaabr@gmail.com"
    sender_password = "yckxyhkriylysxbw"   # your app password

    try:
        # ✅ CORRECT SMTP SERVER
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        server.sendmail(sender_email, email, message)

        server.quit()
        return "Form submitted successfully! Check your email."

    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)