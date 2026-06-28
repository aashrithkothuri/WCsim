import json

with open("initial.json","r") as f:
    matches = json.load(f)

with open("elos.json","r") as f:
    elos = json.load(f)

# No valid implementation for now
def get_winner(t1,t2):
    return t1

rounds = ["r32","r16","Q","SF","F"]

for round in rounds:

    for match in matches.keys():

        if match.startswith(round):

            if matches[match]["winner"] is not None:
                continue

            team1 = matches[match]["teams"][0]
            team2 = matches[match]["teams"][1]

            winner = get_winner(team1,team2)

            matches[match]["winner"] = winner

            if round != "F":
                next_match = matches[match]["next_match"]
                matches[next_match]["teams"].append(winner)


print(matches["F"])