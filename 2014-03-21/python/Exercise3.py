from pyplasm import *
from scipy import *

def base3D(base, x,y,z):
	verts=[[x,y],[x+base,y],[x+base,y+base],[x,y+base]]
	cells=[[1,2,3,4]]
	pols=None
	base2D=MKPOL([verts,cells,pols])
	base3D=PROD([base2D,Q(z)])
	return base3D

def templetop3D(base,height,x,y,z):
	verts=[[x,y],[x+base,y],[x+base,y+height],[x,y+height]]
	cells=[[1,2,3,4]]
	pols=None
	base2D=MKPOL([verts,cells,pols])
	base3D=PROD([base2D,Q(z)])
	return base3D



floor0=base3D(60,0,0,2)
floor1=base3D(56,2,2,4)
floor2=base3D(52,4,4,6)
floor3=base3D(48,6,6,8)
floor4=base3D(44,8,8,10)
floor5=base3D(40,10,10,12)
floor6=base3D(36,12,12,14)
floor7=base3D(32,14,14,16)
floor8=base3D(28,16,16,18)

floor9=templetop3D(20,18,20,21,26)

door=templetop3D(3,2,28.5,21,20)


building=STRUCT([floor0,floor1,floor2,floor3,floor4,floor5,floor6,floor7,floor8,floor9, COLOR([0.5,0.2,0])(door)])

VIEW(building)

