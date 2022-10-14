mode: user.power_mode
# have made specific power mode changes in this file
-
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
#This is for zooming the area around the mouse.
#zoom area: tracking.zoom()
#scroll up: edit.page_up()
#scroll down: edit.page_down()
(copy it now | cap bat now): edit.copy()
#cut it: edit.cut()
carve it now: edit.cut()
(pace | paste) it now: edit.paste()
# (pace | paste) enter:
#   edit.paste()
#   key(enter)
(pace | paste) plain: edit.paste_match_style()
(pace | paste) match style: edit.paste_match_style()
undo it: edit.undo()
redo it: edit.redo()
(file | five) save: edit.save()
(file | five) save all: edit.save_all()
#padding: user.insert_between(" ", " ")
slap: edit.line_insert_down()
new (line | row): edit.line_insert_down()
(line | row) new: edit.line_insert_down()
(new paragraph | paragraph new): 
  edit.line_insert_down() 
  edit.line_insert_down()