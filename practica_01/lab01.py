from helpers import *

#----------------MAPPERS---------------------->
# molino
techo = cone(6,20,80)
body = cone(6, 16, 80)
aspa = cube(1.5,17,.1)
estaca = cube(.5,.5,5.7)

# pato
body_duck       = cube(.7,.8,1.2)
ala_duck        = cube(.15,.5, .7)
cuello_duck     = cube(.5,.7, .5)
eye_duck        = cube(.12, .12, .05)
pico_duck       = cube(.4, .1, .4)
cresta_duck     = cube(.2, .2, .2)
pata1_duck      = cube(.15, .5, .15)
pata2_duck      = cube(.3, .1, .3)


# cerdo
body_pig  =  cube(2, 2, 4.5)
leg_pig   =  cube(.5, 1.2, .5)
nose_pig  =  cube(.5,0.75,.75)
eye_pig   =  cube(.35,.35,.35)
casco_pig  = cube(.52, .3, .52)
tail_pig   = cube(.2, .2 , 1.5)
head_pig = cube(2, 2 , 2)
nose_pig  = cube(1 , .75 ,1)

#oveja
body_sheep     = cube(1.5, 1.5, 4)
legs_sheep     = cube(.5, 1.2, .5)
cascos_sheep   = cube(.52, .3, .52)
head_sheep     = cube(1.5, 1.5 , 1.5)
eye_sheep      = cube(.2, .25, .05)
oreja_sheep    = cube(.2 , .5 ,.2)
nose_sheep  =    cube(.6 , .45 ,.6)

body_hourse     = cube(1.5, 1.5, 4)
legs_hourse     = cube(.5, 1.2, .5)
cascos_hourse   = cube(.52, .3, .52)
cuello_hourse   = cube(.85, 2, .85)
head_hourse     = cube(1, .8 , 1.5)
eye_hourse      = cube(.2, .20, .04)
oreja_hourse    = cube(.2 , .4 ,.15)
cola_hourse     = cube(.2, .2 , 1.5)
melena_hourse   = cube(.2, 1.9 , .5)

#perro
body_dog     = cube(1.0, 1.0, 2.5)
legs_dog     = cube(.3, 0.8, .3)
patas_dog   = cube(.36, .24, .36)
cuello_dog   = cube(.55, 1.0, .55)
head_dog     = cube(0.6, .6 , 1.2)
eye_dog      = cube(.2, .25, .05)
oreja_dog    = cube(.1 , 0.7 ,0.45)
cola_dog     = cube(.2, .2 , 1.5)

grass = cube(80,.1,80)

house = cube(10,10,10)
door = cube(4,7,0.8)
window = cube(0.4,3,6)
pommel = sphere(0.3,10,10)
roof = cone(8,8,30)

trunk1 = cylinder(1.8, 8, 30)
tree_cone11 = cone(4.6, 8, 30)
tree_cone21 = cone(4.2, 7, 30)
tree_cone31 = cone(3.8, 6, 30)
tree_cone41 = cone(3.4, 5, 30)
trunk2 = cylinder(1.2, 6, 30)
tree_cone12 = cone(3.6, 6, 20)
tree_cone22 = cone(3.2, 5, 20)
tree_cone32 = cone(2.8, 4, 20)
tree_cone42 = cone(2.4, 3, 20)

grass3d = triangle([[0, 0, 0.6], [0, 0, 0], [0, 0.6, 0.3]])

bush = sphere(2.8,20,7)
bush2 = sphere(1.8,20,6)

#-----granero-----------

x0 = [(0.0, 0.0, 0.4), (2.0, 0.0, 0.4), (2.0, 1.0, 0.4), (0.0, 1.0, 0.4),
	 (0.0, 0.0, 2.6), (2.0, 0.0, 2.6), (2.0, 1.0, 2.6), (0.0, 1.0, 2.6)]

x1 = [(0.0, 1.0, 1.5), (2.0, 1.0, 1.5), (2.0, 1.0, 0.0), (0.0, 1.0, 0.0),
     (0.0, 1.0, 3.0), (2.0, 1.0, 3.0), (2.0, 2.0, 1.5), (0.0, 2.0, 1.5)]

