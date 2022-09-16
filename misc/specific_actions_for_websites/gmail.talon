tag: browser
browser.host: mail.google.com
-
(conversation | convo | thread) last: key(k)
(conversation | convo | thread) next: key(j)

(email | message) last: key(p)
(email | message) next: key(n)

go to inbox: 
    key(g)
    key(i)
go to starred: 
    key(g)
    key(s)
go to drafts: 
    key(g)
    key(d)
go to sent: 
    key(g)
    key(t)

(email | message) flag: key(s)
report spam: key(!)
(email | message): key(#)
reply: key(r)
reply all: key(a)
(email | message) forward: key(f)
(undo | undo it | undo send): key(z)

search: key(/)

#keyboard shortcuts: key()