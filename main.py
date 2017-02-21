# -*- coding: mbcs -*-
from part import *
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
import time 

start = time.time()

H = Honeycomb()
H.setEdgeSize(25e-3)
H.setGapSize(0.5e-3)
H.setNumberColumns(7)
H.setNumberRows(7)
H.generateHexs()
H.generateCohesives()
H.generateAssembly()
H.generateInteractions()
H.generateMesh(25e-4)
H.setCohesiveProperty()
H.setHexsProperty()

# Colocar as condicoes de restricao nodal
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Sym-y', 
    region=Region(
    edges=mdb.models['Model-1'].rootAssembly.instances['Instance-4-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-4-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-6-0'].edges[3:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-8-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-8-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-10-0'].edges[3:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-12-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-12-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-14-0'].edges[3:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-16-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-16-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-18-0'].edges[3:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-20-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-20-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-22-0'].edges[3:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-24-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-24-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-26-0'].edges[3:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-0'].edges[5:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-0'].edges[4:5]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-0'].edges[3:4], 
)
    , u1=SET, u2=UNSET, ur3=UNSET)
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-Sym-x', 
    region=Region(
    edges=mdb.models['Model-1'].rootAssembly.instances['Instance-0-0'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-2'].edges[10:11]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-4'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-4'].edges[6:7]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-6'].edges[10:11]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-8'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-8'].edges[6:7]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-10'].edges[10:11]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-12'].edges[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-12'].edges[6:7]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-14'].edges[4:5]), 
    u1=UNSET, u2=SET, ur3=UNSET)

# Colocar as condicoes de periodicidade

mdb.models['Model-1'].rootAssembly.Set(name='Ref-x', nodes=
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-0'].nodes[4:5])
mdb.models['Model-1'].rootAssembly.Set(name='Slave-x', nodes=
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-2'].nodes[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-2'].nodes[5:14]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-2'].nodes[50:59]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-0'].nodes[44:48]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-4'].nodes[34:43]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-6'].nodes[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-6'].nodes[5:14]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-6'].nodes[50:59]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-8'].nodes[34:43]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-10'].nodes[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-10'].nodes[5:14]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-10'].nodes[50:59]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-12'].nodes[34:43]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-14'].nodes[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-14'].nodes[34:43])
mdb.models['Model-1'].Equation(name='Constraint-323', terms=((1.0, 'Slave-x', 
    2), (-1.0, 'Ref-x', 2)))
mdb.models['Model-1'].rootAssembly.Set(name='Ref-y', nodes=
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-14'].nodes[4:5])
mdb.models['Model-1'].rootAssembly.Set(name='Slave-y', nodes=
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-6-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-6-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-10-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-10-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-14-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-14-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-18-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-18-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-22-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-22-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-26-14'].nodes[1:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-26-14'].nodes[19:35]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-14'].nodes[4:12])
mdb.models['Model-1'].Equation(name='Constraint-324', terms=((1.0, 'Slave-x', 
    1), (-1.0, 'Ref-x', 1)))
mdb.models['Model-1'].constraints['Constraint-324'].setValues(terms=((1.0, 
    'Slave-y', 1), (-1.0, 'Ref-y', 1)))

# Criar step
## Energy fraction
## Stabilization

mdb.models['Model-1'].StaticStep(adaptiveDampingRatio=0.05, 
    continueDampingFactors=False, extrapolation=NONE, initialInc=0.01, maxInc=
    0.01, maxNumInc=10000, minInc=1e-15, name='Step-1', nlgeom=ON, previous=
    'Initial', stabilizationMagnitude=0.0002, stabilizationMethod=
    DISSIPATED_ENERGY_FRACTION)
# Criar carregamento termico
## Criar amplitude 
mdb.models['Model-1'].PeriodicAmplitude(a_0=1.0, data=((0.0, -1.0), ), 
    frequency=3.14159, name='Amp-1', start=0.0, timeSpan=STEP)
mdb.models['Model-1'].Temperature(createStepName='Initial', 
    crossSectionDistribution=CONSTANT_THROUGH_THICKNESS, distributionType=
    UNIFORM, magnitudes=(1500.0, ), name='Predefined Field-1', region=Region(
    faces=mdb.models['Model-1'].rootAssembly.instances['Instance-2-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-4-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-3-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-1-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-4-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-6-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-5-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-3-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-4-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-3-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-1-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-4-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-6-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-5-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-3-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-4-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-3-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-1-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-4-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-6-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-5-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-3-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-6-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-8-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-7-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-5-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-8-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-10-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-9-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-7-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-6-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-8-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-7-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-5-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-8-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-10-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-9-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-7-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-6-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-8-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-7-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-5-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-8-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-10-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-9-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-7-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-10-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-12-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-11-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-9-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-12-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-14-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-13-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-11-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-10-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-12-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-11-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-9-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-12-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-14-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-13-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-11-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-10-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-12-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-11-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-9-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-12-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-14-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-13-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-11-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-14-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-16-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-15-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-13-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-16-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-18-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-17-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-15-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-14-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-16-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-15-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-13-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-16-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-18-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-17-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-15-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-14-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-16-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-15-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-13-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-16-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-18-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-17-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-15-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-18-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-20-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-19-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-17-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-20-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-22-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-21-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-19-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-18-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-20-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-19-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-17-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-20-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-22-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-21-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-19-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-18-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-20-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-19-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-17-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-20-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-22-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-21-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-19-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-22-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-24-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-23-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-21-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-24-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-26-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-25-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-23-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-22-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-24-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-23-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-21-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-24-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-26-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-25-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-23-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-22-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-24-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-23-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-21-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-24-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-26-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-25-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-23-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-26-2'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-28-2'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-27-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-25-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-4'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-29-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-27-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-26-6'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-28-6'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-27-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-25-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-8'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-29-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-27-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-26-10'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-28-10'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-27-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-25-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-12'].faces[0:6]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-29-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-27-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-4'].faces[0:3]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-4'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-1-3'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-8'].faces[0:3]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-8'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-1-7'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-12'].faces[0:3]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-12'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-1-11'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-2'].faces[0:3]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-29-1'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-6'].faces[0:3]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-29-5'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-10'].faces[0:3]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-29-9'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-4-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-6-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-8-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-10-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-12-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-14-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-16-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-18-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-20-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-22-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-24-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-26-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-28-0'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-2-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-4-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-3-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-1-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-6-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-8-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-7-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-5-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-10-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-12-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-11-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-9-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-14-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-16-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-15-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-13-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-18-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-20-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-19-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-17-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-22-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-24-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-23-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-21-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-26-14'].faces[0:4]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-28-14'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-060-27-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-25-13'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-0-0'].faces[0:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-000-2-0'].faces[0:1]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-30-14'].faces[0:2]+\
    mdb.models['Model-1'].rootAssembly.instances['Instance-Cohesive-120-29-13'].faces[0:1]))
mdb.models['Model-1'].predefinedFields['Predefined Field-1'].setValuesInStep(
    amplitude='Amp-1', stepName='Step-1')
print("--- %s seconds ---" % (time.time() - start))

