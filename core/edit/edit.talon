find it: edit.find()

next one: edit.find_next()

last one: edit.find_previous()

go word left: edit.word_left()
pre$: edit.word_left()

go word right: edit.word_right()
post$: edit.word_right()

go left: edit.left()

go right: edit.right()

go up: edit.up()

go down: edit.down()

go line start: edit.line_start()

go line end: edit.line_end()

go way left: edit.line_start()

go way right: edit.line_end()

(go | scroll) way down: edit.file_end()

(go | scroll) way up: edit.file_start()

(go | scroll) bottom: edit.file_end()

(go | scroll) top: edit.file_start()

go page down: edit.page_down()

go page up: edit.page_up()

# selecting
select line: edit.select_line()

select all: edit.select_all()

select left: edit.extend_left()

select right: edit.extend_right()

select up: edit.extend_line_up()

select down: edit.extend_line_down()

select word: edit.select_word()

select word left: edit.extend_word_left()

select word right: edit.extend_word_right()

select way left: edit.extend_line_start()

select way right: edit.extend_line_end()

select way up: edit.extend_file_start()

select way down: edit.extend_file_end()

# editing
indent: edit.indent_more()

(indent less | dedent): edit.indent_less()

# deleting
clear line: edit.delete_line()

clear left: key(backspace)

clear right: key(delete)

clear up:
    edit.extend_line_up()
    edit.delete()

clear down:
    edit.extend_line_down()
    edit.delete()

clear word: edit.delete_word()

(clear word left | cleft):
    edit.extend_word_left()
    edit.delete()

(clear word right | cright):
    edit.extend_word_right()
    edit.delete()

clear way left:
    edit.extend_line_start()
    edit.delete()

clear way right:
    edit.extend_line_end()
    edit.delete()

clear way up:
    edit.extend_file_start()
    edit.delete()

clear way down:
    edit.extend_file_end()
    edit.delete()

clear all:
    edit.select_all()
    edit.delete()

#copy commands
copy all:
    edit.select_all()
    edit.copy()
#to do: do we want these variants, seem to conflict
# copy left:
#      edit.extend_left()
#      edit.copy()
# copy right:
#     edit.extend_right()
#     edit.copy()
# copy up:
#     edit.extend_up()
#     edit.copy()
# copy down:
#     edit.extend_down()
#     edit.copy()

copy word:
    edit.select_word()
    edit.copy()

copy word left:
    edit.extend_word_left()
    edit.copy()

copy word right:
    edit.extend_word_right()
    edit.copy()

copy line:
    edit.select_line()
    edit.copy()

#cut commands
cut all:
    edit.select_all()
    edit.cut()
#to do: do we want these variants
# cut left:
#      edit.select_all()
#      edit.cut()
# cut right:
#      edit.select_all()
#      edit.cut()
# cut up:
#      edit.select_all()
#     edit.cut()
# cut down:
#     edit.select_all()
#     edit.cut()

cut word:
    edit.select_word()
    edit.cut()

cut word left:
    edit.extend_word_left()
    edit.cut()

cut word right:
    edit.extend_word_right()
    edit.cut()

#cut line:
#    edit.select_line()
#    edit.cut()

carve line:
    edit.select_line()
    edit.cut()

(pace | paste) all:
    edit.select_all()
    edit.paste()

#THE COMMANDS BELOW ARE FROM DICTATION_MODE.TALON
# Navigation
go up <number_small> (line|lines):
    edit.up()
    repeat(number_small - 1)
go down <number_small> (line|lines):
    edit.down()
    repeat(number_small - 1)
go left <number_small> (word|words):
    edit.word_left()
    repeat(number_small - 1)
go right <number_small> (word|words):
    edit.word_right()
    repeat(number_small - 1)
    
# Selection
select left <number_small> (word|words):
    edit.extend_word_left()
    repeat(number_small - 1)
select right <number_small> (word|words):
    edit.extend_word_right()
    repeat(number_small - 1)
select left <number_small> (character|characters):
    edit.extend_left()
    repeat(number_small - 1)
select right <number_small> (character|characters):
    edit.extend_right()
    repeat(number_small - 1)
clear left <number_small> (word|words):
    edit.extend_word_left()
    repeat(number_small - 1)
    edit.delete()
clear right <number_small> (word|words):
    edit.extend_word_right()
    repeat(number_small - 1)
    edit.delete()
clear left <number_small> (character|characters):
    edit.extend_left()
    repeat(number_small - 1)
    edit.delete()
clear right <number_small> (character|characters):
    edit.extend_right()
    repeat(number_small - 1)
    edit.delete()