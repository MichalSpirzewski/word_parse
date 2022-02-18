import sys, re
import wordle as wrd


def filter_dict_stat(all_words):

    stats = {}

    filtered_words = []

    for word in all_words:
        word = word.lower().strip()
        if "'" in word or len(word) != 5:
            continue
        filtered_words.append(word)
        for letter in word:
            try:
                stats[letter] += 1
            except:
                stats[letter] = 1

    return filtered_words, stats




def get_top_letter(letters_dict, start=0, stop=30):
    sorted_stats = {k: v for k, v in sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)}
    top_letters = list(sorted_stats.keys())[start:stop]
    return top_letters



def filter_excluded(a_dictionary, excluded):
    #####
    # pętla na exclude-y:
    #####

    excluded_indices = []
    for k, word in enumerate(a_dictionary[:]):
        for exl in excluded:
            if exl in word:
                excluded_indices.append(k)

    for excl_ind in list(set(excluded_indices))[::-1]:
        a_dictionary.pop(excl_ind)
    return a_dictionary


def word_from_letters(some_dict, letters, top_count=5):
    top_reg = ''.join(letters)
    to_compile = '['+top_reg[:top_count]+']'
    t_comp_2 = to_compile*5
    first_guess = re.compile(t_comp_2)
    all_possible = []
    for word in some_dict:
        asd = first_guess.match(word)
        if asd:
            all_possible.append(word)
    return all_possible


def filter_yellow(excluded_dict, yellow):
    #####
    # Pętla na yellow letters
    #####

    yellow_included_list = []
    if len(yellow) != 0:
        for word in excluded_dict:
            for incl in yellow:
                if incl not in word:
                    break
            else:
                yellow_included_list.append(word)
    else:
        yellow_included_list = excluded_dict
    return yellow_included_list


def filter_green(yellow_dictonary, green):
    green = re.compile(green)
    green_match = []
    for word in yellow_dictonary:
        if green.match(word):
            green_match.append(word)
    return green_match




def main(language, *grupy):
    if language == 'en':
        file_name = 'new_words.txt'
    elif language == 'pl':
        top_count = 6
        file_name = 'nowe_slowa.txt'
    # file_name = sys.argv[1]
    excluded, yellow, green = grupy
    with open(file_name) as f:
        all_words = f.readlines()
    filtered, stats = filter_dict_stat(all_words)
    top_letters = get_top_letter(stats)
    # print(top_letters)
    #### Jeżeli excluded == 0, to robi słowo ze statystki calego słownika
    if len(wrd.excluded) == 0:
        words = word_from_letters(filtered, top_letters)
        print(words)
    else:
        excluded_dict = filter_excluded(filtered, excluded)
        yellow_dict = filter_yellow(excluded_dict, yellow)
        green_dict = filter_green(yellow_dict, green)
        _, green_stats = filter_dict_stat(green_dict)
        green_top_letters = get_top_letter(green_stats)
        green_words = word_from_letters(green_dict, green_top_letters, top_count)

        print(5, green_words[:20])




if __name__ == '__main__':
    # main()
    excluded = 'dupa'
    yellow = ''
    green = '.....'
    main('pl', excluded, yellow, green)