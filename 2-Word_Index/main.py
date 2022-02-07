import os
import fileinput
import re
import json

INPUT_FILE_PATH = os.path.join(os.path.dirname(__file__),
                               "donQuixoteOfLaMancha.txt")

OUTPUT_FILE_PATH = os.path.join(os.path.dirname(__file__),
                                "donQuixoteOfLaMancha_wordIndex.txt")


def getUpdatedDict(org_dict, new_word, number_line):
    '''From the given dictionary search for the new_word as a key. If exists
    adds the line number to the list, if not creates new key with the line as
    value.
    '''

    if new_word in org_dict:
        new_list = org_dict[new_word]
        if number_line not in new_list:
            new_list.append(number_line)
        org_dict[new_word] = new_list
    else:
        org_dict[new_word] = [number_line]
    return org_dict


def main():
    '''Executes main function'''

    word_dict = {}
    count = 1
    for lines in fileinput.input([INPUT_FILE_PATH]):
        words = lines.split()
        for word in words:
            clean_word = re.sub(r'[^a-zA-Z0-9]', '', word)
            word_dict = getUpdatedDict(word_dict, clean_word.lower(), count)
        count += 1

    word_dict_ord = dict(sorted(word_dict.items()))
    dict_encoded = json.dumps(word_dict_ord, indent=2).encode("utf-8")

    with open(OUTPUT_FILE_PATH, "wb") as file:
        file.write(dict_encoded)
        file.close


if __name__ == "__main__":
    main()
