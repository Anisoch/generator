import pygame as pg

start_x = 0
start_y = 0

length = 40
height = 60

step = 10

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,255,0)

x_coordinates = [i for i in range(
								  0,
								  length,
								  step
								  )
				]

y_coordinates = [i for i in range(
								  0,
								  height,
								  step)
				]

square_coordinates = []
for x in x_coordinates:
	l = [(x,y) for y in y_coordinates]
	square_coordinates.extend(l)


d_sqare_coordinates = {
i : (square_coordinates[i], WHITE) 
for i in range(0,len(square_coordinates))
						}


c = (17,43)
for i in square_coordinates:
	if c[0] in range(i[0],i[0] + step) and c[1] in range(i[1],i[1] + step):
		print('match',i)

for i in d_sqare_coordinates:
	print(i, d_sqare_coordinates[i])


