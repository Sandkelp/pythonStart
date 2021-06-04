import json
from difflib import get_close_matches
data = json.load(open("C:\\Users\\ssubh\\OneDrive\\Desktop\\python\\Basic\\data.json"))

def define_wrd(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead?(Enter y/n): " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return get_close_matches(w, data.keys())[0]
        elif yn == "n":
            return "the word you entered does not exist, double check it"
        
        else:
            return "We did not understand what you entered."
            
    
    else:
        return "Im sorry that word does not seem to be in the dictionary."

word = input("What word do you need defined?: ")

output = define_wrd(word)

if type(output) == list:
    for item in output:
        print(item)
