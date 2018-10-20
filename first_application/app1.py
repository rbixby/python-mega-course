import json
import glob2

from difflib import get_close_matches

the_file = glob2.glob('**/data.json')
data = json.load(open(the_file[0]))

def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes, or N for no: " % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return "That word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "That word cannot be found in the dictionary. Please double check it."

w = input("Enter a word: ")

output = get_definition(w)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
