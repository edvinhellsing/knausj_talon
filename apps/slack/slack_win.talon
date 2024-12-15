os: windows
os: linux
app: slack
not tag: browser
-
tag(): user.messaging
tag(): user.emoji

# Workspaces
workspace <number>: key("ctrl-{number}")
workspace next: key(ctrl-tab)
workspace (last | back | previous): key(ctrl-shift-tab)
# Channel
#(slack | lack | like) [channel] info: key(ctrl-shift-i)

# Navigation
#focus (move | next): key(ctrl-`)
(go [to] | section | zone) next: key(f6)
(go [to] | section | zone) (previous | last): key(shift-f6)
go [to] messages: key(ctrl-shift-k)
go [to] threads: key(ctrl-shift-t)
go (next | forth): key("alt-right")
go (last | back | previous): key("alt-left")
element next: key(tab)
element (last | back | previous): key(shift-tab)
go [to] mentions [and reactions]: key(ctrl-shift-m)
go [to] people [and user groups]: key(ctrl-shift-e)
go [to] (saved | later): key(ctrl-shift-s)
go [to] (unread | unreads): key(ctrl-shift-a)
mark [messages] as read: key(esc)
mark all [messages] [as] read: key(shift-esc)
go [to] channels: key(ctrl-shift-l)
go [to] search: key(ctrl-g)
go [to] unread next: key(alt-shift-down)
# Messaging
go up: key(up)
go down: key(down)
#grab left: key(shift-up)
#grab right: key(shift-down)
edit (message | last): key(ctrl-up)
message edit: key(ctrl-up)
message send: key(enter)
#add line: key(shift-enter)
(format command | [format] commandify): key(ctrl-shift-c)
(format code | [format] codify): key(ctrl-alt-shift-c)
[format] (bullet | bulleted) list: key(ctrl-shift-8)
[format] (number | numbered) list: key(ctrl-shift-7)
(format quotes | format quotation | [format] quotify): key(ctrl-shift-9)
(format bold | [format] boldify): key(ctrl-b)
(format italic | [format] italify): key(ctrl-i)
(format strike | format strikethrough | [format] strikify): key(ctrl-shift-x)
(format link | [format] linkify): key(ctrl-shift-u)
[format] snippet: key(ctrl-shift-enter)
formatting apply: key(ctrl-shift-f)
#formatting (clear | remove): key(ctrl-z)

# Calls
(huddle | call) (new | join): 
    key(ctrl-shift-h)
    sleep(200ms)
    key(scroll_lock)
(huddle | call) close: key(ctrl-shift-h)
#toggle (mute | unmute): key(m)
#toggle video: key(v)
#invite people: key(a)
# Miscellaneous
keyboard shortcuts: key(ctrl-/)
#emote <user.text>: "{text}"
[toggle] left sidebar: key(ctrl-shift-d)
[toggle] right sidebar: key(ctrl-.)

go [to] messages <phrase>$: user.slack_browse_dms("{phrase}")

go [to] channel <phrase>$: user.slack_browse_channels("{phrase}")

# Ideas to channels
# go [to] channel analytics: user.slack_browse_channels("analytics")
# go [to] channel backend: user.slack_browse_channels("backend")
# go [to] channel booking platform: user.slack_browse_channels("booking-platform")
go [to] channel business development: user.slack_browse_channels("business-development")
go [to] channel creative: user.slack_browse_channels("creative-marketing-and-communications")
# go [to] channel daily updates: user.slack_browse_channels("daily-updates")
# go [to] channel design: user.slack_browse_channels("design")
# go [to] channel design management: user.slack_browse_channels("design-management")
go [to] channel economy: user.slack_browse_channels("ekonomi")
# go [to] channel general: user.slack_browse_channels("general")
go [to] channel hr: user.slack_browse_channels("hr")
go [to] channel human relations: user.slack_browse_channels("hr")
# go [to] channel ideas: user.slack_browse_channels("ideas")
# go [to] channel jacqueline: user.slack_browse_channels("jacqueline")
# go [to] channel management: user.slack_browse_channels("management")
# go [to] channel management and leads: user.slack_browse_channels("management-and-leads")
# go [to] channel random: user.slack_browse_channels("random")
# go [to] channel release notes: user.slack_browse_channels("release-notes")
go [to] channel pr: user.slack_browse_channels("public-relations-pr")
go [to] channel qa: user.slack_browse_channels("qa")
go [to] channel quality assurance: user.slack_browse_channels("qa")
# go [to] channel successes: user.slack_browse_channels("successes")
go [to] channel sails: user.slack_browse_channels("sales")
go [to] channel team sweden: user.slack_browse_channels("team-sweden")
# go [to] channel web: user.slack_browse_channels("web")
# go [to] channel web management: user.slack_browse_channels("web-management")