from Application.logic import *
import time

def io():
    while True:
        print("Welcome to Safecredit!")
        time.sleep(1)
        name = input("Please input your name as in your NRIC (Press 0 to break): ")
        name = name.upper()
        if name == "0":
            break
        print("")
        dob = input("Please input your Date of Birth in DD-MM-YYYY (Press 0 to break): ")
        if dob == "0":
            break
        if dob == "0":
            break
        print("")
        time.sleep(1)
        input("Please take a clear photo of your NRIC in your picture folder for verification \nPlease Press enter when done")
        Vname, Vdob = verifyAPI()
        print("")
        IDverify(name, dob, Vname, Vdob)
        print("")
        input("Please upload a picture of a photo ID to your pictures folder labelled \"Picture\" and take a selfie. \nPress enter when finished")
        print("")
        identical, confidence = faceverify()
        facecheck(confidence, identical)
        break