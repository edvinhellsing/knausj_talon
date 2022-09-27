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
#(slack | lack | like) [channel] info: key(ctrl-shift-i)
# Navigation
#focus (move | next): key(ctrl-`)
(section | zone) next: key(f6)
(section | zone) (previous | last): key(shift-f6)
(slack | lack | like) [direct] messages: key(ctrl-shift-k)
(slack | lack | like) threads: key(ctrl-shift-t)
go (forward | next): key("alt-right")
go (backward | last | back | previous): key("alt-left")
element next: key(tab)
element (last | previous): key(shift-tab)
(slack | lack | like) (mentions | reactions | activity): key(ctrl-shift-m)
(slack | lack | like) directory: key(ctrl-shift-e)
(slack | lack | like) (starred [items] | stars): key(ctrl-shift-s)
(slack | lack | like) unread [messages]: key(ctrl-shift-a)
(slack | lack | like) channels: key(ctrl-shift-l)
(slack | lack | like) search: key(ctrl-g)
# Messaging
go up: key(up)
go down: key(down)
grab left: key(shift-up)
grab right: key(shift-down)
#add line: key(shift-enter)
#"(slack | lack | like) (slap | slaw | slapper): [key(cmd-right) key(shift-enter")],
(slack | lack | like) (react | reaction): key(ctrl-shift-\)
[insert] (command | commandify): key(ctrl-shift-c)
[insert] (code | codify): key(ctrl-alt-shift-c)
[insert] (bullet | bulleted) list: key(ctrl-shift-8)
[insert] (number | numbered) list: key(ctrl-shift-7)
[insert] (quotes | quotation | quotify): key(ctrl-shift-9)
[insert] (insert bold | boldify): key(ctrl-b)
[insert] (italic | italify): key(ctrl-i)
[insert] (strike | strikethrough | strikify): key(ctrl-shift-x)
[insert] snippet: key(ctrl-shift-enter)
# Calls
start huddle: key(ctrl-shift-h)
(slack | lack | like) ([toggle] mute | unmute): key(m)
(slack | lack | like) ([toggle] video): key(v)
(slack | lack | like) invite: key(a)
# Miscellaneous
keyboard shortcuts: key(ctrl-/)
#emote <user.text>: "{text}"
toggle left sidebar: key(ctrl-shift-d)
toggle right sidebar: key(ctrl-.)

message send: key(enter)

go channel <phrase>$: user.slack_browse_channels("{phrase}")
# go channel analytics: user.slack_browse_channels("analytics")
# go channel app: user.slack_browse_channels("app")
# go channel backend: user.slack_browse_channels("backend")
# go channel booking platform: user.slack_browse_channels("booking-platform")
# go channel creative corner: user.slack_browse_channels("creative-corner")
# go channel daily updates: user.slack_browse_channels("daily-updates")
# go channel design: user.slack_browse_channels("design")
# go channel design management: user.slack_browse_channels("design-management")
# go channel economy: user.slack_browse_channels("ekonomi")
# go channel general: user.slack_browse_channels("general")
go channel hr: user.slack_browse_channels("hr")
# go channel ideas: user.slack_browse_channels("ideas")
# go channel jacqueline: user.slack_browse_channels("jacqueline")
# go channel management: user.slack_browse_channels("management")
# go channel management and leads: user.slack_browse_channels("management-and-leads")
# go channel random: user.slack_browse_channels("random")
# go channel release notes: user.slack_browse_channels("release-notes")
go channel pr: user.slack_browse_channels("public-relations-pr")
go channel qa: user.slack_browse_channels("qa")
# go channel successes: user.slack_browse_channels("successes")
# go channel team sweden: user.slack_browse_channels("team-sweden")
# go channel web: user.slack_browse_channels("web")
# go channel web management: user.slack_browse_channels("web-management")

go (dm | messages) <phrase>$: user.slack_browse_dms("{phrase}")

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
