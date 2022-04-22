import random
import time
import pygame
import sys
pygame.init()
pygame.mixer.init()
something_clicked = False
display_width = 800
display_height = 600
gromk = 1.0
vivod = gromk*10
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
car_width = 50
car_height = 100
on_mus = False
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Racing")

clock = pygame.time.Clock()
mus = pygame.mixer.Sound("BADTRIP MUSIC, GREEN ORXNGE, Send 1 - S.X.N.D. N.X.D.E.S.-1.mp3")
mus.play(-1)
print(mus.get_volume)
carImg = pygame.image.load("car1.png")  # load the car image
car2Img = pygame.image.load("car2.png")
bgImg = pygame.image.load("bbg.png")
crash_img = pygame.image.load("crash.png")
bgsImg = pygame.image.load("car.png")



def highscore(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score : " + str(count), True, black)
    gameDisplay.blit(text, (30, 30))


def draw_things(thingx, thingy, thing):
    gameDisplay.blit(thing, (thingx, thingy))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()


def message_display(message, x, y, font_size=30, Font_color=(0, 0, 0), font_type='font.otf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, Font_color)
    gameDisplay.blit(text, (x, y))
def get_font(size):
    return pygame.font.Font('font.otf',size)

def crash(x, y):
    gameDisplay.blit(crash_img, (x, y))
    message_display("GAME OVER", (display_height / 2) - 100, (display_width / 2) - 200, 64)
    pygame.display.update()
    time.sleep(1)
    gameloop()


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
        message_display("PAUSED", (display_height / 2) - 37, (display_width / 2) - 200, 64)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

    pygame.display.update()
    clock.tick(15)


class Button:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height
        self.inactiv_color = (13, 162, 58)
        self.activ_color = (23, 204, 58)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.heigth:
            pygame.draw.rect(gameDisplay, self.activ_color, (x, y, self.width, self.heigth))
            if click[0] == 1:
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()


        else:
            pygame.draw.rect(gameDisplay, self.inactiv_color, (x, y, self.width, self.heigth))

        message_display(message=message, x=x + 10, y=y + 10, font_size=font_size)


button = Button((display_height / 2) - 37, (display_width / 2) - 200)

# noinspection PyRedeclaration
on_mus = False


def menu():
    menu_back = pygame.image.load('menu_back.jpg')
    start_btn = Button(288, 70)
    music_btn = Button(200,70)
    quit_btn = Button(120, 70)
    color_smen_btn = Button(340,70)
    spravka_btn = Button(200,70)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(menu_back, (0,0))
        color_smen_btn.draw(250,300,'color change',color_change,36)
        start_btn.draw(270,200,'start game',start_game, 36)
        quit_btn.draw(358, 400, 'Quit', quit, 36)
        music_btn.draw(640,500,'Music',Sound_r,36)
        message_display("Tetris-Gonki", 150, 10, 64)

        pygame.display.update()
        clock.tick(60)
def Vih():
    global on_mus
    on_mus = False
def Plus():
    global gromk, vivod, something_clicked
    if something_clicked:
        if gromk < 1.0:
            gromk += 0.001
            vivod = gromk*10
        else:
            gromk = 1.0
            vivod = gromk * 10
        mus.set_volume(gromk)
def Minus():
    global gromk,vivod, something_clicked
    if something_clicked:
        if gromk < 0.0:
            gromk = 0.039
        elif gromk > 0.0:
            gromk -= 0.001
            vivod = gromk*10
        mus.set_volume(gromk)
def Sound_r():
    global vivod, on_mus, gromk, something_clicked
    on_mus = True
    sound_plus_btn = Button(180, 70)
    sound_minus_btn = Button(180, 70)
    sound_back_btn = Button(150, 70)
    Sound_btn = pygame.mouse.get_pos()
    while on_mus:
        if gromk < 0.0:
            gromk = 0.001
            vivod = gromk*10
        if vivod >= 10:
            k = 2
        else:
            k = 1
        gameDisplay.fill("white")
        sound_plus_btn.draw(460,300,'Plus',Plus,36)
        sound_minus_btn.draw(160,300,'Minus',Minus,36)
        sound_back_btn.draw(1,460, 'back', Vih,36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pressed = pygame.mouse.get_pressed()
        if pressed[0]:
            something_clicked = True
            if not on_mus:
                menu()
        else:
            something_clicked = False
        message_display(str(vivod)[0:3], (display_height / 2) + 44, (display_width / 2) - 200, 64)
        pygame.display.update()


def color_change():
    global on_mus,carImg
    on_mus = True
    change_back_btn = Button(150, 70)
    while True:
        right_btn = Button(180,70)
        left_btn = Button(180,70)
        change_btn = pygame.mouse.get_pos()
        gameDisplay.fill("white")
        message_display('change color',235,100,36)
        left_btn.draw(460,300,'left',Left,36)
        right_btn.draw(160,300,'Right',Right,36)
        change_back_btn.draw(1, 460, 'BAck', Vih, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not on_mus:
                    menu()
        gameDisplay.blit(carImg,(380,200))
        pygame.display.update()
def Left():
    global carImg
    carImg = pygame.image.load('car1_version2.png')
    gameDisplay.blit(carImg,(380,200))
def Right():
    global carImg
    carImg = pygame.image.load("car1.png")
    gameDisplay.blit(carImg,(380,200))







def start_game():
    gameloop()
def gameloop():
    pygame.mixer.music.pause()
    bg_x1 = (display_width / 2) - (360 / 2)
    bg_x2 = (display_width / 2) - (360 / 2)
    bg_y1 = 0
    bg_y2 = -600
    bg_speed = 10
    car_x = ((display_width / 2) - (car_width / 2))
    car_y = (display_height - car_height)
    car_x_change = 0
    road_start_x: float = (display_width / 2) - 130
    road_end_x = (display_width / 2) + 130

    thing_startx = random.randrange(road_start_x, road_end_x - car_width)
    thing_starty = -600
    thingw = 50
    thingh = 100
    thing_speed = 10
    count = 0
    gameExit = False
    while not gameExit:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -10
                elif event.key == pygame.K_RIGHT:
                    car_x_change = 10
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pause()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0

        car_x += car_x_change


        if car_x > road_end_x - car_width:
            crash(car_x, car_y)
        if car_x < road_start_x:
            crash(car_x - car_width, car_y)

        if car_y < thing_starty + thingh:
            if car_x >= thing_startx and car_x <= thing_startx + thingw:
                crash(car_x - 25, car_y - car_height / 2)
            if car_x + car_width >= thing_startx and car_x + car_width <= thing_startx + thingw:
                crash(car_x, car_y - car_height / 2)

        gameDisplay.fill(green)  # display white background
        gameDisplay.blit(bgsImg, (0, 0))
        gameDisplay.blit(bgsImg, (440, 0))

        gameDisplay.blit(bgImg, (bg_x1, bg_y1))
        gameDisplay.blit(bgImg, (bg_x2, bg_y2))

        car(car_x, car_y)  # display car
        draw_things(thing_startx, thing_starty, car2Img)

        highscore(count)
        count += 1
        thing_starty += (thing_speed) + 10

        if thing_starty > display_height:
            thing_startx = random.randrange(road_start_x, road_end_x - car_width)
            thing_starty = -200

        bg_y1 += bg_speed
        bg_y2 += bg_speed

        if bg_y1 >= display_height:
            bg_y1 = -600

        if bg_y2 >= display_height:
            bg_y2 = -600

        pygame.display.update()  # update the screen
        clock.tick(60)  # frame per sec
menu()
