import math
def Euclidean_distance(coords):
    distance={}
    i=0
    while i<len(coords):
        temp=coords[i]
        x=int(temp[0])
        y=int(temp[1])
        distance[x,y]=(round(math.sqrt(x*x+y*y),2))
        i=i+1
    return distance

coords = [(3, 4), (1, 1), (0, 5), (2, -2), (5, 7)]
dist=Euclidean_distance(coords)
print(dist)
