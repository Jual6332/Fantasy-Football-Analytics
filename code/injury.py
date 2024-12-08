class Injury():
    def __init__(self):
        self.description = ""
        self.year = 0
        self.severity = ""
    def set_description(self,d):
        self.description = d
    def set_year(self,y):
        self.year = y
    def set_severity(self,s):
        self.severity = s
    def get_description(self):
        return self.description
    def get_year(self):
        return self.year
    def get_severity(self):
        return self.severity