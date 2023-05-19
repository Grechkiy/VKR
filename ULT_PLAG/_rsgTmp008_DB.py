from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class _rsgTmp008_DB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Drawing',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        HFrame_3 = FXHorizontalFrame(p=self, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VFrame_4 = FXVerticalFrame(p=HFrame_3, opts=LAYOUT_FILL_X, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        ComboBox_2 = AFXComboBox(p=VFrame_4, ncols=0, nvis=1, text='Select a shape of billet', tgt=form.DieSelectorKw, sel=0)
        ComboBox_2.setMaxVisible(10)
        ComboBox_2.appendItem(text='Hex')
        ComboBox_2.appendItem(text='Circle')
        ComboBox_3 = AFXComboBox(p=VFrame_4, ncols=0, nvis=1, text='Select a type of Die:', tgt=form.DieTypeKw, sel=0)
        ComboBox_3.setMaxVisible(10)
        ComboBox_3.appendItem(text='Rigid')
        ComboBox_3.appendItem(text='Deformable')
        TabBook_2 = FXTabBook(p=VFrame_4, tgt=None, sel=0,
            opts=TABBOOK_NORMAL|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING)
        tabItem = FXTabItem(p=TabBook_2, text='Hexagonal Die', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_3 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_8 = FXHorizontalFrame(p=TabItem_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VFrame_10 = FXVerticalFrame(p=HFrame_8, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_5 = FXGroupBox(p=VFrame_10, text='Model', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        AFXTextField(p=GroupBox_5, ncols=12, labelText='Model Name:', tgt=form.H_ModelNameKw, sel=0)
        GroupBox_6 = FXGroupBox(p=VFrame_10, text='Die Parameters', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='Die Name:', tgt=form.H_DieNameKw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='R(mm)', tgt=form.H_RKw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='r(mm):', tgt=form.H_rKw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='S (mm):', tgt=form.H_SKw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='h1 (mm):', tgt=form.H_h1Kw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='h2 (mm):', tgt=form.H_h2Kw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='h3 (mm):', tgt=form.H_h3Kw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='alpha1 (DEG):', tgt=form.H_a1Kw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='alpha2 (DEG):', tgt=form.H_a2Kw, sel=0)
        AFXTextField(p=GroupBox_6, ncols=12, labelText='alpha3 (DEG):', tgt=form.H_a3Kw, sel=0)
        GroupBox_7 = FXGroupBox(p=VFrame_10, text='Wire Parameters', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        AFXTextField(p=GroupBox_7, ncols=12, labelText='Wire Name:', tgt=form.H_WireNameKw, sel=0)
        AFXTextField(p=GroupBox_7, ncols=12, labelText='R wire (mm):', tgt=form.H_RwireKw, sel=0)
        AFXTextField(p=GroupBox_7, ncols=12, labelText='Wire Length (mm):', tgt=form.H_WireLengthKw, sel=0)
        VFrame_11 = FXVerticalFrame(p=HFrame_8, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=50, pb=0)
        fileName = os.path.join(thisDir, 'hexxxxxxxxxx_795_405(1).png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=VFrame_11, text='', ic=icon)
        tabItem = FXTabItem(p=TabBook_2, text='Circle Die', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_4 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        HFrame_7 = FXHorizontalFrame(p=TabItem_4, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        VFrame_8 = FXVerticalFrame(p=HFrame_7, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
        GroupBox_10 = FXGroupBox(p=VFrame_8, text='Model', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_10, ncols=12, labelText='Model Name:', tgt=form.C_ModelNameKw, sel=0)
        GroupBox_11 = FXGroupBox(p=VFrame_8, text='Die Parameters', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='Die Name:', tgt=form.C_DieNameKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='R (mm):', tgt=form.C_RKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='r (mm):', tgt=form.C_rKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='S (mm):', tgt=form.C_SKw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='h1 (mm):', tgt=form.C_h1Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='h2 (mm):', tgt=form.C_h2Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='h3 (mm):', tgt=form.C_h3Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='h4 (mm):', tgt=form.C_h4Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='h5 (mm):', tgt=form.C_h5Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='alpha1 (DEG):', tgt=form.C_a1Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='alpha2 (DEG):', tgt=form.C_a2Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='alpha3 (DEG):', tgt=form.C_a3Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='alpha4 (DEG):', tgt=form.C_a4Kw, sel=0)
        AFXTextField(p=GroupBox_11, ncols=12, labelText='alpha5 (DEG):', tgt=form.C_a5Kw, sel=0)
        GroupBox_12 = FXGroupBox(p=VFrame_8, text='Wire Parameters', opts=FRAME_GROOVE)
        AFXTextField(p=GroupBox_12, ncols=12, labelText='Wire Name:', tgt=form.C_WireNameKw, sel=0)
        AFXTextField(p=GroupBox_12, ncols=12, labelText='R wire (mm):', tgt=form.C_RwireKw, sel=0)
        AFXTextField(p=GroupBox_12, ncols=12, labelText='Wire Length (mm):', tgt=form.C_WireLengthKw, sel=0)
        VFrame_9 = FXVerticalFrame(p=HFrame_7, opts=LAYOUT_FILL_X|LAYOUT_FILL_Y, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=50, pb=0)
        fileName = os.path.join(thisDir, 'Circle_664_462.png')
        icon = afxCreatePNGIcon(fileName)
        FXLabel(p=VFrame_9, text='', ic=icon)
        tabItem = FXTabItem(p=TabBook_2, text='Analysis Setup', ic=None, opts=TAB_TOP_NORMAL,
            x=0, y=0, w=0, h=0, pl=6, pr=6, pt=DEFAULT_PAD, pb=DEFAULT_PAD)
        TabItem_5 = FXVerticalFrame(p=TabBook_2,
            opts=FRAME_RAISED|FRAME_THICK|LAYOUT_FILL_X,
            x=0, y=0, w=0, h=0, pl=DEFAULT_SPACING, pr=DEFAULT_SPACING,
            pt=DEFAULT_SPACING, pb=DEFAULT_SPACING, hs=DEFAULT_SPACING, vs=DEFAULT_SPACING)
        GroupBox_8 = FXGroupBox(p=TabItem_5, text='ExperimentSetup', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        AFXTextField(p=GroupBox_8, ncols=12, labelText='Friction Coefficient:', tgt=form.FrictionCoefKw, sel=0)
        AFXTextField(p=GroupBox_8, ncols=12, labelText='Drawing Speed (mm/s):', tgt=form.SpeedKw, sel=0)
        GroupBox_9 = FXGroupBox(p=TabItem_5, text='Analysis Setup', opts=FRAME_GROOVE|LAYOUT_FILL_X)
        AFXTextField(p=GroupBox_9, ncols=12, labelText='Simulation Time (s):', tgt=form.TimeKw, sel=0)
        VFrame_5 = FXVerticalFrame(p=HFrame_3, opts=0, x=0, y=0, w=0, h=0,
            pl=0, pr=0, pt=0, pb=0)
