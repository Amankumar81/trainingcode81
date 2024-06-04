# CLI base project 
#  passowrd=wine gjgf dyau cfbs 
import smtplib
try:
    server=smtplib.SMTP(host='smtp.gmail.com',port=587)  # creating sever and port
    server.starttls()  # start the server
    receiver_email=input("enter the email:") # make a receiver variable and take input
    sender_email='amankumar75432@gmail.com'   # sender email
    password='wine gjgf dyau cfbs '  # password generted in google security
    server.login(sender_email,password=password) # login in the server with password and email
    subject=input("what is your problem:")   # write the subject of email
    body=input("thoda deatil me batao:")   # add additional info.
    message=f"subject:{subject}\n\n{body}"   # create a message variable and assign subject and body
    server.sendmail(sender_email,receiver_email,message)  # by the send mail function send sender and reveiver mail and fuction 
    print("mene mail send kar diya h")   # print the 
    server.quit()   # close the server 
except Exception as e:
    print("mail send nhi hua h ")    
