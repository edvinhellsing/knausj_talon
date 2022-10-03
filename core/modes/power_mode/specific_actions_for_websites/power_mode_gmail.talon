mode: user.power_mode
tag: browser
browser.host: mail.google.com
-
(conversation | convo | thread) last: key(k)
(conversation | convo | thread) next: key(j)

(email | message) last: key(p)
(email | message) next: key(n)

go inbox: 
    key(g)
    key(i)
go starred: 
    key(g)
    key(s)
go drafts: 
    key(g)
    key(d)
go sent: 
    key(g)
    key(t)

(email | message) flag: key(s)
report spam: key(!)
(email | message): key(#)
reply: key(r)
reply all: key(a)
(email | message) forward: key(f)
(email | message) send: key(ctrl-enter)
(undo | undo it | undo send): key(z)

search: key(/)

#keyboard shortcuts: key()