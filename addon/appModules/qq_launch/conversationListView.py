# -*- coding: utf-8 -*-
import ui
from NVDAObjects.UIA import UIA
from logHandler import log

class ConversationListView(UIA):
	pass

class Summary(UIA):

	def event_nameChange(self):
		log.info(self.name)

