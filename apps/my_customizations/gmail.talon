tag: browser
browser.host: mail.google.com
#https://support.google.com/mail/answer/6594?hl=en&co=GENIE.Platform%3DDesktop
-
(conversation | convo | thread) last: key(k)
(conversation | convo | thread) next: key(j)
(comment | message | email) last: key(p)
(comment | message | email) next: key(n)

go [to] inbox: 
    key(g)
    key(i)
go [to] starred: 
    key(g)
    key(s)
go [to] drafts: 
    key(g)
    key(d)
go [to] sent: 
    key(g)
    key(t)

#(comment | message | email) new: key(n)
(comment | message | email) flag: key(s)
report spam: key(!)
(comment | message | email) (delete | remove): key(#)
(comment | message | email) reply: key(r)
(comment | message | email) reply all: key(a)
(comment | message | email) forward: key(f)
(comment | message | email) send: key(ctrl-enter)
(undo | undo it | undo send): key(z)
#mark as read: key(q)
#mark as unread: key(u)

search: key(/)
#keyboard shortcuts: key()