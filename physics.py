#-------------------------------------------------------------------------------
# Name:        physics.py
# Purpose:      determiner des mouvements
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import math,funcs,threading

class Vector:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __mul__(self,nombre):
        self.x *= nombre
        self.y *= nombre
    def __add__(self,vecteur):
        self.x = self.x + vecteur.x
        self.y = self.y + vecteur.y

    def setcoord(self,x,y):
        self.x = x
        self.y = y


class Force(Vector):

    def __init__(self,x,y,brlev = 0,update = False ):

        Vector.__init__(self,x,y)
        self.bras_de_levier = brlev
        self.newtons = math.sqrt(x**2 + y**2)
        self.updatable = update
        self.id = ""


    def point_a_point(self,pointa,pointb):
        xa,ya = pointa
        xb,yb = pointb
        x = xb - xa
        y = yb - ya
        distance = math.sqrt(x**2+y**2)
        self.x = self.newtons*(x/distance)
        self.y = self.newtons*(y/distance)

    def nullifie(self):
        self.x = 0
        self.y = 0

class Frottements(Force):

    def __init__(self,obj,k,power):
        Force.__init__(self,-k*(obj.vitx)**power,-k*(obj.vity)**power,0,True)
        self.obj = obj
        self.k = k
        self.power = power

    def update(self):
        self.x = -self.k*(self.obj.vitx)**self.power
        self.y = -self.k*(self.obj.vity)**self.power

class Force_centrale(Force):

    def __init__(self,obj1,obj2,newts):

        Force.__init__(self,0,0,0,True)
        self.obj1 = obj1
        self.obj2 = obj2
        self.newtons = newts

    def centraleupdate(self):
        pointa = self.obj1.posx,self.obj1.posy
        pointb = self.obj2.posx,self.obj2.posy
        self.newtons_update()
        self.point_a_point(pointa,pointb)

    def setobjets(self,objet1,objet2):
        self.obj1 = objet1
        self.obj2 = objet2

class Attraction_grav(Force_centrale):
    def __init__(self,obj1,obj2):
        newtons = (6.67*obj1.mass*obj2.mass)/obj1.distance(obj2)**2
        Force_centrale.__init__(self,obj1,obj2,newtons)
        self.setobjets(obj1,obj2)
    def newtons_update(self):
        self.newtons = (6.67*self.obj1.mass*self.obj2.mass)/(self.obj1.distance(self.obj2)**2)
    def update(self):
        self.centraleupdate()
        self.newtons_update()

class ForceElastique(Force_centrale):
    def __init__(self,obj1,obj2,lo,k):
        self.lo = lo
        self.k = k
        newtons = self.k*(obj1.distance(obj2) - self.lo)
        Force_centrale.__init__(self,obj1,obj2,newtons)
        self.setobjets(obj1,obj2)

    def newtons_update(self):
        self.newtons = self.k*(self.obj1.distance(self.obj2) - self.lo)
    def update(self):
        self.centraleupdate()
        self.newtons_update()

class PhysObject:


    nombre_objets = 0
    def __init__(self,x,y,m):
        self.posx = x
        self.posy = y
        self.posx_ = x
        self.posy_ = y

        self.mass = m
        self.size = 1

        self.vitx = 0
        self.vity = 0

        self.accx = 0
        self.accy = 0

        self.omega = 0
        self.theta = 0

        self.pas = 0.01
        self.passquare = self.pas**2
        self.gravityforce = True
        PhysObject.nombre_objets += 1
        self.forces_fixes = []
        self.forces_updates = []
        self.sumforces = Force(0,0)

#MODIFICATION DATTRIBUTS
    def ch_pos(self,x,y):
        self.posx = x
        self.posy = y

    def ch_speed(self,x,y):
        self.vitx = x
        self.vity = y

    def ch_speed_vector(self,vecteur):
        self.vitx = vecteur.x
        self.vity = vecteur.y

    def ch_accel(self,x,y):
        self.accx = x
        self.accy = y

    def ch_speed_vector(self,vecteur):
        self.accx = vecteur.x
        self.accy = vecteur.y

    def ch_pas(self,pas):
        self.pas = pas
        self.passquare = pas**2

    def gravityforce(self,booleen):
        self.gravityforce = booleen

    def addforce(self,force,update=False):
        if update:
            self.forces_updates.append(force)
        else:
            self.forces_fixes.append(force)

    def addforcecart(self,x,y, update = False,brlv = 0):
        frc = Force(x,y,brlv,update)
        if update:
            self.forces_updates.append(frc)
        else:
            self.forces_fixes.append(frc)

    def addcentralforce(self,obj,N):
        frc = Force_centrale(self,obj,N)
        self.forces_updates.append(frc)

    def sommeforces(self):
        self.sumforces.nullifie()
        for i in self.forces_fixes:
            self.sumforces + i
        for i in self.forces_updates:
            i.update()
            self.sumforces + i
    def distancesquare(self,obj):
        return (self.posx-obj.posx)**2 + (self.posy-obj.posy)**2

