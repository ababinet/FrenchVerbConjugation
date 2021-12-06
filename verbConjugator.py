#This program parses in a list of french verbs and
#quizzes the user on conjugations of that verb in the desired tense

from graphics import *
from Verb import *

#Generates the title screen
def titleScreen():
    win = GraphWin("Verb Conjugater", 600, 400)
    win.setBackground("light blue")

    #title text
    title = Text(Point(300, 20), "Which tense would you like to practice in?")
    title.setSize(25)
    title.draw(win)

    yVal1 = 70
    yVal2 = 130
    for i in range(3):
        rec = Rectangle(Point(200, yVal1), Point(400, yVal2))
        rec.draw(win)
        yVal1 = yVal1 + 100
        yVal2 = yVal2 + 100

    presentText = Text(Point(300, 100), "Present")
    presentText.setSize(20)
    presentText.draw(win)

    imparfaitText = Text(Point(300, 200), "Imparfait")
    imparfaitText.setSize(20)
    imparfaitText.draw(win)

    passeText = Text(Point(300, 290), "P̶a̶s̶s̶é̶ ̶C̶o̶m̶p̶o̶s̶é̶")
    passeNotReady = Text(Point(300, 310), "not avalible yet :(")
    passeNotReady.setSize(10)
    passeNotReady.setFill("red")
    passeNotReady.draw(win)
    passeText.setSize(20)
    passeText.setFill("red")
    passeText.draw(win)

    return win

#collects the user input of which tense to use
def userClick(win):
    #get user input of which tense to practice
    userClick = win.getMouse()
    x = userClick.getX()
    y = userClick.getY()

    win.close()
    return x, y

#checks the position of the mouse click and determines the tense
#then calls the function for the tense
def tenseChoice(x, y):
    if x >= 200 and x <= 400:
        xVal = True
    else:
        xVal = False

    if y >= 70 and y <= 130 and xVal == True:
        present()
    elif y >= 170 and y <= 230 and xVal == True:
        imparfait()
    elif y >= 270 and y <= 330 and xVal == True:
        invalid()
    else:
        invalid()

#generates the list of verbs and sorts them into directories, ER, IR, RE, and
#iregulars
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
                ERDict[verb[0]] = verb[1]
            elif verbInfin[-2: ] == "ir":
                IRDict[verb[0]] = verb[1]
            else:
                REDict[verb[0]] = verb[1]
        else:
            iregDict[verb[0]] = verb[1]
        
    f.close
    return verbList, ERDict, IRDict, REDict, iregDict

#Option if the user does not click on one of the valid tense options
def invalid():
    win = GraphWin("Verb Conjugater", 600, 400)
    win.setBackground("red")

    title = Text(Point(300, 200),
                     "You did not click on one of the tense options")
    title1 = Text(Point(300, 250),
                      "Please click to restart the program")
    title.setSize(25)
    title.draw(win)
    title1.setSize(25)
    title1.draw(win)
    
    win.getMouse()
    win.close()
    main()

#gets the dictionaries and verbList and loops through verbList popping off
#the first verb and checking which dictionary it is in, then calling the
#appropriate function based off of the verb ending
def present():
    verbList, ERDict, IRDict, REDict, iregDict = generateVerbs()
    tense = "present tense"
          
    for i in range(len(verbList)):
        if verbList == []:
            break
        else:
            target = verbList.pop(0)

            if target in ERDict:
                win = GraphWin("Present Tense", 600, 400)
                win.setBackground("light green")
                ER(target, win, tense) 
                
            elif target in IRDict:
                win = GraphWin("Present Tense", 600, 400)
                win.setBackground("light green")
                IR(target, win, tense)
                
            elif target in REDict:
                win = GraphWin("Present Tense", 600, 400)
                win.setBackground("light green")
                RE(target, win, tense)
            else:
                irregular(target)

#gets the dictionaries and verbList and loops through verbList popping off
#the first verb and checking which dictionary it is in, then calling the
#appropriate function based off of the verb ending
def imparfait():
    verbList, ERDict, IRDict, REDict, iregDict = generateVerbs()
    tense = "imparfait"
          
    for i in range(len(verbList)):
        if verbList == []:
            break
        else:
            target = verbList.pop(0)

            if target in ERDict:
                win = GraphWin("Imparfait", 600, 400)
                win.setBackground("peachpuff")
                ER(target, win, tense) 
                
            elif target in IRDict:
                win = GraphWin("Imparfait", 600, 400)
                win.setBackground("peachpuff")
                IR(target, win, tense)
                
            elif target in REDict:
                win = GraphWin("Imparfait", 600, 400)
                win.setBackground("peachpuff")
                RE(target, win, tense)
            else:
                irregular(target)
                
#loops through conList and checks if it matches the user input
#If it doesn't, calls wrongAnswers(), if it does, displays a message
def ER(target, win, tense):
    conjug = ERVerb(target)
    if tense == "present tense":
        conList = conjug.getERPresent()
    elif tense == "imparfait":
        conList = conjug.getERImparfait()
    userInput = generateScreen(conList, target, win, tense)
    for i in range(len(conList)):
        if conList[i] != userInput[i]:
            wrongAnswers(target, tense, conList, win)
            cont = Text(Point(515, 220),"(click anywhere to continue)")
            cont.draw(win)
            win.getMouse()
            win.close()
            right = False
            return
        else:
            right = True
            continue
    if right == True:
        correct = Text(Point(515, 200), "CORRECT!")
        correct.draw(win)
    cont = Text(Point(515, 220),"(click anywhere to continue)")
    cont.draw(win)
    win.getMouse()
    win.close()

