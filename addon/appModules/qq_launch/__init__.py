# -*- coding: UTF-8 -*-


import UIAHandler
import conversationListView
import messageListBox
import api
import appModuleHandler
import controlTypes
import ui
from logHandler import log
from NVDAObjects.UIA import UIA


import time


class AppModule(appModuleHandler.AppModule):


	def chooseNVDAObjectOverlayClasses(self,obj,clsList):
		
		if isinstance(obj,UIA) and obj.UIAElement.CachedAutomationId=='MsgRichTextBlock' :
		
			clsList.insert(0,messageListBox.MsgRichTextBlock)
			
		elif isinstance(obj,UIA) and obj.UIAElement.CachedAutomationId=='Summary' :
			clsList.insert(0,conversationListView.Summary)
			
		elif isinstance(obj,UIA) and obj.role==controlTypes.ROLE_BUTTON :
			clsList.insert(0,messageListBox.MessageToolButton)
	def event_NVDAObject_init(self,obj):
		if isinstance(obj, UIA):
			try:
				res = obj._getUIACacheablePropertyValue(UIAHandler.UIA_IsVirtualizedItemPatternAvailablePropertyId)
			except COMError:
				res = False
			if res and obj.children:
				obj.name = obj.children[0].name