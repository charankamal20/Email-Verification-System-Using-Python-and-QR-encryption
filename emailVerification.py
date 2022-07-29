import os
import math
import random
import smtplib
import ssl
import qrcode

def qrGenerator(content,name):
    img = qrcode.make(content)

    img.save('D:/'+ name + '.png')

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

def emailWithAttatchment(emailID,receiver):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    
    fromaddr = "co21314@ccet.ac.in"
    toaddr = emailID
    
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    
    # storing the senders email address  
    msg['From'] = fromaddr
    
    # storing the receivers email address 
    msg['To'] = toaddr
    
    # storing the subject 
    msg['Subject'] = "Your E-Mail credentials"
    
    # string to store the body of the mail
    body = """Please Scan the QR code for your login credentials"""
    
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    
    # open the file to be sent 
    filename = receiver + ".png"
    attachment = open(r"D:/" + filename , "rb")
    
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    
    # To change the payload into encoded form
    p.set_payload((attachment).read())
    
    # encode into base64
    encoders.encode_base64(p)
    
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(fromaddr, "Bazook@12506")
    
    # Converts the Multipart msg into a string
    text = msg.as_string()
    
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    
    # terminating the session
    s.quit()


print("----Welcome to registration system----\n")

####code begins

while True:
    
    print("\nAre you a: \n1. Teacher\n2. Student")
    choice = input("Your choice: ")

    if choice == "1":       ####teacher case
        
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
            Thank You for Registring
            
            Visit this link for project:
            https://github.com/charankamal20/Email-Verification-System-Using-Python-and-QR-encryption.git """

            qrGenerator(qrContent, receiver)

            emailWithAttatchment(emailID, receiver)
            print("Check your email")

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
            Thank You for Registring
            
            Visit this link for project:
            https://github.com/charankamal20/Email-Verification-System-Using-Python-and-QR-encryption.git """

            qrGenerator(qrContent, receiver)
            
            emailWithAttatchment(emailIDstud, receiver)
            print("Check your email")

        else:
            print("Wrong OTP Entered\nTry again :(")

    else:
        print("Wrong choice entered")
