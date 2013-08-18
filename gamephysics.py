#-------------------------------------------------------------------------------
# Name:        gamephysics
# Purpose:
#
# Author:      Blacky
#
# Created:     12/04/2013
# Copyright:   (c) Blacky 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import physics



class Universe(physics.System):

    def __init__(self,sizex,sizey):
        physics.System.__init__(self)
        self.sizex = sizex
        self.sizey = sizey


    def selectbyid(self,id):
        l = []
        for i in self.objectlist:
            if i.id == id:
                l.append(i)
        return l

    def selectbytype(self,type):
        l = []
        for i in self.objectlist:
            if i.type == type:
                l.append(i)
        return l

    def setgravity(self):
        self.gravity = True
        for i in self.selectbytype("vaisseau"):
            for j in self.selectbytype("planete"):
                if i != j:
                    i.addforce(newgravity(i,j),True)

    def getallcoord(self):
        l= []
        for i in self.objectlist:
            l.append((i.posx,i.posy,i.theta,i.id))
        return l


class Ship(physics.PhysObject):

    def __init__(self,x,y,m,id):

        self.id = id
        self.type = "nothing"

        physics.PhysObject.__init__(self,x,y,m)


class newgravity(physics.Attraction_grav):
    pass



def make_string_of_coord(listeofcoord):
    string = ""
    for i in listeofcoord:
        for x in i:
            string += (str(x) + " ")
        string += "\n"
    return string


def setboost(shipid):
    pass



def main():
    pass

if __name__ == '__main__':
    main()