x2 = [(0.7, 1.0, 3.0), (1.0, 1.0, 3.0), (1.3, 1.0, 3.0), (1.0, 1.5, 3.0),
     (0.7, 1.0, 0.0), (1.0, 1.0, 0.0), (1.3, 1.0, 0.0), (1.0, 1.5, 0.0)]

x3 = [(0.2, 0.0, 0.0), (0.4, 0.0, 0.0), (0.4, 1.0, 0.0), (0.2, 1.0, 0.0),
     (0.2, 0.0, 0.2), (0.4, 0.0, 0.2), (0.4, 1.0, 0.2), (0.2, 1.0, 0.2)]

x4 = [(1.6, 0.0, 0.0), (1.8, 0.0, 0.0), (1.8, 1.0, 0.0), (1.6, 1.0, 0.0),
     (1.6, 0.0, 0.2), (1.8, 0.0, 0.2), (1.8, 1.0, 0.2), (1.6, 1.0, 0.2)]

x5 = [(0.2, 0.0, 2.8), (0.4, 0.0, 2.8), (0.4, 1.0, 2.8), (0.2, 1.0, 2.8),
     (0.2, 0.0, 3.0), (0.4, 0.0, 3.0), (0.4, 1.0, 3.0), (0.2, 1.0, 3.0)]

x6 = [(1.6, 0.0, 2.8), (1.8, 0.0, 2.8), (1.8, 1.0, 2.8), (1.6, 1.0, 2.8),
     (1.6, 0.0, 3.0), (1.8, 0.0, 3.0), (1.8, 1.0, 3.0), (1.6, 1.0, 3.0)]

tamanio=9

x0=size(tamanio,x0)
x1=size(tamanio,x1)
x2=size(tamanio,x2)
x3=size(tamanio,x3)
x4=size(tamanio,x4)
x5=size(tamanio,x5)
x6=size(tamanio,x6)

cube1 = createCube(x0,pts)
cube2 = createCube(x1,pts)
cube3 = createCube(x2,pts)
cube4 = createCube(x3,pts)
cube5 = createCube(x4,pts)
cube6 = createCube(x5,pts)
cube7 = createCube(x6,pts)

puerta = cube(10, 5, 5)

#--------CERCAS---------

c1 = [(5.0, 0.0, 0.0), (5.1, 0.0, 0.0), (5.1, 0.5, 0.0), (5.0, 0.5, 0.0),
     (5.0, 0.0, 0.1), (5.1, 0.0, 0.1), (5.1, 0.5, 0.1), (5.0, 0.5, 0.1)]

c2 = [(5.0, 0.0, 1.0), (5.1, 0.0, 1.0), (5.1, 0.5, 1.0), (5.0, 0.5, 1.0),
     (5.0, 0.0, 1.1), (5.1, 0.0, 1.1), (5.1, 0.5, 1.1), (5.0, 0.5, 1.1)]

c3 = [(5.0, 0.15, 0.0), (5.1, 0.15, 0.0), (5.1, 0.25, 0.0), (5.0, 0.25, 0.0),
     (5.0, 0.15, 1.0), (5.1, 0.15, 1.0), (5.1, 0.25, 1.0), (5.0, 0.25, 1.0)]

c4 = [(5.0, 0.35, 0.0), (5.1, 0.35, 0.0), (5.1, 0.45, 0.0), (5.0, 0.45, 0.0),
     (5.0, 0.35, 1.0), (5.1, 0.35, 1.0), (5.1, 0.45, 1.0), (5.0, 0.45, 1.0)]


tamcerca=8
c1=size(tamcerca,c1)
c2=size(tamcerca,c2)
c3=size(tamcerca,c3)
c4=size(tamcerca,c4)

cube8 = createCube(c1,pts)
cube9 = createCube(c2,pts)
cube10 = createCube(c3,pts)
cube11 = createCube(c4,pts)



