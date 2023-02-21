def menu():
    print("Enter t for encoding text\nEnter m for decoding morse code\nEnter e to exit program\n")
def load():
    file=open('Morse.txt','r') 
    encode={}
    decode={}
    encode[" "]="   " 
    decode[" "]="   "
    for a in file:      #for loop to input morse code and english to dictionary
        key,value=a.split() 
        encode[key]=value
        decode[value]=key
    file.close()
    return (encode,decode) #returned for use in other functions
def encoding():
    encode,decode=load()
    
    c=""
    x=input("Enter text: ")
    for i in x:             #use for loop to read as letters
        if i in encode:
            c=c+encode[i] + " "
    print(c)

def decoding():
    encode,decode=load()
    y=""
    v=input("Enter text: ")
    iv=v.split("  ")
    for ii in iv:
        for iii in ii.split(" "):   #use nested loop to break down words->letters
            if iii in decode:
                y=y+decode[iii] + " "
    print(y)

def main():
    load()
    menu()
    option=input("My input is: ")
    while option != 'e':
        while option != "t" and option != "m" and option != "e": 
            print("Option not valid\n")
            option=input("Enter t for encoding text\nEnter m for decoding morse code\nEnter e to exit program\n")
        while option == 't':
            encoding()
            option=input("Enter t for encoding text\nEnter m for decoding morse code\nEnter e to exit program\n")
        while option == 'm':
            decoding()
            option=input("Enter t for encoding text\nEnter m for decoding morse code\nEnter e to exit program\n")
        while option == 'e':
            break
main()



