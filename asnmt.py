
class akg:
    def __init__(self,branch,section,techinical,cultural,name) :
        self.branch=branch
        self.section=section
        self.techinical=techinical
        self.cultural=cultural
        self.name=name
        
    def br(self):
        print("branch is :",self.branch)

class sec(akg):
        
    def pr(self):
        print("section is :",self.section)
        
class tech(sec):
        
    def s1(self):
        print("techinical society is :",self.techinical)
        
class cul(sec):
        
        
    def s2(self):
        print("cultural society is :",self.cultural)
        
class intro(tech,cul):
        
    def info(self):
        print("name is :",self.name)
a=intro("cse(aiml)","s4","brl","goonj","aniket mishra")
a.info()
a.s1()
a.s2()
a.pr()
a.br()