import sys, re


def filter_dict_stat(dict_file):
    with open(dict_file) as f:
        all_words = f.readlines()

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




def get_top_letter(letters_dict, start=0, stop=20):
    sorted_stats = {k: v for k, v in sorted(letters_dict.items(), key=lambda item: item[1], reverse=True)}
    print()
    top_letters = tuple(sorted_stats.keys())[start:stop]
    return top_letters



def main():

    file_name = sys.argv[1]


    filtered, stats = filter_dict_stat(file_name)

    top_letters = get_top_letter(stats, 0, 10)

    top_reg = ''.join(top_letters[:5])
    print(top_reg)
    to_compile = '['+top_reg+']'
    p = re.compile(to_compile*5)

    alt_p = re.compile('f[^lh]ame')

    letters = ''

    matched_words = []
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