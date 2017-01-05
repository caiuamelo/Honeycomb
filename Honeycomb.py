# Funcao: Automatiza a criacao de um honeycomb com gaps preenchidos por elementos coesivos
# Autores: Caiua e Bruno
# Data de criacao: 2/12/2016
 
# Para executar no abaqus?
## Carrega a classe
# H = Honeycomb()
## Seta o tamanho da aresta do hexagono
# H.setEdgeSize(1)
## Tamanho do gap
# H.setGapSize(0.05)
## Numero de colunas  
# H.setNumberColumns(7)
## Numero de linhas
# H.setNumberRows(6)
# H.generateHexs()
# H.generateCohesives()
# H.generateAssembly()

# -*- coding: mbcs -*-
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

class Honeycomb:
    # Atributos
    edge = 4 # Lado do hexagono
    nr = 5 # Numero na linha de hexagonos na aresta
    nc = 5 # Numero na linha de hexagonos na coluna

    gap = 0.05 # Tamanho do gap para os elementos coesivos
     
    # Metodos    
    def setEdgeSize(self,edge):
        self.edge = edge
    def setGapSize(self,gap):
        self.gap = gap
    def setNumberRows(self,nr):
        self.nr = nr
    def setNumberColumns(self,nc):
        self.nc = nc

    def generateHexs(self):
        # Hexagonos: gera as partes hexagonais do honeycomb
        for j in range(2,4*self.nr,4):
            k=0
            for i in range(2,2*self.nc,2):
                k=k+1
                mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0),
                    point2=(1.0*self.edge, 0.0))
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0*self.edge, 0.0),
                    point2=(1.5*self.edge, (sqrt(3)/2)*self.edge))
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.5*self.edge, (sqrt(3)/2)*self.edge), 
                    point2=(1.0*self.edge, sqrt(3)*self.edge))
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0*self.edge, sqrt(3)*self.edge), 
                    point2=(0.0, sqrt(3)*self.edge))
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, sqrt(3)*self.edge), 
                    point2=(-0.5*self.edge, (sqrt(3)/2)*self.edge))
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.5*self.edge, (sqrt(3)/2)*self.edge),
                     point2=(0.0, 0.0))
                mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(j+((k-1)%2)*2)+'-'+str(i), type=
                    DEFORMABLE_BODY)
                mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].BaseShell(sketch=
                    mdb.models['Model-1'].sketches['__profile__'])
                del mdb.models['Model-1'].sketches['__profile__']
                # Cria as particoes para melhorar a malha
                mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                    sheetSize=5.29, transform=
                    mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].MakeSketchTransform(
                    sketchPlane=mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].faces[0],
                    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.5*self.edge, 0.5*sqrt(3)*self.edge,
                    0.0)))
                mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].projectReferencesOntoSketch(filter=
                    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-1.0,
                    4.03784438551824e-07), point2=(1.0, 4.03784438551824e-07))
                mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
                    addUndoState=False, entity=
                    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, -0.5*sqrt(3)*self.edge),
                    point2=(-0.5*self.edge, 0.5*sqrt(3)*self.edge))
                mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.5*self.edge, -0.5*sqrt(3)*self.edge),
                    point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
                mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].PartitionFaceBySketch(faces=
                    mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].faces[0:1],
                    sketch=mdb.models['Model-1'].sketches['__profile__'])
                del mdb.models['Model-1'].sketches['__profile__']
        # Gera as partes hexagonais do honeycomb da aresta inferior
        for i in range(4,2*self.nc,4):
            mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.5*self.edge, (sqrt(3)/2)*self.edge),
                point2=(1.5*self.edge, (sqrt(3)/2)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.5*self.edge, (sqrt(3)/2)*self.edge), 
                point2=(1.0*self.edge, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0*self.edge, sqrt(3)*self.edge), 
                point2=(0.0, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, sqrt(3)*self.edge), 
                point2=(-0.5*self.edge, (sqrt(3)/2)*self.edge))
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(0)+'-'+str(i), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
            # Particoes
            mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                sheetSize=5.29, transform=
            mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)].MakeSketchTransform(
                sketchPlane=mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)].faces[0],
                sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(-0.5*self.edge, 0.5*sqrt(3)*self.edge, 0.0)))
            mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)].projectReferencesOntoSketch(filter=
                COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0), point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0), point2=(1.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)].PartitionFaceBySketch(faces=
                mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)].faces[0:1],
                sketch=mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
        # Gera as partes hexagonais do honeycomb da aresta superior
        for i in range(2,2*self.nc,4):
            mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0),
                point2=(1.0*self.edge, 0.0))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0*self.edge, 0.0),
                point2=(1.5*self.edge, (sqrt(3)/2)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.5*self.edge, (sqrt(3)/2)*self.edge), 
                point2=(-0.5*self.edge, (sqrt(3)/2)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.5*self.edge, (sqrt(3)/2)*self.edge),
                 point2=(0.0, 0.0))
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(4*self.nr+2)+'-'+str(i), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
            # Particoes
            mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                sheetSize=5.29, transform=
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].MakeSketchTransform(
                sketchPlane=mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].faces[0],
                sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].projectReferencesOntoSketch(filter=
                COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0, 0), point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0), point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].PartitionFaceBySketch(faces=
                mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].faces[0:1],
                sketch=mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
        # Gera as partes hexagonais do honeycomb do lado esquerdo
        for j in range(4,4*(self.nr+1),4):
            mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5, 0.0),
                point2=(1.0*self.edge, 0.0))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0*self.edge, 0.0),
                point2=(1.5*self.edge, (sqrt(3)/2)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.5*self.edge, (sqrt(3)/2)*self.edge), 
                point2=(1.0*self.edge, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0*self.edge, sqrt(3)*self.edge), 
                point2=(0.5*self.edge, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, sqrt(3)*self.edge),
                point2=(0.5*self.edge, 0.0))
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(j)+'-'+str(0), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
            # Particoes
            mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                sheetSize=5.29, transform=
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].MakeSketchTransform(
                sketchPlane=mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].faces[0],
                sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.5*self.edge, 0.0, 0.0)))
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].projectReferencesOntoSketch(filter=
                COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0, 0.5*sqrt(3)*self.edge), point2=(0.5*self.edge, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0, 0.5*sqrt(3)*self.edge), point2=(self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0, 0.5*sqrt(3)*self.edge), point2=(0.5*self.edge, 0.0))
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].PartitionFaceBySketch(faces=
                mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].faces[0:1],
                sketch=mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
        # Gera as partes hexagonais do honeycomb do lado direito
        for j in range(2,4*(self.nr),4):
            mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0),
                point2=(0.5*self.edge, 0.0))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.0),
                point2=(0.5*self.edge, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, sqrt(3)*self.edge), 
                point2=(0.0, sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, sqrt(3)*self.edge), 
                point2=(-0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.5*self.edge, 0.5*sqrt(3)*self.edge),
                point2=(0.0, 0.0))
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
            # Particoes
            mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                sheetSize=5.29, transform=
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].MakeSketchTransform(
                sketchPlane=mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].faces[0],
                sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].projectReferencesOntoSketch(filter=
                COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.5*sqrt(3)*self.edge), point2=(0.0, 0.0))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.5*sqrt(3)*self.edge), point2=(-0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.5*sqrt(3)*self.edge), point2=(0.0, sqrt(3)*self.edge))
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].PartitionFaceBySketch(faces=
                mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].faces[0:1],
                sketch=mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
        # Gera as partes hexagonais do honeycomb dos vertices
        mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0),
            point2=(self.edge, 0.0))
        mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0.0),
            point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
        mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.5*sqrt(3)*self.edge), 
            point2=(0, 0.5*sqrt(3)*self.edge))
        mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0, 0.5*sqrt(3)*self.edge),
            point2=(0.0, 0.0))
        mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(0)+'-'+str(0), type=
            DEFORMABLE_BODY)
        mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(0)].BaseShell(sketch=
            mdb.models['Model-1'].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
        mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
            sheetSize=5.29, transform=
        mdb.models['Model-1'].parts['Hex-0-0'].MakeSketchTransform(
            sketchPlane=mdb.models['Model-1'].parts['Hex-0-0'].faces[0],
            sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
        mdb.models['Model-1'].parts['Hex-0-0'].projectReferencesOntoSketch(filter=
            COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
        mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
        mdb.models['Model-1'].parts['Hex-0-0'].PartitionFaceBySketch(faces=
            mdb.models['Model-1'].parts['Hex-0-0'].faces[0:1],
            sketch=mdb.models['Model-1'].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
        if (self.nc % 2) == 1:
            mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0),
                point2=(0.5*self.edge, 0.0))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.0),
                point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.5*sqrt(3)*self.edge), 
                point2=(-0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.5*self.edge, 0.5*sqrt(3)*self.edge), 
                point2=(0.0, 0.0))
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
            mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                sheetSize=5.29, transform=
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)].MakeSketchTransform(
                sketchPlane=mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)].faces[0],
                sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)].projectReferencesOntoSketch(filter=
                COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)].PartitionFaceBySketch(faces=
                mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+ str(2*self.nc)].faces[0:1],
                sketch=mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
        else:
            mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0),
                point2=(self.edge, 0.0))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0.0),
                point2=(self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0.5*sqrt(3)*self.edge), 
                point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.5*self.edge, 0.5*sqrt(3)*self.edge),
                point2=(0.0, 0.0))
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(0)+'-'+str(2*self.nc), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(2*self.nc)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.13, name='__profile__',
                sheetSize=5.29, transform=
            mdb.models['Model-1'].parts['Hex-0-'+str(2*self.nc)].MakeSketchTransform(
                sketchPlane=mdb.models['Model-1'].parts['Hex-0-'+str(2*self.nc)].faces[0],
                sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
            mdb.models['Model-1'].parts['Hex-0-'+str(2*self.nc)].projectReferencesOntoSketch(filter=
                COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
            mdb.models['Model-1'].sketches['__profile__'].Line(point1=(self.edge, 0.0), point2=(0.5*self.edge, 0.5*sqrt(3)*self.edge))
            mdb.models['Model-1'].parts['Hex-0-'+str(2*self.nc)].PartitionFaceBySketch(faces=
                mdb.models['Model-1'].parts['Hex-0-'+str(2*self.nc)].faces[0:1],
                sketch=mdb.models['Model-1'].sketches['__profile__'])
            del mdb.models['Model-1'].sketches['__profile__']
    def generateCohesives(self):
        # Elementos coesivos: gera os elementos coesivos
        # Coesive de angulo 0
        mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, sqrt(3)*self.edge), 
            point2=(self.edge, self.gap + sqrt(3)*self.edge))
        mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Cohesive000', type=
            DEFORMABLE_BODY)
        mdb.models['Model-1'].parts['Cohesive000'].BaseShell(sketch=
            mdb.models['Model-1'].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
        # Coesive de angulo 0 metade (para preencher o lado direito e esquerdo)
        mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(0.0, sqrt(3)*self.edge), 
            point2=(0.5*self.edge, self.gap + sqrt(3)*self.edge))
        mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Cohesive000h', type=
            DEFORMABLE_BODY)
        mdb.models['Model-1'].parts['Cohesive000h'].BaseShell(sketch=
            mdb.models['Model-1'].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
        # Coesive de angulo 60
        mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-0.5*self.edge, 
            0.5*sqrt(3)*self.edge), point2=(-0.5*self.edge-self.gap, self.edge*(1+0.5*sqrt(3))))
        mdb.models['Model-1'].sketches['__profile__'].rotate(angle=-30.0, centerPoint=(-0.5*self.edge, 0.5*sqrt(3)*self.edge), objectList=(
            mdb.models['Model-1'].sketches['__profile__'].geometry[2], 
            mdb.models['Model-1'].sketches['__profile__'].geometry[3], 
            mdb.models['Model-1'].sketches['__profile__'].geometry[4], 
            mdb.models['Model-1'].sketches['__profile__'].geometry[5]))
        mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Cohesive060', 
            type=DEFORMABLE_BODY)
        mdb.models['Model-1'].parts['Cohesive060'].BaseShell(sketch=
            mdb.models['Model-1'].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
        # Coesive de angulo 120
        mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
        mdb.models['Model-1'].sketches['__profile__'].rectangle(point1=(-0.5*self.edge, 
            0.5*sqrt(3)*self.edge), point2=(-0.5*self.edge-self.gap, self.edge*(-1+0.5*sqrt(3))))
        mdb.models['Model-1'].sketches['__profile__'].rotate(angle=30.0, centerPoint=(-0.5*self.edge, 0.5*sqrt(3)*self.edge), objectList=(
            mdb.models['Model-1'].sketches['__profile__'].geometry[2], 
            mdb.models['Model-1'].sketches['__profile__'].geometry[3], 
            mdb.models['Model-1'].sketches['__profile__'].geometry[4], 
            mdb.models['Model-1'].sketches['__profile__'].geometry[5]))
        mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Cohesive120', 
            type=DEFORMABLE_BODY)
        mdb.models['Model-1'].parts['Cohesive120'].BaseShell(sketch=
            mdb.models['Model-1'].sketches['__profile__'])
        del mdb.models['Model-1'].sketches['__profile__']
    def generateAssembly(self):
        # Criar e posicionar os hexagonos e coesivos
        mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
        l=0
        for j in range(2,4*self.nr,4):
            l=l+1
            k=0
            for i in range(2,2*self.nc,2):
                k=k+1
                # Monta hexagono
                mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                    name='Instance-'+str(j+((k-1)%2)*2)+'-'+str(i), 
                    part=mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)])
                # Monta os tres cohesivos para o hexagono
                # Coesivo 0 graus
                mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                    name='Instance-Cohesive-000-'+str(j+2+((k-1)%2)*2)+'-'+str(i), 
                    part=mdb.models['Model-1'].parts['Cohesive000'])
                # Coesivo 60 graus
                mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                    name='Instance-Cohesive-060-'+str(j+1+((k-1)%2)*2)+'-'+str(i-1), 
                    part=mdb.models['Model-1'].parts['Cohesive060'])
                # Coesivo 120 graus
                mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                    name='Instance-Cohesive-120-'+str(j-1+((k-1)%2)*2)+'-'+str(i-1), 
                    part=mdb.models['Model-1'].parts['Cohesive120'])
                # posiciona as 4 partes (tres coesivos e dois hexagonos)
                if (k!=1  or l!=1):
                    mdb.models['Model-1'].rootAssembly.translate(instanceList=
                        ('Instance-'+str(j+((k-1)%2)*2)+'-'+str(i), 
                        'Instance-Cohesive-000-'+str(j+2+((k-1)%2)*2)+'-'+str(i), 
                        'Instance-Cohesive-060-'+str(j+1+((k-1)%2)*2)+'-'+str(i-1), 
                        'Instance-Cohesive-120-'+str(j-1+((k-1)%2)*2)+'-'+str(i-1)), 
                        vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(k-1), 
                            ((k-1) % 2)*((sqrt(3)/2)*self.edge+0.5*self.gap) + (l-1)*(self.edge)*(sqrt(3)+self.gap) , 0.0))
        # Monta elementos da aresta inferior
        k=-1
        for i in range(4,2*self.nc,4):
            k=k+2
            # Monta hexagono
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(0)+'-'+str(i), 
                part=mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(i)])
            # Coesivo 0 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-000-'+str(2)+'-'+str(i), 
                part=mdb.models['Model-1'].parts['Cohesive000'])
            # Coesivo 60 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-060-'+str(1)+'-'+str(i-1), 
                part=mdb.models['Model-1'].parts['Cohesive060'])
            # Posiciona as partes coesivas e os hex da aresta
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(0)+'-'+str(i),
                'Instance-Cohesive-060-'+str(1)+'-'+str(i-1),
                'Instance-Cohesive-000-'+str(2)+'-'+str(i)), 
                vector=(k*(1.5*self.edge + 0.5*sqrt(3)*self.gap), -(0.5*sqrt(3)*self.edge + 0.5*self.gap), 0.0))
        k=0
        for i in range(2,2*self.nc,4):
            k=k+1
            # Coesivo 0 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-000-'+str(0)+'-'+str(i), 
                part=mdb.models['Model-1'].parts['Cohesive000'])
            # Posiciona as partes coesivas e os hex da aresta
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-Cohesive-000-'+str(0)+'-'+str(i),), 
                vector=((k-1)*(3*self.edge + sqrt(3)*self.gap), -(sqrt(3)*self.edge + self.gap), 0.0))              
        # Monta elementos da aresta superior
        k=-2
        for i in range(2,2*self.nc,4):
            k=k+2
            # Monta hexagono
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(4*self.nr+2)+'-'+str(i), 
                part=mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)])
            # Coesivo 120 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(i-1), 
                part=mdb.models['Model-1'].parts['Cohesive120'])
            # Posiciona as partes coesivas e os hex da aresta
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(4*self.nr+2)+'-'+str(i),
                'Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(i-1)), 
                vector=((k/2)*((3)*self.edge + sqrt(3)*self.gap), self.nr*(sqrt(3)*self.edge + self.gap), 0.0))
        # Monta elementos da aresta da esquerda
        k=-2
        for j in range(4,4*(self.nr+1),4):
            k=k+2
            # Monta hexagono
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(j)+'-'+str(0), 
                part=mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)])
            # Coesivo 0 graus (metade)
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-000-'+str(j+2)+'-'+str(0), 
                part=mdb.models['Model-1'].parts['Cohesive000h'])
            # Posiciona as partes coesivas e os hex da aresta
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-Cohesive-000-'+str(j+2)+'-'+str(0),), 
                vector=(0.5*self.edge, 0.0, 0.0))
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(j)+'-'+str(0),
                'Instance-Cohesive-000-'+str(j+2)+'-'+str(0)), 
                vector=(-(1.5*self.edge + 0.5*sqrt(3)*self.gap), 0.5*(sqrt(3)*self.edge + self.gap) +
                    0.5*k*(sqrt(3)*self.edge + self.gap), 0.0))
        # Monta elementos da aresta da direita
        mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
        l=0
        for j in range(2,4*self.nr,4):
            l=l+1
            # Monta hexagono
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)])
            # Monta os tres cohesivos para o hexagono
            # Coesivo 0 graus (metade)
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-000-'+str(j+2+((self.nc-1)%2)*2)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Cohesive000h'])
            # Coesivo 60 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-060-'+str(j+1+((self.nc-1)%2)*2)+'-'+str(2*self.nc-1), 
                part=mdb.models['Model-1'].parts['Cohesive060'])
            # Coesivo 120 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-120-'+str(j-1+((self.nc-1)%2)*2)+'-'+str(2*self.nc-1), 
                part=mdb.models['Model-1'].parts['Cohesive120'])
            # posiciona as 4 partes (tres coesivos e dois hexagonos)
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc),
                'Instance-Cohesive-000-'+str(j+2+((self.nc-1)%2)*2)+'-'+str(2*self.nc),
                'Instance-Cohesive-060-'+str(j+1+((self.nc-1)%2)*2)+'-'+str(2*self.nc-1),
                'Instance-Cohesive-120-'+str(j-1+((self.nc-1)%2)*2)+'-'+str(2*self.nc-1)), 
                 vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(self.nc-1), 
                    ((self.nc-1) % 2)*((sqrt(3)/2)*self.edge+0.5*self.gap) + (l-1)*(self.edge)*(sqrt(3)+self.gap) , 0.0))
        ## Coloca coesivo no canto inferior direito
        # Coesivo 0 graus (metade)
        if (self.nc % 2) == 1: 
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-000-'+str(0)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Cohesive000h'])
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-Cohesive-000-'+str(0)+'-'+str(2*self.nc),), 
                 vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(self.nc-1),-sqrt(3)*self.edge-self.gap , 0.0))
        # Monta elementos dos vertices
        ## Monta hex do vertice inferior esquerdo
        mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
            name='Instance-'+str(0)+'-'+str(0), 
            part=mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(0)])
        mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
            name='Instance-Cohesive-000-'+str(2)+'-'+str(0), 
            part=mdb.models['Model-1'].parts['Cohesive000h'])
        ### posiciona o elemento coesivo
        mdb.models['Model-1'].rootAssembly.translate(instanceList=
            ('Instance-Cohesive-000-'+str(2)+'-'+str(0),), 
            vector=(-(1.0*self.edge + 0.5*sqrt(3)*self.gap), -0.5*(sqrt(3)*self.edge + self.gap) , 0.0))
        ### posiciona o hex 
        mdb.models['Model-1'].rootAssembly.translate(instanceList=
            ('Instance-'+str(0)+'-'+str(0),), 
            vector=(-(self.edge + 0.5*sqrt(3)*self.gap), -0.5*self.gap, 0.0))
        ## posiciona o hex do vertice superior direito
        if (self.nc % 2) == 1:
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(4*self.nr+2)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)])
            # Coesivo 120 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.nc-1), 
                part=mdb.models['Model-1'].parts['Cohesive120'])
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(4*self.nr+2)+'-'+str(2*self.nc),
                'Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.nc-1)), 
                vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(self.nc-1), self.nr*(sqrt(3)*self.edge + self.gap), 0.0))
        else:
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(0)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(2*self.nc)])
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-000-'+str(2)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Cohesive000h'])
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-060-'+str(1)+'-'+str(2*self.nc-1), 
                part=mdb.models['Model-1'].parts['Cohesive060'])
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(0)+'-'+str(2*self.nc),), 
                 vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(self.nc-1)-0.5*self.edge, -0.5*self.gap, 0.0))
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-Cohesive-000-'+str(2)+'-'+str(2*self.nc),), 
                 vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(self.nc-1), -0.5*(sqrt(3)*self.edge+ self.gap), 0.0))
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-Cohesive-060-'+str(1)+'-'+str(2*self.nc-1),), 
                 vector=(((1.5*(self.edge)+(sqrt(3)/2)*self.gap))*(self.nc-1), -0.5*(sqrt(3)*self.edge+ self.gap), 0.0))
    def generateInteractions(self):
        # Gera as interacoes para o centro do honeycomb
        for j in range(2,4*self.nr,4):
            k=0
            for i in range(2,2*self.nc,2):
                k=k+1
                index = j+((k-1)%2)*2
                mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(i)].edges[4:5])
                    , name='Hex-'+str(index)+'-'+str(i)+'-Coe-'+str(index+2)+'-'+str(i),
                    positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances[
                        'Instance-Cohesive-000-'+str(index+2)+'-'+str(i)].edges[0:1])
                    , thickness=ON, tieRotations=ON)
                mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(i)].edges[1:2])
                    , name='Hex-'+str(index)+'-'+str(i)+'-Coe-'+str(index+1)+'-'+str(i-1), 
                    positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances[
                        'Instance-Cohesive-060-'+str(index+1)+'-'+str(i-1)].edges[1:2])
                    , thickness=ON, tieRotations=ON)
                mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(i)].edges[5:6])
                    , name='Hex-'+str(index)+'-'+str(i)+'-Coe-'+str(index-1)+'-'+str(i-1), 
                    positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances[
                        'Instance-Cohesive-120-'+str(index-1)+'-'+str(i-1)].edges[3:4])
                    , thickness=ON, tieRotations=ON)
                mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(i)].edges[10:11])
                    , name='Hex-'+str(index)+'-'+str(i)+'-Coe-'+str(index-2)+'-'+str(i),
                    positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances[
                        'Instance-Cohesive-000-'+str(index-2)+'-'+str(i)].edges[2:3])
                    , thickness=ON, tieRotations=ON)
                mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(i)].edges[11:12])
                    , name='Hex-'+str(index)+'-'+str(i)+'-Coe-'+str(index-1)+'-'+str(i+1), 
                    positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances[
                        'Instance-Cohesive-060-'+str(index-1)+'-'+str(i+1)].edges[3:4])
                    , thickness=ON, tieRotations=ON)
                mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(i)].edges[8:9])
                    , name='Hex-'+str(j)+'-'+str(i)+'-Coe-'+str(j+1)+'-'+str(i+1), 
                    positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances[
                        'Instance-Cohesive-120-'+str(index+1)+'-'+str(i+1)].edges[1:2])
                    , thickness=ON, tieRotations=ON)
        # Interacoes da aresta inferior
        for i in range(4,2*self.nc,4):
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-0-'+str(i)].edges[5:6])
                , name='Hex-'+str(0)+'-'+str(i)+'-Coe-1'+'-'+str(i-1),
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-1-'+str(i-1)].edges[1:2])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-0-'+str(i)].edges[4:5])
                , name='Hex-'+str(0)+'-'+str(i)+'-Coe-2'+'-'+str(i), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-'+str(i)].edges[0:1])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-0-'+str(i)].edges[2:3])
                , name='Hex-'+str(0)+'-'+str(i)+'-Coe-1'+'-'+str(i+1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-1-'+str(i+1)].edges[1:2])
                , thickness=ON, tieRotations=ON)
        # Interacoes da aresta superior
        for i in range(2,2*self.nc,4):
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(4*self.nr+2)+'-'+str(i)].edges[1:2])
                , name='Hex-'+str(4*self.nr+2)+'-'+str(i)+'-Coe-'+str(4*self.nr+1)+'-'+str(i+1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-'+str(4*self.nr+1)+'-'+str(i+1)].edges[3:4])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(4*self.nr+2)+'-'+str(i)].edges[6:7])
                , name='Hex-'+str(4*self.nr+2)+'-'+str(i)+'-Coe-'+str(4*self.nr)+'-'+str(i), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(4*self.nr)+'-'+str(i)].edges[2:3])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(4*self.nr+2)+'-'+str(i)].edges[5:6])
                , name='Hex-'+str(4*self.nr+1)+'-'+str(i-1)+'-Coe-'+str(4*self.nr+1)+'-'+str(i-1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(i-1)].edges[3:4])
                , thickness=ON, tieRotations=ON)
        # Interacoes do lado direito
        for j in range(2,4*(self.nr),4):
            index=j+((self.nc+1)%2)*2
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(2*self.nc)].edges[4:5])
                , name='Hex-'+str(index)+'-'+str(2*self.nc)+'-Coe-'+str(index-2)+'-'+str(2*self.nc),
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(index-2)+'-'+str(2*self.nc)].edges[2:3])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(2*self.nc)].edges[8:9])
                , name='Hex-'+str(index)+'-'+str(2*self.nc)+'-Coe-'+str(index-1)+'-'+str(2*self.nc-1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-'+str(index-1)+'-'+str(2*self.nc-1)].edges[3:4])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(2*self.nc)].edges[7:8])
                , name='Hex-'+str(index)+'-'+str(2*self.nc)+'-Coe-'+str(index+1)+'-'+str(2*self.nc-1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-'+str(index+1)+'-'+str(2*self.nc-1)].edges[1:2])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(index)+'-'+str(2*self.nc)].edges[2:3])
                , name='Hex-'+str(index)+'-'+str(2*self.nc)+'-Coe-'+str(index+2)+'-'+str(2*self.nc), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(index+2)+'-'+str(2*self.nc)].edges[0:1])
                , thickness=ON, tieRotations=ON)
        # Interacoes do lado esquerdo
        for j in range(4,4*(self.nr+1),4):
           mdb.models['Model-1'].Tie(adjust=ON, master=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(j)+'-0'].edges[4:5])
               , name='Hex-'+str(j)+'-'+str(0)+'-Coe-'+str(j+2)+'-0',
               positionToleranceMethod=COMPUTED, slave=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(j+2)+'-0'].edges[0:1])
               , thickness=ON, tieRotations=ON)
           mdb.models['Model-1'].Tie(adjust=ON, master=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(j)+'-0'].edges[8:9])
               , name='Hex-'+str(j)+'-'+str(0)+'-Coe-'+str(j+1)+'-1',
               positionToleranceMethod=COMPUTED, slave=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-'+str(j+1)+'-1'].edges[1:2])
               , thickness=ON, tieRotations=ON)
           mdb.models['Model-1'].Tie(adjust=ON, master=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(j)+'-0'].edges[7:8])
               , name='Hex-'+str(j)+'-'+str(0)+'-Coe-'+str(j-1)+'-1',
               positionToleranceMethod=COMPUTED, slave=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-'+str(j-1)+'-1'].edges[3:4])
               , thickness=ON, tieRotations=ON)
           mdb.models['Model-1'].Tie(adjust=ON, master=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(j)+'-0'].edges[2:3])
               , name='Hex-'+str(j)+'-'+str(0)+'-Coe-'+str(j-2)+'-0',
               positionToleranceMethod=COMPUTED, slave=Region(
               side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(j-2)+'-0'].edges[2:3])
               , thickness=ON, tieRotations=ON)
        # Interacoes do canto inferior esquerdo
        mdb.models['Model-1'].Tie(adjust=ON, master=Region(
           side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-0-0'].edges[3:4])
           , name='Hex-0-0-Coe-2-0', positionToleranceMethod=COMPUTED, slave=Region(
           side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-0'].edges[0:1])
           , thickness=ON, tieRotations=ON)
        mdb.models['Model-1'].Tie(adjust=ON, master=Region(
           side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-0-0'].edges[2:3])
           , name='Hex-0-0-coe-1-1', positionToleranceMethod=COMPUTED, slave=Region(
           side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-1-1'].edges[1:2])
           , thickness=ON, tieRotations=ON)
        # Interacoes dos cantos direitos
        if (self.nc % 2) == 1:
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(4*self.nr+2)+'-'+str(2*self.nc)].edges[1:2])
                , name='Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)+'-Coe-'+str(4*self.nr)+'-'+str(2*self.nc), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(4*self.nr)+'-'+str(2*self.nc)].edges[2:3])
                            , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(4*self.nr+2)+'-'+str(2*self.nc)].edges[4:5])
                , name='Hex-'+str(4*self.nr+2)+'-'+str(2*self.nc)+'-Coe-'+str(4*self.nr+1)+'-'+str(2*self.nc-1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.nc-1)].edges[3:4])
                , thickness=ON, tieRotations=ON)
        else:
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(0)+'-'+str(2*self.nc)].edges[2:3]) #Acertar arestas
                , name='Hex-'+str(0)+'-'+str(2*self.nc)+'-Coe-'+str(1)+'-'+str(2*self.nc-1), 
                positionToleranceMethod=COMPUTED, slave=Region(
                    side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-'+str(2)+'-'+str(2*self.nc)].edges[1:2])
                , thickness=ON, tieRotations=ON)
            mdb.models['Model-1'].Tie(adjust=ON, master=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-'+str(0)+'-'+str(2*self.nc)].edges[3:4])
                , name='Hex-'+str(0)+'-'+str(2*self.nc-1)+'-Coe-'+str(2)+'-'+str(2*self.nc), 
                positionToleranceMethod=COMPUTED, slave=Region(
                side1Edges=mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-'+str(1)+'-'+str(2*self.nc-1)].edges[0:1])
                , thickness=ON, tieRotations=ON)

    def setHexsProperty(self):
        pass
    def setCohesveProperty(self):
        pass
    def generateMesh(self,seed=0.1):
        # Gera malha para hex do centro
        for j in range(2,4*self.nr,4):
            k=0
            for i in range(2,2*self.nc,2):
                k = k+1
                mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
                mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].setMeshControls(regions=
                    mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].faces[:], technique=STRUCTURED)
                mdb.models['Model-1'].parts['Hex-'+str(j+((k-1)%2)*2)+'-'+str(i)].generateMesh()
        # aresta inferior
        for i in range(4,2*self.nc,4):
            mdb.models['Model-1'].parts['Hex-0-'+str(i)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
            mdb.models['Model-1'].parts['Hex-0-'+str(i)].setMeshControls(regions=
                mdb.models['Model-1'].parts['Hex-0-'+str(i)].faces[:], technique=STRUCTURED)
            mdb.models['Model-1'].parts['Hex-0-'+str(i)].generateMesh()
        # aresta superior
        for i in range(2,2*self.nc,4):
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].setMeshControls(regions=
                mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].faces[:], technique=STRUCTURED)
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+str(i)].generateMesh()
        # lado esquerdo
        for j in range(4,4*(self.nr+1),4):
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].setMeshControls(regions=
                mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].faces[:], technique=STRUCTURED)
            mdb.models['Model-1'].parts['Hex-'+str(j)+'-'+str(0)].generateMesh()
        # lado direito
        for j in range(2,4*(self.nr),4): 
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].setMeshControls(regions=
                mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].faces[:], technique=STRUCTURED)
            mdb.models['Model-1'].parts['Hex-'+str(j+((self.nc-1)%2)*2)+'-'+str(2*self.nc)].generateMesh()
        # Canto inferior esquerdo
        mdb.models['Model-1'].parts['Hex-0-0'].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
        mdb.models['Model-1'].parts['Hex-0-0'].setMeshControls(regions=
            mdb.models['Model-1'].parts['Hex-0-0'].faces[:], technique=STRUCTURED)
        mdb.models['Model-1'].parts['Hex-0-0'].generateMesh()
        # Canto direito
        if (self.nc % 2) == 1:
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+ str(2*self.nc)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+ str(2*self.nc)].setMeshControls(regions=
                mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+ str(2*self.nc)].faces[:], technique=STRUCTURED)
            mdb.models['Model-1'].parts['Hex-'+str(4*self.nr+2)+'-'+ str(2*self.nc)].generateMesh()
        else:
            mdb.models['Model-1'].parts['Hex-0-'+ str(2*self.nc)].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
            mdb.models['Model-1'].parts['Hex-0-'+ str(2*self.nc)].setMeshControls(regions=
                mdb.models['Model-1'].parts['Hex-0-'+ str(2*self.nc)].faces[:], technique=STRUCTURED)
            mdb.models['Model-1'].parts['Hex-0-'+ str(2*self.nc)].generateMesh()
        # Malha nos coesivos
        # Coesivo 0
        mdb.models['Model-1'].parts['Cohesive000'].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
        mdb.models['Model-1'].parts['Cohesive000'].setMeshControls(regions=
            mdb.models['Model-1'].parts['Cohesive000'].faces[:], technique=STRUCTURED)
        mdb.models['Model-1'].parts['Cohesive000'].generateMesh()
        # Coesivo 0 metade
        mdb.models['Model-1'].parts['Cohesive000h'].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
        mdb.models['Model-1'].parts['Cohesive000h'].setMeshControls(regions=
            mdb.models['Model-1'].parts['Cohesive000h'].faces[:], technique=STRUCTURED)
        mdb.models['Model-1'].parts['Cohesive000h'].generateMesh()
        # Coesivo 60
        mdb.models['Model-1'].parts['Cohesive060'].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
        mdb.models['Model-1'].parts['Cohesive060'].setMeshControls(regions=
            mdb.models['Model-1'].parts['Cohesive060'].faces[:], technique=STRUCTURED)
        mdb.models['Model-1'].parts['Cohesive060'].generateMesh()
        # Coesivo 120
        mdb.models['Model-1'].parts['Cohesive120'].seedPart(deviationFactor=0.1,  minSizeFactor=0.1, size=seed)
        mdb.models['Model-1'].parts['Cohesive120'].setMeshControls(regions=
            mdb.models['Model-1'].parts['Cohesive120'].faces[:], technique=STRUCTURED)
        mdb.models['Model-1'].parts['Cohesive120'].generateMesh()

