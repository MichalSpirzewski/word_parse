import sys, re
import matplotlib.pyplot as plt




def main():

    file_name = sys.argv[1]

    with open(file_name) as f:
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

            # print(letter)
            # break
        # print(word)
        # break

    # print(stats)
    sorted_stats = {k: v for k, v in sorted(stats.items(), key=lambda item: item[1], reverse=True)}
    top_letters = tuple(sorted_stats.keys())[:10]
    top_reg = ''.join(top_letters[:6])
    print(top_reg)
    to_compile = '['+top_reg+']'
    p = re.compile(to_compile*5)

    matched_words = []
    for word in filtered_words[:]:
        m = p.match(word)
        if m:
            matched_words.append(word)
    print(matched_words)
    # plt.bar(stats.keys(), list(stats.values()))
    # plt.savefig(file_name.replace('txt', 'png'))
    # plt.close()


if __name__ == '__main__':
    main()