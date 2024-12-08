from player import *
from injury import *

def loadWRData():
    pass

def compare2Players(Player1,Player2):
    # First compare ages of players (If age is within 3 years, negligible difference then)
    if (Player1.get_age() > Player2.get_age()):
        age_diff = Player1.get_age() - Player2.get_age()
        print("{0} is younger by {1} years.".format(Player2.get_name(),age_diff))
    elif (Player1.get_age() < Player2.get_age()):
        age_diff = Player2.get_age() - Player1.get_age()
        print("{0} is younger by {1} years.".format(Player1.get_name(),age_diff))
    else:
        print("{0} and {1} are the same age.".format(Player2.get_name(),age_diff))
    # Then check if each player has an injury history

# If a player is older than 35 years old, mention that he is probably past his prime and might retire.

#loadWrData()

# Add Patrick Mahomes
pm = Player()
pm.set_name("Patrick Mahomes")
pm.set_age(29)
pm.set_position("QB")
inj1 = Injury()
inj1.set_description("Patrick Mahomes sprained his ankle in the playoffs")
inj1.set_year(2022) # Verify
inj1.set_severity("Major")

# Add Aaron Rodgers
ar = Player()
ar.set_name("Aaron Rodgers")
ar.set_age(41)
ar.set_position("QB")
inj2 = Injury()
inj2.set_description("Aaron Rodgers tore his Achilles in the first game of Jets season")
inj2.set_year(2023)
inj2.set_severity("Major")
ar.add_injury_to_history(inj1)

print(ar.get_name())


compare2Players(pm,ar)

# Did this player overachieve or underachieve based on where he was drafted?