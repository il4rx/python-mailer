from email.message import EmailMessage
from platform import platform
import time, datetime, colorama
from traceback import print_tb
from colorama import Fore, Back , Style
import os
import pyfiglet
from pyfiglet import figlet_format as fgd
import platform
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from prettytable import PrettyTable

date = datetime.datetime.now()
s = date.strftime('%c')

os.system("cls||clear")
fl = fgd("EMAIL SENDER")
print(fl)
print("\n")
print(Fore.GREEN + "Email Sender" + Style.RESET_ALL)
print("\n")

sender_email = "Your Mail"
receiver_email = input(Fore.RED + "[+] " + Style.RESET_ALL + "Rechiever Email > ")
receiver_email
subject = input(Fore.RED + "[+] " + Style.RESET_ALL + "Subject > ")
pesan = input(Fore.RED + "[+] " + Style.RESET_ALL + "Message > ")
password = "Key App Password"
    
print("\n")
print("Information Services [ EMAIL STATUS ]")
myTable = PrettyTable(["Author", "Email Sender", "Rechiever", "Message Length", "Timestamp"])
myTable.add_row([platform.node(), sender_email, receiver_email, len(pesan), s])
print(myTable)
  


    

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = "Random Mail"
message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
html = f"""\
    <html>
    <body>
        <p>{pesan}</p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
mailTest = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
message.attach(mailTest)

    # Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
os.system("cls||clear")
print("email was sent to " + Fore.BLUE + receiver_email + Style.RESET_ALL + " by " + Fore.RED + sender_email +  Style.RESET_ALL)
time.sleep(10)
os.system("cls||clear")
