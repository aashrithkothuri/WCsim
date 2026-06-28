import json
import numpy as np

with open("initial.json","r") as f:
    matches = json.load(f)

with open("elos.json","r") as f:
    elos = json.load(f)

# No valid implementation for now
def get_winner(t1,t2):
    elo1 = elos[t1]
    elo2 = elos[t2]

    TOTAL_RATE = 2.7
    SCALE = 600

    # Calculates average goal rate for each team
    # then calculates goals using poisson (goals in 90-120 mins excluding pens)

    elo_diff = elo1 - elo2
    rate1 = TOTAL_RATE * 1/(1 + 10 ** (-elo_diff/SCALE))
    rate2 = TOTAL_RATE - rate1

    goals1 = np.random.poisson(rate1)
    goals2 = np.random.poisson(rate2)

    if goals1 > goals2:
        return t1
    elif goals1 < goals2:
        return t2
    else: # 50-50 chance if it goes to pens
        return str(np.random.choice([t1,t2]))

rounds = ["r32","r16","Q","SF","F"]
for round in rounds:

    for match in matches.keys():

        if match.startswith(round):
            
            # Gets winner, updates current match with winner 
            # then adds winning team to next match

            if matches[match]["winner"] is not None:
                continue

            team1 = matches[match]["teams"][0]
            team2 = matches[match]["teams"][1]

            winner = get_winner(team1,team2)

            matches[match]["winner"] = winner

            if round != "F": # Final does not have a next match
                next_match = matches[match]["next_match"]
                matches[next_match]["teams"].append(winner)


print(matches)