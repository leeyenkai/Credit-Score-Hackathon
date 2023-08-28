from Application.logic import *
connector = connector()

def io():
    while True:
        df = testingdata(connector)
        application = input("Please input Application_ID: ")
        score = getScore(df,application)
        creditscore = print("This Applicant's Credit Score is:",int(round((score[0])*100)))
        break
