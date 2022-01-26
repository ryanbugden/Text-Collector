import os
from mojo.UI import CurrentSpaceCenter, preferencesChanged
from mojo.events import addObserver
from lib.tools.defaults import getDefault, setDefault
from vanilla import ImageButton

class textCollector:
	
	'''
	Extension that puts a button in Space Center.
	This button allows you to save the current 
	string to your Input Text strings.
	
	Ryan Bugden
	2020.01.28
	'''
	
	def __init__(self):
		self.resources_path = os.path.abspath("./resources")
		addObserver(self, "makeButton", "spaceCenterDidOpen")
		
	def makeButton(self, notification):
		csc = CurrentSpaceCenter()
		gutter = 10
		b_w = 20
		inset_b = 1
		
		l, t, w, h = csc.top.glyphLineInput.getPosSize()
		b_h = h - inset_b*2
		
		csc.top.glyphLineInput.setPosSize((l + b_w + gutter, t, w, h))
		l, t, w, h = csc.top.glyphLineInput.getPosSize()
		
		csc.save = ImageButton(
		  (l - gutter - b_w, t + inset_b, b_w, b_h), 
		  imagePath = self.resources_path + '/_icon_Save.pdf',
		  callback = self.saverCallback, 
		  sizeStyle = 'regular'
		  )
		csc.save.getNSButton().setBordered_(0)
		csc.save.getNSButton().setBezelStyle_(2)
		
	def saverCallback(self, sender):
		print("saving input text")
		csc = CurrentSpaceCenter()
		
		string = csc.getRaw()
		print("string is", string)
		
		before = getDefault("spaceCenterInputSamples")
		print("before is ", before)
		after = list(before)
		print("after is ", after)
		if string not in after:
			after.append(string)
			print("after2 is ", after)
			setDefault("spaceCenterInputSamples", after)
			print("saved input text.")
		else:
			print("did nothing.")
		
		preferencesChanged()
		
		 
textCollector()
	