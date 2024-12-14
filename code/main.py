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

pm.add_injury_to_history(inj1)

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

#print(ar.get_name())


compare2Players(pm,ar)

# Unit Testing:
# Test 1: Print injury history of Patrick Mahomes
mahomes_injury_history = pm.get_injury_history()
print("Mahomes injury history: ")
for injury in mahomes_injury_history:
    print("{0}".format(injury.get_description()))


# Did this player overachieve or underachieve based on where he was drafted?

# WHat percentage of the time does San frnacisco run the ball?
# WHat percentage of these touches will go to X player?
# WHat percentage of these yards will go to X player

# Average 200 yards rushing
# McCaffrey gets 50% of the touches, 50% of the yards
# 20% more if playing Panthers. How many yards does the Panthers defense give up?

# Stephon Diggs had an injury

