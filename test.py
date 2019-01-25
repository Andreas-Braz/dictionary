import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def word_definition (w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]

    #if get_close_matches don't return any similar word (length = 0)
    # that means program couldn't find an alternative, so it jumps to the next
    # if statement.

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s? Enter Y for YES or N for NO: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn =="y":
            return data [get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "Word not found"
        else:
            return "Invalid imput."
    else:
        return "Word not found."

w = input("Enter a word: ")
output = word_definition(w)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)