import json
from pathlib import Path
from difflib import get_close_matches

data = Path("data.json").read_text(encoding="utf-8-sig")
words_list = json.loads(data)

def get_user_input():
    word = input("Please enter the word: ")
    return word

def confirm_new_word(word):
    return input(f" if you are looking for the meaning of the {word} enter Y:")

def search_in_dictionary(w):
    try:
        meanings = words_list[w]
        for meaning in meaning:
            print(meaning)

    except:
        similar_words = get_close_matches(w,words_list.keys() , n=5 , cutoff=0.80)
        if similar_words:
            res = confirm_new_word(similar_words[0])
            if res == "Y":
                search_in_dictionary(similar_words[0])
            else:
                print("The search has no result")

word = get_user_input()
search_in_dictionary(word)


