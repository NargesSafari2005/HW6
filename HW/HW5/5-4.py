import re


def Gword(num_difference , sentence , word) :
    special_words = []
    try :
        sentence = re.sub('[.:ØŒ]' , '' , sentence)
    except :
        pass
    finally :
        words = sentence.split()
        for x in words :
            if len(x) > len(word) + num_difference or len(x) < len(word) - num_difference :
                continue
            count = sum(1 for y in zip(x , word) if y[0] != y[1])
            count += abs(len(x) - len(word))
            if count <= num_difference :
                special_words.append(x)
        for item in special_words :
            print(item)


a = int(input())
b = input()
c = input()
Gword(a , b , c)
