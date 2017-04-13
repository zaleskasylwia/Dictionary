import csv

dictionary = {"FUNCTION": ("co to f", "zrodlo f"), "PARAMETR": ("co to parametr", "zrodlo p"), 
                "VARIABLE": ("co to variable", "zrodlo v"), "ARGUMENT": ("co to argument", "zrodlo a"), 
                "DICTIONARY": ("co to dictionary", "zrodlo d"), "TUPLE": ("co to tuple", "zrodlo t"), 
                "ASCII table": ("co to ascii", "zrodlo asc"),"MODULE": ("co to module", "zrodlo m"),
                "LIST": ("co to list", "zrodlo l"),"CONDITIONAL": ("co to conditional", "zrodlo c"),
                "LOOPS": ("co to loops", "zrodlo lo"),"BUILT-IN": ("co to built-in", "zrodlo b"),
                "SLOTS": ("co to slots", "zrodlo s"),"GENERATORS": ("co to generators", "zrodlo g"),
                "CLASSES": ("co to classes", "zrodlo cl")}

with open('dictionary1.csv', 'w') as f:  
    w = csv.DictWriter(f, dictionary.keys())
    w.writeheader()
    w.writerow(dictionary)
    

#1
def search():
    print("Tell definition would you want to find")
    name = input().upper()
    if dictionary.get(name):
        print(dictionary.get(name))
    else:
        print("Dictionary don't have this definition")

#2
def add():
    print("Tell me a definition")
    defintion = input().upper()
    print("Tell me explenation")
    explenation = input()
    print("Tell me source")
    source = input()
    dictionary.update({defintion: (explenation, source)})
    print(dictionary)


#3
def show_all():
    for definition in sorted(dictionary.items()):
        print(definition[0])

#4
def show_available():
    print("Tell me first letter of a word")
    key_first_letter = input().upper() 
    if len(key_first_letter) == 1:
        for definition, explanation in sorted(dictionary.items()):
            if definition[0] == key_first_letter:
                print(definition,explanation)
    else:
        print("Tell me just one")


def main():
    while True:
        # read_from_csv("nazwa.csv")
        print("Dictionary for a little programmer:")
        print("1 - serach")
        print("2 - add")
        print("3 - show all appellations alphabetically")
        print("4 - show all by first letter")
        print("0 - exit")
        print("Tell me a number from 0 to 4")

        #input_read = int(input()) #nie odporny na dupa
        input_read = input()
        #yes = input_read.isdigit()
        if input_read.isdigit():
            #print ("ok")
            input_read = int(input_read)
        else: 
            print("It's not a number from 0 to 4")
        

        
        #while yes:
        if input_read == 1:
            search()
        elif input_read == 2:
            add()
        elif input_read == 3:
            show_all()
        elif input_read == 4:
            show_available()
        elif input_read == 0:
            return
        else:
            print("In menu no such a number, try again'\n") #zeby wracało???

        #else:
            #print("Type a number from 0 to 4")

        ask = ""
        while not (ask == 'YES' or ask== 'NO'):                                     #ask about game again
            ask = input("Do you want to try again? (YES/NO) ").upper()
        if ask == 'NO':
            break

main()

    
