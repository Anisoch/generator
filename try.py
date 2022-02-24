from generator import d_square_coordinates as dsc
from generator import additional_info as ai
from generator import vertical_lines
from generator import horizontal_lines
import pygame as pg

# устанавливаем ширину и высоту окна
# setting a width and height of the window
res_x = ai['res_x']
res_y = ai['res_y']

# основные цвета
# basic colours
BLACK = (0,0,0)
WHITE = (100,100,100)

# устанавливаем ФПС
# setting FPS
FPS = 60

# запускаем pygame
# run pygame
pg.init()
screen = pg.display.set_mode((res_x, res_y))
pg.display.set_caption("name")
clock = pg.time.Clock()

side = ai['square_side']

running = True
while running:
	screen.fill(BLACK)
	for i in dsc:
		pg.draw.rect(
					 screen,
					 dsc[i][0],
					 dsc[i][1])
	for i in vertical_lines:
		pg.draw.line(screen,WHITE,i[0],i[1])
	for b in horizontal_lines:
		pg.draw.line(screen,WHITE,b[0],b[1])

	for event in pg.event.get():
# проверяем закрывшееся окно
		if event.type == pg.QUIT:
		    running = False
		if event.type == pg.KEYDOWN:
			if event.key == pyg.K_KP_ENTER:
				print('ok')

	clock.tick(FPS)
	pg.display.flip()


pg.quit()
