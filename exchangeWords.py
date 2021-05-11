
def front_back(word):
    if len(word)>1:
        print(word[len(word)-1]+word[1:len(word)-1]+word[0])
    else:
        print(word)

front_back("a")
