from Data.API import *
from Data.Database import *

def testingdata(connector):
    df = connector.run_process("//EIS/RandomForestTestingSet")
    return df

def getScore(df,application):
    score = df[df["Application_ID"] == int(application)]["confidence(1)"]
    score = score.values
    return score