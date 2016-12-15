# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 6.14-1 replay file
# Internal Version: 2014_06_04-16.37.49 134264
# Run by caiua on Thu Dec 15 16:02:56 2016
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=178.858322143555, 
    height=175.042602539062)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].view.setValues(nearPlane=28.8818, 
    farPlane=34.6215, width=12.5451, height=12.2919, viewOffsetX=-0.404944, 
    viewOffsetY=-0.180455)
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.9106, 
    farPlane=32.5926, width=3.539, height=3.46759, viewOffsetX=3.68937, 
    viewOffsetY=-4.15972)
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.8044, 
    farPlane=32.6988, width=4.14551, height=4.09542, viewOffsetX=3.46502, 
    viewOffsetY=-3.91813)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.7863, 
    farPlane=32.717, width=4.14306, height=4.09301, viewOffsetX=4.09986, 
    viewOffsetY=0.103385)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.7863, 
    viewOffsetX=4.09315, viewOffsetY=3.12281)
session.viewports['Viewport: 1'].view.setValues(farPlane=32.717, 
    viewOffsetX=3.96577, viewOffsetY=3.37778)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.1507, 
    farPlane=33.3526, width=7.00386, height=6.91925, viewOffsetX=3.03527, 
    viewOffsetY=4.28883)
session.viewports['Viewport: 1'].view.setValues(nearPlane=30.1213, 
    farPlane=33.3819, width=6.99705, height=6.91251, viewOffsetX=3.11157, 
    viewOffsetY=2.85683)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.8138, 
    farPlane=33.6895, width=8.47612, height=8.37372, viewOffsetX=2.6086, 
    viewOffsetY=3.30572)
session.viewports['Viewport: 1'].view.setValues(nearPlane=29.7791, 
    farPlane=33.7242, width=8.46626, height=8.36398, viewOffsetX=3.24944, 
    viewOffsetY=-0.962388)
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.5533, 
    farPlane=35.9499, width=20.7702, height=20.5193, viewOffsetX=-0.217146, 
    viewOffsetY=-3.19513)
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
session.viewports['Viewport: 1'].view.setValues(nearPlane=27.8451, 
    farPlane=35.6582, width=16.4713, height=16.2723, viewOffsetX=2.23474, 
    viewOffsetY=2.07134)
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
#* AttributeError: Honeycomb instance has no attribute 'rc'
#* File "teste.py", line 8, in <module>
#*     H.generateAssembly()
#* File "Honeycomb.py", line 385, in generateAssembly
#*     name='Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.rc),
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
#* AttributeError: Honeycomb instance has no attribute 'rc'
#* File "teste.py", line 8, in <module>
#*     H.generateAssembly()
#* File "Honeycomb.py", line 385, in generateAssembly
#*     name='Instance-Cohesive-120-'+str(4*self.nr+1)+'-'+str(2*self.rc),
cliCommand("""execfile('Honeycomb.py')""")
cliCommand("""execfile('teste.py')""")
