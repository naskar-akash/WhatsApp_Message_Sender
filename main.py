# Installing required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone = os.getenv("TWILIO_PHONE_NUMBER")

# twilio client set up
client = Client(account_sid, auth_token)

# making send msg function
def send_message(sender_phone, message_content):
    try:
        message = client.messages.create(
        from_=f'whatsapp:{from_phone}',
        body=message_content,
        to=f'whatsapp:{sender_phone}'
        )
        print(f"Message send sussessfully! Message SID: {message.sid}")
    except Exception as e:
        print("Error sending message:",str(e))

# inputs from user
sender_name = input("Enter the sender's name: ")
sender_phone = str("+91") + input("Enter the sender's whatsapp number: ")
message_content = input(f"Enter the message you want to send to {sender_name}: ")

# parse datetime and calculate delay
date_str = input("Enter the date to send the message (yyyy-mm-dd): ")
time_str = input("Enter the time to send the message (hh:mm in 24 hour format): ")

# datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")    # convert string date-time into datetime object
current_time = datetime.now()    # get current date-time

# calculate delay in seconds
delay = (schedule_datetime - current_time).total_seconds()

if delay > 0:
    print(f"Message scheduled to be sent to {sender_name} at {schedule_datetime}. Waiting...")
    time.sleep(delay)  # wait until the scheduled time
    send_message(sender_phone, message_content)  # send the message
else:
    print("Scheduled time is in the past. Please enter a future date and time.")
