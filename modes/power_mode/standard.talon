mode: user.power_mode
-
zoom in: edit.zoom_in()
zoom out: edit.zoom_out()
zoom reset: edit.zoom_reset()
#This is for zooming the area around the mouse.
zoom area: tracking.zoom()
#scroll up: edit.page_up()
#scroll down: edit.page_down()
copy it: edit.copy()
cut it: edit.cut()
#carve it: edit.cut()
(pace | paste) it: edit.paste()
(pace | paste) enter:
  edit.paste()
  key(enter)
(pace | paste) plain: edit.paste_match_style()
#(pace | paste) match: edit.paste_match_style()
undo it: edit.undo()
redo it: edit.redo()
file save: edit.save()
file save all: edit.save_all()
(pad | padding): user.insert_between(" ", " ")
#slap: edit.line_insert_down()
new (line | row): edit.line_insert_down()
new paragraph: 
  edit.line_insert_down() 
  edit.line_insert_down()