cubos = [cube8,cube9,cube10,cube11]


vallas=crearVallas(cubos,[255, 225, 53],[0,90,None],[36,0,78],9,8,0)
vallas1=crearVallas(cubos,[255, 225, 53],[0,180,None],[4,0,45],10,0,7.5)
vallas2=crearVallas(cubos,[255, 225, 53],[0,180,None],[77,0,45],10,0,7.5)
vallas3=crearVallas(cubos,[255, 225, 53],[0,90,None],[36,0,2],9,8,0)

vallas4=crearVallas(cubos,[255, 225, 53],[0,90,None],[-5,0,30],3,7,0)
vallas5=crearVallas(cubos,[255, 225, 53],[0,90,None],[-5,0,50],3,7,0)

vallas6=crearVallas(cubos,[255, 225, 53],[0,180,None],[15,0,15],3,0,5.5)
vallas7=crearVallas(cubos,[255, 225, 53],[0,180,None],[37,0,15],3,0,5.5)

vallas8=crearVallas(cubos,[255, 225, 53],[0,90,None],[25,0,30],3,7,0)
vallas9=crearVallas(cubos,[255, 225, 53],[0,90,None],[25,0,50],3,7,0)

vallas10=crearVallas(cubos,[255, 225, 53],[0,180,None],[45,0,15],3,0,5.5)
vallas11=crearVallas(cubos,[255, 225, 53],[0,180,None],[67,0,15],3,0,5.5)




#--------------ACTORS(mapper/[position]/[angle]/[color]/texture_name)------------------------>
act_techo  = actor(techo, [20,14,20], [None,None,90], [219, 172, 121], None)
act_body   = actor(body, [20,8,20], [None,None,90], [209, 204, 190], None)
act_aspa1   = actor(aspa, [20,16,26], [None,None,None], [163, 130, 93],None)
act_aspa2   = actor(aspa, [20,16,26], [None,None,90], [163, 130, 93],None)
act_estaca   = actor(estaca, [20,16,23], [None,None,90], [163, 130, 93],None)

