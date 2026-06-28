import json
import numpy as np
import copy

with open("initial.json","r") as f:
    initial_matches = json.load(f)

with open("elos.json","r") as f:
    elos = json.load(f)

def get_penalty_winner(t1,t2):
    BASE_PENALTY_RATE = 0.75
    SCALE = 10000

    elo1 = elos[t1]
    elo2 = elos[t2]

    elo_diff = elo1 - elo2

    prob1 = max(0.65,min(BASE_PENALTY_RATE + elo_diff/SCALE,0.85))
    prob2 = max(0.65,min(BASE_PENALTY_RATE - elo_diff/SCALE,0.85))

    # First 5 pens
    converted1 = 0
    converted2 = 0
    for taken in range(1,6):
        if np.random.random() < prob1:
            converted1 += 1

        if np.random.random() < prob2:
            converted2 += 1

        if 5-taken + converted1 < converted2:
            return t2
        
        if 5-taken + converted2 < converted1:
            return t1
        
    # Sudden death
    while True:
        if np.random.random() < prob1:
            converted1 += 1

        if np.random.random() < prob2:
            converted2 += 1

        if converted1 > converted2:
            return t1
        elif converted1 < converted2:
            return t2

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
    else: 
        return get_penalty_winner(t1,t2)

def simulate():

    matches = copy.deepcopy(initial_matches)
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

    return matches

