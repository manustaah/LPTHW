import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is -a %%%.",
    "class %%%(object):\n\tdef__init__(self, ***)":
        "class %%% has -a __init__ that takes self and *** parameters".
    "class %%%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters."
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@."
    "***.*** = '***'":
        "From *** get the *** attributes and set it to '***'."
        }
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for words in urlopen(WORD_URL).redlines()_
    WORDS.append(word.strip())

dev convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
        other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.joing(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results



try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, # QUESTION:

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer

exept EOFError:
    print "]\nBye"