#loops through conList and checks if it matches the user input
#If it doesn't, calls wrongAnswers(), if it does, displays a message
def IR(target, win, tense):
    conjug = IRVerb(target)
    if tense == "present tense":
        conList = conjug.getIRPresent()
    elif tense == "imparfait":
        conList = conjug.getIRImparfait()
    userInput = generateScreen(conList, target, win, tense)
    for i in range(len(conList)):
        if conList[i] != userInput[i]:
            wrongAnswers(target, tense, conList, win)
            cont = Text(Point(515, 220),"(click anywhere to continue)")
            cont.draw(win)
            win.getMouse()
            win.close()
            return
        else:
            continue
        correct = Text(Point(515, 200), "CORRECT!")
        correct.draw(win)
    cont = Text(Point(515, 220),"(click anywhere to continue)")
    cont.draw(win)
    win.getMouse()
    win.close()

#loops through conList and checks if it matches the user input
#If it doesn't, calls wrongAnswers(), if it does, displays a message
def RE(target, win, tense):
    conjug = REVerb(target)
    if tense == "present tense":
        conList = conjug.getPresent()
    elif tense == "imparfait":
        conList = conjug.getImparfait()
    userInput = generateScreen(conList, target, win, tense)

    for i in range(len(conList)):
        if conList[i] != userInput[i]:
            wrongAnswers(target, tense, conList, win)
            cont = Text(Point(515, 220),"(click anywhere to continue)")
            cont.draw(win)
            win.getMouse()
            win.close()
            break
        else:
            correct = Text(Point(515, 200), "CORRECT!")
            correct.draw(win)
            cont = Text(Point(515, 220),"(click anywhere to continue)")
            cont.draw(win)
            win.getMouse()
            win.close()
        
    

#Displays an error screen if it comes across an irregular verb, then allows the user to
#continue
def irregular(verb):
    win = GraphWin("error", 600, 400)
    title = Text(Point(300, 200), "It appears " + verb + " cannot be processed yet,")
    title1 = Text(Point(300, 220), "please click anywhere to move to the next verb")
    win.setBackground("tomato")
    title.draw(win)
    title1.draw(win)

    win.getMouse()
    win.close()
    return

#Creates the page for entering in conjugations 
def generateScreen(conList, verb, win, tense):
    title = Text(Point(300, 50),
                     "Conjugate " + verb + " in the " + tense)
    title.draw(win)
    
    nextButton = Rectangle(Point(10, 350), Point(110, 390))
    nextButton.setFill("gold")
    nextButton.draw(win)
    cont = Text(Point(60, 370), "Continue")
    cont.draw(win)

    checkButton = Rectangle(Point(490, 350), Point(590, 390))
    checkButton.setFill("lawngreen")
    checkButton.draw(win)
    check = Text(Point(540, 370), "Check")
    check.draw(win)
    
    conjugatedList = conjugationSetUp(win)
    return conjugatedList

#Collects the user input of the verb conjugations and returns them in a list
def conjugationSetUp(win):
    FS = Text(Point(200, 100), "Je")
    SS = Text(Point(200, 140), "Tu")
    TS = Text(Point(200, 180), "Il/Elle/On")
    FP = Text(Point(200, 220), "Nous")
    SP = Text(Point(200, 260), "Vous")
    TP = Text(Point(200, 300), "Ils/Elles")
    FS.draw(win)
    SS.draw(win)
    TS.draw(win)
    FP.draw(win)
    SP.draw(win)
    TP.draw(win)

    FSInput = Entry(Point(400, 100),10)
    SSInput = Entry(Point(400, 140),10)
    TSInput = Entry(Point(400, 180),10)
    FPInput = Entry(Point(400, 220),10)
    SPInput = Entry(Point(400, 260),10)
    TPInput = Entry(Point(400, 300),10)
    FSInput.draw(win)
    SSInput.draw(win)
    TSInput.draw(win)
    FPInput.draw(win)
    SPInput.draw(win)
    TPInput.draw(win)

    win.getMouse()

    return [FSInput.getText(), SSInput.getText(), TSInput.getText(),
            FPInput.getText(), SPInput.getText(), TPInput.getText()]

#If the user input does not match the generated conjugations
def wrongAnswers(verb, tense, conList, win):
    loc = 100
    for con in conList:
        text = Text(Point(300, loc), con)
        loc = loc + 40
        text.setFill("red")
        text.draw(win)

    wrong = Text(Point(515, 180), "It appears some of your")
    wrong1 = Text(Point(515, 200),  "answers are incorrect")
    wrong1.draw(win)
    wrong.draw(win)
    return
    
def main():
    #Sets up the sreen and collects the user input for the tense
    win = titleScreen()

    pointClickX, pointClickY = userClick(win)
    
    tense = tenseChoice(pointClickX, pointClickY)
    

if __name__ == "__main__":
    main()
    
