 #-*- coding: utf-8 -*-
from logHandler import log
from NVDAObjects.UIA import UIA
import controlTypes
import ui
import api
class MessageListBox(UIA):

	pass


class MsgRichTextBlock(UIA):

	def event_nameChange(self):

		ui.message(self.previous.name+self.name)

class MessageToolButton(UIA):



	def initOverlayClass(self):

		if self.UIAElement.CachedAutomationId=='EmotionButton' :
			self.name=u'表情'
			return

		elif self.previous and isinstance(self.previous,UIA) and self.previous.UIAElement.CachedAutomationId=='EmotionButton' :
			self.name=u'图片'
			return

		elif self.UIAElement.CachedAutomationId=='GraffitiButton' :
			self.name=u'涂鸦'
			return

		elif self.UIAElement.CachedAutomationId=='ChatHistoryButton':
			self.name=u'聊天记录'
			return self

		elif self.UIAElement.CachedAutomationId=='PttButton' :
			self.name=u'语音'
			return self

		elif self.UIAElement.CachedAutomationId=='BackButton' :
			self.name=u'返回'
			return self


		elif self.previous and self.previous.previous and isinstance(self.previous.previous,UIA) and self.previous.previous.UIAElement.CachedAutomationId=='EmotionButton' :
			self.name=u'文件'
			return self

		elif self.previous and self.previous.previous and isinstance(self.previous.previous,UIA) and self.previous.previous.UIAElement.CachedAutomationId=='SubTitleText' :
			self.name=u'视频通话'
			return self

		elif self.previous and isinstance(self.previous,UIA) and self.previous.UIAElement.CachedAutomationId=='SubTitleText' :
			self.next
			self.name=u'语音通话'
			return
