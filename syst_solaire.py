#-------------------------------------------------------------------------------
# Name:        randoom uni grav
# Purpose:      montrer ce que peut faire le moteur physique
#
# Author:      Timosis
#
# Created:     08/04/2013
# Copyright:   (c) Timosis 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import physics,pygame,sys,math
from pygame.locals import *
import random,time
from funcs import *
pygame.init()
fen = pygame.display.set_mode((1024,560))
systeme = physics.System()
grosastre = physics.PhysObject(400,250,400000)
systeme.addobject(grosastre)
objectlist = []

for i in range(9):
	mhh = physics.PhysObject(400 + (-1)**(i %2)*40*(i+1),250,40*(i+1))
	mhh.vity =  (-1)**(i%2)* math.sqrt(6*400000/(3*(i+1))**2)
	objectlist.append(mhh)
	
for i in objectlist:
	systeme.addobject(i)

systeme.setgravity()

	
def main():
	boucle = 1
	trace = False
	while boucle:
		for event in pygame.event.get():
			if event.type == QUIT:
				boucle = 0
			if event.type == KEYDOWN:
				if event.key == K_t:
					trace = obool(trace)
	
		if not trace:
			fen.fill((255,255,255))
		pygame.draw.circle(fen,(0,0,0),(int(grosastre.posx),int(grosastre.posy)),10)
		for i in objectlist:
			pygame.draw.circle(fen,(0,0,0),(int(i.posx),int(i.posy)),3)
		start = time.time()
		systeme.update_euler()
		end = time.time()
		print 1/(end - start)
		
		
		pygame.display.flip()
		
if __name__ == '__main__':
	main()
