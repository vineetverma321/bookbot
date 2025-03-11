def count_words(str):
    words = str.split()
    num_words = 0
    for word in words:
            num_words+= 1
    print(f"Found {num_words} total words") 

def count_char(str):
    # chars = str.split("")
    count_dict = {}
    for char in str:
        if char.lower() in count_dict:
                count_dict[char.lower()]+= 1
        else:
                count_dict[char.lower()] = 1
    return count_dict

def sort_on(dict):
      return dict["count"]

def sorted_dict(dict):
    list_dict = []
    for key, value in dict.items():
            row_dict = {"character": key, "count": value}
            list_dict.append(row_dict)
    list_dict.sort(key = sort_on, reverse = True)
    return list_dict
    