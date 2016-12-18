# Funcao: Automatiza a criacao de um honeycomb com gaps preenchidos por elementos coesivos
# Autores: Caiua e Bruno
# Data de criacao: 2/12/2016
# Data de modificacao: 12/12/2016
 
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
        l=0
        for j in range(2,4*self.nr,4):
            l=l+1
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
        # Gera as partes hexagonais do honeycomb do lado direito
        for j in range(2,4*(self.nr+1),4):
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
            mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Hex-'+str(2*self.nr)+'-'+str(2*self.nc), type=
                DEFORMABLE_BODY)
            mdb.models['Model-1'].parts['Hex-'+str(2*self.nr)+'-'+str(2*self.nc)].BaseShell(sketch=
                mdb.models['Model-1'].sketches['__profile__'])
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
        for i in range(3,2*self.nc+1,4):
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
        # Monta elementos dos vertices
        ## Monta hex do vertice inferior esquerdo
        mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
            name='Instance-'+str(0)+'-'+str(0), 
            part=mdb.models['Model-1'].parts['Hex-'+str(0)+'-'+str(0)])
        mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
            name='Instance-Cohesive-000-'+str(0)+'-'+str(1), 
            part=mdb.models['Model-1'].parts['Cohesive000h'])
        ### posiciona o elemento coesivo
        mdb.models['Model-1'].rootAssembly.translate(instanceList=
            ('Instance-Cohesive-000-'+str(0)+'-'+str(1),), 
            vector=(-(1.0*self.edge + 0.5*sqrt(3)*self.gap), -0.5*(sqrt(3)*self.edge + self.gap) , 0.0))
        ### posiciona o hex 
        mdb.models['Model-1'].rootAssembly.translate(instanceList=
            ('Instance-'+str(0)+'-'+str(0),), 
            vector=(-(self.edge + 0.5*sqrt(3)*self.gap), -0.5*self.gap, 0.0))
        ## posiciona o hex do vertice superior direito
        if (self.nc % 2) == 1:
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-'+str(2*self.nr)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Hex-'+str(2*self.nr)+'-'+str(2*self.nc)])
            # Coesivo 120 graus
            mdb.models['Model-1'].rootAssembly.Instance(dependent=ON,
                name='Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.nc), 
                part=mdb.models['Model-1'].parts['Cohesive120'])
            mdb.models['Model-1'].rootAssembly.translate(instanceList=
                ('Instance-'+str(2*self.nr)+'-'+str(2*self.nc),'Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.nc)), 
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






