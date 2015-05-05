# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 03:11:15 2013

@author: alex
"""

#Programa de Dethined
#px = -1.85998
#py = 1.64535
#pz = 1.28393
#x = 9.949343
#y = 2.1
#datos = [px,py,pz,x,y]
#print datos


# -----------------LA CLASE VECTOR----------#
import math
import random
import numpy as np

class vector:
    def __init__(self,lista):
        self.x=[]
        for xi in lista:
          self.x.append(float(xi))
        self.dim=len(self.x) 
        self.mod=math.sqrt(self.prod_escalar(self))

    def prod_escalar(self,a):
        if (self.dim == a.dim):
            pesc=0.
            for i in range(0,self.dim):
                pesc += (self.x[i] * a.x[i])
            return pesc
        else:
            print "El productor escalar se define para vectores de la misma dimension"
            return None

def suma(a, b):
    suma=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          suma.append(a.x[i]+b.x[i])
       return vector(suma)
    else:
       return None

def resta(a, b):
    resta=[]
    if (a.dim == b.dim):
       for i in range(0,a.dim):
          resta.append(a.x[i]-b.x[i])
       return vector(resta)
    else:
       return None

def vector_escalar(a, num):
    escalar=[]
    for i in range(0,a.dim):
      escalar.append(num*a.x[i])
    return vector(escalar)

#-----------LEYENDO EL ARCHIVO DE TEXTO-----------------
#for lista in open("DATOS.txt"):
#    if len(lista.split())==8:
#        if not lista.startswith('#'):
#            idcorsika = float(lista.split()[0])/1e3            
#            px = float(lista.split()[1])
#            py = float(lista.split()[2])
#            pz = float(lista.split()[3])
#            x = float(lista.split()[4])/1e2
#            y = float(lista.split()[5])/1e2
#            t = float(lista.split()[6])
#            w = float(lista.split()[7])
           # print lista

#----------CALCULOS REQUERIDOS--------------------------

#contador=0
 
#beta_elec = 3 # [grados/km]
#beta_muon = 1	
#beta_hadr = 1
#epsilon = 50 # [g/cm^2]
#dx = 750 # DUDA 
#probabilidad = math.exp(-dx/epsilon) 

def dist_gauss(val, media, des):
    descuad = float(des)**2
    denom = (2*math.pi*descuad)**0.5
    num = math.exp(-(float(val)-float(media))**2/(2*descuad))
    return num/denom

wfile1=open('salida_prueba_maestria_11.txt','w')
wfile1.write('# coordenanas de las partículas a nivel del detector'+"\n")
wfile1.write('#x #y #z'+"\n")


#for n in range (1,2):
for lista in open("proton_1e-8_maestria"):
    if len(lista.split())==8:
        if not lista.startswith('#'):
            idcorsikap = int(float(lista.split()[0])/1e3)            
            px = float(lista.split()[1])
            py = float(lista.split()[2])
            pz = float(lista.split()[3])
            x = float(lista.split()[4])/1e2
            y = float(lista.split()[5])/1e2
            t = float(lista.split()[6])
            w = float(lista.split()[7])
            peso = float(w)            
            peso_ent= int(peso)
            r = vector([x,y,0]) 
            p = vector([px, py, pz])
            c = 3e8*1e-9
            normap = p.mod
            normar = r.mod            
            #unitar = vector_escalar(r,1/normar)
            #unitap = vector_escalar(p,1/normap)

######---DICTIONARY ANGLE OF PARTICLES---##################################

            nparticle =int(idcorsikap)
            primer_parte = 1
            sec_part = 2
            mydic = {1: [0, 3, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
            beta = mydic[primer_parte][nparticle]
      #      print nparticle, beta

##########---END OF DICTIONARY---#########################################


######---DICTIONARY MASS OF PARTICLES---##################################

            nparticle =int(idcorsikap)
            primer_parte = 1
            sec_part = 2
            mydic = {1: [0, 0, 0.510*1e-3, 0.510*1e-3, 0, 0.105658, 0.105658, 0.13497, 0.13957, 0.13957, 
            0.497648, 0.493677, 0.493677, 0.939565, 0.938272, 0.938272, 0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0.939565]}
            masa = mydic[primer_parte][nparticle]
   #         print nparticle, masa

##########---END OF DICTIONARY---#########################################



######---DICTIONARY INTERACTION LENGHT OF PARTICLES---##################################

            nparticle =int(idcorsikap)
            primer_parte = 1
            sec_part = 2
            mydic = {1: [0, 37, 37, 37, 52, 52, 52, 90, 90, 90, 90, 90, 90, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90]}
            long_interaction = mydic[primer_parte][nparticle]
	 #   if nparticle > 15:	
#		print Hola

#            print nparticle, long_interaction

##########---END OF DICTIONARY---#########################################

            if normap!=0 and normar!=0:
                unitar = vector_escalar(r,1/normar)
                unitap = vector_escalar(p,1/normap)                
                Dmax = ((c**2*(t**2)-normar**2)/(2*(c*t-r.prod_escalar(unitap))))                
		wfile1.write(str(idcorsikap)+' '+str(x)+' '+str(y)+"\n")
		wfile1.write("\n")                
		for k in range(0, peso_ent -1):
                    dtheta_x = random.gauss(0,0.1)
                    dtheta_y = random.gauss(0,0.1)   
		    cor_theta_x = beta*x
		    cor_theta_y = beta*y
		    dx = Dmax*math.tan(math.radians(cor_theta_x))
                    dy = Dmax*math.tan(math.radians(cor_theta_y))         
                    x_tot = (x + dx)*1e2
                    y_tot = (y + dy)*1e2
                    r_normita = math.sqrt((x_tot)**2+(y_tot)**2)
                    r_tot = vector([x_tot, y_tot, -Dmax])
                    r_tot_norm = r_tot.mod
		    theta_tot = math.acos(Dmax/r_tot_norm) 
                    p_x = pz*math.tan(math.radians(dtheta_x)) + px
                    p_y = pz*math.tan(math.radians(dtheta_y)) + py   
                    p_z = math.sqrt(np.absolute((normap**2-(p_x)**2-(p_y)**2))) 
                    pvector = vector([p_x,p_y,p_z])
                    pnorma = pvector.mod		
                    tn=(r_tot_norm)/c
                    radio=math.sqrt((x_tot)**2+(y_tot)**2)
                                       
		    altura_h=(r_tot_norm*math.cos(theta_tot)) #*100  #*10e2 #cm
                        
       #             print dtheta_x,dtheta_y,r_normita                   
       #         print

###CONSTANTES-------------------------CAPA 1--------------------------------
                    const_a = -135.708 #g/cm²                   
                    const_b = 1174.01 # g/cm² 
                    const_c = 994186 # cm
#####Función de la densidad de la primera capa------------------------------
                    X_1=const_a+const_b*math.exp(-altura_h/const_c)                     
###CONSTANTES-------------------------CAPA 2--------------------------------
		    const_a_2 = -22.0191 # g/cm² 	
		    const_b_2 = 1261.58 # g/cm²	 
		    const_c_2 = 721829 # cm 
	            X_2 = const_a_2+const_b_2*math.exp(-altura_h/const_c_2)
		    deltax = X_2 - X_1 
		#    print nparticle, deltax	
###CONSTANTES-------------------------CAPA 3--------------------------------
		    const_a_3 = 0.587399 # g/cm²
		    const_b_3 = 1350.34 # g/cm²
		    const_c_3 = 636143 # cm		
		    X_3 = const_a_3+const_b_3*math.exp(-altura_h/const_c_3)
		    delta_2 = X_3 - X_2
###CONSTANTES-------------------------CAPA 4--------------------------------
		    const_a_4 = -0.000677176 # g/cm²
		    const_b_4 = 560.655 # g/cm²
		    const_c_4 = 772170 # cm	
		    X_4 = const_a_4 + const_b_4*math.exp(-altura_h/const_c_4) 
	   	    delta_3 = X_4 - X_3		
###CONSTANTES-------------------------CAPA 5--------------------------------
                    const_a_5 = 0.000124205 # g/cm²                                           
                    const_b_5= 1 # g/cm²
                    const_c_5= 9.35523*10e9 # cm
		    X_5 = const_a_5 + const_b_5*math.exp(-altura_h/const_c_5) 			
		    delta_4 = X_5 - X_4
#####Función de la densidad de la segunda capa------------------------------
                   # rho_1=const_d+const_e*math.exp(-altura_h/const_f)

                    prob_part_1= math.exp(-deltax/long_interaction)
		    prob_part_2= math.exp(-delta_2/long_interaction)
		    prob_part_3= math.exp(-delta_3/long_interaction)
		    prob_part_4= math.exp(-delta_4/long_interaction)
		#    print nparticle, prob_part_1*100, altura_h	
            
		    E_part = math.sqrt((masa)**2 + normap**2)
		    E_gauss =random.gauss(E_part,10)
		#    print nparticle, rad, abs(E_part)
	        #    print nparticle, radio, abs(E_gauss) 

		    	
   		    wfile1.write(str(idcorsikap)+' '+str(x_tot)+' '+str(y_tot)+"\n")	
       #          print x_tot, y_tot                 
       #         print
