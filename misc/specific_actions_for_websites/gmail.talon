tag: browser
browser.host: mail.google.com
#https://support.google.com/mail/answer/6594?hl=en&co=GENIE.Platform%3DDesktop
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

#(email | message) new: key(n)
(email | message) flag: key(s)
report spam: key(!)
(email | message) (delete | remove): key(#)
reply: key(r)
reply all: key(a)
(email | message) forward: key(f)
(email | message) send: key(ctrl-enter)
(undo | undo it | undo send): key(z)
#mark as read: key(q)
#mark as unread: key(u)

search: key(/)
#keyboard shortcuts: key()