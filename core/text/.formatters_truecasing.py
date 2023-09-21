from talon import Module, Context, actions
import nltk

# download the punkt and maxent_ne_chunker resources
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk.chunk import ne_chunk

ctx=Context()

@ctx.action_class("user")
class UserActions:
    def truecase(text):
        words = word_tokenize(text)
        tagged = pos_tag(words)
        named_entities = ne_chunk(tagged, binary=True)
        truecased_text = ''
        for i, tree in enumerate(named_entities):
            if hasattr(tree, 'label') and tree.label() == 'NE':
                word = ' '.join([child[0] for child in tree])
                truecased_text += word
            else:
                word = tree[0]
                if i == 0 or truecased_text[-1] in ['.', '!', '?']:
                    truecased_text += word.capitalize()
                else:
                    truecased_text += word.lower()
            truecased_text += ' '
        return truecased_text


#import formatters_truecasing.py.
#"TRUECASE": (SEP, formatters_truecasing.py.truecase())
#"truecase": "TRUECASE"
