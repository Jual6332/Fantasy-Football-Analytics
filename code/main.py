from player import *
from injury import *

def loadWRData():
    pass

def compare2Players():
    # First check if each player has an injury history
    pass

#loadWrData()

ar = Player()
ar.set_name("Aaron Rodgers")

inj1 = Injury()
inj1.set_description("Aaron Rodgers tore his Achilles in the first game of Jets season")
inj1.set_year(2023)
inj1.set_severity("Major")

print(ar.get_name())


# Did this player overachieve or underachieve based on where he was drafted?