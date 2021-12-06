from graphics import *
from Verb import *
def generateVerbs():
    f = open("Verbs.csv", "r")
    ERDict = {}
    IRDict = {}
    REDict = {}
    iregDict = {}
    verbList = []
    
    for verb in f:
        verb = verb.strip().split(",")
        verbList.append(verb[0])
        regular = verb[2]
        
        if regular == "Regular":
            verbInfin = verb[0]

            if verbInfin[-2: ] == "er":
                ERDict[verbInfin] = verb[1]
            elif verbInfin[-2: ] == "ir":
                IRDict[verb[0]] = verb[1]
            else:
                REDict[verb[0]] = verb[1]
        else:
            iregDict[verb[0]] = verb[1]
   
    f.close
    return verbList, ERDict, IRDict, REDict, iregDict


def present():
    #win = GraphWin("Present Tense", 600, 400)
    #win.setBackground("light green")

    verbList, ERDict, IRDict, REDict, iregDict = generateVerbs()

    for verb in verbList:
        if verb in ERDict:
            conjug = ERVerb(verb)
            conList = conjug.getPresent()
            generateScreen(conList, verb)
        elif verb in IRDict:
            con = IRVerb(verb)
        elif verb in REDict:
            con = REVerb(verb)
        else:
            pass
            #ireegulars
"""
    for verb in range(len(verbList)):
        if verb in ERDict:
            con = ERVerb(verb)
            presentList.append(con.firstSing)
            presentList.append(con.firstSing
        elif verb in IRDict:
            con = IRVerb(verb)
        elif verb in REDict:
            con = REVerb(verb)
"""
present()
