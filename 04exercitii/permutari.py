from itertools import combinations
dictionar = {"1": "abc", "2": "s", "3": "o", "4": "n", "5": "lm", "6": "jk", "7": "gi", "8": "def", "9": "abc"}

all_values = "".join(dictionar.values())

comb2litere = list(combinations(all_values, 2))

print(comb2litere)

for i in comb2litere:
    print("".join(i))
