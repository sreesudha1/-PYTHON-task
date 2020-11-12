uname="aman"
upass="12345"
username=input("please enter the username")
if username==uname:
    password=input(f"hey{username},please enter your password")
if password==upass:
    print("hello you are logged in now")
else:
    print("please enter a correct password")
else:
    print("please enter the valid username")
