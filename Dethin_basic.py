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

# algo algo
# -----------------LA CLASE VECTOR----------#
import math
import random

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

wfile1=open('salida_dethin_proton_1e-8.txt','w')
wfile1.write('# coordenanas de las partículas a nivel del detector'+"\n")
wfile1.write('#x #y #z'+"\n")


#for n in range (1,2):
for lista in open("proton_1e-8"):
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
            if normap!=0 and normar!=0:
                unitar = vector_escalar(r,1/normar)
                unitap = vector_escalar(p,1/normap)                
                Dmax = ((c**2*(t**2)-normar**2)/(2*(c*t-r.prod_escalar(unitap))))                
		wfile1.write(str(idcorsikap)+' '+str(x)+' '+str(y)+"\n")
		wfile1.write("\n")                
		for k in range(0, peso_ent -1):
                    dtheta_x = random.gauss(0,0.1)
                    dtheta_y = random.gauss(0,0.1)            
                    dx = Dmax*math.tan(math.radians(dtheta_x))
                    dy = Dmax*math.tan(math.radians(dtheta_y))
                    x_tot = (x + dx)*1e2
                    y_tot = (y + dy)*1e2
        #            r_normita = math.sqrt((x_tot)**2+(y_tot)**2)
        #            r_tot = vector([x_tot, y_tot, -Dmax])
        #            r_tot_norm = r_tot.mod
        #            p_x = pz*math.tan(math.radians(dtheta_x)) + px
        #            p_y = pz*math.tan(math.radians(dtheta_y)) + py   
        #            p_z = math.sqrt(normap**2-(p_x)**2-(p_y)**2) 
        #            pvector = vector([p_x,p_y,p_z])
        #            pnorma = pvector.mod		
        #            tn=(r_tot_norm)/c:
        #            radio=math.sqrt((x_tot)**2+(y_tot)**2)
		    	
   		    wfile1.write(str(idcorsikap)+' '+str(x_tot)+' '+str(y_tot)+"\n")	
       #          print x_tot, y_tot                 
       #         print
