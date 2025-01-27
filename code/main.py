from player import *
from injury import *
from week import *
from team import *

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

# Compare 2 players based on a number of factors: age, best yearly fantasy performance (maybe include mvps, superbowl rings, )
compare2Players(pm,ar)

# Unit Testing:
# Test 1: Print injury history of Patrick Mahomes
mahomes_injury_history = pm.get_injury_history()
print("Mahomes injury history: ")
for injury in mahomes_injury_history:
    print("{0}".format(injury.get_description()))
    
    
# Mahomes data
mahomes_2024_weeks = []
    
# Add game information
wk1 = Week()
wk1.home = "Kansas City"
wk1.opponent = "Baltimore"
wk1.yards = 291
wk1.TDs = 1
wk1.INTs = 1
wk1.F = 0
wk1.FPTS = 14.14

mahomes_2024_weeks.append(wk1)

#print("Wk1.home: {0}".format(wk1.home))
#print("Wk1.__home: {0}".format(wk1.__home))

wk2 = Week()
wk2.home = "Kansas City"
wk2.opponent = "Cincinnati"
wk2.yards = 151
wk2.TDs = 2
wk2.INTs = 2
wk2.F = 0
wk2.FPTS = 12.94

mahomes_2024_weeks.append(wk2)

wk3 = Week()
wk3.home = "Atlanta"
wk3.opponent = "Kansas City"
wk3.yards = 217
wk3.TDs = 2
wk3.INTs = 1
wk3.F = 0
wk3.FPTS = 16.38

mahomes_2024_weeks.append(wk3)

wk4 = Week()
wk4.home = "Los Angeles"
wk4.opponent = "Kansas City"
wk4.yards = 245
wk4.TDs = 1
wk4.INTs = 1
wk4.F = 0
wk4.FPTS = 13.00

mahomes_2024_weeks.append(wk4)

wk5 = Week()
wk5.set_home("Kansas City")
wk5.opponent = "New Orleans"
wk5.yards = 331
wk5.TDs = 0
wk5.INTs = 1
wk5.F = 0
wk5.FPTS = 13.44

mahomes_2024_weeks.append(wk5)

wk6 = Week()
wk6.home = ""
wk6.opponent = ""
wk6.yards = 0
wk6.TDs = 0
wk6.INTs = 0
wk6.F = 0
wk6.FPTS = 0
wk6.notes = "Bye week"

mahomes_2024_weeks.append(wk6)

wk7 = Week()
wk7.home = "San Francisco"
wk7.opponent = "Kansas City"
wk7.yards = 154
wk7.TDs = 0
wk7.INTs = 2
wk7.F = 0
wk7.FPTS = 12.06
wk7.notes = ""

mahomes_2024_weeks.append(wk7)

wk8 = Week()
wk8.home = "Las Vegas"
wk8.opponent = "Kansas City"
wk8.yards = 262
wk8.TDs = 2
wk8.INTs = 1
wk8.F = 0
wk8.FPTS = 18.18
wk8.notes = ""

mahomes_2024_weeks.append(wk8)

wk9 = Week()
wk9.home = "Kansas City"
wk9.opponent = "Tampa Bay"
wk9.yards = 291
wk9.TDs = 3
wk9.INTs = 0
wk9.F = 0
wk9.FPTS = 24.54
wk9.notes = ""

mahomes_2024_weeks.append(wk9)

wk10 = Week()
wk10.home = "Kansas City"
wk10.opponent = "Denver"
wk10.yards = 266
wk10.TDs = 1
wk10.INTs = 0
wk10.F = 0
wk10.FPTS = 16.54
wk10.notes = ""

mahomes_2024_weeks.append(wk10)

wk11 = Week()
wk11.home = "Buffalo"
wk11.opponent = "Kansas City"
wk11.yards = 196
wk11.TDs = 3
wk11.INTs = 2
wk11.F = 0
wk11.FPTS = 15.84
wk11.notes = ""

mahomes_2024_weeks.append(wk11)

wk12 = Week()
wk12.home = "Carolina"
wk12.opponent = "Kansas City"
wk12.yards = 269
wk12.TDs = 3
wk12.INTs = 0
wk12.F = 0
wk12.FPTS = 28.76
wk12.notes = ""

mahomes_2024_weeks.append(wk12)

wk13 = Week()
wk13.home = "Kansas City"
wk13.opponent = "Las Vegas"
wk13.yards = 306
wk13.TDs = 1
wk13.INTs = 0
wk13.F = 0
wk13.FPTS = 16.64
wk13.notes = ""

