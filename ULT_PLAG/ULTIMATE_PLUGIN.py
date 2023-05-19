from abaqus import *
from abaqusConstants import *
import __main__


def drawing_process(DieSelector, DieType, H_ModelName, H_DieName, H_r, H_R, H_S, H_h1, H_h2, H_h3, H_WireName, H_Rwire, H_WireLength,
                    C_ModelName, C_DieName, C_R, C_r, C_S, C_h1, C_h2, C_h3, C_h4, C_h5, C_WireName, C_Rwire,
                    C_WireLength, Time, Speed, FrictionCoef, H_a1, H_a2, H_a3, C_a1, C_a2, C_a3, C_a4, C_a5):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    import math

    def CIRCLE(DieType, C_ModelName, C_DieName, C_R, C_r, C_S, C_h1, C_h2, C_h3, C_h4, C_h5, C_WireName, C_Rwire, C_WireLength,
               Time, Speed, FrictionCoef, C_a1, C_a2, C_a3, C_a4, C_a5):
        C_ModelName = "CIRCLE_" + DieType + "_" + C_ModelName
        C_DieName = "CIRCLE_" + C_DieName
        C_WireName = "CIRCLE_" + C_WireName
        
        if (DieType == "Rigid"):
            Type = DISCRETE_RIGID_SURFACE
        elif (DieType == "Deformable"):
            Type = DEFORMABLE_BODY
        
        # Create a Die
        mdb.Model(name=C_ModelName, modelType=STANDARD_EXPLICIT)
        a = mdb.models[C_ModelName].rootAssembly
        session.viewports['Viewport: 1'].setValues(displayedObject=None)
        s = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, C_R))
        s.Line(point1=(C_r / 2, C_r * sqrt(3) / 2), point2=(C_r, 0.0))
        s.Line(point1=(C_r, 0.0), point2=(C_r / 2, -C_r * sqrt(3) / 2))
        s.Line(point1=(C_r / 2, -C_r * sqrt(3) / 2), point2=(-C_r / 2, -C_r * sqrt(3) / 2))
        s.HorizontalConstraint(entity=g[5], addUndoState=False)
        s.Line(point1=(-C_r / 2, -C_r * sqrt(3) / 2), point2=(-C_r, 0.0))
        s.Line(point1=(-C_r, 0.0), point2=(-C_r / 2, C_r * sqrt(3) / 2))
        s.Line(point1=(-C_r / 2, C_r * sqrt(3) / 2), point2=(C_r / 2, C_r * sqrt(3) / 2))
        s.HorizontalConstraint(entity=g[8], addUndoState=False)
        p = mdb.models[C_ModelName].Part(name=C_DieName, dimensionality=THREE_D,
                                         type=Type)
        p = mdb.models[C_ModelName].parts[C_DieName]
        p.BaseSolidExtrude(sketch=s, depth=C_S)
        s.unsetPrimaryObject()
        p = mdb.models[C_ModelName].parts[C_DieName]
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models[C_ModelName].sketches['__profile__']
        p = mdb.models[C_ModelName].parts[C_DieName]
        f = p.faces
        p.DatumPlaneByOffset(plane=f[7], flip=SIDE1, offset=C_h4)
        p = mdb.models[C_ModelName].parts[C_DieName]
        f1, d1 = p.faces, p.datums
        p.DatumPlaneByOffset(plane=d1[2], flip=SIDE1, offset=C_h3)
        p = mdb.models[C_ModelName].parts[C_DieName]
        f, d2 = p.faces, p.datums
        p.DatumPlaneByOffset(plane=d2[3], flip=SIDE1, offset=C_h2)
        p = mdb.models[C_ModelName].parts[C_DieName]
        f1, d1 = p.faces, p.datums
        p.DatumPlaneByOffset(plane=d1[4], flip=SIDE1, offset=C_h1)
        p = mdb.models[C_ModelName].parts[C_DieName]
        f, d2 = p.faces, p.datums
        p.DatumPlaneByOffset(plane=f[8], flip=SIDE1, offset=C_h5)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[6], sketchUpEdge=e[19],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          -C_h5))
        s1 = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                       sheetSize=238.0, gridSpacing=5.95, transform=t)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
        C_r5 = C_r + 2 * C_h5 * tan(C_a5*pi/180) / sqrt(3)
        s1.Line(point1=(0.0, C_r5), point2=(C_r5 * sqrt(3) / 2, C_r5 / 2))
        s1.Line(point1=(C_r5 * sqrt(3) / 2, C_r5 / 2), point2=(C_r5 * sqrt(3) / 2, -C_r5 / 2))
        s1.VerticalConstraint(entity=g[3], addUndoState=False)
        s1.Line(point1=(C_r5 * sqrt(3) / 2, -C_r5 / 2), point2=(0.0, -C_r5))
        s1.Line(point1=(0.0, -C_r5), point2=(-C_r5 * sqrt(3) / 2, -C_r5 / 2))
        s1.Line(point1=(-C_r5 * sqrt(3) / 2, -C_r5 / 2), point2=(-C_r5 * sqrt(3) / 2, C_r5 / 2))
        s1.VerticalConstraint(entity=g[6], addUndoState=False)
        s1.Line(point1=(-C_r5 * sqrt(3) / 2, C_r5 / 2), point2=(0.0, C_r5))
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, C_R))
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[6], sketchUpEdge=e1[19], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s1)
        s1.unsetPrimaryObject()
        del mdb.models[C_ModelName].sketches['__profile__']
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=e[25],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          C_S + C_h4))
        s = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=238.0, gridSpacing=5.95, transform=t)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_R, 0.0))
        C_r4 = C_r + 2 * C_h4 * tan(C_a4*pi/180) / sqrt(3)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_r4, 0.0))
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[2], sketchUpEdge=e1[25], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s)
        s.unsetPrimaryObject()
        del mdb.models[C_ModelName].sketches['__profile__']
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[3], sketchUpEdge=e[27],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          C_S + C_h4 + C_h3))
        s1 = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                       sheetSize=238.0, gridSpacing=5.95, transform=t)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_R, 0.0))
        C_r3 = C_r4 + 2 * C_h3 * tan(C_a3*pi/180) / sqrt(3)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_r3, 0.0))
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[3], sketchUpEdge=e1[27], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s1)
        s1.unsetPrimaryObject()
        del mdb.models[C_ModelName].sketches['__profile__']
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[4], sketchUpEdge=e[29],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          C_S + C_h4 + C_h3 + C_h2))
        s = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=238.0, gridSpacing=5.95, transform=t)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
        C_r2 = C_r3 + 2 * C_h2 * tan(C_a2*pi/180) / sqrt(3)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(0.0, C_r2))
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_R, 0.0))
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[4], sketchUpEdge=e1[29], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s)
        s.unsetPrimaryObject()
        del mdb.models[C_ModelName].sketches['__profile__']
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[5], sketchUpEdge=e[31],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          C_S + C_h4 + C_h3 + C_h2 + C_h1))
        s1 = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                       sheetSize=238.0, gridSpacing=5.95, transform=t)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_R, 0.0))
        C_r1 = C_r2 + 2 * C_h1 * tan(C_a1*pi/180) / sqrt(3)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_r1, 0.0))
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[5], sketchUpEdge=e1[31], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s1)
        s1.unsetPrimaryObject()
        del mdb.models[C_ModelName].sketches['__profile__']
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[14],), (e[1],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[13],), (e1[12],)), startCondition=NONE,
                  endCondition=NONE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[13],), (e[10],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[10],), (e1[11],)), startCondition=NONE,
                  endCondition=NONE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[12],), (e[0],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[8],), (e1[9],)), startCondition=NONE,
                  endCondition=NONE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[9],), (e[16],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[8], e1[9], e1[10], e1[11], e1[12], e1[13]), (e1[7],
                                                                                 )), startCondition=NONE,
                  endCondition=NONE)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[28],), (e[0],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)
        p = mdb.models[C_ModelName].parts[C_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[1], e1[2], e1[3], e1[4], e1[5], e1[6]), (e1[7],
                                                                             e1[8], e1[9], e1[10], e1[11], e1[12])),
                  startCondition=NONE,
                  endCondition=NONE)
        # From Solid-To-Shell
        if DieType == "Rigid":
            p = mdb.models[C_ModelName].parts[C_DieName]
            c1 = p.cells
            p.RemoveCells(cellList=c1[0:6])
        
            p = mdb.models[C_ModelName].parts[C_DieName]
            v1, e, d1, n = p.vertices, p.edges, p.datums, p.nodes
            p.ReferencePoint(point=v1[12])

        # Create a Wire
        s = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(C_Rwire, 0.0))
        p = mdb.models[C_ModelName].Part(name=C_WireName, dimensionality=THREE_D,
                                         type=DEFORMABLE_BODY)
        p = mdb.models[C_ModelName].parts[C_WireName]
        p.BaseSolidExtrude(sketch=s, depth=C_WireLength)
        s.unsetPrimaryObject()
        p = mdb.models[C_ModelName].parts[C_WireName]
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models[C_ModelName].sketches['__profile__']
        session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,
                                                               engineeringFeatures=ON)
        session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
            referenceRepresentation=OFF)
        
        # Create Partition
        if DieType == "Deformable":
            p = mdb.models[C_ModelName].parts[C_WireName]
            c = p.cells
            pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
            v, e, d = p.vertices, p.edges, p.datums
            p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
                edge=e[1], rule=CENTER), point2=p.InterestingPoint(edge=e[1], 
                rule=MIDDLE), point3=p.InterestingPoint(edge=e[0], rule=MIDDLE))
            p = mdb.models[C_ModelName].parts[C_WireName]
            c = p.cells
            pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
            v1, e1, d1 = p.vertices, p.edges, p.datums
            p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
                edge=e1[6], rule=MIDDLE), point2=p.InterestingPoint(edge=e1[4], 
                rule=CENTER), point3=p.InterestingPoint(edge=e1[5], rule=MIDDLE))
        elif DieType == "Rigid":
            p = mdb.models[C_ModelName].parts[C_WireName]
            f, e, d = p.faces, p.edges, p.datums
            t = p.MakeSketchTransform(sketchPlane=f[1], sketchUpEdge=e[0], 
                sketchPlaneSide=SIDE1, origin=(0.0, 0.0, 200.0))
            s = mdb.models[C_ModelName].ConstrainedSketch(name='__profile__', 
                sheetSize=415.69, gridSpacing=10.39, transform=t)
            g, v, d1, c = s.geometry, s.vertices, s.dimensions, s.constraints
            s.setPrimaryObject(option=SUPERIMPOSE)
            p = mdb.models[C_ModelName].parts[C_WireName]
            p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
            s.Line(point1=(0.0, C_Rwire), point2=(0.0, -C_Rwire))
            s.VerticalConstraint(entity=g[3], addUndoState=False)
            s.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
            s.CoincidentConstraint(entity1=v[2], entity2=g[2], addUndoState=False)
            s.CoincidentConstraint(entity1=v[3], entity2=g[2], addUndoState=False)
            s.Line(point1=(-C_Rwire, 0.0), point2=(C_Rwire, 0.0))
            s.HorizontalConstraint(entity=g[4], addUndoState=False)
            s.PerpendicularConstraint(entity1=g[2], entity2=g[4], addUndoState=False)
            s.CoincidentConstraint(entity1=v[4], entity2=g[2], addUndoState=False)
            p = mdb.models[C_ModelName].parts[C_WireName]
            f = p.faces
            pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
            e1, d2 = p.edges, p.datums
            p.PartitionFaceBySketch(sketchUpEdge=e1[0], faces=pickedFaces, sketch=s)
            s.unsetPrimaryObject()
            del mdb.models[C_ModelName].sketches['__profile__']
        
            
                   
        #create Material for wire
        mdb.models[C_ModelName].Material(name='Wire_Material')
        mdb.models[C_ModelName].materials['Wire_Material'].Density(
            table=((7.64e-09, ), ))
        mdb.models[C_ModelName].materials['Wire_Material'].Elastic(
            table=((211000.0, 0.3), ))
        mdb.models[C_ModelName].materials['Wire_Material'].Plastic(
            table=((10.0, 0.0), (193.4570359, 0.1), (221.9159247, 0.2), (
            240.4664753, 0.3), (254.5613161, 0.4), (266.0606147, 0.5), (275.840783, 
            0.6), (284.3897511, 0.7), (292.0090737, 0.8), (298.8990579, 0.9), (
            305.2, 1.0), (311.014245, 1.1), (316.4188997, 1.2), (321.4735995, 1.3), 
            (326.2254812, 1.4), (330.712491, 1.5), (334.9656596, 1.6), (
            339.0107077, 1.7), (342.8692088, 1.8), (346.5594473, 1.9), (
            350.0970638, 2.0)))
        mdb.models[C_ModelName].materials['Wire_Material'].plastic.RateDependent(
            table=((115.0, 5.0), ))
        #create Material for Die
        mdb.models[C_ModelName].Material(name='Die_Material')
        mdb.models[C_ModelName].materials['Die_Material'].Density(table=((1.5e-08, ),))
        mdb.models[C_ModelName].materials['Die_Material'].Elastic(table=((63300.0, 0.21), ))
        
        #Create Section fo Die
        if (DieType == "Deformable"):
            mdb.models[C_ModelName].HomogeneousSolidSection(
                name='Section-Die', material='Die_Material', thickness=None)
            p = mdb.models[C_ModelName].parts[C_DieName]
            c = p.cells
            cells = c.getSequenceFromMask(mask=('[#3f ]', ), )
            region = p.Set(cells=cells, name='All_Die')
            p = mdb.models[C_ModelName].parts[C_DieName]
            p.SectionAssignment(region=region, sectionName='Section-Die', offset=0.0, 
                offsetType=MIDDLE_SURFACE, offsetField='', 
                thicknessAssignment=FROM_SECTION)
        
        #Create a Section for Wire
        mdb.models[C_ModelName].HomogeneousSolidSection(
            name='Section-Wire', material='Wire_Material', thickness=None)
        p = mdb.models[C_ModelName].parts[C_WireName]
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#f ]', ), )
        region = regionToolset.Region(cells=cells)
        p = mdb.models[C_ModelName].parts[C_WireName]
        p.SectionAssignment(region=region, sectionName='Section-Wire', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION)
        
        #Create Instances
        if (DieType == "Rigid"):
            a = mdb.models[C_ModelName].rootAssembly
            a.DatumCsysByDefault(CARTESIAN)
            p = mdb.models[C_ModelName].parts[C_DieName]
            C_DieInstance = C_DieName + "-1"
            a.Instance(name=C_DieInstance, part=p, dependent=ON)
            p = mdb.models[C_ModelName].parts[C_WireName]
            C_WireInstance = C_WireName + "-1"
            a.Instance(name=C_WireInstance, part=p, dependent=ON)
            #Translate Instance
            a = mdb.models[C_ModelName].rootAssembly
            C_trn = C_h1 + C_h2 + C_h3 + C_h4 + C_S
            a.translate(instanceList=(C_WireInstance,), vector=(0.0, 0.0, C_trn))
            session.viewports['Viewport: 1'].assemblyDisplay.setValues(
                adaptiveMeshConstraints=ON)
        elif (DieType == "Deformable"):
            a = mdb.models[C_ModelName].rootAssembly
            a.DatumCsysByDefault(CARTESIAN)
            p = mdb.models[C_ModelName].parts[C_DieName]
            C_DieInstance = C_DieName + "-1"
            a.Instance(name=C_DieInstance, part=p, dependent=ON)
            p = mdb.models[C_ModelName].parts[C_WireName]
            C_WireInstance = C_WireName + "-1"
            a.Instance(name=C_WireInstance, part=p, dependent=ON)
            a = mdb.models[C_ModelName].rootAssembly
            C_trn = C_h1 + C_h2 + C_h3 + C_h4 + C_S
            a.translate(instanceList=(C_WireInstance, ), vector=(0.0, 0.0, C_trn))
            session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
            
            
        #Create Step
        mdb.models[C_ModelName].ExplicitDynamicsStep(name='Drawing', previous='Initial',
                                                     timePeriod=Time, improvedDtMethod=ON)
        
        #Create a Field Output
        mdb.models[C_ModelName].fieldOutputRequests['F-Output-1'].setValues(variables=(
                'A', 'COORD', 'CSTRESS', 'E', 'EVF', 'EVOL', 'LE', 'MISES', 'PE', 
                'PEEQ', 'PEEQVAVG', 'PEVAVG', 'RF', 'S', 'SVAVG', 'U', 'V'), numIntervals=200)
    
        #Create Interaction Properties
        if (DieType == "Rigid"):
            mdb.models[C_ModelName].ContactProperty('IntProp-1')
            mdb.models[C_ModelName].interactionProperties['IntProp-1'].TangentialBehavior(
                formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
                pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
                table=((FrictionCoef, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
                fraction=0.005, elasticSlipStiffness=None)
            a = mdb.models[C_ModelName].rootAssembly
            s1 = a.instances[C_DieInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#493f3f3f ]', ), )
            region1=a.Surface(side1Faces=side1Faces1, name='Die_Surf')
            a = mdb.models[C_ModelName].rootAssembly
            s1 = a.instances[C_WireInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#28 ]', ), )
            region2=a.Surface(side1Faces=side1Faces1, name='Wire_Surf')
            mdb.models[C_ModelName].SurfaceToSurfaceContactExp(name ='Int-1', 
                createStepName='Drawing', master = region1, slave = region2, 
                mechanicalConstraint=KINEMATIC, sliding=FINITE, 
                interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
                clearanceRegion=None)
        elif (DieType == "Deformable"):
            mdb.models[C_ModelName].ContactProperty('IntProp-1')
            mdb.models[C_ModelName].interactionProperties['IntProp-1'].TangentialBehavior(
                formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
                pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
                table=((FrictionCoef, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
                fraction=0.005, elasticSlipStiffness=None)
            a = mdb.models[C_ModelName].rootAssembly
            s1 = a.instances[C_DieInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#493f3f3f ]', ), )
            region1=a.Surface(side1Faces=side1Faces1, name='Die-surf')
            a = mdb.models[C_ModelName].rootAssembly
            s1 = a.instances[C_WireInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#b8ac ]', ), )
            region2=a.Surface(side1Faces=side1Faces1, name='Wire-surf')
            mdb.models[C_ModelName].SurfaceToSurfaceContactExp(
                name ='Int-1', createStepName='Initial', master = region1, 
                slave = region2, mechanicalConstraint=KINEMATIC, sliding=FINITE, 
                interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
                clearanceRegion=None)
            
        
        # Create a BC's
        if DieType == "Rigid":
            a = mdb.models[C_ModelName].rootAssembly
            r1 = a.instances[C_DieInstance].referencePoints
            refPoints1=(r1[23], )
            region = regionToolset.Region(referencePoints=refPoints1)
            mdb.models[C_ModelName].VelocityBC(name='Velocity', 
                createStepName='Drawing', region=region, v1=0.0, v2=0.0, v3=Speed, 
                vr1=0.0, vr2=0.0, vr3=0.0, amplitude=UNSET, localCsys=None, 
                distributionType=UNIFORM, fieldName='')
            a = mdb.models[C_ModelName].rootAssembly
            f1 = a.instances[C_WireInstance].faces
            faces1 = f1.getSequenceFromMask(mask=('[#20 ]', ), )
            region = regionToolset.Region(faces=faces1)
            mdb.models[C_ModelName].ZsymmBC(name='Zsymm', 
                createStepName='Drawing', region=region, localCsys=None)
            a = mdb.models[C_ModelName].rootAssembly
            v1 = a.instances[C_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[C_ModelName].XsymmBC(name='Xsymm', 
                createStepName='Drawing', region=region, localCsys=None)
            a = mdb.models[C_ModelName].rootAssembly
            v1 = a.instances[C_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[C_ModelName].YsymmBC(name='Ysymm', 
                createStepName='Drawing', region=region, localCsys=None)
            session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
                bcs=OFF, predefinedFields=OFF, connectors=OFF)
            session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
                meshTechnique=ON) 
        elif DieType == "Deformable":
            a = mdb.models[C_ModelName].rootAssembly
            v1 = a.instances[C_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[C_ModelName].XsymmBC(name='Xsymm', 
                createStepName='Drawing', region=region, localCsys=None)
            a = mdb.models[C_ModelName].rootAssembly
            v1 = a.instances[C_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[C_ModelName].YsymmBC(name='Ysymm', 
                createStepName='Drawing', region=region, localCsys=None)
            a = mdb.models[C_ModelName].rootAssembly
            f1 = a.instances[C_WireInstance].faces
            faces1 = f1.getSequenceFromMask(mask=('[#8884 ]', ), )
            region = regionToolset.Region(faces=faces1)
            mdb.models[C_ModelName].VelocityBC(name='Velociry', 
                createStepName='Drawing', region=region, v1=UNSET, v2=UNSET, 
                v3=-Speed, vr1=UNSET, vr2=UNSET, vr3=0.0, amplitude=UNSET, 
                localCsys=None, distributionType=UNIFORM, fieldName='')
            a = mdb.models[C_ModelName].rootAssembly
            c1 = a.instances[C_DieInstance].cells
            cells1 = c1.getSequenceFromMask(mask=('[#3f ]', ), )
            f1 = a.instances[C_DieInstance].faces
            faces1 = f1.getSequenceFromMask(mask=('[#ffffffff #3 ]', ), )
            e1 = a.instances[C_DieInstance].edges
            edges1 = e1.getSequenceFromMask(mask=('[#ffffffff #1bffff ]', ), )
            v1 = a.instances[C_DieInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#ffffffff ]', ), )
            region = regionToolset.Region(vertices=verts1, edges=edges1, faces=faces1, 
                cells=cells1)
            mdb.models[C_ModelName].EncastreBC(name='Pin', 
                createStepName='Drawing', region=region, localCsys=None)
            

        #Meshing
        if DieType == "Rigid":
            p = mdb.models[C_ModelName].parts[C_DieName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[C_ModelName].parts[C_DieName]
            p.generateMesh()
            p = mdb.models[C_ModelName].parts[C_WireName]
            session.viewports['Viewport: 1'].setValues(displayedObject=p)
            p = mdb.models[C_ModelName].parts[C_WireName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[C_ModelName].parts[C_WireName]
            p.generateMesh()
        elif DieType == "Deformable":
            p = mdb.models[C_ModelName].parts[C_DieName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[C_ModelName].parts[C_DieName]
            p.generateMesh()
            p = mdb.models[C_ModelName].parts[C_WireName]
            e = p.edges
            pickedEdges = e.getSequenceFromMask(mask=('[#1e725a00 ]', ), )
            p.seedEdgeBySize(edges=pickedEdges, size=2.85, deviationFactor=0.1, 
                constraint=FINER)
            p = mdb.models[C_ModelName].parts[C_WireName]
            e = p.edges
            pickedEdges = e.getSequenceFromMask(mask=('[#42108 ]', ), )
            p.seedEdgeBySize(edges=pickedEdges, size=4.5, deviationFactor=0.1, 
                constraint=FINER)
            p = mdb.models[C_ModelName].parts[C_WireName]
            e = p.edges
            pickedEdges = e.getSequenceFromMask(mask=('[#10980d2 ]', ), )
            p.seedEdgeBySize(edges=pickedEdges, size=2.85, deviationFactor=0.1, 
                constraint=FINER)
            p = mdb.models[C_ModelName].parts[C_WireName]
            p.generateMesh()
        
        session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
        session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
            meshTechnique=OFF)
        session.viewports['Viewport: 1'].view.setValues(session.views['Iso'])
        def Replace(str1):
            str1 = str1.replace('.', '_')
            return str1
        

        C_JobName = C_ModelName + "_" + Replace(str(Speed)) + "_" + Replace(str(FrictionCoef))
        mdb.Job(name=C_JobName, model=C_ModelName, description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, explicitPrecision=DOUBLE_PLUS_PACK,
                nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF,
                contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='',
                resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=3,
                activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=3)
        a = mdb.models[C_ModelName].rootAssembly
        a.regenerate()
        

    def HEX(DieType, H_ModelName, H_DieName, H_r, H_R, H_S, H_h1, H_h2, H_h3, H_WireName, H_Rwire, H_WireLength, Time, Speed,
            FrictionCoef, H_a1, H_a2, H_a3):
        H_ModelName = "HEX_" + DieType + "_" + H_ModelName
        H_DieName = "HEX_" + H_DieName
        H_WireName = "HEX_" + H_WireName
        
        if (DieType == "Rigid"):
            Type = DISCRETE_RIGID_SURFACE
        elif (DieType == "Deformable"):
            Type = DEFORMABLE_BODY
        
        mdb.Model(name=H_ModelName, modelType=STANDARD_EXPLICIT)
        a = mdb.models[H_ModelName].rootAssembly
        session.viewports['Viewport: 1'].setValues(displayedObject=None)

        s = mdb.models[H_ModelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)

        # Create the smallest die radius
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(H_R, 0.0))
        s.Line(point1=(-H_r, 0.0), point2=(-H_r / 2, H_r * sqrt(3) / 2))
        s.Line(point1=(-H_r / 2, H_r * sqrt(3) / 2), point2=(H_r / 2, H_r * sqrt(3) / 2))
        s.HorizontalConstraint(entity=g[4], addUndoState=False)
        s.Line(point1=(H_r / 2, H_r * sqrt(3) / 2), point2=(H_r, 0.0))
        s.Line(point1=(H_r, 0.0), point2=(H_r / 2, -H_r * sqrt(3) / 2))
        s.Line(point1=(H_r / 2, -H_r * sqrt(3) / 2), point2=(-H_r / 2, -H_r * sqrt(3) / 2))
        s.HorizontalConstraint(entity=g[7], addUndoState=False)
        s.Line(point1=(-H_r / 2, -H_r * sqrt(3) / 2), point2=(-H_r, 0.0))
        p = mdb.models[H_ModelName].Part(name=H_DieName, dimensionality=THREE_D,
                                         type=Type)
        p = mdb.models[H_ModelName].parts[H_DieName]
        p.BaseSolidExtrude(sketch=s, depth=H_S)
        s.unsetPrimaryObject()
        p = mdb.models[H_ModelName].parts[H_DieName]
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models[H_ModelName].sketches['__profile__']
        p = mdb.models[H_ModelName].parts[H_DieName]
        f = p.faces
        p.DatumPlaneByOffset(plane=f[7], flip=SIDE1, offset=H_h2)
        p = mdb.models[H_ModelName].parts[H_DieName]
        f1, d1 = p.faces, p.datums
        p.DatumPlaneByOffset(plane=d1[2], flip=SIDE1, offset=H_h1)

        p = mdb.models[H_ModelName].parts[H_DieName]
        f, d2 = p.faces, p.datums
        p.DatumPlaneByOffset(plane=f[8], flip=SIDE1, offset=H_h3)
        p = mdb.models[H_ModelName].parts[H_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[4], sketchUpEdge=e[14],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          -H_h3))
        s1 = mdb.models[H_ModelName].ConstrainedSketch(name='__profile__',
                                                       sheetSize=216.04, gridSpacing=5.4, transform=t)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[H_ModelName].parts[H_DieName]
        p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)

        H_r3 = H_r + 2*H_h3*tan(H_a3*pi/180)/sqrt(3)
        H_r3 = round(H_r3, 2)
        s1.Line(point1=(0.0, H_r3), point2=(sqrt(3) * H_r3 / 2, H_r3 / 2))
        s1.Line(point1=(sqrt(3) * H_r3 / 2, H_r3 / 2), point2=(sqrt(3) * H_r3 / 2, -H_r3 / 2))
        s1.VerticalConstraint(entity=g[3], addUndoState=False)
        s1.Line(point1=(sqrt(3) * H_r3 / 2, -H_r3 / 2), point2=(0.0, -H_r3))
        s1.Line(point1=(0.0, -H_r3), point2=(-sqrt(3) * H_r3 / 2, -H_r3 / 2))
        s1.Line(point1=(-sqrt(3) * H_r3 / 2, -H_r3 / 2), point2=(-sqrt(3) * H_r3 / 2, H_r3 / 2))
        s1.VerticalConstraint(entity=g[6], addUndoState=False)
        s1.Line(point1=(-sqrt(3) * H_r3 / 2, H_r3 / 2), point2=(0.0, H_r3))
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(H_R, 0.0))
        p = mdb.models[H_ModelName].parts[H_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[4], sketchUpEdge=e1[14], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s1)
        s1.unsetPrimaryObject()
        del mdb.models[H_ModelName].sketches['__profile__']
        p = mdb.models[H_ModelName].parts[H_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[2], sketchUpEdge=e[19],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          H_S + H_h2))
        s = mdb.models[H_ModelName].ConstrainedSketch(name='__profile__',
                                                      sheetSize=216.04, gridSpacing=5.4, transform=t)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[H_ModelName].parts[H_DieName]
        p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
        H_r2 = H_r + tan(H_a2*pi/180) * H_h2 * 2 / sqrt(3)
        s.Line(point1=(0.0, H_r2), point2=(H_r2 * sqrt(3) / 2, H_r2 / 2))
        s.Line(point1=(H_r2 * sqrt(3) / 2, H_r2 / 2), point2=(H_r2 * sqrt(3) / 2, -H_r2 / 2))
        s.VerticalConstraint(entity=g[3], addUndoState=False)
        s.Line(point1=(H_r2 * sqrt(3) / 2, -H_r2 / 2), point2=(0.0, -H_r2))
        s.Line(point1=(0.0, -H_r2), point2=(-H_r2 * sqrt(3) / 2, -H_r2 / 2))
        s.Line(point1=(-H_r2 * sqrt(3) / 2, -H_r2 / 2), point2=(-H_r2 * sqrt(3) / 2, H_r2 / 2))
        s.VerticalConstraint(entity=g[6], addUndoState=False)
        s.Line(point1=(-H_r2 * sqrt(3) / 2, H_r2 / 2), point2=(0.0, H_r2))
        s.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(H_R, 0.0))
        p = mdb.models[H_ModelName].parts[H_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[2], sketchUpEdge=e1[19], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s)
        s.unsetPrimaryObject()
        del mdb.models[H_ModelName].sketches['__profile__']
        p = mdb.models[H_ModelName].parts[H_DieName]
        e, d1 = p.edges, p.datums
        t = p.MakeSketchTransform(sketchPlane=d1[3], sketchUpEdge=e[26],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0,
                                                                                          H_S + H_h2 + H_h1))
        s1 = mdb.models[H_ModelName].ConstrainedSketch(name='__profile__',
                                                       sheetSize=216.04, gridSpacing=5.4, transform=t)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models[H_ModelName].parts[H_DieName]
        p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
        H_r1 = H_r2 + 2 * H_h1 * tan(H_a1*pi/180) / sqrt(3)
        s1.CircleByCenterPerimeter(center=(0.0, 0.0), point1=(H_R, 0.0))
        s1.Line(point1=(H_r1 * sqrt(3) / 2, H_r1 / 2), point2=(H_r1 * sqrt(3) / 2, -H_r1 / 2))
        s1.VerticalConstraint(entity=g[3], addUndoState=False)
        s1.Line(point1=(H_r1 * sqrt(3) / 2, -H_r1 / 2), point2=(0.0, -H_r1))
        s1.Line(point1=(0.0, -H_r1), point2=(-H_r1 * sqrt(3) / 2, -H_r1 / 2))
        s1.Line(point1=(-H_r1 * sqrt(3) / 2, -H_r1 / 2), point2=(-H_r1 * sqrt(3) / 2, H_r1 / 2))
        s1.VerticalConstraint(entity=g[6], addUndoState=False)
        s1.Line(point1=(-H_r1 * sqrt(3) / 2, H_r1 / 2), point2=(0.0, H_r1))
        s1.Line(point1=(0.0, H_r1), point2=(H_r1 * sqrt(3) / 2, H_r1 / 2))
        p = mdb.models[H_ModelName].parts[H_DieName]
        e1, d2 = p.edges, p.datums
        p.Wire(sketchPlane=d2[3], sketchUpEdge=e1[26], sketchPlaneSide=SIDE1,
               sketchOrientation=RIGHT, sketch=s1)
        s1.unsetPrimaryObject()
        del mdb.models[H_ModelName].sketches['__profile__']
        p = mdb.models[H_ModelName].parts[H_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[6],), (e[21],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)

        p = mdb.models[H_ModelName].parts[H_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[15], e1[16], e1[17], e1[18], e1[19], e1[20]), (
            e1[21], e1[22], e1[23], e1[24], e1[25], e1[26])), startCondition=NONE,
                  endCondition=NONE)

        p = mdb.models[H_ModelName].parts[H_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[13],), (e[32],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)

        p = mdb.models[H_ModelName].parts[H_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[8], e1[9], e1[10], e1[11], e1[12], e1[13]), (
            e1[14], e1[15], e1[16], e1[17], e1[18], e1[19])), startCondition=NONE,
                  endCondition=NONE)
        p = mdb.models[H_ModelName].parts[H_DieName]
        e, d1 = p.edges, p.datums
        p.SolidLoft(loftsections=((e[0],), (e[42],)), startCondition=NONE,
                    endCondition=NONE, keepInternalBoundaries=ON)

        p = mdb.models[H_ModelName].parts[H_DieName]
        e1, d2 = p.edges, p.datums
        p.CutLoft(loftsections=((e1[1], e1[2], e1[3], e1[4], e1[5], e1[6]), (e1[7],
                                                                             e1[8], e1[9], e1[10], e1[11], e1[12])),
                  startCondition=NONE,
                  endCondition=NONE)
        
        
        if DieType == "Rigid":
            p = mdb.models[H_ModelName].parts[H_DieName]
            session.viewports['Viewport: 1'].setValues(displayedObject=p)
            p = mdb.models[H_ModelName].parts[H_DieName]
            c = p.cells
            p.RemoveCells(cellList = c[0:4])
            
            p = mdb.models[H_ModelName].parts[H_DieName]
            v, e, d, n = p.vertices, p.edges, p.datums, p.nodes
            p.ReferencePoint(point=v[12])
            
        # create Wire
        s = mdb.models[H_ModelName].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        x = H_Rwire/2.0
        y = H_Rwire*sqrt(3)/2.0
        s.Line(point1=(-H_Rwire, 0.0), point2=(-x, y))
        s.Line(point1=(-x, y), point2=(x, y))
        s.HorizontalConstraint(entity=g[3], addUndoState=False)
        s.Line(point1=(x, y), point2=(H_Rwire, 0.0))
        s.Line(point1=(H_Rwire, 0.0), point2=(x, -y))
        s.Line(point1=(x, -y), point2=(-x, -y))
        s.HorizontalConstraint(entity=g[6], addUndoState=False)
        s.Line(point1=(-x, -y), point2=(-H_Rwire, 0.0))
        p = mdb.models[H_ModelName].Part(name=H_WireName, dimensionality=THREE_D, 
            type=DEFORMABLE_BODY)
        p = mdb.models[H_ModelName].parts[H_WireName]
        p.BaseSolidExtrude(sketch=s, depth=H_WireLength)
        s.unsetPrimaryObject()
        p = mdb.models[H_ModelName].parts[H_WireName]
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models[H_ModelName].sketches['__profile__']
        
        # Create Set for Wire
        if DieType == "Rigid":
            p = mdb.models[H_ModelName].parts[H_WireName]
            c = p.cells
            pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
            v, e, d = p.vertices, p.edges, p.datums
            p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
                edge=e[4], rule=MIDDLE), point2=p.InterestingPoint(edge=e[13], 
                rule=MIDDLE), point3=p.InterestingPoint(edge=e[6], rule=MIDDLE))
            p = mdb.models[H_ModelName].parts[H_WireName]
            c = p.cells
            pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
            v1, e1, d1 = p.vertices, p.edges, p.datums
            p.PartitionCellByPlaneThreePoints(point1=v1[12], point2=v1[10], point3=v1[14], 
                cells=pickedCells)
        elif DieType == "Deformable":
            p = mdb.models[H_ModelName].parts[H_WireName]
            session.viewports['Viewport: 1'].setValues(displayedObject=p)
            p = mdb.models[H_ModelName].parts[H_WireName]
            c = p.cells
            pickedCells = c.getSequenceFromMask(mask=('[#1 ]', ), )
            v, e, d = p.vertices, p.edges, p.datums
            p.PartitionCellByPlaneThreePoints(cells=pickedCells, point1=p.InterestingPoint(
                edge=e[4], rule=MIDDLE), point2=p.InterestingPoint(edge=e[13], 
                rule=MIDDLE), point3=p.InterestingPoint(edge=e[6], rule=MIDDLE))
            p = mdb.models[H_ModelName].parts[H_WireName]
            c = p.cells
            pickedCells = c.getSequenceFromMask(mask=('[#3 ]', ), )
            v1, e1, d1 = p.vertices, p.edges, p.datums
            p.PartitionCellByPlaneThreePoints(point1=v1[12], point2=v1[10], point3=v1[14], 
                cells=pickedCells)
        

        # Create a material for Wire
        mdb.models[H_ModelName].Material(name='Wire_Material')
        mdb.models[H_ModelName].materials['Wire_Material'].Density(
            table=((7.64e-09, ), ))
        mdb.models[H_ModelName].materials['Wire_Material'].Elastic(
            table=((211000.0, 0.3), ))
        mdb.models[H_ModelName].materials['Wire_Material'].Plastic(
            table=((10.0, 0.0), (193.4570359, 0.1), (221.9159247, 0.2), (
            240.4664753, 0.3), (254.5613161, 0.4), (266.0606147, 0.5), (275.840783, 
            0.6), (284.3897511, 0.7), (292.0090737, 0.8), (298.8990579, 0.9), (
            305.2, 1.0), (311.014245, 1.1), (316.4188997, 1.2), (321.4735995, 1.3), 
            (326.2254812, 1.4), (330.712491, 1.5), (334.9656596, 1.6), (
            339.0107077, 1.7), (342.8692088, 1.8), (346.5594473, 1.9), (
            350.0970638, 2.0)))
        mdb.models[H_ModelName].materials['Wire_Material'].plastic.RateDependent(
            table=((115.0, 5.0), ))
        
        #create Material for Die
        mdb.models[H_ModelName].Material(name='Die_Material')
        mdb.models[H_ModelName].materials['Die_Material'].Density(table=((1.5e-08, ),))
        mdb.models[H_ModelName].materials['Die_Material'].Elastic(table=((63300.0, 0.21), ))
        
        # Create and assign a Section for Wire
        mdb.models[H_ModelName].HomogeneousSolidSection(
            name='Section-Wire', material='Wire_Material', thickness=None)
        p = mdb.models[H_ModelName].parts[H_WireName]
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#f ]', ), )
        region = p.Set(cells=cells, name='All_Wire')
        p = mdb.models[H_ModelName].parts[H_WireName]
        p.SectionAssignment(region=region, sectionName='Section-Wire', offset=0.0, 
            offsetType=MIDDLE_SURFACE, offsetField='', 
            thicknessAssignment=FROM_SECTION)
        
        # Create and assign a Section for Die
        p = mdb.models[H_ModelName].parts[H_DieName]
        mdb.models[H_ModelName].HomogeneousSolidSection(name='Section-Die', 
            material='Die_Material', thickness=None)
        if DieType == "Deformable":
            p = mdb.models[H_ModelName].parts[H_DieName]
            c = p.cells
            cells = c.getSequenceFromMask(mask=('[#f ]', ), )
            region = p.Set(cells=cells, name='Die')
            p = mdb.models[H_ModelName].parts[H_DieName]
            p.SectionAssignment(region=region, sectionName='Section-Die', offset=0.0, 
                offsetType=MIDDLE_SURFACE, offsetField='', 
                thicknessAssignment=FROM_SECTION)
               
        # create Instance
        if DieType == "Rigid":
            H_DieInstance = H_DieName + "-1"
            H_WireInstance = H_WireName + "-1"
            a = mdb.models[H_ModelName].rootAssembly
            a.DatumCsysByDefault(CARTESIAN)
            p = mdb.models[H_ModelName].parts[H_DieName]
            a.Instance(name=H_DieInstance, part=p, dependent=ON)
            p = mdb.models[H_ModelName].parts[H_WireName]
            a.Instance(name=H_WireInstance, part=p, dependent=ON)
            a = mdb.models[H_ModelName].rootAssembly
            a.translate(instanceList=(H_WireInstance, ), vector=(0.0, 0.0, H_S+H_h1+H_h2))
        elif DieType == "Deformable":
            H_DieInstance = H_DieName + "-1"
            H_WireInstance = H_WireName + "-1"
            a = mdb.models[H_ModelName].rootAssembly
            a.DatumCsysByDefault(CARTESIAN)
            p = mdb.models[H_ModelName].parts[H_DieName]
            a.Instance(name=H_DieInstance, part=p, dependent=ON)
            p = mdb.models[H_ModelName].parts[H_WireName]
            a.Instance(name=H_WireInstance, part=p, dependent=ON)
            a = mdb.models[H_ModelName].rootAssembly
            a.translate(instanceList=(H_WireInstance, ), vector=(0.0, 0.0, H_S+H_h1+H_h2))
        
        # create Step
        mdb.models[H_ModelName].ExplicitDynamicsStep(name='Drawing', 
            previous='Initial', timePeriod=Time, improvedDtMethod=ON)
                                                     
        mdb.models[H_ModelName].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'A', 'COORD', 'CSTRESS', 'E', 'EVF', 'EVOL', 'LE', 'MISES', 'PE', 
        'PEEQ', 'PEEQVAVG', 'PEVAVG', 'RF', 'S', 'SVAVG', 'U', 'V'), numIntervals=200)
        
        # create Interaction
        if DieType == "Rigid":
            mdb.models[H_ModelName].ContactProperty('IntProp-1')
            mdb.models[H_ModelName].interactionProperties['IntProp-1'].TangentialBehavior(
                formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
                pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
                table=((FrictionCoef, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
                fraction=0.005, elasticSlipStiffness=None)
            a = mdb.models[H_ModelName].rootAssembly
            s1 = a.instances[H_DieInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#7e3f3f3f ]', ), )
            region1=a.Surface(side1Faces=side1Faces1, name='Die_Surf')
            a = mdb.models[H_ModelName].rootAssembly
            s1 = a.instances[H_WireInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#bfb18 ]', ), )
            region2=a.Surface(side1Faces=side1Faces1, name='Wire_Surf')
            mdb.models[H_ModelName].SurfaceToSurfaceContactExp(name ='Int-1', 
                createStepName='Drawing', master = region1, slave = region2, 
                mechanicalConstraint=KINEMATIC, sliding=FINITE, 
                interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
                clearanceRegion=None)
        elif DieType == "Deformable":
            mdb.models[H_ModelName].ContactProperty('IntProp-1')
            mdb.models[H_ModelName].interactionProperties['IntProp-1'].TangentialBehavior(
                formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF, 
                pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, 
                table=((FrictionCoef, ), ), shearStressLimit=None, maximumElasticSlip=FRACTION, 
                fraction=0.005, elasticSlipStiffness=None)
            a = mdb.models[H_ModelName].rootAssembly
            s1 = a.instances[H_DieInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#7e3f3f3f ]', ), )
            region1=a.Surface(side1Faces=side1Faces1, name='Die-surf')
            a = mdb.models[H_ModelName].rootAssembly
            s1 = a.instances[H_WireInstance].faces
            side1Faces1 = s1.getSequenceFromMask(mask=('[#bfb18 ]', ), )
            region2=a.Surface(side1Faces=side1Faces1, name='Wire-surf')
            mdb.models[H_ModelName].SurfaceToSurfaceContactExp(name ='Int-1', 
                createStepName='Drawing', master = region1, slave = region2, 
                mechanicalConstraint=KINEMATIC, sliding=FINITE, 
                interactionProperty='IntProp-1', initialClearance=OMIT, datumAxis=None, 
                clearanceRegion=None)
        
        #Create a BC for RIGID
        if DieType == "Rigid":
            a = mdb.models[H_ModelName].rootAssembly
            r1 = a.instances[H_DieInstance].referencePoints
            refPoints1=(r1[15], )
            region = regionToolset.Region(referencePoints=refPoints1)
            mdb.models[H_ModelName].VelocityBC(name='Velocity', 
                createStepName='Drawing', region=region, v1=0.0, v2=0.0, v3=Speed, 
                vr1=0.0, vr2=0.0, vr3=0.0, amplitude=UNSET, localCsys=None, 
                distributionType=UNIFORM, fieldName='')
            a = mdb.models[H_ModelName].rootAssembly
            f1 = a.instances[H_WireInstance].faces
            faces1 = f1.getSequenceFromMask(mask=('[#80118 ]', ), )
            region = regionToolset.Region(faces=faces1)
            mdb.models[H_ModelName].ZsymmBC(name='Zsymm', createStepName='Drawing', 
                region=region, localCsys=None)
            a = mdb.models[H_ModelName].rootAssembly
            v1 = a.instances[H_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[H_ModelName].XsymmBC(name='Xsymm', createStepName='Drawing', 
                region=region, localCsys=None)
            a = mdb.models[H_ModelName].rootAssembly
            v1 = a.instances[H_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[H_ModelName].YsymmBC(name='Ysymm', createStepName='Drawing', 
                region=region, localCsys=None)
        elif DieType == "Deformable":
            a = mdb.models[H_ModelName].rootAssembly
            v1 = a.instances[H_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[H_ModelName].XsymmBC(name='Xsymm', 
                createStepName='Drawing', region=region, localCsys=None)
            a = mdb.models[H_ModelName].rootAssembly
            v1 = a.instances[H_WireInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#1 ]', ), )
            region = regionToolset.Region(vertices=verts1)
            mdb.models[H_ModelName].YsymmBC(name='Ysymm', 
                createStepName='Drawing', region=region, localCsys=None)
            a = mdb.models[H_ModelName].rootAssembly
            f1 = a.instances[H_WireInstance].faces
            faces1 = f1.getSequenceFromMask(mask=('[#80118 ]', ), )
            region = regionToolset.Region(faces=faces1)
            mdb.models[H_ModelName].VelocityBC(name='Velocity', 
                createStepName='Drawing', region=region, v1=UNSET, v2=UNSET, 
                v3=-Speed, vr1=UNSET, vr2=UNSET, vr3=0.0, amplitude=UNSET, 
                localCsys=None, distributionType=UNIFORM, fieldName='')
            a = mdb.models[H_ModelName].rootAssembly
            c1 = a.instances[H_DieInstance].cells
            cells1 = c1.getSequenceFromMask(mask=('[#f ]', ), )
            f1 = a.instances[H_DieInstance].faces
            faces1 = f1.getSequenceFromMask(mask=('[#ffffffff #1 ]', ), )
            e1 = a.instances[H_DieInstance].edges
            edges1 = e1.getSequenceFromMask(mask=('[#ec1fffff #3fffff5b ]', ), )
            v1 = a.instances[H_DieInstance].vertices
            verts1 = v1.getSequenceFromMask(mask=('[#e5507fff #3f ]', ), )
            region = regionToolset.Region(vertices=verts1, edges=edges1, faces=faces1, 
                cells=cells1)
            mdb.models[H_ModelName].EncastreBC(name='Pin', 
                createStepName='Drawing', region=region, localCsys=None)

  
        # Meshing
        if DieType == "Rigid":
            p = mdb.models[H_ModelName].parts[H_DieName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[H_ModelName].parts[H_DieName]
            p.generateMesh()
            p = mdb.models[H_ModelName].parts[H_WireName]
            session.viewports['Viewport: 1'].setValues(displayedObject=p)
            p = mdb.models[H_ModelName].parts[H_WireName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[H_ModelName].parts[H_WireName]
            p.generateMesh()
        elif DieType == "Deformable":
            p = mdb.models[H_ModelName].parts[H_DieName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[H_ModelName].parts[H_DieName]
            p.generateMesh()
            p = mdb.models[H_ModelName].parts[H_WireName]
            session.viewports['Viewport: 1'].setValues(displayedObject=p)
            p = mdb.models[H_ModelName].parts[H_WireName]
            p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
            p = mdb.models[H_ModelName].parts[H_WireName]
            p.generateMesh()
            
        def Replace(str1):
            str1 = str1.replace('.', '_')
            return str1
        

        # create a Job
        JobName = H_ModelName + "_" + Replace(str(Speed)) + "_" + Replace(str(FrictionCoef))
        mdb.Job(name=JobName, model=H_ModelName, description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, explicitPrecision=DOUBLE_PLUS_PACK,
                nodalOutputPrecision=SINGLE, echoPrint=OFF, modelPrint=OFF,
                contactPrint=OFF, historyPrint=OFF, userSubroutine='', scratch='',
                resultsFormat=ODB, parallelizationMethodExplicit=DOMAIN, numDomains=3,
                activateLoadBalancing=False, multiprocessingMode=DEFAULT, numCpus=3)
        a = mdb.models[H_ModelName].rootAssembly
        a.regenerate()
        
    if (DieSelector == "Hex"):
        HEX(DieType, H_ModelName, H_DieName, H_r, H_R, H_S, H_h1, H_h2, H_h3, H_WireName, H_Rwire, H_WireLength, Time, Speed, FrictionCoef, H_a1, H_a2, H_a3)
    elif (DieSelector == "Circle"):
        CIRCLE(DieType, C_ModelName, C_DieName, C_R, C_r, C_S, C_h1, C_h2, C_h3, C_h4, C_h5, C_WireName, C_Rwire, C_WireLength, Time, Speed, FrictionCoef, C_a1, C_a2, C_a3, C_a4, C_a5)
