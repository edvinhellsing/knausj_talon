go to {user.website}: user.open_url(website)
{user.search_engine} search <user.text>$: user.search_with_search_engine(search_engine, user.text)
{user.search_engine} this:
    text = edit.selected_text()
    user.search_with_search_engine(search_engine, text)