mahomes_2024_weeks.append(wk13)

wk14 = Week()
wk14.home = "Kansas City"
wk14.opponent = "Los Angeles"
wk14.yards = 210
wk14.TDs = 1
wk14.INTs = 0
wk14.F = 0
wk14.FPTS = 14.1
wk14.notes = ""

mahomes_2024_weeks.append(wk14)

wk15 = Week()
wk15.home = "Cleveland"
wk15.opponent = "Kansas City"
wk15.yards = 159
wk15.TDs = 2
wk15.INTs = 0
wk15.F = 0
wk15.FPTS = 15.76
wk15.notes = ""

mahomes_2024_weeks.append(wk15)

wk16 = Week()
wk16.home = "Kansas City"
wk16.opponent = "Houston"
wk16.yards = 260
wk16.TDs = 1
wk16.INTs = 0
wk16.F = 0
wk16.FPTS = 23.7
wk16.notes = ""

mahomes_2024_weeks.append(wk16)

wk17 = Week()
wk17.home = "Pittsburgh"
wk17.opponent = "Kansas City"
wk17.yards = 0
wk17.TDs = 0
wk17.INTs = 0
wk17.F = 0
wk17.FPTS = 0
wk17.notes = "not yet played"

mahomes_2024_weeks.append(wk17)

wk18 = Week()
wk18.home = "Denver"
wk18.opponent = "Kansas City"
wk18.yards = 0
wk18.TDs = 0
wk18.INTs = 0
wk18.F = 0
wk18.FPTS = 0
wk18.notes = "not yet played"

mahomes_2024_weeks.append(wk18)

# Calculate which week was Mahomes' best
maximum=0
for item in mahomes_2024_weeks:
    if maximum <= item.FPTS:
        maximum = item.FPTS
print("Mahomes_2024_weeks maximum: {0}".format(maximum))

# Calculate average of Mahomes' weeks
sumz=0
count=0
for item in mahomes_2024_weeks:
    if (item.notes!="Bye week" and item.notes!="not yet played"):
        sumz+=item.FPTS
        count+=1
calculation = sumz/count
average = round(calculation,1)
print("Mahomes_2024_weeks average: {0}".format(average))

# Calculate home record for Mahomes

# Calculate home points average
sumz_home=0
count_home=0
sumz_away=0
count_away=0
for item in mahomes_2024_weeks:
    if (item.home=="Kansas City" and item.notes!="Bye week" and item.notes!="not yet played"):
        sumz_home+=item.FPTS
        count_home+=1
    elif (item.opponent=="Kansas City" and item.notes!="Bye week" and item.notes!="not yet played"):
        sumz_away+=item.FPTS
        count_away+=1
calculation_home = sumz_home/count_home
average_home = round(calculation_home,1)
print("Mahomes_2024_weeks home average: {0}".format(average_home))

calculation_away = sumz_away/count_away
average_away = round(calculation_away,1)
print("Mahomes_2024_weeks away average: {0}".format(average_away))
#print(sumz_away)
#print(sumz)
#print(count_away)
#print(count)

# Setup Team objects and their Rankings
pit = Team()
pit.name = "Steelers"
pit.city = "Pittsburgh"
pit.rankings_against_qbs = 4 # The higher the rank, the better
pit.rankings_against_wrs = 8
pit.offense = 14

print("Pittsburgh offense ranking: {0}".format(pit.offense))

# Was week1 a home game for Mahomes? Looks like it. But we need a function to determine that - Completed 12/23/24
# How does Mahomes fair on the road? Road win percentage in his career 12/23/24
# mahomes has not had an interception in 5 straight weeks (as of Week 16), function to "notice" this
# Who had the best week1 performance on my team among wrs? among rbs? of my qbs?
# How to determine if player started a certain week? For flex and waiver wire guys

# make sure to include head-head matchups when comparing players (most notably quarterbacks)

# Did this player overachieve or underachieve based on where he was drafted in the fantasy draft?

# WHat percentage of the time does San frnacisco run the ball?
# WHat percentage of these touches will go to X player?
# WHat percentage of these yards will go to X player

# Average 200 yards rushing
# McCaffrey gets 50% of the touches, 50% of the yards
# 20% more if playing Panthers. How many yards does the Panthers defense give up?

# Stephon Diggs had an injury

