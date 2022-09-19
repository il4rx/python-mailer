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
fl = fgd("CYBERMAIL")
print(fl)
print("\n")
print(Fore.GREEN + "Anonymous Email Sender" + Style.RESET_ALL)
print("By Using This Feature you will send anonymous email.")
print("You're real email was encrypted. this method will recorded")
print("You can see the current record by html file, the file will generated")
print("after you send a email. and automaticaly deleted when you start new journey")
print("\n")
print(Fore.RED + "ATTENTION ALERT FOR USER" + Style.RESET_ALL)
print("This method is illegal, don't use this method for scamming")
print("criminal issues, or some criminal case")
print("\n")

sender_email = "antromaxxcii@gmail.com"
rec_email = input(Fore.RED + "[+] " + Style.RESET_ALL + "Rechiever Email [Username] > ")
user_name = input(Fore.RED + "[+] " + Style.RESET_ALL + "Your Name [Username] > ")
receiver_email = rec_email + "@gmail.com"
subject = input(Fore.RED + "[+] " + Style.RESET_ALL + "Subject > ")
pesan = input(Fore.RED + "[+] " + Style.RESET_ALL + "Message > ")
password = "wdtxourvbunortmz"
    
print("\n")
print("Information Services [ EMAIL STATUS ]")
myTable = PrettyTable(["Author", "Email Sender", "Rechiever", "Message Length", "Timestamp"])
myTable.add_row([platform.node(), sender_email, receiver_email, len(pesan), s])
print(myTable)
  


    

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = "The Second Ronin"
message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
html = f"""\
    <html>
    <body>
        <div class="border-content" style="border : 1px solid #ddd; height : 100vh; width: 100%; border-radius: 5px; height : max-content;background : white;">
            <div class="content-box" style="background: linear-gradient(160deg, rgba(19,1,107,1) 5%, rgba(255,78,218,1) 100%); margin : 0; padding : 0;">
                <div class="header" style="font-family: arial; background: none; color : white; padding : 20px; font-weight: bold;">
                    Greeper.io <br><span style="font-weight :lighter; opacity: .8; font-size: small;">Third Party Email Service Manager</span>
                </div>
            </div>

            <div class="sender" style="margin: 0; padding : 0; margin-top: -10px; background : white!important;">
                <div class="cardHe" style="display : flex ; padding : 20px; align-items : center; font-family: Arial; margin-top : 5px;">
                    <img style="border : 1px solid #ddd; padding : 1px; border-radius : 100%;" src="https://cdn.discordapp.com/attachments/1014711843614367757/1020980413704970260/20220917_204611.png" alt="" width="40">

                    <div class="sa" style="margin-left : 10px;">
                        <span class="jd" style="font-weight: bold; font-size : large;">{user_name}</span><br>
                    </div>
                </div>

                <div class="msga" style="font-family: arial; margin : 15px; margin-top : -20px; border-radius : 2px; padding : 10px; background : white!important;">
                    {pesan}
                </div>

                <div class="description-text">
                    <div class="text" style=" margin : 0px; margin-top: -10px; color : black; font-family: Arial, Helvetica, sans-serif; padding : 20px; font-size: medium; width: max-content; overflow: hidden;">
                        Device Name As <b>{platform.node()}</b>

                    </div>
                  
                </div>

            </div>
        </div>
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
