def count_words(text):
    words = str.split(text)
    num_words = len(words)
    print(f"Found {num_words} total words")

def count_letters(text):
    new_text = text.lower()
    words = str.split(new_text)
    letter_dict = {}
    for word in words:
        for letter in word:
            if letter not in letter_dict:
                letter_dict[letter] = 1
            else:
                letter_dict[letter]+=1
    return letter_dict

def sort_on(item):
    return item['num']

def list_of_dict(letter_dict):

    end_list = []
    for letter in letter_dict:
        curr_dict = {"char": letter, "num": letter_dict[letter]}
        end_list.append(curr_dict)
    
    end_list.sort(reverse= True, key=sort_on)
    
    for dicts in end_list:
        print(f"{dicts['char']}: {dicts['num']}")

    



    
    
    
    
