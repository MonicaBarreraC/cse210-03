import random

class Word:
        def __inti__(self):
                """Constructor
                
                Args: self (Word)
                """
                
                self._word = ""

        def get_word(self):
                """
                Select a random word from the list of word

                Args: self (Word)
                """
                words = ["ant", "arrow", "apple", "assume", "barn", "beetle", "business", "broom", "cold",
                "code", "client", "charge", "company", "combination", "duke", "dump", "disco",
                "ditch", "discover", "discount", "eat", "earn", "effort", "envelope", "explain",
                "efficient", "effusion", "four", "front", "flame", "fortify", "further", "forgive",
                "frenetic", "gloves", "globe", "grant", "garbage", "haunt", "hire", "harmony", "handicap",
                "hardware", "item", "issue", "intense", "intelligent", "joint", "jump", "jealous", "jelly",
                "jacksaw", "kabbalah", "knee", "kangaroo", "keyboard", "knowledge", "leaf",
                "lollipop", "lobster", "ladybug", "legend", "mother", "moisture", "myself", "military",
                "momentum", "nail", "nose", "number", "necklace", "notebook", "open", "orange",
                "only", "outdoors", "output", "octagon", "pencil", "pardon", "perceptive", "personal",
                "persuasive", "peaceful", "quiet", "queen", "question", "quantity", "rabbit",
                "rainbow", "rectangle", "rocket", "revolutionary", "squash", "skeleton",
                "sepeaker","smooth", "sorry", "sandals", "turtle", "tomato", "thanks", "trouble",
                "traditional", "toilet", "umbrella", "unicorn", "uniform", "unique", "upgrade",
                "volcano", "vacuum", "vegetables", "vanilla", "vacation", "wagon", "watermelon",
                "wheat", "western", "wealth", "website", "xenon", "xylophone", "young", "yolk",
                "yucca", "yard", "yellow", "zircon", "zipper", "zigzag", "zombie"]

                self._word = random.choice(words).upper()
                return self._word
