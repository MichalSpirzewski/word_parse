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


def make_guess(a_dict, letters):

    if len(wrd.excluded) == 0:
        top_reg = ''.join(letters)
        to_compile = '['+top_reg[:5]+']'
        t_comp_2 = to_compile*5
        first_guess = re.compile(t_comp_2)
        first_words = []
        all_possible = []
        for word in a_dict:
            asd = first_guess.match(word)
            if asd:
                all_possible.append(word)
            for x in top_reg[:5]:
                if x not in word:
                    break
            else:
                first_words.append(word)
            # break

        # print(sorted(all_possible))
        # print(first_words)

    green = re.compile(wrd.green)
    matched_words = []
    #####
    # pętla na exclude-y:
    #####
    excluded_words_1 = []
    for word in a_dict:
        for exl in wrd.excluded:
            if exl in word:
                excluded_words_1.append(word)

    included_list = []
    for word in a_dict:
        if word in excluded_words_1:
            continue
        else:
            included_list.append(word)

    #####
    # Pętla na yellow letters
    #####
    yellow_included_list = []
    if len(wrd.yellow) != 0:
        for word in included_list:
            for incl in wrd.yellow:
                if incl not in word:
                    break
            else:
                yellow_included_list.append(word)
    else:
        yellow_included_list = included_list

    #####
    # Pętla na green letters
    #####
    last_match_words = []
    for word in yellow_included_list:
        match = green.match(word)
        # print(word)
        if match:
            last_match_words.append(word)

    print(last_match_words)
    #! TUTAJ TRZEBA POPRAWIĆ
    sys.exit()

    # for word in a_dict:
    #     if len(letters) != 0:


    #         for x in wrd.yellow:
    #             if x in word:
    #                 break
    #         else:
    #             m = red.match(word)
    #             if m:
    #                 matched_words.append(word)

    # new_match = []
    # excluded_words = []
    # for word in matched_words:
    #     for exl in wrd.excluded:
    #         if exl in word:
    #             excluded_words.append(word)
    # for word in matched_words:
    #     if word in excluded_words:
    #         continue
    #     print(word)

    # # print(matched_words)
    # # print('1', new_match)
    return matched_words

def main():

    file_name = sys.argv[1]

    with open(file_name) as f:
        all_words = f.readlines()

    filtered, stats = filter_dict_stat(all_words)
    top_letters = get_top_letter(stats)



    pierwszy = make_guess(filtered, top_letters)
    # print(pierwszy)

    new_filtr, new_stats = filter_dict_stat(pierwszy)
    new_top = get_top_letter(new_stats)

    # print(new_top)

    sys.exit()

    alt_p = re.compile('f[^lh]ame')

    letters = ''

    print(len(filtered))
    for word in filtered[:]:
        if len(letters) != 0:
            for x in letters:
                if x not in word:
                    break
            else:
                print(word)
                m = alt_p.match(word)
                if m:
                    matched_words.append(word)

    print(matched_words)


if __name__ == '__main__':
    main()