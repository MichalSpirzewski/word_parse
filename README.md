# word_parse
word dictionary parser for `wordle` game


# Algorythm

1. Find all 5-letter words
1. Find and sort most commonly used letters.
1. Find a word with 5 most commonly used letters.
1. Use this word to solve the puzzle.
 - If no information was found at all, find a word with 2nd 5 most commonly used letters and guess.
 - If some information was found