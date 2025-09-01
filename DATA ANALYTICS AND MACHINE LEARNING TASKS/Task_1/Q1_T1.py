def encrypt_message(message):
    words=message.split(" ")
    i=0
    while i<len(words):
        if i%2==0:
            print(words[i],end=" ")
            i=i+1
        else:
            print(words[i][::-1],end=" ")
            i=i+1


m=input()
encrypt_message(m)