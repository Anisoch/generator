from generator import d_square_coordinates as dsc
from generator import additional_info as ai
from generator import vertical_lines
from generator import horizontal_lines
import pygame as pg


# финальный список координат точек
# final list of dots coordinates
dot_sample = []
dot_number = len(dot_sample)

# устанавливаем ширину и высоту окна
# setting a width and height of the window
res_x = ai['res_x']
res_y = ai['res_y']

# устанавливаем сторону квадрата
side = ai['square_side']

# основные цвета
# basic colours
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (100,100,100)
BLUE = (0,50,150)
RED = (200,50,50)

# создаем поверхность для счетчика точек
# creating a surface for dot counter
surf_w = 220 #ширина
surf_h = 30 #высота
surf = pg.Surface((surf_w,surf_h)) #сама поверхность
surf.fill(WHITE) #цвет
surf.set_alpha(20) #полупрозрачность 0-255

# создаем текст количества точек
#creating a text about dot amount
pg.font.init()
text = 'количество точек: '
f1 = pg.font.SysFont(None,30)
amount = f1.render(text,False,BLACK)
amount.set_alpha(255)





# устанавливаем ФПС
# setting FPS
FPS = 60

# запускаем pygame
# run pygame
pg.init()
screen = pg.display.set_mode((res_x, res_y))
pg.display.set_caption("name")
clock = pg.time.Clock()


a = res_x - surf_w
b = res_y - surf_h

running = True
while running:
	screen.fill(BLACK)

# отрисовка квадратов
	for i in dsc:
		pg.draw.rect(
					 screen,
					 dsc[i][0],
					 dsc[i][1])

# отрисовка линий между квадратами
	for i in vertical_lines:
		pg.draw.line(screen,GREY,i[0],i[1])
	for b in horizontal_lines:
		pg.draw.line(screen,GREY,b[0],b[1])

# отрисовка линий для позиционирования
# линии по центру
		pg.draw.line(screen,RED,((res_x/2),0),(res_x/2,res_y),3)
		pg.draw.line(screen,RED,(0,(res_y/2)), ((res_x),(res_y/2)),3)
# вертикальные линии по четвертям
		pg.draw.line(screen,RED,((res_x/4),0),(res_x/4,res_y),1)
		pg.draw.line(screen,RED,((res_x/4 * 3),0),(res_x/4 *3,res_y),1)	
# горизонтальные линии по четвертям		
		pg.draw.line(screen,RED,(0,(res_y/4)), ((res_x),(res_y/4)),1)
		pg.draw.line(screen,RED,(0,(res_y/4 * 3)), ((res_x),(res_y/4 * 3)),1)

# отрисовываем панель со счетчиком точек
		if a > 0:
			a -= 0.1
			screen.blit(surf, (a,res_y - surf_h))
		else:
			a = res_x - surf_w

		surf.blit(amount,(0,0))
		dot_number = len(dot_sample)
		N = f1.render(str(dot_number),False,BLACK)
		surf.blit(N,(190,0))

# проверяем события
# checking for events
	for event in pg.event.get():

# проверяем закрывшееся окно
		if event.type == pg.QUIT:
		    running = False

# проверяем события клавиатуры
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_KP_ENTER:
				print('ok')

# проверяем события мыши
		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1:
				print('left click', event.pos)
				for i in dsc:
					if (event.pos[0] in range(dsc[i][1][0],(dsc[i][1][0] + side)) and 
						event.pos[1] in range(dsc[i][1][1],(dsc[i][1][1] + side))):
						print(dsc[i])
						dot_plus = ((dsc[i][1][0],
									 dsc[i][1][1]))
						if dot_plus not in dot_sample:
							dot_sample.append(dot_plus)
						print(dot_sample)
						dsc[i][0] = GREY


			if event.button == 3:
				print('right click', event.pos)
				for i in dsc:
					if (event.pos[0] in range(dsc[i][1][0],(dsc[i][1][0] + side)) and 
						event.pos[1] in range(dsc[i][1][1],(dsc[i][1][1] + side))):
						print(dsc[i])
						dsc[i][0] = BLUE
						dot_minus = ((dsc[i][1][0],
									 dsc[i][1][1]))
						if dot_minus in dot_sample:
							dot_sample.remove(dot_minus)
						print(dot_sample)


	clock.tick(FPS)
	pg.display.flip()

pg.quit()
