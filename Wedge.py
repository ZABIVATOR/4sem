import warnings
import sys
warnings.filterwarnings("ignore")
import gmsh
gmsh.initialize()
gmsh.model.add("DFG 3D")

cylinder = gmsh.model.occ.addWedge(0, 0, 0 ,1, 2, 3)	
gmsh.model.occ.addVolume([cylinder])
gmsh.model.occ.synchronize()
gmsh.model.mesh.generate()
if '-nopopup' not in sys.argv:
	gmsh.fltk.run()
gmsh.finalize()
