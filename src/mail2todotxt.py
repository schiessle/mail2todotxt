#!/usr/bin/python
#
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

import sys, email, subprocess
from optparse import OptionParser

try:
	from dialog import TaskDescription
	dialogLoaded = True
except:
	dialogLoaded = False
	pass

class MailHandler:

	def __init__(self, path):
		self.path = path

	def getSubject(self):

		subject = ''

		with open(self.path, 'r') as f:
			for line in f:
				if (line.startswith("Subject")):
					subject = line
					break

		return self.__decodeSubject(subject)


	def __decodeSubject(self, subject):

		default = 'ascii'
    
		headers=email.Header.decode_header(subject)

		for i, (text, charset) in enumerate(headers):
			try:
				headers[i]=unicode(text, charset or default, errors='replace')
			except LookupError:
				# if the charset is unknown, force default 
				headers[i]=unicode(text, default, errors='replace')

		return u" ".join(headers)


if __name__ == "__main__":

	parser = OptionParser("mail2todotxt.py [Optionen] path_to_mail") 
	parser.add_option("-i", "--interactive", dest="interactive",
					  action="store_true", default=False,
					  help="Ask for task description") 

	(optionen, args) = parser.parse_args()

	mailUrl = args[0]

	if optionen.interactive and dialogLoaded:
		dialog = TaskDescription()
		taskDescription = dialog.getTaskDescription()
	else:
		taskDescription = ''

	if taskDescription != False:
		if taskDescription == '':
			mail = MailHandler(mailUrl)
			subject = mail.getSubject()
			task = subject.replace("Subject:", "") + " claws://"+mailUrl
		else:
			task = taskDescription + " claws://"+mailUrl

		subprocess.call(["todo.sh", "-t","add", task.strip()])
