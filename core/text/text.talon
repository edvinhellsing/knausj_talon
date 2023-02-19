#provide both anchored and unachored commands via 'over'
phrase <user.text>$:
    user.add_phrase_to_history(text)
    insert(text)
phrase <user.text> over:
    user.add_phrase_to_history(text)
    insert(text)
{user.prose_formatter} <user.prose>$: user.insert_formatted(prose, prose_formatter)
{user.prose_formatter} <user.prose> over: user.insert_formatted(prose, prose_formatter)
<user.format_text>+$: user.insert_many(format_text_list)
<user.format_text>+ over: user.insert_many(format_text_list)
<user.formatters> selection: user.formatters_reformat_selection(user.formatters)
word <user.word>:
    user.add_phrase_to_history(word)
    insert(word)
recent list: user.toggle_phrase_history()
recent close: user.phrase_history_hide()
recent repeat <number_small>:
    recent_phrase = user.get_recent_phrase(number_small)
    user.add_phrase_to_history(recent_phrase)
    insert(recent_phrase)
recent copy <number_small>: clip.set_text(user.get_recent_phrase(number_small))
# Maybe the commands below should use that instead of it after all
select that: user.select_last_phrase()
before that: user.before_last_phrase()
(nope | scratch) it: user.clear_last_phrase()
nope it was <user.formatters>: user.formatters_reformat_last(formatters)

#pre (say | speak | sentence)
pre {user.prose_formatter} <user.prose>$: 
    key(space)
    user.insert_formatted(prose, prose_formatter)

#post (say | speak | sentence)
post {user.prose_formatter} <user.prose>$: 
    user.insert_formatted(prose, prose_formatter)
    key(space)

#In Google docs an additional edit.extend_left() seems to be needed but not in other applications/websites
select around: 
    edit.word_left()
    edit.extend_word_right()
    edit.extend_word_right()
    #edit.extend_left()

#go word left: edit.word_left()
#go word right: edit.word_right()
contract (word | words):
    edit.word_left()
    edit.extend_word_right()
    edit.extend_word_right()
    #edit.extend_left()
    user.formatters_reformat_selection("smash")

(sink | sunk | lowercase) (word | it):
    edit.select_word()
    user.formatters_reformat_selection("all down")
    edit.left()

(ship | uppercase) (word | it):
    edit.select_word()
    user.formatters_reformat_selection("title")
    edit.left()

#(ship | uppercase) beginning:
    #actions.user.engine_mimic("navigate left period")
    #user.navigation('GO', 'left', 'DEFAULT', 'DEFAULT', re.compile('\\.', re.IGNORECASE), 1)
    #user.history_transform_phrase_text(['navigate', 'left', 'period'])

(ship | uppercase) beginning:
    edit.line_start()
    edit.select_word()
    user.formatters_reformat_selection("title")
    edit.left()

# <user.formatters> (word | it):
#     edit.select_word()
#     user.formatters_reformat_selection(user.formatters)

##########
# formatters_words = {
#     "all cap": formatters_dict["ALL_CAPS"], #THIS IS A STRING
#     "all down": formatters_dict["ALL_LOWERCASE"], #this is a string
#     "camel": formatters_dict["PRIVATE_CAMEL_CASE"], #thisIsAString
#     "dotted": formatters_dict["DOT_SEPARATED"], #this.is.a.string
#     "dub string": formatters_dict["DOUBLE_QUOTED_STRING"], #"this is a string"
#     #"dunder": formatters_dict["DOUBLE_UNDERSCORE"],
#     "hammer": formatters_dict["PUBLIC_CAMEL_CASE"], #ThisIsAString
#     "kebab": formatters_dict["DASH_SEPARATED"], #this-is-a-string
#     "packed": formatters_dict["DOUBLE_COLON_SEPARATED"], #this::is::a::string
#     "padded": formatters_dict["SPACE_SURROUNDED_STRING"], # this is a string 
#     "slasher": formatters_dict["SLASH_SEPARATED"], #/this/is/a/string
#     "smash": formatters_dict["NO_SPACES"], #thisisastring
#     "snake": formatters_dict["SNAKE_CASE"], #this_is_a_string, underscore separated string
#     "string": formatters_dict["SINGLE_QUOTED_STRING"], #'this is a string'
#     "title": formatters_dict["CAPITALIZE_ALL_WORDS"], #This is a String
# 
#     #Added to be used by "<user.formatters> word"
#     "capitalize": formatters_dict["CAPITALIZE_ALL_WORDS"],
#     "ship": formatters_dict["CAPITALIZE_ALL_WORDS"],
#     "sink": formatters_dict["ALL_LOWERCASE"],
# }