pos_x=-20
act_body_duck       = actor(body_duck, [pos_x+ 0,1,0], [None,None,None], [212, 202, 184], None)
act_ala_der_duck    = actor(ala_duck, [pos_x+ -0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_ala_izq_duck    = actor(ala_duck, [pos_x+ 0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_cuello_duck     = actor(cuello_duck, [pos_x+ 0,1.6,.7], [None,None,None], [224, 221, 215], None)
act_eye1_duck       = actor(eye_duck, [pos_x+ -0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_eye2_duck       = actor(eye_duck, [pos_x+ 0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_pico1_duck      = actor(pico_duck, [pos_x+ 0, 1.62, 1], [None,None,None], [207, 189, 87], None)
act_pico2_duck      = actor(pico_duck, [pos_x+ 0, 1.52, 1], [None,None,None], [181, 166, 78], None)
act_cresta_duck     = actor(cresta_duck, [pos_x+ 0, 1.4, 1], [None,None,None], [191, 57, 57], None)
act_pata1_duck      = actor(pata1_duck, [pos_x+ -0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata2_duck      = actor(pata2_duck, [pos_x+ -0.2, .1, .1], [None,None,None], [207, 189, 87], None)
act_pata3_duck      = actor(pata1_duck, [pos_x+ 0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata4_duck      = actor(pata2_duck, [pos_x+ 0.2, .1, .1], [None,None,None], [207, 189, 87], None)

pos_x3=-18
act_body_duck2      = actor(body_duck, [pos_x3+ 0,1,0], [None,None,None], [212, 202, 184], None)
act_ala_der_duck2    = actor(ala_duck, [pos_x3+ -0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_ala_izq_duck2    = actor(ala_duck, [pos_x3+ 0.45, 1.1, 0], [None,None,None], [224, 221, 215], None)
act_cuello_duck2     = actor(cuello_duck, [pos_x3+ 0,1.6,.7], [None,None,None], [224, 221, 215], None)
act_eye1_duck2       = actor(eye_duck, [pos_x3+ -0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_eye2_duck2       = actor(eye_duck, [pos_x3+ 0.15, 1.75, .95], [None,None,None], [0, 0, 0], None)
act_pico1_duck2      = actor(pico_duck, [pos_x3+ 0, 1.62, 1], [None,None,None], [207, 189, 87], None)
act_pico2_duck2      = actor(pico_duck, [pos_x3+ 0, 1.52, 1], [None,None,None], [181, 166, 78], None)
act_cresta_duck2     = actor(cresta_duck, [pos_x3+ 0, 1.4, 1], [None,None,None], [191, 57, 57], None)
act_pata1_duck2      = actor(pata1_duck, [pos_x3+ -0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata2_duck2      = actor(pata2_duck, [pos_x3+ -0.2, .1, .1], [None,None,None], [207, 189, 87], None)
act_pata3_duck2      = actor(pata1_duck, [pos_x3+ 0.2, .4, 0], [None,None,None], [207, 189, 87], None)
act_pata4_duck2     = actor(pata2_duck, [pos_x3+ 0.2, .1, .1], [None,None,None], [207, 189, 87], None)

pos_x2=-15
act_body_hourse     = actor(body_hourse, [pos_x2+ 2,2,0], [None,None,None], [112, 54, 7],None)
act_legs1_hourse    = actor(legs_hourse, [pos_x2+ 1.5,.65,1.5], [None,None,None], [79, 39, 6], None)
act_legs2_hourse    = actor(legs_hourse, [pos_x2+ 2.5,.65,1.5], [None,None,None], [79, 39, 6], None)
act_legs3_hourse    = actor(legs_hourse, [pos_x2+ 1.5,.65,-1.5], [None,None,None], [79, 39, 6], None)
act_legs4_hourse    = actor(legs_hourse, [pos_x2+ 2.5,.65,-1.5], [None,None,None], [79, 39, 6], None)
act_casco1_hourse   = actor(cascos_hourse, [pos_x2+ 1.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco2_hourse   = actor(cascos_hourse, [pos_x2+ 2.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco3_hourse   = actor(cascos_hourse, [pos_x2+ 1.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_casco4_hourse   = actor(cascos_hourse, [pos_x2+ 2.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_cuello_hourse   = actor(cuello_hourse, [pos_x2+ 2, 3, 2], [20,None,None], [112, 54, 7], None)
act_head_hourse     = actor(head_hourse, [pos_x2+ 2, 3.5, 2.5], [20,None,None], [112, 54, 7], None)
act_eye1_hourse     = actor(eye_hourse, [pos_x2+ 2.5, 3.5, 2.5], [20,90,None], [0, 0, 0], None)
act_eye2_hourse     = actor(eye_hourse, [pos_x2+ 1.5, 3.5, 2.5], [20,90,None], [0, 0, 0], None)
act_oreja1_hourse   = actor(oreja_hourse, [pos_x2+ 2.2, 4.2, 2.3], [20,None,None], [112, 54, 7], None)
act_oreja2_hourse   = actor(oreja_hourse, [pos_x2+ 1.8, 4.2, 2.3], [20,None,None], [112, 54, 7], None)
act_cola_hourse   = actor(cola_hourse, [pos_x2+ 2, 2.3, -2.5], [-20,None,None], [112, 54, 7], None)
act_melena_hourse   = actor(melena_hourse, [pos_x2+ 2, 3.5, 1.6], [20,None,None], [205, 217, 102], None)


pos_x4 =  10
act_body_pig     = actor(body_pig, [pos_x4+ 2,2,0], [None,None,None], [108, 44, 66],None)
act_leg1_pig    = actor(leg_pig, [pos_x4+ 1.5,.65,1.5], [None,None,None], [108, 44, 66], None)
act_leg2_pig    = actor(leg_pig, [pos_x4+ 2.5,.65,1.5], [None,None,None], [108, 44, 66], None)
act_leg3_pig    = actor(leg_pig, [pos_x4+ 1.5,.65,-1.5], [None,None,None], [108, 44, 66], None)
act_leg4_pig    = actor(leg_pig, [pos_x4+ 2.5,.65,-1.5], [None,None,None], [108, 44, 66], None)
act_casco1_pig   = actor(casco_pig, [pos_x4+ 1.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco2_pig   = actor(casco_pig, [pos_x4+ 2.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco3_pig   = actor(casco_pig, [pos_x4+ 1.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_casco4_pig   = actor(casco_pig, [pos_x4+ 2.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_tail_pig   = actor(tail_pig, [pos_x4+ 2, 2.3, -2.5], [-20,None,None], [108, 44, 66], None)
act_head_pig   = actor(head_pig, [pos_x4+ 2, 3.5, 2.5], [None,None,None], [108, 44, 66], None)
act_eye1_pig    = actor(eye_pig, [pos_x4+ 1.5, 4.1, 3.4], [None,None,None], [1, 1, 1], None)
act_eye2_pig    = actor(eye_pig, [pos_x4+ 2.5, 4.1, 3.4], [None,None,None], [1, 1, 1], None)
act_nose_pig   = actor(nose_pig, [pos_x4+ 2, 3.3, 3.4], [None,None,None], [108, 44, 66], None)


pos_x5  =  15
act_body_sheep     = actor(body_sheep, [pos_x5+ 2,2,0], [None,None,None], [212, 202, 184],None)
act_legs1_sheep    = actor(legs_sheep, [pos_x5+ 1.5,.65,1.5], [None,None,None], [212, 202, 184], None)
act_legs2_sheep    = actor(legs_sheep, [pos_x5+ 2.5,.65,1.5], [None,None,None], [212, 202, 184], None)
act_legs3_sheep    = actor(legs_sheep, [pos_x5+ 1.5,.65,-1.5], [None,None,None], [212, 202, 184], None)
act_legs4_sheep    = actor(legs_sheep, [pos_x5+ 2.5,.65,-1.5], [None,None,None], [212, 202, 184], None)
act_casco1_sheep   = actor(cascos_sheep, [pos_x5+ 1.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco2_sheep   = actor(cascos_sheep, [pos_x5+ 2.5, .2, 1.5], [None,None,None], [0, 0, 0], None)
act_casco3_sheep   = actor(cascos_sheep, [pos_x5+ 1.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_casco4_sheep   = actor(cascos_sheep, [pos_x5+ 2.5, .2, -1.5], [None,None,None], [0, 0, 0], None)
act_head_sheep     = actor(head_sheep, [pos_x5+ 2, 3, 2], [None,None,None], [212, 202, 184], None)
act_eye1_sheep     = actor(eye_sheep, [pos_x5+ 1.5, 3.5, 2.8], [None,None,None], [0, 0, 0], None)
act_eye2_sheep     = actor(eye_sheep, [pos_x5+ 2.5, 3.5, 2.8], [None,None,None], [0, 0, 0], None)
act_nose_sheep   = actor(nose_sheep, [pos_x5+ 2, 2.8, 2.6], [None,None,None], [108, 44, 66], None)

#perro
pos_x6 = -25
pos_z = 20
act_body_dog     = actor(body_dog, [pos_x6+ 2,1.5,pos_z+0.5], [None,None,None], [180, 140, 31],None)
act_legs1_dog    = actor(legs_dog, [pos_x6+ 1.7,.65,pos_z+1.5], [None,None,None], [180, 140, 31], None)
act_legs2_dog    = actor(legs_dog, [pos_x6+ 2.3,.65,pos_z+1.5], [None,None,None], [180, 140, 31], None)
act_legs3_dog    = actor(legs_dog, [pos_x6+ 1.7,.65,pos_z+-0.6], [None,None,None], [180, 140, 31], None)
act_legs4_dog    = actor(legs_dog, [pos_x6+ 2.3,.65,pos_z+-0.6], [None,None,None], [180, 140, 31], None)
act_pata1_dog   = actor(patas_dog, [pos_x6+ 1.7, .2,pos_z+ 1.6], [None,None,None], [180, 140, 31], None)
act_pata2_dog   = actor(patas_dog, [pos_x6+ 2.3, .2,pos_z+ 1.6], [None,None,None], [180, 140, 31], None)
act_pata3_dog   = actor(patas_dog, [pos_x6+ 1.7, .2,pos_z+ -0.5], [None,None,None], [180, 140, 31], None)
act_pata4_dog   = actor(patas_dog, [pos_x6+ 2.3, .2,pos_z+ -0.5], [None,None,None], [180, 140, 31], None)
act_cuello_dog   = actor(cuello_dog, [pos_x6+ 2, 2.2,pos_z+ 1.6], [20,None,None], [180, 140, 31], None)
act_head_dog     = actor(head_dog, [pos_x6+ 2, 2.7,pos_z+ 2.2], [20,None,None], [180, 140, 31], None)
act_eye1_dog     = actor(eye_dog, [pos_x6+ 2.3, 2.7, pos_z+2.2], [20,90,None], [0, 0, 0], None)
act_eye2_dog     = actor(eye_dog, [pos_x6+ 1.7, 2.7,pos_z+ 2.2], [20,90,None], [0, 0, 0], None)
act_oreja1_dog   = actor(oreja_dog, [pos_x6+ 2.3, 2.5, pos_z+1.8], [None,None,None], [180, 140, 31], None)
act_oreja2_dog   = actor(oreja_dog, [pos_x6+ 1.7, 2.5, pos_z+1.8], [None,None,None], [180, 140, 31], None)
act_cola_dog   = actor(cola_dog, [pos_x6+ 2, 1.5,pos_z+ -1.2], [-20,None,None], [180, 140, 31], None)

act_grass = actor(grass, [0,0,0], [None,None,None], None, "grass.jpg")


act_house = actor(house, [-26,5,-30], [None,None,None], [232,210,100], None)
act_door = actor(door, [-26,3.5,-25], [None,None,None], [80,15,15], None)
act_window = actor(window, [-31,5,-30], [None,None,None], [175,175,175], None)
act_pommel = actor(pommel, [-27.5,3.5,-24.5], [None,None,None], [6,39,132], None)
act_roof = actor(roof, [-26,14,-30], [None,None,90], [80,15,15], None)

# arboles
act_trunk1 = actor(trunk1, [30,4,-25], [None,None,None], [71,33,33], "corteza.jpg")
act_treecone11 = actor(tree_cone11, [30,8,-25], [None,None,90], [0,100,3], None)
act_treecone21 = actor(tree_cone21, [30,9,-25], [None,None,90], [0,100,3], None)
act_treecone31 = actor(tree_cone31, [30,10,-25], [None,None,90], [0,100,3], None)
act_treecone41 = actor(tree_cone41, [30,11,-25], [None,None,90], [0,100,3], None)
act_trunk2 = actor(trunk2, [22,3,-23], [None,None,None], [71,33,33], "corteza.jpg")
act_treecone12 = actor(tree_cone12, [22,8,-23], [None,None,90], [0,100,3], None)
act_treecone22 = actor(tree_cone22, [22,9,-23], [None,None,90], [0,100,3], None)
act_treecone32 = actor(tree_cone32, [22,10,-23], [None,None,90], [0,100,3], None)
act_treecone42 = actor(tree_cone42, [22,11,-23], [None,None,90], [0,100,3], None)

#arbusto
act_bush = actor(bush, [25,2.0,-15], [None,None,None], [0,100,3], "leaves.jpg")
act_bush2 = actor(bush2, [28,2.0,-13], [None,None,None], [0,100,3], "leaves.jpg")


#GRANERO

cubeActor1 = createActor(cube1,[131, 68, 0],[0,90,None],[-15,0,-20])
cubeActor2 = createActor(cube2,[219, 172, 121],[0,90,None],[-15,0,-20])
cubeActor3 = createActor(cube3,[219, 172, 121],[0,90,None],[-15,0,-20])

cubeActor4 = createActor(cube4,[131, 68, 0],[0,90,None],[-15,0,-20])
cubeActor5 = createActor(cube5,[131, 68, 0],[0,90,None],[-15,0,-20])
cubeActor6 = createActor(cube6,[131, 68, 0],[0,90,None],[-15,0,-20])
cubeActor7 = createActor(cube7,[131, 68, 0],[0,90,None],[-15,0,-20])

act_puerta = actor(puerta, [-1.5,2.5,-22], [None,None,None], [71,33,33], 'puerta_madera.jpg')

#------------------------------Config--------------------------------------->
#axes
# transform = vtk.vtkTransform()
# transform.Translate(5.0, 0.0, 0.0) 
# axes = vtk.vtkAxesActor()
# axes.SetUserTransform(transform)

#camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0,0,0)
camera.SetPosition(5,5,50)

#light
light1 = vtk.vtkLight()
light1.SetIntensity(1)
light1.SetPosition(0, 25, 50)

light2 = vtk.vtkLight()
light2.SetIntensity(.5)
light2.SetPosition(0, 25, -50)

light3 = vtk.vtkLight()
light3.SetIntensity(.5)
light3.SetPosition(50, 25, 0)

light4 = vtk.vtkLight()
light4.SetIntensity(.5)
light4.SetPosition(-50, 25, 0)

# renderer ---------------------> AddActor
renderer = vtk.vtkRenderer()
renderer.SetBackground(transformRGBRange([186, 155, 93]))
#molino
renderer.AddActor(act_techo)
renderer.AddActor(act_body)
renderer.AddActor(act_grass)
renderer.AddActor(act_aspa1)
renderer.AddActor(act_aspa2)
renderer.AddActor(act_estaca)

#pato
renderer.AddActor(act_body_duck)
renderer.AddActor(act_ala_der_duck)
renderer.AddActor(act_ala_izq_duck)
renderer.AddActor(act_cuello_duck)
renderer.AddActor(act_eye1_duck)
renderer.AddActor(act_eye2_duck)
renderer.AddActor(act_pico1_duck)
renderer.AddActor(act_pico2_duck)
renderer.AddActor(act_cresta_duck)
renderer.AddActor(act_pata1_duck)
renderer.AddActor(act_pata2_duck)
renderer.AddActor(act_pata3_duck)
renderer.AddActor(act_pata4_duck)

renderer.AddActor(act_body_duck2)
renderer.AddActor(act_ala_der_duck2)
renderer.AddActor(act_ala_izq_duck2)
renderer.AddActor(act_cuello_duck2)
renderer.AddActor(act_eye1_duck2)
renderer.AddActor(act_eye2_duck2)
renderer.AddActor(act_pico1_duck2)
renderer.AddActor(act_pico2_duck2)
renderer.AddActor(act_cresta_duck2)
renderer.AddActor(act_pata1_duck2)
renderer.AddActor(act_pata2_duck2)
renderer.AddActor(act_pata3_duck2)
renderer.AddActor(act_pata4_duck2)

#cerdo
renderer.AddActor(act_head_pig)
renderer.AddActor(act_body_pig)
renderer.AddActor(act_leg1_pig)
renderer.AddActor(act_leg2_pig)
renderer.AddActor(act_leg3_pig)
renderer.AddActor(act_leg4_pig)
renderer.AddActor(act_casco1_pig)
renderer.AddActor(act_casco2_pig)
renderer.AddActor(act_casco3_pig)
renderer.AddActor(act_casco4_pig)
renderer.AddActor(act_tail_pig)
renderer.AddActor(act_nose_pig)
renderer.AddActor(act_eye1_pig)
renderer.AddActor(act_eye2_pig)

#oveja
renderer.AddActor(act_body_sheep)
renderer.AddActor(act_legs1_sheep)
renderer.AddActor(act_legs2_sheep)
renderer.AddActor(act_legs3_sheep)
renderer.AddActor(act_legs4_sheep)
renderer.AddActor(act_casco1_sheep)
renderer.AddActor(act_casco2_sheep)
renderer.AddActor(act_casco3_sheep)
renderer.AddActor(act_casco4_sheep)
renderer.AddActor(act_head_sheep)
renderer.AddActor(act_eye1_sheep)
renderer.AddActor(act_eye2_sheep)
renderer.AddActor(act_nose_sheep)


#caballo
renderer.AddActor(act_body_hourse)
renderer.AddActor(act_legs1_hourse)
renderer.AddActor(act_legs2_hourse)
renderer.AddActor(act_legs3_hourse)
renderer.AddActor(act_legs4_hourse)
renderer.AddActor(act_casco1_hourse)
renderer.AddActor(act_casco2_hourse)
renderer.AddActor(act_casco3_hourse)
renderer.AddActor(act_casco4_hourse)
renderer.AddActor(act_cuello_hourse)
renderer.AddActor(act_head_hourse)
renderer.AddActor(act_eye1_hourse)
renderer.AddActor(act_eye2_hourse)
renderer.AddActor(act_oreja1_hourse)
renderer.AddActor(act_oreja2_hourse)
renderer.AddActor(act_cola_hourse)
renderer.AddActor(act_melena_hourse)

#perro
renderer.AddActor(act_body_dog)
renderer.AddActor(act_legs1_dog)
renderer.AddActor(act_legs2_dog)
renderer.AddActor(act_legs3_dog)
renderer.AddActor(act_legs4_dog)
renderer.AddActor(act_pata1_dog)
renderer.AddActor(act_pata2_dog)
renderer.AddActor(act_pata3_dog)
renderer.AddActor(act_pata4_dog)
renderer.AddActor(act_cuello_dog)
renderer.AddActor(act_head_dog)
renderer.AddActor(act_eye1_dog)
renderer.AddActor(act_eye2_dog)
renderer.AddActor(act_oreja1_dog)
renderer.AddActor(act_oreja2_dog)
renderer.AddActor(act_cola_dog)


renderer.AddActor(act_grass)

renderer.AddActor(act_house)
renderer.AddActor(act_door)
renderer.AddActor(act_window)
renderer.AddActor(act_pommel)
renderer.AddActor(act_roof)

# arboles
renderer.AddActor(act_trunk1)
renderer.AddActor(act_treecone11)
renderer.AddActor(act_treecone21)
renderer.AddActor(act_treecone31)
renderer.AddActor(act_treecone41)
renderer.AddActor(act_trunk2)
renderer.AddActor(act_treecone12)
renderer.AddActor(act_treecone22)
renderer.AddActor(act_treecone32)
renderer.AddActor(act_treecone42)

# pasto
for i in range(0, 20):
	for j in range(0, 40):
		act_grass3d = actor(grass3d, [35-j,0,-30+i], [None,None,None], [0,153,5], None)
		renderer.AddActor(act_grass3d)

renderer.AddActor(act_bush)
renderer.AddActor(act_bush2)

#----GRANERO-------

renderer.AddActor(cubeActor1)
renderer.AddActor(cubeActor2)
renderer.AddActor(cubeActor3)
renderer.AddActor(cubeActor4)
renderer.AddActor(cubeActor5)
renderer.AddActor(cubeActor6)
renderer.AddActor(cubeActor7)
renderer.AddActor(act_puerta)

#----CERCA-------
addActores(renderer,vallas)
addActores(renderer,vallas1)
addActores(renderer,vallas2)
addActores(renderer,vallas3)
addActores(renderer,vallas4)
addActores(renderer,vallas5)
addActores(renderer,vallas6)
addActores(renderer,vallas7)
addActores(renderer,vallas8)
addActores(renderer,vallas9)
addActores(renderer,vallas10)
addActores(renderer,vallas11)


# renderer.AddActor(axes)
renderer.SetActiveCamera(camera)
renderer.AddLight(light1)
renderer.AddLight(light2)
renderer.AddLight(light3)
renderer.AddLight(light4)



#renderWindow ---------------------------------------------------->
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()