# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Mar 29 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculate the equation", pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 300,200 ), wx.Size( 300,200 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.solveButton = wx.Button( self, wx.ID_ANY, u"Solve", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.solveButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.clearButton = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.clearButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.exitButton = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.exitButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.solveButton.Bind( wx.EVT_BUTTON, self.solveFunc )
		self.clearButton.Bind( wx.EVT_BUTTON, self.clearFunc )
		self.exitButton.Bind( wx.EVT_BUTTON, self.exitFunc )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def solveFunc( self, event ):
		event.Skip()
	
	def clearFunc( self, event ):
		event.Skip()
	
	def exitFunc( self, event ):
		self.Close(True)
	

