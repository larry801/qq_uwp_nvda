# qq_uwp: An addon for q

#Copyright (C) 2018 XiaoKe <larry.wang.801@gmail.com>, and Larry Wang

#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

"""qq_uwp:
An app module that extends qq_launch
"""

import addonHandler
import appModuleHandler
#We need to initialize translation and localization support:
addonHandler.initTranslation()

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		pass 
		#If you don't need this function, please remove it.
		
	def event_NVDAObject_init(self):
		pass
	
	def __init__(self):
		super(appModule, self).__init__()
	
	__gestures = {
		#Fill me in please. If you don't need me, delete me.
	}
	
