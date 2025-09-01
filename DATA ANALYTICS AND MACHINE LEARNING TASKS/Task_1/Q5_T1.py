def sort_by_missions(commanders):
    commanders.sort(key=lambda x: x["missions"], reverse=True)
    print(commanders)

def sort_by_rank(commanders):
    commanders.sort(key=lambda x: x["rank"])
    print(commanders)
commanders = [
    {"name": "Xeron", "rank": 4, "missions": 20},
    {"name": "Mira", "rank": 2, "missions": 50},
    {"name": "Zara", "rank": 4, "missions": 21},
    {"name": "Rumi", "rank": 1, "missions": 75},
    {"name": "Larzon", "rank": 5, "missions": 35}
]
sort_by_missions(commanders)
sort_by_rank(commanders)
