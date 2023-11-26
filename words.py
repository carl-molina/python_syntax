def print_upper_words(words, must_start_with = {"e"}):
    """Takes a list of words; prints each words on a separate line in
    uppercase"""
    for word in words:
        word = word.upper()
        for letter in must_start_with:
            if word.startswith(letter.upper()):
                print(word)


word_list = ["hi", "who", "what", "emerge", "Event"]

print_upper_words(word_list)

print_upper_words(
    ["hello", "hey", "goodbye", "yo", "yes"],
    must_start_with={"h", "y"})