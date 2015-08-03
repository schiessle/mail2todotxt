# mail2todotxt.py - convert a mail from Claws Mail into a todo.txt item
#
# Copyright (C) 2014  Bjoern Schiessle <bjoern@schiessle.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

class DialogTaskDescription(Gtk.Dialog):

	def __init__(self):
		Gtk.Dialog.__init__(self, "Create ToDo.txt Entry", None, 0,
							(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
							 Gtk.STOCK_OK, Gtk.ResponseType.OK))

		self.set_default_size(150, 100)

		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)

		self.label = Gtk.Label("Task Description:")
		self.taskDescription = Gtk.Entry()
		hbox.pack_start(self.label, False, True, 0)
		hbox.pack_start(self.taskDescription, True, True, 0)
        
		box = self.get_content_area()
		box.add(hbox)

		# enter key should trigger default action
		self.taskDescription.set_activates_default(True)

		# make OK button the default
		okButton = self.get_widget_for_response(response_id=Gtk.ResponseType.OK)
		okButton.set_can_default(True)
		okButton.grab_default()
		
		self.show_all()

	def getTaskDescription(self):
		return self.taskDescription.get_text()

class TaskDescription:

	def __init__(self):
		self.dialog = DialogTaskDescription()

	def getTaskDescription(self):
		response = self.dialog.run()

		if response == Gtk.ResponseType.OK:
			taskDescription = self.dialog.getTaskDescription()
		else:
			taskDescription = False
        
		self.dialog.destroy()

		return taskDescription
 
