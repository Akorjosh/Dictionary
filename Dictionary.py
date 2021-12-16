import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


def dictionary(deff):
    dic = json.load(open("dictionary_compact.json"))

    deff = input("What word would you like to know the meaning of?: ")
    deff = deff.lower()

    if deff in dic:
        print(dic[deff])
    else:
        print("Word does not exist")
    
        real_word = input("did you mean %s instead? :(Y/N)" % get_close_matches(deff, dic.keys(), cutoff=0.8)[0])
        actual_word = get_close_matches(deff, dic.keys(), cutoff=0.8)[0]

        real_word.lower()

        if real_word == "y":
            print(dic[actual_word])
        else:
            print("No such word exists")


dictionary("word")

