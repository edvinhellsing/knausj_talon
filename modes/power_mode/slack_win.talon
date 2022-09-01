mode: user.power_mode
os: windows
os: linux
app: slack
#todo: some sort of plugin, consolidate with teams or something?
-
tag(): user.messaging
tag(): user.emoji
# Workspaces
workspace <number>: key("ctrl-{number}")
# Channel
(slack | lack | like) [channel] info: key(ctrl-shift-i)
# Navigation
#focus (move | next): key(ctrl-`)
(section | zone) [next]: key(f6)
(section | zone) (previous | last): key(shift-f6)
(slack | lack | like) [direct] messages: key(ctrl-shift-k)
(slack | lack | like) threads: key(ctrl-shift-t)
(slack | lack | like) (history [next] | back | backward): key(alt-left)
(slack | lack | like) forward: key(alt-right)
element [next]: key(tab)
element (previous | last): key(shift-tab)
(slack | lack | like) (my stuff | activity): key(ctrl-shift-m)
(slack | lack | like) directory: key(ctrl-shift-e)
(slack | lack | like) (starred [items] | stars): key(ctrl-shift-s)
(slack | lack | like) unread [messages]: key(ctrl-shift-a)
(slack | lack | like) search: key(ctrl-g)
# Messaging
go up: key(up)
go down: key(down)
go (forward | next): key("alt-right")
go (backward | last | back | previous): key("alt-left")
grab left: key(shift-up)
grab right: key(shift-down)
#add line: key(shift-enter)
#"(slack | lack | like) (slap | slaw | slapper): [key(cmd-right) key(shift-enter")],
(slack | lack | like) (react | reaction): key(ctrl-shift-\)
(slack | lack | like) (insert command | commandify): key(ctrl-shift-c)
(slack | lack | like) insert code: key(ctrl-alt-shift-c)
(slack | lack | like) (bull | bullet | bulleted) [list]: key(ctrl-shift-8)
(slack | lack | like) (number | numbered) [list]: key(ctrl-shift-7)
(slack | lack | like) (quotes | quotation): key(ctrl-shift-9)
(slack | lack | like) bold: key(ctrl-b)
(slack | lack | like) (italic | italicize): key(ctrl-i)
(slack | lack | like) (strike | strikethrough): key(ctrl-shift-x)
(slack | lack | like) snippet: key(ctrl-shift-enter)
# Calls
(slack | lack | like) ([toggle] mute | unmute): key(m)
(slack | lack | like) ([toggle] video): key(v)
(slack | lack | like) invite: key(a)
# Miscellaneous
(slack | lack | like) shortcuts: key(ctrl-/)
#emote <user.text>: "{text}"
toggle left sidebar: key(ctrl-shift-d)
toggle right sidebar: key(ctrl-.)

# DEPRECATED
#(move | next) focus:
#    app.notify("please use the voice command 'focus next' instead of 'next focus'")
#    key(ctrl-`)
#[next] (section | zone):
#    app.notify("please use the voice command 'section next' instead of 'next section'")
#    key(f6)
#(previous | last) (section | zone):
#    app.notify("please use the voice command 'section last' instead of 'last section'")
#    key(shift-f6)
#[next] (element | bit):
#    app.notify("please use the voice command 'element next' instead of 'next element'")
#    key(tab)
#(previous | last) (element | bit):
#    app.notify("please use the voice command 'element last' instead of 'last element'")
#    key(shift-tab)
