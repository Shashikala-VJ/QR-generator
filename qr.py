import qrcode
import os

name=input("Enter the name:")
contact=input("Enter ph.no:")
course=input("Enter your course:")
reg=input("Enter regno:")
profile="Name: " + name + "\nContact: " + contact + "\nCourse: " + course + "\nReg No: " + reg 
print(profile)
img=qrcode.make(profile)
img.save('profile.png',"PNG")
os.startfile('profile.png')