#PHYSIQUE
    def rotate(self):
        self.theta += self.pas*self.omega

    def minieuler(self):
        h = self.pas
        self.vitx += h*self.accx
        self.vity += h*self.accy
        self.posx += h*self.vitx
        self.posy += h*self.vity

    def verlet(self):
        self.posx,self.posx_ = 2*self.posx - self.posx_ + self.accx*self.passquare,self.posx
        self.posy,self.posy_ = 2*self.posy - self.posy_ + self.accy*self.passquare,self.posy

    def pfd(self):
        self.sommeforces()

        x,y = self.sumforces.x,self.sumforces.y
        self.accx = x/self.mass
        self.accy = y/self.mass

    def tick(self):
        self.pfd()
        self.verlet()
        self.rotate()

    def tick_euler(self):
        self.pfd()
        self.minieuler()
        self.rotate()


class System:

    def __init__(self):
        self.objectlist = []
        self.pas = 0.1
        self.gravity = False
        self.threading = False
        self.collisions = False
        self.bounce = False
        self.splitobjectlist = []

    def addobject(self,objec):
        self.objectlist.append(objec)

    def setgravity(self):
        self.gravity = True
        for i in self.objectlist:
            for j in self.objectlist:
                if i != j:
                    i.addforce(Attraction_grav(i,j),True)

    def checkcollisions(self):
        liste_collisions = []
        for i in self.objectlist:
            for j in self.objectlist:
                if j != i and not funcs.isin((j,i),liste_collisions):
                    if i.distancesquare(j) < (i.size + j.size)**2 :
                        liste_collisions.append((i,j))
        return liste_collisions

    def applycollisions(self):

        for i in self.checkcollisions():

            obj1,obj2 = i
            m1,m2 = obj1.mass,obj2.mass
            M = m1+m2
            v1x,v1y = obj1.vitx,obj1.vity
            v2x,v2y = obj2.vitx,obj2.vity
            vbarx = (1.0/(M))*(m1*v1x + m2*v2x)

            vbary = (1.0/(M))*(m1*v1y + m2*v2y)
            print vbary
            obj1.vitx = -v1x + 2*vbarx
            obj1.vity = -v1y + 2*vbary
            obj2.vitx = -v2x + 2*vbarx
            obj2.vity = -v2y + 2*vbary

    def split(self):
        self.splitobjectlist = funcs.split_seq(self.objectlist,2)

    def join(self):
        self.objectlist = []
        for i in self.splitobjectlist:
            self.objectlist += i

    def update(self):
        for i in self.objectlist:
            i.tick()
    def update_euler(self):
        for i in self.objectlist:
            i.tick_euler()
        if self.collisions:
            self.applycollisions()

    def updatethr(self):
        threadList = []
        for i in self.splitobjectlist:
            curthread = updateThread(i)
            curthread.start()
            threadList.append(curthread)
        for i in threadList:
            i.join()

    def setpas(self):
        for i in self.objectlist:
            i.pas = self.pas
            i.passquare = self.pas**2

class Arbre():

    def __init__(self,string,recursion):
        self.branches = []
        self.recursion = recursion
        self.string = string


    def addbranche(self,string):
        branche = Arbre(string,self.recursion + 1)
        self.branches.append(branche)

    def setbranchestring(self,number,string):
        self.branches[number].string  = string


class updateThread(threading.Thread):

    def __init__(self, liste):

        threading.Thread.__init__(self)
        self.liste = liste

    def run(self):
        for i in self.liste:
            i.tick()

def barycentre (liste_objets):
    """renvoie les coordonnees et la masse du barycentre d'une liste de plusieurs objets du type PhysObject"""
    x = 0
    y = 0
    summass = 0
    for i in liste_objets:
        x += i.mass * i.posx
        y += i.mass * i.posy
        summass += i.mass
    x /= summass
    y /= summass
    return x,y,summass


def main():
    pass

if __name__ == '__main__':
    main()

