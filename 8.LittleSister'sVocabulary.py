"""Instructions

You are helping your younger sister with her English vocabulary homework, which she is finding very tedious. Her class is learning to create new words by adding prefixes and suffixes. Given a set of words, the teacher is looking for correctly transformed words with correct spelling by adding the prefix to the beginning or the suffix to the ending.

The assignment has four activities, each with a set of text or words to work with.

Task 1: Add a prefiz to a word
 One of the most common prefixes in English is un, meaning "not". In this activity, your sister needs to make negative, or "not" words by adding un to them.

 Implement the add_prefix_un(<word>) function that takes word as a parameter and returns a new un prefixed word.

Task 2: Add prefixes to word groups
 There are four more common prefixes that your sister's class is studying: en (meaning to 'put into' or 'cover with'), pre (meaning 'before' or 'forward'), auto (meaning 'self' or 'same'), and inter (meaning 'between' or 'among').

 In this exercise, the class is creating groups of vocabulary words using these prefixes, so they can be studied together. Each prefix comes in a list with common words it's used with. The students need to apply the prefix and produce a string that shows the prefix applied to all of the words.

 Implement the make_word_groups(<vocab_words>) function that takes a vocab_words as a parameter in the following form: [<prefix>, <word_1>, <word_2> .... <word_n>], and returns a string with the prefix applied to each word that looks like: '<prefix> :: <prefix><word_1> :: <prefix><word_2> :: <prefix><word_n>'.

Task 3: Remove a suffix from a word
 ness is a common suffix that means 'state of being'. In this activity, your sister needs to find the original root word by removing the ness suffix. But of course there are pesky spelling rules: If the root word originally ended in a consonant followed by a 'y', then the 'y' was changed to 'i'. Removing 'ness' needs to restore the 'y' in those root words. e.g. happiness --> happi --> happy.

 Implement the remove_suffix_ness(<word>) function that takes in a word, and returns the root word without the ness suffix.
 
Task 4: Extract and transform a word
 Suffixes are often used to change the part of speech a word is assigned to. A common practice in English is "verbing" or "verbifying" -- where an adjective becomes a verb by adding an en suffix.

 In this task, your sister is going to practice "verbing" words by extracting an adjective from a sentence and turning it into a verb. Fortunately, all the words that need to be transformed here are "regular" - they don't need spelling changes to add the suffix.

 Implement the adjective_to_verb(<sentence>, <index>) function that takes two parameters. A sentence using the vocabulary word, and the index of the word, once that sentence is split apart. The function should return the extracted adjective as a verb.
 
"""

def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    result = f"{prefix}"
    for word in range(1, len(vocab_words)):
        result += f" :: {prefix + vocab_words[word]}"
    return result
    
def remove_suffix_ness(word):
    root = word[:-4]
    if root[-1] == "i":
        return root.replace("i", "y")
    return root

def adjective_to_verb(sentence, index):
    palavras = sentence.split()
    req = palavras[index]
    if req[-1] == ".":
        req = req[:len(req) -1]
    return req + "en"
