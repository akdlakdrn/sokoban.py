import pygame
import sys
import time
from UserString import MutableString
pygame.init()
pixelx      =      60
pixely      =      60
tylex       =      10
tyley       =      8
iot_count   =      0
displayx    =      tylex*pixelx
displayy    =      tyley*pixely
manx        =      0
many        =      0
stage_num   =      0



WHITE = (255, 255, 255)
ImgWall = pygame.image.load('toi_om.png')
ImgNaxt = pygame.image.load('gem5.png')
ImgBox = pygame.image.load('gem3.png')
ImgManR = pygame.image.load('iot_manR.png')
ImgManL = pygame.image.load('iot_manL.png')
ImgManU = pygame.image.load('iot_manU.png')
ImgManD = pygame.image.load('iot_manD.png')
ImgStar = pygame.image.load('gem4.png')
ImgClear = pygame.image.load('iot_end.png')
ImgMan = ImgManU


iot_stage = [[
				MutableString("@       % "),
				MutableString(" ######## "),
				MutableString("        # "),
				MutableString(" ###### # "),
				MutableString(" ###### # "),
				MutableString(" #!$    # "),
				MutableString(" ######## "),
				MutableString("          ")
				],
				[
				MutableString("@#########"),
				MutableString(" #        "),
				MutableString(" # ###### "),
				MutableString(" # #!$  # "),
				MutableString(" #  ### # "),
				MutableString(" ##     # "),
				MutableString("   ###### "),
				MutableString(" #        ")
				],
				[
				MutableString("##########"),
				MutableString("#@   $ ! #"),
				MutableString("#        #"),
				MutableString("#        #"),
				MutableString("#!$      #"),
				MutableString("#        #"),
				MutableString("#      $!#"),
				MutableString("######   #")
				]
]


def Iotinit():
	global DISPLAYSURF
	iot_caption = 'IOT sokoban'
	pygame.display.set_caption('IOT sokoban')
	DISPLAYSURF = pygame.display.set_mode((displayx,displayy), 0, 32)
	IotLoadMap()
	
def IotSetCaption(Caption):
	pygame.display.set_caption(Caption)

def IotLoadMap():
	global iot_map

	for iStage in range(tyley):
		iot_map.append(iot_stage[stage_num][iStage][:])

def IotDraw():

	global manx
	global many
	global stage_end
	
	DISPLAYSURF.fill(WHITE)
	stage_end = True
	for ix in range(tylex):
		for iy in  range(tyley):
			if '#' == iot_map[iy][ix]:
				DISPLAYSURF.blit(ImgWall, (ix*pixelx, iy*pixely))
			elif '@' == iot_map[iy][ix]:
				DISPLAYSURF.blit(ImgMan, (ix*pixelx, iy*pixely))
				manx = ix
				many = iy
			elif '!' == iot_map[iy][ix]:
				DISPLAYSURF.blit(ImgNaxt, (ix*pixelx, iy*pixely))
			elif '$' == iot_map[iy][ix]:
				DISPLAYSURF.blit(ImgBox, (ix*pixelx, iy*pixely))
				if '!' != iot_stage[stage_num][iy][ix]:
					stage_end = False
			elif '%' == iot_map[iy][ix]:
				DISPLAYSURF.blit(ImgStar, (ix*pixelx, iy*pixely))
	pygame.display.update()

#iot_caption = "IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count) 
stage_end = False
iot_map = []

iot_caption = 'IOT sokoban'
pygame.display.set_caption('IOT sokoban')
pygame.display.set_caption(iot_caption)
DISPLAYSURF = pygame.display.set_mode((displayx,displayy), 0, 32)


IotLoadMap()
while True:
	IotDraw()

	if True == stage_end:
		DISPLAYSURF.blit(ImgClear, (120, 0))
		pygame.display.update()
		keyinput = False
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					keyinput = True
					break
			if True == keyinput:
				break
			time.sleep(0.1)
			iot_caption = "IOT sokoban[stage:%d]"%(stage_num + 2) 
			continue
		stage_num += 1
		iot_map = []

		for iStage in range(tyley):
			iot_map.append(iot_stage[stage_num][iStage][:])
		iot_count = 0

#iot_caption = "IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count)
		IotSetCaption("IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count))
		continue

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			TempX = manx
			TempY = many
			if event.key == pygame.K_DOWN:
				ImgMan = ImgManD
				many = many + 1
			elif event.key == pygame.K_UP:
				ImgMan = ImgManU
				many = many - 1
			elif event.key == pygame.K_RIGHT:
				ImgMan = ImgManR
				manx = manx + 1
			elif event.key == pygame.K_LEFT:
				ImgMan = ImgManL
				manx = manx - 1
			elif event.key == pygame.K_r:
				iot_map = []
				for iStage in range(tyley):
					iot_map.append(iot_stage[stage_num][iStage][:])
				iot_count = 0
#iot_caption = "IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count)
				IotSetCaption("IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count))
				break
			else:
				continue
			#if ' '==iot_map[many][manx] or '%'==iot_map[many][manx]:


			if '#'!=iot_map[many][manx]:
				if '$'== iot_map[many][manx]:
					if ' ' ==	iot_map [2*many-TempY][2*manx-TempX] or '!' == iot_map [2*many-TempY][2*manx-TempX]:
						iot_map [2*many-TempY][2*manx-TempX] = '$'
					else:
						many = TempY
						manx = TempX
						continue
				if '%'== iot_stage[stage_num][TempY][TempX]:	
					iot_map[TempY][TempX] = '%'
				if '!'== iot_stage[stage_num][TempY][TempX]:	
					iot_map[TempY][TempX] = '!'
				else:
					iot_map[TempY][TempX] = ' '
				iot_map[many][manx] = '@'
				iot_count += 1
#print iot_count
#iot_caption = "IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count) 
				IotSetCaption("IOT sokoban[stage:%d][count:%d]"%(stage_num + 1,iot_count))
				


			elif event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
