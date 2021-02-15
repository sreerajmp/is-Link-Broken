import os
import csv
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client import exceptions

def send_it(self,errorList):
    message = Mail(
        from_email='amalaabraham3@gmail.com',
        to_emails='sreerajmp1996@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
       )
    print(errorList)
    #Using os won't work for Chrome extension...
    message.dynamic_template_data = {
        'row': errorList,
    }
    message.template_id = self.settings["TEMPLATE_ID"]
    print("SENDGRID_API_KEY:",self.settings["SENDGRID_API_KEY"])
    sg = SendGridAPIClient(self.settings["SENDGRID_API_KEY"])

    try:
      response = sg.send(message)
      print(response.status_code)
      print(response.body)
      print(response.headers)
    except exceptions.BadRequestsError as e:
        print(e.body)
        exit()
    print(response.status_code, response.body, response.headers)