class Verb:
    def __init__(self, verb):
        self.verb = verb
        self.verbEnding = verb[-2:]

class ERVerb(Verb):
    def __init__(self, verb):
        self.verb = verb

        self.presFS = verb[0:-2] + "e"
        self.presSS = verb[0:-2] + "es"
        self.presTS = verb[0:-2] + "e"
        self.presFP = verb[0:-2] + "ons"
        self.presSP = verb[0:-2] + "ez"
        self.presTP = verb[0:-2] + "ent"
        
        impRoot = self.presFP[0:-3]

        self.impFS = verb[0:-2] + "ais"
        self.impSS = verb[0:-2] + "ais"
        self.impTS = verb[0:-2] + "ait"
        self.impFP = verb[0:-2] + "ions"
        self.impSP = verb[0:-2] + "iez"
        self.impTP = verb[0:-2] + "aient"

    def getERPresent(self):
        return [self.presFS, self.presSS, self.presTS,
                self.presFP, self.presSP, self.presTP]

    def getERImparfait(self):
        return [self.impFS, self.impSS, self.impTS,
                self.impFP, self.impSP, self.impTP]

    def __str__(self):
        return "{0}".format(self.verb)

class IRVerb(Verb):
    def __init__(self, verb):
        self.verb = verb

        self.presFS = verb[0:-2] + "is"
        self.presSS = verb[0:-2] + "is"
        self.presTS = verb[0:-2] + "it"
        self.presFP = verb[0:-2] + "issons"
        self.presSP = verb[0:-2] + "issez"
        self.presTP = verb[0:-2] + "issent"

        self.impFS = self.presFP[0:-3] + "ais"
        self.impSS = self.presFP[0:-3] + "ais"
        self.impTS = self.presFP[0:-3] + "ait"
        self.impFP = self.presFP[0:-3] + "ions"
        self.impSP = self.presFP[0:-3] + "iez"
        self.impTP = self.presFP[0:-3] + "aient"

    def getIRPresent(self):
        return [self.presFS, self.presSS, self.presTS,
                self.presFP, self.presSP, self.presTP]
    
    def getIRImparfait(self):
        return [self.impFS, self.impSS, self.impTS,
                self.impFP, self.impSP, self.impTP]
    
    def __str__(self):
        return "{0}".format(self.verb)

class REVerb(Verb):
    def __init__(self, verb):
        self.verb = verb

        self.presFS = verb[0:-2] + "s"
        self.presSS = verb[0:-2] + "s"
        self.presTS = verb[0:-2]
        self.presFP = verb[0:-2] + "ons"
        self.presSP = verb[0:-2] + "ez"
        self.presTP = verb[0:-2] + "ent"

        impRoot = self.presFP[0:-3]

        self.impFS = impRoot + "ais"
        self.impSS = impRoot + "ais"
        self.impTS = impRoot + "ait"
        self.impFP = impRoot + "ions"
        self.impSP = impRoot + "iez"
        self.impTP = impRoot + "aient"


    def getPresent(self):
        return [self.presFS, self.presSS, self.presTS,
                self.presFP, self.presSP, self.presTP]

    def getImparfait(self, verb):
        return [self.impFS, self.impSS, self.impTS,
                self.impFP, self.impSP, self.impTP]
    
    def __str__(self):
        return "{0}".format(self.verb)


        
