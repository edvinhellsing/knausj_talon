double dash: "--"
triple quote: "'''"
(triple grave | triple back tick | gravy):
    insert("```")
(dot dot | dotdot): ".."
ellipses: "..."
(comma and | spamma): ", "
comgap: ", "
arrow: "->"
dub arrow: "=>"
#new line: "\\n"
carriage return: "\\r"
line feed: "\\r\\n"
empty dubstring: user.insert_between('"', '"')
empty escaped (dubstring|dub quotes): user.insert_between('\\"', '\\"')
empty string: user.insert_between("'", "'")
empty escaped string: user.insert_between("\\'", "\\'")
(inside parens | args): user.insert_between("(", ")")
inside (squares | square brackets | list): user.insert_between("[", "]")
inside (bracket | braces): user.insert_between("{", "}")
inside percent: user.insert_between("%", "%")
inside (quotes | string): user.insert_between("'", "'")
inside (double quotes | dubquotes): user.insert_between('"', '"')
inside (graves | back ticks): user.insert_between("`", "`")
angle it:
    text = edit.selected_text()
    user.paste("<{text}>")
(square | square bracket) it:
    text = edit.selected_text()
    user.paste("[{text}]")
(bracket | brace) it:
    text = edit.selected_text()
    user.paste("{{{text}}}")
(parens | args) it:
    text = edit.selected_text()
    user.paste("({text})")
percent it:
    text = edit.selected_text()
    user.paste("%{text}%")
quote it:
    text = edit.selected_text()
    user.paste("'{text}'")
double quote it:
    text = edit.selected_text()
    user.paste('"{text}"')
(grave | back tick) it:
    text = edit.selected_text()
    user.paste('`{text}`')

em phrase: "Mm, "
hem phrase: "Hmm, "
ah phrase: "Aa, "
ha ha phrase: "Haha "
ha ha ha phrase: "Hahaha "