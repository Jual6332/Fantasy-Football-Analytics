class Week():
    def __init__(self):
        self.home = ""
        self.opponent = ""
        self.yards = 0
        self.TDs = 0
        self.INTs = 0
        self.F = 0
        self.FPTS = 0
    def get_home(self):
        return self.home
    def get_opponent(self):
        return self.opponent
    def get_yards(self):
        return self.yards
    def get_TDs(self):
        return self.TDs
    def get_INTs(self):
        return self.INTs
    def get_F(self):
        return self.F
    def get_FPTS(self):
        return self.FPTS
    def set_home(self,hm):
        self.home = hm
    def set_opponent(self,opp):
        self.opponent = opp
    def set_yards(self,yds):
        self.yards = yds
    def set_TDs(self,tds):
        self.TDs = tds
    def set_INTs(self,ints):
        self.INTs = ints
    def set_F(self,f):
        self.F = f
    def get_FPTS(self,fpts):
        self.FPTS = fpts
    
