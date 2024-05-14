import os
from mojo.UI import CurrentSpaceCenter, preferencesChanged
from mojo.subscriber import Subscriber, registerSpaceCenterSubscriber
from lib.tools.defaults import getDefault, setDefault
from vanilla import ImageButton

class TextCollector(Subscriber):
	'''
	Start-up script that puts a button in Space Center.
	This button allows you to save the current 
	string to your Input Text strings.
	
	Ryan Bugden
	'''
		
	def spaceCenterWillOpen(self, notification):
		csc = notification['spaceCenter']
		gutter = 10
		b_w = 20
		inset_b = 1
		
		l, t, w, h = csc.top.glyphLineInput.getPosSize()
		b_h = h - inset_b*2
		
		csc.top.glyphLineInput.setPosSize((l + b_w + gutter, t, w, h))
		l, t, w, h = csc.top.glyphLineInput.getPosSize()
		
		image_path = os.path.join(os.path.dirname(__file__), "resources", "_icon_Save.pdf")
		csc.top.save = ImageButton(
		  (l - gutter - b_w, t + inset_b, b_w, b_h), 
		  imagePath = image_path,
		  callback = self.saver_callback, 
		  sizeStyle = 'regular'
		  )
		csc.top.save.getNSButton().setBordered_(0)
		csc.top.save.getNSButton().setBezelStyle_(2)
		# Set as a template image to handle dark mode well
		csc.top.save.getNSButton().image().setTemplate_(True)
		

	def saver_callback(self, sender):
		csc = CurrentSpaceCenter()
		string = csc.getRaw()
		before = getDefault("spaceCenterInputSamples")
		after = list(before)
		if string not in after:
			after.append(string)
			setDefault("spaceCenterInputSamples", after)
			preferencesChanged()
		
		 
registerSpaceCenterSubscriber(TextCollector)
	