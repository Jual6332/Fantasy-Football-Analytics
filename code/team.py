class Team():
    def __init__(self):
        self.name = ""
        self.city = ""
        self.rank_against_qbs = ""
        self.rankings_against_wrs = ""
        self.offense = ""
    def set_name(self,nm):
        self.name = nm
    def set_city(self,ct):
        self.city = ct
    def set_rank_against_qbs(self,rnk_qbs):
        self.rank_against_qbs = rnk_qbs
    def set_rank_against_wrs(self,rnk_wrs):
        self.rank_against_wrs = rnk_wrs
    def set_offense(self,off):
        self.offense = off
    def get_name(self,nm):
        return self.name
    def get_city(self,ct):
        return self.city
    def get_rank_against_qbs(self):
        return self.rank_against_qbs
    def get_rank_against_wrs(self):
        return self.rank_against_wrs
    def get_offense(self):
        return self.offense