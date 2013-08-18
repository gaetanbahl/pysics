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

grosastre = physics.PhysObject(400,250,4000)
grosastre2 = physics.PhysObject(600,250,7000)
objectlist = []
for i in range(1):
	objectlist.append(physics.PhysObject(random.randint(200,500),random.randint(150,300),80))
	
for i in objectlist:	
	i.addforce(physics.Attraction_grav(i,grosastre),True)
	i.addforce(physics.Attraction_grav(i,grosastre2),True)
	i.ch_pas(0.05)

objectlist[0].posx_ = objectlist[0].posx + 0.5
objectlist[0].posy_ = objectlist[0].posy - 0.5
objectlist[0].vitx =  -10
objectlist[0].vity =  10
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
		pygame.draw.circle(fen,(0,0,0),(int(grosastre2.posx),int(grosastre2.posy)),10)
		for i in objectlist:
			pygame.draw.circle(fen,(0,0,0),(int(i.posx),int(i.posy)),3)
		start = time.time()
		for i in objectlist:
			i.tick_euler()
		end = time.time()
		print 1/(end - start)
		
		
		pygame.display.flip()
		
if __name__ == '__main__':
	main()
