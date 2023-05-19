from abaqusGui import *
from abaqusConstants import ALL
import osutils, os


###########################################################################
# Class definition
###########################################################################

class _rsgTmp008_Form(AFXForm):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, owner):
        
        # Construct the base class.
        #
        AFXForm.__init__(self, owner)
        self.radioButtonGroups = {}

        self.cmd = AFXGuiCommand(mode=self, method='drawing_process',
            objectName='ULTIMATE_PLUGIN', registerQuery=False)
        pickedDefault = ''
        self.DieSelectorKw = AFXStringKeyword(self.cmd, 'DieSelector', True)
        self.DieTypeKw = AFXStringKeyword(self.cmd, 'DieType', True)
        self.H_ModelNameKw = AFXStringKeyword(self.cmd, 'H_ModelName', True, 'Model-1')
        self.H_DieNameKw = AFXStringKeyword(self.cmd, 'H_DieName', True, 'Die')
        self.H_RKw = AFXFloatKeyword(self.cmd, 'H_R', True, 35)
        self.H_rKw = AFXFloatKeyword(self.cmd, 'H_r', True, 18.974)
        self.H_SKw = AFXFloatKeyword(self.cmd, 'H_S', True, 8)
        self.H_h1Kw = AFXFloatKeyword(self.cmd, 'H_h1', True, 6)
        self.H_h2Kw = AFXFloatKeyword(self.cmd, 'H_h2', True, 16)
        self.H_h3Kw = AFXFloatKeyword(self.cmd, 'H_h3', True, 6)
        self.H_a1Kw = AFXFloatKeyword(self.cmd, 'H_a1', True, 20)
        self.H_a2Kw = AFXFloatKeyword(self.cmd, 'H_a2', True, 8)
        self.H_a3Kw = AFXFloatKeyword(self.cmd, 'H_a3', True, 30)
        self.H_WireNameKw = AFXStringKeyword(self.cmd, 'H_WireName', True, 'Wire')
        self.H_RwireKw = AFXFloatKeyword(self.cmd, 'H_Rwire', True, 20)
        self.H_WireLengthKw = AFXFloatKeyword(self.cmd, 'H_WireLength', True, 200)
        self.C_ModelNameKw = AFXStringKeyword(self.cmd, 'C_ModelName', True, 'Model-1')
        self.C_DieNameKw = AFXStringKeyword(self.cmd, 'C_DieName', True, 'Die')
        self.C_RKw = AFXFloatKeyword(self.cmd, 'C_R', True, 35)
        self.C_rKw = AFXFloatKeyword(self.cmd, 'C_r', True, 18.974)
        self.C_SKw = AFXFloatKeyword(self.cmd, 'C_S', True, 8)
        self.C_h1Kw = AFXFloatKeyword(self.cmd, 'C_h1', True, 6)
        self.C_h2Kw = AFXFloatKeyword(self.cmd, 'C_h2', True, 6)
        self.C_h3Kw = AFXFloatKeyword(self.cmd, 'C_h3', True, 6)
        self.C_h4Kw = AFXFloatKeyword(self.cmd, 'C_h4', True, 16)
        self.C_h5Kw = AFXFloatKeyword(self.cmd, 'C_h5', True, 6)
        self.C_a1Kw = AFXFloatKeyword(self.cmd, 'C_a1', True, 6)
        self.C_a2Kw = AFXFloatKeyword(self.cmd, 'C_a2', True, 8)
        self.C_a3Kw = AFXFloatKeyword(self.cmd, 'C_a3', True, 10)
        self.C_a4Kw = AFXFloatKeyword(self.cmd, 'C_a4', True, 13)
        self.C_a5Kw = AFXFloatKeyword(self.cmd, 'C_a5', True, 30)
        self.C_WireNameKw = AFXStringKeyword(self.cmd, 'C_WireName', True, 'Wire')
        self.C_RwireKw = AFXFloatKeyword(self.cmd, 'C_Rwire', True, 20)
        self.C_WireLengthKw = AFXFloatKeyword(self.cmd, 'C_WireLength', True, 200)
        self.FrictionCoefKw = AFXFloatKeyword(self.cmd, 'FrictionCoef', True, 0.15)
        self.SpeedKw = AFXFloatKeyword(self.cmd, 'Speed', True, 1000)
        self.TimeKw = AFXFloatKeyword(self.cmd, 'Time', True, 0.35)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getFirstDialog(self):

        import _rsgTmp008_DB
        return _rsgTmp008_DB._rsgTmp008_DB(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def doCustomChecks(self):

        # Try to set the appropriate radio button on. If the user did
        # not specify any buttons to be on, do nothing.
        #
        for kw1,kw2,d in self.radioButtonGroups.values():
            try:
                value = d[ kw1.getValue() ]
                kw2.setValue(value)
            except:
                pass
        return True

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def deactivate(self):
    
        try:
            osutils.remove(os.path.join('d:\\temp\\abaqus_plugins\\ULT_PLAG', '_rsgTmp008_DB.py'), force=True )
            osutils.remove(os.path.join('d:\\temp\\abaqus_plugins\\ULT_PLAG', '_rsgTmp008_DB.pyc'), force=True )
        except:
            pass
        try:
            osutils.remove(os.path.join('d:\\temp\\abaqus_plugins\\ULT_PLAG', '_rsgTmp008_Form.py'), force=True )
            osutils.remove(os.path.join('d:\\temp\\abaqus_plugins\\ULT_PLAG', '_rsgTmp008_Form.pyc'), force=True )
        except:
            pass
        AFXForm.deactivate(self)

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getCommandString(self):

        cmds = 'import ULTIMATE_PLUGIN\n'
        cmds += AFXForm.getCommandString(self)
        return cmds

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def okToCancel(self):

        # No need to close the dialog when a file operation (such
        # as New or Open) or model change is executed.
        #
        return False
