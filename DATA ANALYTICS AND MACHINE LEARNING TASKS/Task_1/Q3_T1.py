def count_supplies(supplies):
    i=0
    suffix=[]
    while i<len(supplies):
        temp=supplies[i].split("-")
        suffix.append(temp[0])
        i=i+1

    i=0
    counts = {"MED": 0, "FOOD": 0, "WPN": 0}
    while i<len(suffix):
        if suffix[i]==("MED"):
            counts["MED"] += 1
            i=i+1

        elif suffix[i]==("FOOD"):
            counts["FOOD"] += 1
            i=i+1

        elif suffix[i]==("WPN"):
            counts["WPN"] += 1
            i=i+1
    print(counts)


count_supplies(supplies = ["MED-234", "FOOD-789", "WPN-101", "MED-456", "FOOD-321"])
