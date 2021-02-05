import pygame
import time
import random
pygame.init()
Gameicon = pygame.image.load('cari.png')
pygame.display.set_icon(Gameicon)
displayw = 800
displayh = 600
pause = False
gamedisplays = pygame.display.set_mode((displayw, displayh))
pygame.display.set_caption('Go Go 2')
gray = (148, 142, 142)
lightred = (255, 0, 0)
white = (255, 255, 255)
lightgreen = (0, 255, 0)
red = (224, 25, 25)
green = (37, 204, 37)
blue = (42, 42, 181)
lightblue = (0, 0, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
carimg = pygame.image.load('car1.png')
garageImg1 = pygame.image.load('car1.png')
garageImg2 = pygame.image.load('car2.png')
garageImg3 = pygame.image.load('car3.png')
garageImg4 = pygame.image.load('car4.png')
garageImg5 = pygame.image.load('truck1.png')
backgroundpic = pygame.image.load('Grass.png')
white_strip = pygame.image.load('White-strip.png')
strip = pygame.image.load('Strip.png')
introbackgroundpic = pygame.image.load('introb.jpg')
introductionbackgroundpic = pygame.image.load('instructionb.jpg')
car_width = 64
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(introbackgroundpic, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Go Go 2', largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)
        button('Play', 150, 520, 100, 50, green, lightgreen, 'play')
        button('Quit', 550, 520, 100, 50, red, lightred, 'quit')
        button('Introduction', 300, 520, 200, 50, blue, lightblue, 'introduction')
        button('Garage', 350, 300, 100, 50, blue, lightblue, 'garage')
        pygame.display.update()
        clock.tick(60)
def button(msg, x, y, w, h, ic, ac, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click [0] == 1 and action != None:
            if action == 'play':
                countdown()
            elif action == 'quit':
                pygame.quit()
                quit()
                sys.exit()
            elif action == 'introduction':
                introduction()
            elif action == 'menu':
                intro_loop()
            elif action == 'paused':
                paused()
            elif action == 'unpaused':
                unpaused()
            elif action == 'garage':
                garage()
            elif action == 'Coupe_car':
                Coupe_car()
            elif action == 'Sport_car':
                Sport_car()
            elif action == 'Sedan_car':
                Sedan_car()
            elif action == 'F1_car':
                F1_Car()
            elif action == 'Truck':
                Truck()
    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))
    smalltext = pygame.font.Font('freesansbold.ttf', 20)
    textsurf, textrect = text_objects(msg, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)
def garage():
    gamedisplays.fill(gray)
    gamedisplays.blit(garageImg1, (108, 300))
    gamedisplays.blit(garageImg2, (280, 300))
    gamedisplays.blit(garageImg3, (452, 300))
    gamedisplays.blit(garageImg4, (624, 300))
    gamedisplays.blit(garageImg5, (366, 100))
    Garage = True
    while Garage: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        button('F1 car', 91, 400, 100, 50, blue, lightblue, 'F1_car')  
        button('Coupe car', 262, 400, 100, 50, blue, lightblue, 'Coupe_car') 
        button('Sport car', 434, 400, 100, 50, blue, lightblue, 'Sport_car') 
        button('Sedan car', 606, 400, 100, 50, blue, lightblue, 'Sedan_car') 
        button('Truck', 348, 200, 100, 50, blue, lightblue, 'Truck')
def F1_Car():
    global carimg
    carimg = pygame.image.load('car1.png')
    countdown()
def Coupe_car():
    global carimg
    carimg = pygame.image.load('car2.png')
    countdown()
def Sport_car():
    global carimg
    carimg = pygame.image.load('car3.png')
    countdown()
def Sedan_car():
    global carimg
    carimg = pygame.image.load('car4.png')
    countdown()
def Truck():
    global carimg        
    carimg = pygame.image.load('truck1.png')
    countdown()
def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(introductionbackgroundpic, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 80)
        smalltext = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)
        textSurf, textRect = text_objects("Oh so cool! You have a car and your mission is to make sure the car", smalltext)
        ctextsurf, ctextrect = text_objects("doesn't collide with other cars. Sounds easy but don't be fooled.", smalltext)
        cctextsurf, cctextrect = text_objects("Each time you go one level higher, your speed increases and as a", smalltext)
        ccctextsurf, ccctextrect = text_objects("result, it becomes harder to control the car. But I'm sure", smalltext)
        cccctextsurf, cccctextrect = text_objects("you can get to the top. see you.", smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects('Introduction', largetext)
        TextRect.center = ((400), (100))
        ctextrect.center = ((350), (220))
        cctextrect.center = ((350), (240))
        ccctextrect.center = ((350), (260))
        cccctextrect.center = ((350), (280))
        gamedisplays.blit(TextSurf, TextRect)
        gamedisplays.blit(textSurf, textRect)
        gamedisplays.blit(ctextsurf, ctextrect)
        gamedisplays.blit(cctextsurf, cctextrect)
        gamedisplays.blit(ccctextsurf, ccctextrect)
        gamedisplays.blit(cccctextsurf, cccctextrect)
        stextSurf, stextRect = text_objects('Left turn = Left arrow', smalltext)
        stextRect.center = ((350), (400))
        hTextSurf, hTextRect = text_objects('Right turn = Right arrow', smalltext)
        hTextRect.center = ((600), (400))
        ptextSurf, ptextRect = text_objects('Pause = p', smalltext)
        ptextRect.center = ((150), (400))
        sTextSurf, sTextRect = text_objects('Controls', mediumtext)
        sTextRect.center = ((350), (320))
        gamedisplays.blit(sTextSurf, sTextRect)
        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(hTextSurf, hTextRect)
        gamedisplays.blit(ptextSurf, ptextRect)
        button('Back', 650, 540, 100, 50, blue, lightblue, 'menu')
        pygame.display.update()
        clock.tick(60)
def paused():
    global pause
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(introductionbackgroundpic, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('Paused', largetext)
        TextRect.center = ((displayw / 2), (displayh / 2))
        gamedisplays.blit(TextSurf, TextRect)
        button('Continue', 150, 450, 150, 50, green, lightgreen, 'unpaused')
        button('Restart', 350, 450, 150, 50, blue, lightblue, 'play')
        button('Main menu', 550, 450, 150, 50, red, lightred, 'menu')
        button('Garage', 350, 520, 150, 50, blue, lightblue, 'garage')
        pygame.display.update()
        clock.tick(60)
def unpaused():
    global pause
    pause = False
def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (displayw * 0.45)
    y = (displayh * 0.8)
    gamedisplays.blit(backgroundpic,(0, 0))
    gamedisplays.blit(backgroundpic,(700, 0))
    gamedisplays.blit(white_strip,(385, 10))
    gamedisplays.blit(white_strip,(385, 110))
    gamedisplays.blit(white_strip,(385, 210))
    gamedisplays.blit(white_strip,(385, 310))
    gamedisplays.blit(white_strip,(385, 410))
    gamedisplays.blit(white_strip,(385, 510))
    gamedisplays.blit(strip,(120, 0))
    gamedisplays.blit(strip,(664, 0)) 
    gamedisplays.blit(carimg,(x, y))
    text = font.render('Passed = 0', True, black)
    score = font.render('Score = 0', True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))
    button('Pause', 700, 0, 100, 50, blue, lightblue, 'paused')        
def countdown():
    countdown = True
    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('3', largetext)
        TextRect.center = ((displayw / 2), (displayh / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('2', largetext)
        TextRect.center = ((displayw / 2), (displayh / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)        
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('1', largetext)
        TextRect.center = ((displayw / 2), (displayh / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects('GO!!!!', largetext)
        TextRect.center = ((displayw / 2), (displayh / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)
        game_loop()
def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load('car5.png')
    elif obs == 1:
        obs_pic = pygame.image.load('car6.png')
    elif obs == 2:
        obs_pic = pygame.image.load('car7.png')
    elif obs == 3:
        obs_pic = pygame.image.load('car8.png')
    elif obs == 4:
        obs_pic = pygame.image.load('truck2.png')
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))
def score_system(passed, score):
    font = pygame.font.SysFont(None, 27)
    text = font.render('passed: ' + str(passed), True, white)
    score = font.render('score: ' + str(score), True, lightred)
    gamedisplays.blit(text, (2, 50))
    gamedisplays.blit(score, (2, 30))
def text_objects(text, font):
    textsurface = font.render(text, True, white)
    return textsurface, textsurface.get_rect()
def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 89)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((displayw / 2), (displayh / 2))
    gamedisplays.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(6)
    game_loop()
def crash():
    message_display('You crashed')
def background():
    gamedisplays.blit(backgroundpic,(0, 0))
    gamedisplays.blit(backgroundpic,(700, 0))
    gamedisplays.blit(white_strip,(385, 10))
    gamedisplays.blit(white_strip,(385, 110))
    gamedisplays.blit(white_strip,(385, 210))
    gamedisplays.blit(white_strip,(385, 310))
    gamedisplays.blit(white_strip,(385, 410))
    gamedisplays.blit(white_strip,(385, 510))
    gamedisplays.blit(strip,(120, 0))
    gamedisplays.blit(strip,(664, 0)) 
def car(x, y):
    gamedisplays.blit(carimg,(x, y))
def game_loop():
    global pause
    x = (displayw * 0.45)
    y = (displayh * 0.8)
    xchange = 0
    obstacle_speed = 10
    obs = 0
    ychange = 0
    obs_startx = random.randrange(200, (displayw - 200))
    obs_starty = -750
    obsw = 64
    obsh = 64
    passed = 0
    level = 0
    score = 0
    y2 = 10
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -5
                if event.key == pygame.K_p:
                    paused()
                if event.key == pygame.K_RIGHT:
                    xchange = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0                
        x += xchange
        pause = True
        gamedisplays.fill(gray)
        rel_y = y2 % backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
        if rel_y < 800:
            gamedisplays.blit(backgroundpic,(0, rel_y))
            gamedisplays.blit(backgroundpic,(700, rel_y))
            gamedisplays.blit(white_strip,(385, rel_y))
            gamedisplays.blit(white_strip,(385, rel_y + 100))
            gamedisplays.blit(white_strip,(385, rel_y + 200))
            gamedisplays.blit(white_strip,(385, rel_y + 300))
            gamedisplays.blit(white_strip,(385, rel_y + 400))
            gamedisplays.blit(white_strip,(385, rel_y + 500))
            gamedisplays.blit(white_strip,(385, rel_y - 100))
            gamedisplays.blit(strip,(120, 0))
            gamedisplays.blit(strip,(664, 0)) 
        y2 += obstacle_speed
        obs_starty -= obstacle_speed / 4
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x> 664 - car_width or x< 116:
            crash()
        if x > displayw - (car_width + 116) or x< 116:
            crash()
        if obs_starty > displayh:
            obs_starty = 0 - obsh
            obs_startx = random.randrange(170, (displayw - 170))
            obs = random.randrange(0, 4)
            passed = passed + 1
            score = passed * 10
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed += 2
                largetext = pygame.font.Font('freesansbold.ttf', 133)
                textsurf, textrect = text_objects('Level ' + str(level), largetext)
                textrect.center = ((displayw / 2), (displayh / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(2)
        if y < obs_starty + obsh:
            if x > obs_startx and x < obs_startx + obsw or x + car_width > obs_startx and x + car_width < obs_startx + obsw:
                crash()
        button('Pause', 700, 0, 100, 50, blue, lightblue, 'paused')
        pygame.display.update()
        clock.tick(60)
intro_loop()
countdown()
game_loop()
pygame.quit()
quit()
