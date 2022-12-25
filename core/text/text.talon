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
contract (word | it):
    edit.word_left()
    edit.extend_word_right()
    edit.extend_word_right()
    #edit.extend_left()
    user.formatters_reformat_selection("smash")
 
<user.formatters> (word | it):
    edit.select_word()
    #edit.extend_left()
    user.formatters_reformat_selection(user.formatters)

##########
# formatters_words = {
#     "all cap": formatters_dict["ALL_CAPS"],
#     "all down": formatters_dict["ALL_LOWERCASE"],
#     "camel": formatters_dict["PRIVATE_CAMEL_CASE"],
#     "dotted": formatters_dict["DOT_SEPARATED"],
#     "dub string": formatters_dict["DOUBLE_QUOTED_STRING"],
#     #"dunder": formatters_dict["DOUBLE_UNDERSCORE"],
#     "hammer": formatters_dict["PUBLIC_CAMEL_CASE"],
#     "kebab": formatters_dict["DASH_SEPARATED"],
#     "packed": formatters_dict["DOUBLE_COLON_SEPARATED"],
#     "padded": formatters_dict["SPACE_SURROUNDED_STRING"],
#     "slasher": formatters_dict["SLASH_SEPARATED"],
#     "smash": formatters_dict["NO_SPACES"],
#     "snake": formatters_dict["SNAKE_CASE"],
#     "string": formatters_dict["SINGLE_QUOTED_STRING"],
#     "title": formatters_dict["CAPITALIZE_ALL_WORDS"],
# 
#     #Added to be used by "<user.formatters> word"
#     "capitalize": formatters_dict["CAPITALIZE_ALL_WORDS"],
#     #"cap": formatters_dict["CAPITALIZE_ALL_WORDS"],
#     "ship": formatters_dict["CAPITALIZE_ALL_WORDS"],
#     "sink": formatters_dict["ALL_LOWERCASE"],
# }