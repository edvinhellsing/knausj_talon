tag: user.tabs
-
#tab new: app.tab_open()
tab (last | previous): app.tab_previous()
tab next: app.tab_next()
tab (close | plus): user.tab_close_wrapper()
ten (close | plus): user.tab_close_wrapper()
tab (reopen | restore): app.tab_reopen()
tab <number>: user.tab_jump(number)
tab final: user.tab_final()
tab duplicate: user.tab_duplicate()

tab left: user.tab_left_wrapper()
tab right: user.tab_right_wrapper()

#Made changes that work better with the following plugin: https://chrome.google.com/webstore/detail/open-tabs-next-to-current/gmpnnmonpnnmnhpdldahlekfofigiffh?hl=en
#The issue with this approach is that other programs that also use the tag user.tabs but doesn't support user.tab_final() it might not work for. For example this seemed to be the case with the Figma app before I made some changes.
tab new: 
    user.tab_final()
    sleep(50ms)
    app.tab_open()
tab new here: app.tab_open()
