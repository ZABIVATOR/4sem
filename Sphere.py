import warnings
import sys
warnings.filterwarnings("ignore")
import gmsh
gmsh.initialize()
gmsh.model.add("DFG 3D")

cylinder = gmsh.model.occ.addSphere (0, 0,0,1)

gmsh.model.occ.synchronize()
gmsh.model.mesh.generate(2)
if '-nopopup' not in sys.argv:
	gmsh.fltk.run()
gmsh.finalize()






