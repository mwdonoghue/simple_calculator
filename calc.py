#importing wx files
import wx
 
#import the newly created GUI file
import gui
 
#importing * : to enable writing sin(13) instead of math.sin(13)
from math import *
 
#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class CalcFrame(gui.MainFrame):
    #constructor
    def __init__(self,parent):
        #initialize parent class
        gui.MainFrame.__init__(self,parent)
 
    #what to when 'Solve' is clicked
    #wx calls this function with and 'event' object
    def solveFunc(self,event):
        try:
            #evaluate the string in 'text' and put the answer back
            ans = eval(self.text.GetValue())
            self.text.SetValue (str(ans))
        except Exception:
            self.text.SetValue( 'error' )
    #put a blank string in text when 'Clear' is clicked
    def clearFunc(self,event):
        self.text.SetValue(str(''))
 
#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
#refer manual for details
app = wx.App(False)
 
#create an object of CalcFrame
frame = CalcFrame(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()