'''
В этом модуле создается словари:
1) (цвет квадратов), (коордниата х, координата y, сторона, сторона)
2) разрешение экрана и сторона квадрата

This module creates dictionaries:
1) (COLOUR), (coordinate_x, coordinate_y, side, side)
2) screen resolution, side of a square
'''

# разрешение экрана
# screen resolution
res_x = 800
res_y = 800

# размер квадрата
# square side
side = 50

# основные цвета
# basic colurs
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,150)

# создаем список всех координат 'x'
# creating a list of all 'x' coordinates
x_coordinates = [i for i in range(
								  0,
								  res_x,
								  side
								  )
				]

# создаем список всех координат 'y'
# creating a list of all 'y' coordinates
y_coordinates = [i for i in range(
								  0,
								  res_y,
								  side
								  )
				]

# создаем список вложенных кортежей координат ('x','y')
# creating a list of tuples of coordinates ('x', 'y')
square_coordinates = []
for x in x_coordinates:
	l = [(x,y) for y in y_coordinates]
	square_coordinates.extend(l)

# переводим список в словарь (номер : ЦВЕТ, ('x','y'))
# turnig a list in a dictionary (number : COLOUR, ('x','y'))
d_square_coordinates = {
	i : (BLUE, 
		(square_coordinates[i][0],square_coordinates[i][1], side, side))
	for i in range(0,len(square_coordinates))
						}




vertical_lines = [
				  ((i,0), (i,res_y)) for i in range(
													 side,
													 res_x,
													 side
													 )
				  ]

horizontal_lines = [
					((0,i),(res_x,i)) for i in range(
													 side,
													 res_y,
													 side)
					]

# дополнительная информация по разрешению экрана и размеру квадрата
# additional information about screen resolution and square side
additional_info= {
				'res_x' : res_x,
				'res_y' : res_y,
				'square_side' : side
				 }



# c = (20,37)
# for i in square_coordinates:
# 	if c[0] in range(i[0],i[0] + side) and c[1] in range(i[1],i[1] + side):
# 		print('match',i)
