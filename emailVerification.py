import os
import math
import random
import smtplib
import ssl
import pyqrcode


def qrGenerator(content,name):
    from pyqrcode import QRCode  
    # String which represent the QR code 
    s = content
    # Generate QR code 
    url = pyqrcode.create(s)  
    nameofourfile = name + ".svg"  
    # Create and save the png file naming "myqr.png"
    url.svg(nameofourfile, scale = 8)

def OTPsend(receiver, message):

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "co21314@ccet.ac.in"

    password = "Bazook@12506"
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        
        server.starttls(context=context) # Secure the connection

        server.login(sender_email, password)
        
        server.sendmail(sender_email,receiver,message)
        # TODO: Send email here
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

def OTPgen():
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP



print("----Welcome to registration system----\n")

####code begins

while True:
    
    print("\nAre you a: \n1. Teacher\n2. Student")
    choice = input("Your choice: ")

    if choice == "1": ####teacher case
        
        print("Enter the username of your email id(Example: username@ccet.ac.in)\n")

        receiver = input("Enter your username: ")
        emailID = receiver + "@ccet.ac.in"
        print("\n::You will receive an OTP on your email ID::")
        
        OTP = OTPgen()
        message = OTP  + " is your OTP"
        
        OTPsend(emailID, message)

        print("OTP sent...")

        UserOTP = input("Enter the OTP: ")

        if UserOTP == OTP: 
            print("You are verified")
            print("\nYour login credentials are being encrypted......")
            newPass = OTPgen()
            qrContent = """Your login credentials are: 
            Username: """ + emailID + """
            Password: """ + newPass + """
            Thank You for Registring"""

            qrGenerator(qrContent, receiver)

        else:
            print("Wrong OTP Entered\nTry again :(")

    elif choice == "2": #####studnet choice else

        receiver = input("Enter your roll number: ")
        emailIDstud = "co" + receiver + "@ccet.ac.in"
        print("\n::You will receive an OTP on your email ID::")
        
        OTP = OTPgen()
        message =  OTP + " is your OTP"
        
        OTPsend(emailIDstud, message)
        print("OTP sent...")

        UserOTP = input("Enter the OTP: ")

        if UserOTP == OTP: 
            print("You are verified")
            print("\nYour login credentials are being encrypted......")
            newPass = OTPgen()
            qrContent = """Your login credentials are: 
            Username: """ + emailIDstud + """
            Password: """ + newPass + """
            Thank You for Registring"""

            qrGenerator(qrContent, receiver)


        else:
            print("Wrong OTP Entered\nTry again :(")

    else:
        print("Wrong choice entered")