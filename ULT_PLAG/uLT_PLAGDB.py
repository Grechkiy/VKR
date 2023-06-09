# Do not edit this file or it may not load correctly
# if you try to open it with the RSG Dialog Builder.

# Note: thisDir is defined by the Activator class when
#       this file gets exec'd

from rsg.rsgGui import *
from abaqusConstants import INTEGER, FLOAT
dialogBox = RsgDialog(title='Drawing', kernelModule='ULTIMATE_PLUGIN', kernelFunction='drawing_process', includeApplyBtn=True, includeSeparator=True, okBtnText='OK', applyBtnText='Apply', execDir=thisDir)
RsgHorizontalFrame(name='HFrame_3', p='DialogBox', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgVerticalFrame(name='VFrame_4', p='HFrame_3', layout='LAYOUT_FILL_X', pl=0, pr=0, pt=0, pb=0)
RsgComboBox(name='ComboBox_2', p='VFrame_4', text='Select a shape of billet', keyword='DieSelector', default='', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_2', text='Hex')
RsgListItem(p='ComboBox_2', text='Circle')
RsgComboBox(name='ComboBox_3', p='VFrame_4', text='Select a type of Die:', keyword='DieType', default='', comboType='STANDARD', repository='', rootText='', rootKeyword=None, layout='')
RsgListItem(p='ComboBox_3', text='Rigid')
RsgListItem(p='ComboBox_3', text='Deformable')
RsgTabBook(name='TabBook_2', p='VFrame_4', layout='LAYOUT_FILL_X')
RsgTabItem(name='TabItem_3', p='TabBook_2', text='Hexagonal Die')
RsgHorizontalFrame(name='HFrame_8', p='TabItem_3', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgVerticalFrame(name='VFrame_10', p='HFrame_8', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_5', p='VFrame_10', text='Model', layout='LAYOUT_FILL_X')
RsgTextField(p='GroupBox_5', fieldType='String', ncols=12, labelText='Model Name:', keyword='H_ModelName', default='Model-1')
RsgGroupBox(name='GroupBox_6', p='VFrame_10', text='Die Parameters', layout='LAYOUT_FILL_X')
RsgTextField(p='GroupBox_6', fieldType='String', ncols=12, labelText='Die Name:', keyword='H_DieName', default='Die')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='R(mm)', keyword='H_R', default='35')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='r(mm):', keyword='H_r', default='18.974')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='S (mm):', keyword='H_S', default='8')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='h1 (mm):', keyword='H_h1', default='6')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='h2 (mm):', keyword='H_h2', default='16')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='h3 (mm):', keyword='H_h3', default='6')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='alpha1 (DEG):', keyword='H_a1', default='20')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='alpha2 (DEG):', keyword='H_a2', default='8')
RsgTextField(p='GroupBox_6', fieldType='Float', ncols=12, labelText='alpha3 (DEG):', keyword='H_a3', default='30')
RsgGroupBox(name='GroupBox_7', p='VFrame_10', text='Wire Parameters', layout='LAYOUT_FILL_X')
RsgTextField(p='GroupBox_7', fieldType='String', ncols=12, labelText='Wire Name:', keyword='H_WireName', default='Wire')
RsgTextField(p='GroupBox_7', fieldType='Float', ncols=12, labelText='R wire (mm):', keyword='H_Rwire', default='20')
RsgTextField(p='GroupBox_7', fieldType='Float', ncols=12, labelText='Wire Length (mm):', keyword='H_WireLength', default='200')
RsgVerticalFrame(name='VFrame_11', p='HFrame_8', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y', pl=0, pr=0, pt=50, pb=0)
RsgIcon(p='VFrame_11', fileName=r'hexxxxxxxxxx_795_405(1).png')
RsgTabItem(name='TabItem_4', p='TabBook_2', text='Circle Die')
RsgHorizontalFrame(name='HFrame_7', p='TabItem_4', layout='0', pl=0, pr=0, pt=0, pb=0)
RsgVerticalFrame(name='VFrame_8', p='HFrame_7', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y', pl=0, pr=0, pt=0, pb=0)
RsgGroupBox(name='GroupBox_10', p='VFrame_8', text='Model', layout='0')
RsgTextField(p='GroupBox_10', fieldType='String', ncols=12, labelText='Model Name:', keyword='C_ModelName', default='Model-1')
RsgGroupBox(name='GroupBox_11', p='VFrame_8', text='Die Parameters', layout='0')
RsgTextField(p='GroupBox_11', fieldType='String', ncols=12, labelText='Die Name:', keyword='C_DieName', default='Die')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='R (mm):', keyword='C_R', default='35')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='r (mm):', keyword='C_r', default='18.974')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='S (mm):', keyword='C_S', default='8')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='h1 (mm):', keyword='C_h1', default='6')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='h2 (mm):', keyword='C_h2', default='6')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='h3 (mm):', keyword='C_h3', default='6')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='h4 (mm):', keyword='C_h4', default='16')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='h5 (mm):', keyword='C_h5', default='6')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='alpha1 (DEG):', keyword='C_a1', default='6')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='alpha2 (DEG):', keyword='C_a2', default='8')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='alpha3 (DEG):', keyword='C_a3', default='10')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='alpha4 (DEG):', keyword='C_a4', default='13')
RsgTextField(p='GroupBox_11', fieldType='Float', ncols=12, labelText='alpha5 (DEG):', keyword='C_a5', default='30')
RsgGroupBox(name='GroupBox_12', p='VFrame_8', text='Wire Parameters', layout='0')
RsgTextField(p='GroupBox_12', fieldType='String', ncols=12, labelText='Wire Name:', keyword='C_WireName', default='Wire')
RsgTextField(p='GroupBox_12', fieldType='Float', ncols=12, labelText='R wire (mm):', keyword='C_Rwire', default='20')
RsgTextField(p='GroupBox_12', fieldType='Float', ncols=12, labelText='Wire Length (mm):', keyword='C_WireLength', default='200')
RsgVerticalFrame(name='VFrame_9', p='HFrame_7', layout='LAYOUT_FILL_X|LAYOUT_FILL_Y', pl=0, pr=0, pt=50, pb=0)
RsgIcon(p='VFrame_9', fileName=r'Circle_664_462.png')
RsgTabItem(name='TabItem_5', p='TabBook_2', text='Analysis Setup')
RsgGroupBox(name='GroupBox_8', p='TabItem_5', text='ExperimentSetup', layout='LAYOUT_FILL_X')
RsgTextField(p='GroupBox_8', fieldType='Float', ncols=12, labelText='Friction Coefficient:', keyword='FrictionCoef', default='0.15')
RsgTextField(p='GroupBox_8', fieldType='Float', ncols=12, labelText='Drawing Speed (mm/s):', keyword='Speed', default='1000')
RsgGroupBox(name='GroupBox_9', p='TabItem_5', text='Analysis Setup', layout='LAYOUT_FILL_X')
RsgTextField(p='GroupBox_9', fieldType='Float', ncols=12, labelText='Simulation Time (s):', keyword='Time', default='0.35')
RsgVerticalFrame(name='VFrame_5', p='HFrame_3', layout='0', pl=0, pr=0, pt=0, pb=0)
dialogBox.show()