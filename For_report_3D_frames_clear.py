from abaqus import *
from abaqusConstants import *
import __main__
from odbAccess import *
from abaqusConstants import *
from odbMaterial import *
from odbSection import *

dir = 'D:/VKR/For_VKR_All/'
naming = '/500_015_055_18974_Hex_die_Rigit_200'
db = '/HEX_Rigid_Model-18974_500_0_15'
path_import = dir + naming
path_export = path_import + '/output'
names = [db]

step = 0

for name in names:
    temp_odb_view = session.openOdb(name=path_import + name + '.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=temp_odb_view)
    odb = session.odbs[path_import + name + '.odb']

    steps_ = odb.steps.values()[0]
    nframes = len(steps_.frames) - 1

    frames = [0, nframes]

    for frame in frames:
        session.viewports['Viewport: 1'].odbDisplay.setFrame(step=step, frame=frame)
        session.fieldReportOptions.setValues(printTotal=OFF, printMinMax=OFF)

        session.writeFieldReport(fileName=path_export + name + '_' + str(frame) + '.txt', append=OFF, sortItem='Nodal Label',
                                 odb=odb, step=step, frame=frame, outputPosition=NODAL,
                                 variable=(
                                     ('COORD', NODAL,
                                      ((COMPONENT, 'COOR1'), (COMPONENT, 'COOR2'), (COMPONENT, 'COOR3'),)),
                                     ('S', INTEGRATION_POINT, (
                                     (COMPONENT, 'S11'), (COMPONENT, 'S22'), (COMPONENT, 'S33'), (COMPONENT, 'S12'),
                                     (COMPONENT, 'S13'), (COMPONENT, 'S23'),)),
                                     ('PE', INTEGRATION_POINT, (
                                     (COMPONENT, 'PE11'), (COMPONENT, 'PE22'), (COMPONENT, 'PE33'), (COMPONENT, 'PE12'),
                                     (COMPONENT, 'PE13'), (COMPONENT, 'PE23'),)),
                                     ('LE', INTEGRATION_POINT, (
                                     (COMPONENT, 'LE11'), (COMPONENT, 'LE22'), (COMPONENT, 'LE33'), (COMPONENT, 'LE12'),
                                     (COMPONENT, 'LE13'), (COMPONENT, 'LE23'),),),
                                 ))

    odb.close()
