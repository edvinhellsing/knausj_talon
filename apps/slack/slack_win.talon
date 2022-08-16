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
(slack | lack) [channel] info: key(ctrl-shift-i)
# Navigation
#focus (move | next): key(ctrl-`)
(section | zone) [next]: key(f6)
(section | zone) (previous | last): key(shift-f6)
(slack | lack) [direct] messages: key(ctrl-shift-k)
(slack | lack) threads: key(ctrl-shift-t)
(slack | lack) (history [next] | back | backward): key(alt-left)
(slack | lack) forward: key(alt-right)
(element | bit) [next]: key(tab)
(element | bit) (previous | last): key(shift-tab)
(slack | lack) (my stuff | activity): key(ctrl-shift-m)
(slack | lack) directory: key(ctrl-shift-e)
(slack | lack) (starred [items] | stars): key(ctrl-shift-s)
(slack | lack) unread [messages]: key(ctrl-shift-a)
(slack | lack) search: key(ctrl-g)
# Messaging
go up: key(up)
go down: key(down)
grab left: key(shift-up)
grab right: key(shift-down)
#add line: key(shift-enter)
#"(slack | lack) (slap | slaw | slapper): [key(cmd-right) key(shift-enter")],
(slack | lack) (react | reaction): key(ctrl-shift-\)
(slack | lack) (insert command | commandify): key(ctrl-shift-c)
(slack | lack) insert code: key(ctrl-alt-shift-c)
(slack | lack) (bull | bullet | bulleted) [list]: key(ctrl-shift-8)
(slack | lack) (number | numbered) [list]: key(ctrl-shift-7)
(slack | lack) (quotes | quotation): key(ctrl-shift-9)
(slack | lack) bold: key(ctrl-b)
(slack | lack) (italic | italicize): key(ctrl-i)
(slack | lack) (strike | strikethrough): key(ctrl-shift-x)
(slack | lack) snippet: key(ctrl-shift-enter)
# Calls
([toggle] mute | unmute): key(m)
(slack | lack) ([toggle] video): key(v)
(slack | lack) invite: key(a)
# Miscellaneous
(slack | lack) shortcuts: key(ctrl-/)
emote <user.text>: "{text}"
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
