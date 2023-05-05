fix text:
    edit.select_all()
    old = edit.selected_text()
    new = user.open_ai_fixup_text_gpt(old)
    user.paste(new)

fix text davinci:
    edit.select_all()
    old = edit.selected_text()
    new = user.open_ai_fixup_text_davinci(old)
    user.paste(new)

fix text davinci edit:
    edit.select_all()
    old = edit.selected_text()
    new = user.open_ai_fixup_text_davinci_edit(old)
    user.paste(new)

fix selection:
    old = edit.selected_text()
    new = user.open_ai_fixup_text_gpt(old)
    user.paste(new)

