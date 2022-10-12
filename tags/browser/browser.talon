tag: browser
-
go address | go url: browser.focus_address()
address copy | url copy | copy address | copy url:
    browser.focus_address()
    sleep(50ms)
    edit.copy()
#go home: browser.go_home()
go (forward | next | forth): browser.go_forward()
go (backward | last | back | previous): browser.go_back()

go [to] {user.website}: browser.go(website)
private new: browser.open_private_window()

bookmark it: browser.bookmark()
#bookmark tabs: browser.bookmark_tabs()
(refresh | reload) it: browser.reload()
(refresh | reload) it hard: browser.reload_hard()
tab (refresh | reload): browser.reload()
tab (refresh | reload) hard: browser.reload_hard()

bookmark (show | open): browser.bookmarks()
bookmark bar (show | open): browser.bookmarks_bar()
downloads (show | open): browser.show_downloads()
extensions (show | open): browser.show_extensions()
history (show | open): browser.show_history()
cache (show | open): browser.show_clear_cache()
dev tools (show | open): browser.toggle_dev_tools()

incognito new: key(ctrl-shift-n)

# Legacy [verb noun] commands to be removed at a later time
#show downloads: browser.show_downloads()
#show extensions: browser.show_extensions()
#show history: browser.show_history()
#show cache: browser.show_clear_cache()

#todo - port to apps
# navigating current page
# help: key(?)
# scroll tiny down: key(j)
# scroll tiny up: key(k)
# scroll left: key(h)
# scroll right: key(l)
# scroll (pop | spring): key(z H)
# scroll push: key(z L)
# scroll top: key(gg)
# scroll (bottom | end): key(G)
# (scroll half down | mini page): key(d)
# scroll half up: key(u)
# [open] link: key(f)
# [open] link new: key(F)
# copy link: key(y f)
# copy (address | url): key(escape y y)
# (refresh | reload): browser.reload()
# view source: key(g s)
# insert mode: key(i)
# next frame: key(g f)
# main frame: key(g F)
# navigating to new pages
# (open | go) (url | history): key(o)
# (open | go) (url | history) new: key(O)
# (open | go) bookmark: key(b)
# (open | go) bookmark new: key(B)
# using find
# find mode: key(/)
# next match: key(n)
# previous match: key(N)
# navigating history
# history back: key(H)
# history forward: key(L)
# manipulating tabs
# last visited: key(^)
# dupe tab: key(y t)
# restore: key(X)
# search tabs: key(T)
# move to window: key(W)
