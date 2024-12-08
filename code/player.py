class Player():
    def __init__(self):
        self.name = ""
        self.age = ""
        self.position = ""
        self.injury_history = []
    def set_name(self,nm):
        self.name=nm
    def set_age(self,g):
        self.age=g
    def set_position(self,p):
        self.position=p
    def add_injury_to_history(self,inj):
        self.injury_history.append(inj)
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_position(self):
        return self.position
    def get_injury_history(self):
        return self.injury_history
    
    