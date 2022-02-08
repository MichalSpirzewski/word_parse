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

        print(sorted(all_possible))
        print(first_words)

    # else:
    #     [letters.remove(x) for x in wrd.excluded]






    # yellow = re.compile(wrd.yellow)
    red = re.compile(wrd.red)
    matched_words = []

    for word in a_dict:
        if len(letters) != 0:
            print(word)
            for z in wrd.excluded:
                if z in word:
                    break
            else:
                break

            # break
            print(word)
            for x in wrd.yellow:
                if x not in word:
                    break
            else:
                m = red.match(word)
                if m:
                    matched_words.append(word)
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

    print(new_top)

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