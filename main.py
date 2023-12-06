import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def read_birthdays(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def send_birthday_email(name, email):
    sender_email = "your_email@gmail.com"
    app_password = "your_email_password"

    subject = "Happy Birthday!"
    body = f"Dear {name},\n\nHappy Birthday! 🎉🎂\n\nBest wishes,\nRic"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, email, message.as_string())

def main():
    today = datetime.now().strftime('%Y-%m-%d')
    file_path = 'data/friends_birthdays.csv'

    birthdays = read_birthdays(file_path)

    for friend in birthdays:
        if today[5:] == friend['Birthday'][5:]:
            send_birthday_email(friend['Name'], friend['Email'])
            print(f"Email sent to {friend['Name']} at {friend['Email']}")

if __name__ == "__main__":
    main()
