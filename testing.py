#!/usr/bin/env python3

mazebertURL = "https://mazebert.com/rest/player/profile?id=";
roles = [{"name" : "Apprentice",
        "min" : 1,
        "max" : 20},
        {"name" : "Scholar",
        "min" : 21,
        "max" : 40},
        {"name" : "Master",
        "min" : 41,
        "max" : 60},
        {"name" : "Master Defender",
        "min" : 61,
        "max" : 80},
        {"name" : "Master Commander",
        "min" : 81,
        "max" : 99},
        {"name" : "King's Hand",
        "min" : 100,
        "max" : 105},
        {"name" : "King",
        "min" : 106,
        "max" : 110},
        {"name" : "Emperor",
        "min" : 111,
        "max" : 115},
        {"name" : "Master of the Universe",
        "min" : 116,
        "max" : 129},
        {"name" : "Chuck Norris",
        "min" : 130,
        "max" : 999999}]
for x in roles:
#    print(x)
    print(f"{roles.index(x)} is called {x['name']} from {x['min']} to {x['max']}.")
print(f"{roles[1]['name']}")
