def clean_and_sort_ages():
    data = ["23", "17", "thirty", "45", "19a", "31", "20", "twenty_seven", "25c"]
    i=0
    data1=[]
    while i<len(data):
        if data[i].isnumeric():
            data1.append(int(data[i]))
            i=i+1
        else:
            i=i+1

    data1.sort()
    print(data1)

clean_and_sort_ages()
