from Data.VerifyAPI import *
from Data.FaceverifyAPI import *

def IDverify(name, dob, Vname, Vdob):
    while name != Vname or dob != Vdob:
        print("Your credentials cannot be verified")
        dob = input("Please retype your DOB: ")
        name = input("Please retype your name as in your NRIC: ")
        name = name.upper()
    if dob == Vdob and name == Vname:
        print("Verified! Please move on to the next step")

def facecheck(confidence, identical):
    while identical == False:
        print("Your identity cannot be verified")
        print("")
        input("Please upload a picture of a photo ID to your pictures folder labelled \"Picture\" and take a selfie. \nPress enter when finished")
        identical, confidence = faceverify()
    else:
        print("Your credentials are verified. \nHave a nice day!")