import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from flask import Flask, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)

# Create a SQLite database connection
conn = sqlite3.connect('contacts.db', check_same_thread=False)
cursor = conn.cursor()

# Create a contacts table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    message TEXT
                )''')
conn.commit()

@app.route('/')
def index():
    conn = sqlite3.connect('contacts.db', check_same_thread=False)
    cursor = conn.cursor()
    # Fetch data from the database
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Render the HTML template and pass the contacts data
    return render_template('index.html', contacts=contacts)


@app.route('/about')
def about():
    return render_template('about.html')

messages = []

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        try:
            conn = sqlite3.connect('contacts.db', check_same_thread=False)
            cursor = conn.cursor()
            # Insert the contact into the database
            cursor.execute('''INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)''', (name, email, message))
            conn.commit()
            print("Record inserted successfully")         
        
            # Close the connection when done
            conn.close()     

        except sqlite3.Error as e:
         print("Error inserting record:", e)      
        
        return redirect(url_for('thank_you'))
    return render_template('contact.html')

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

if __name__ == '__main__':
    app.run(debug=True)

    