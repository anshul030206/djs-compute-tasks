def detect_aliens(dna_list):
    i=0
    Aliens=[]
    Humans=[]
    while i<len(dna_list):
        temp=dna_list[i][::-1]
        if temp[0]=="Z" and temp[1]=="X":
            Aliens.append(dna_list[i])
            i=i+1
        elif "QW" in dna_list[i]:
            Aliens.append(dna_list[i])
            i=i+1
        elif len(dna_list[i])>12:
            Aliens.append(dna_list[i])
            i=i+1
        else:
            Humans.append(dna_list[i])
            i=i+1

    print("Aliens:",Aliens)
    print("Humans:",Humans)




dna_list = ["ATCGXZ", "AATGQWGG", "TTAGCTA", "GATTACAGATTACA", "AXGTQWGGGXZ", "ATTGTCTA"]
detect_aliens(dna_list)
