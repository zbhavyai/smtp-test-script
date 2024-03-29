#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage

from dotenv import dotenv_values

html_content = '<img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Ours_brun_parcanimalierpyrenees_1.jpg" style="width: 500px; display: inline; outline: none !important; text-decoration: none !important; -ms-interpolation-mode: bicubic; clear: both; border: 0;" align="none" />'


def test_smtp(smtp_server, smtp_port, smtp_username, smtp_password, sender_email, receiver_email):
    try:
        # Create a new SMTP session
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)

        # Login to the SMTP server
        server.login(smtp_username, smtp_password)

        # Create a test email message
        message = EmailMessage()
        message["Subject"] = "Test Email"
        message["From"] = sender_email
        message["To"] = receiver_email
        # message.set_content("This is a test email.")
        message.add_alternative(html_content, subtype="html")

        # Send the email
        server.send_message(message)

        print("Test email sent successfully!")

    except Exception as e:
        print("Failed to send test email.")
        print(f"Error: {str(e)}")

    finally:
        # Close the SMTP connection
        server.quit()


if __name__ == "__main__":
    config = dotenv_values(".env")
    smtp_server = config.get("SMTP_SERVER")
    smtp_port = int(config.get("SMTP_PORT"))
    smtp_username = config.get("SMTP_USERNAME")
    smtp_password = config.get("SMTP_PASSWORD")
    sender_email = config.get("SENDER_EMAIL")
    receiver_email = config.get("RECEIVER_EMAIL")

    # Call the function to test SMTP details
    test_smtp(smtp_server, smtp_port, smtp_username,
              smtp_password, sender_email, receiver_email)
