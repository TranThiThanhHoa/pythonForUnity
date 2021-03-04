# -*- coding: utf-8 -*-

# Macro Begin: C:\Users\thi-t\AppData\Roaming\FreeCAD\Macro\testPython.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import Part
import UnityEngine 
# Gui.runCommand('Std_DlgMacroRecord',0)
### Begin command Part_Box
App.ActiveDocument.addObject("Part::Box","Box")
App.ActiveDocument.ActiveObject.Label = "Cube"
App.ActiveDocument.recompute()
# Gui.SendMsgToActiveView("ViewFit")
### End command Part_Box
# Macro End: C:\Users\thi-t\AppData\Roaming\FreeCAD\Macro\testPython.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
