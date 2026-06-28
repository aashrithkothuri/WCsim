from sim import simulate
import json

winners = {
  "Germany": 0,
  "Paraguay": 0,
  "France": 0,
  "Sweden": 0,

  "South Africa": 0,
  "Canada": 0,
  "Netherlands": 0,
  "Morocco": 0,

  "Portugal": 0,
  "Croatia": 0,
  "Spain": 0,
  "Austria": 0,

  "United States": 0,
  "Bosnia and Herzegovina": 0,
  "Belgium": 0,
  "Senegal": 0,

  "Brazil": 0,
  "Japan": 0,
  "Ivory Coast": 0,
  "Norway": 0,

  "Mexico": 0,
  "Ecuador": 0,
  "England": 0,
  "DR Congo": 0,

  "Argentina": 0,
  "Cape Verde": 0,
  "Australia": 0,
  "Egypt": 0,

  "Switzerland": 0,
  "Algeria": 0,
  "Colombia": 0,
  "Ghana": 0
}

winner = ""
c = 0
while winner != "Switzerland":
    result = simulate()
    winner = result["F"]["winner"]
    c+=1
    print(c)

print(json.dumps(result, indent=2))