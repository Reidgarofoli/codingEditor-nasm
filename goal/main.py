import pygame, sys

try:
    fileName = sys.argv[1]
except:
    print("You need to enter a command line argument of the name of the file")
    exit(1)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pygame.init()

screen = pygame.display.set_mode((500,500))

# Set the text color
text_color = (125, 125, 125)

pygame.font.init()
fontSize = 30
my_font = pygame.font.SysFont('Arial', fontSize)
lines = open(fileName, "r").readlines()

cursorX = 0
cursorY = 0
cursor_num = 0

clock = pygame.time.Clock()

import time

frame_cap = 1.0/60
time_1 = time.perf_counter()
unprocessed = 0

keys = "`1234567890-=~!@#$%^&*()_+qwertyuiop[]\asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘åß∂ƒ©˙∆˚¬…æ≈ç√∫˜µ≤≥÷≈ç√∫˜µ≤≥÷Œ„´‰ˇÁ¨Ø∏”’»"
running = True
while running:
    can_render = False
    time_2 = time.perf_counter()
    passed = time_2 - time_1
    unprocessed += passed
    time_1 = time_2

    while(unprocessed >= frame_cap):
        unprocessed -= frame_cap
        can_render = True

    if can_render:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_KP_ENTER:
                    lines += []
                elif event.key == pygame.K_EQUALS:
                    fontSize += 1
                    my_font = pygame.font.SysFont('Arial', fontSize)
                elif event.key == pygame.K_MINUS:
                    fontSize -= 1
                    my_font = pygame.font.SysFont('Arial', fontSize)
                elif event.key == pygame.K_LEFT:
                    cursorX -= 1
                    if cursorX < 0:
                        cursorY -= 1
                        cursorX = len(lines[cursorY])
                elif event.key == pygame.K_UP:
                    cursorY -= 1
                    if cursorY < 0:
                        cursorY = 0
                elif event.key == pygame.K_RIGHT:
                    cursorX += 1
                    if cursorX > len(lines[cursorY]):
                        cursorY += 1
                        cursorX = 0
                elif event.key == pygame.K_DOWN:
                    cursorY += 1
                    if cursorY >= len(lines):
                        cursorY = len(lines)-1
                    elif cursorX >= len(lines[cursorY]):
                        cursorX = len(lines[cursorY])
                elif event.key == pygame.K_BACKSPACE:
                    if cursorX != 0:
                        lines[cursorY] = lines[cursorY][:cursorX-1] + lines[cursorY][cursorX:]
                        cursorX -= 1
                elif event.key == pygame.K_SPACE:
                    lines[cursorY] = lines[cursorY][:cursorX] + " " + lines[cursorY][cursorX:]
                    cursorX += 1
                else:
                    try:
                        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                            lines[cursorY] = lines[cursorY][:cursorX] + chr(event.key).upper() + lines[cursorY][cursorX:]
                            cursorX += 1
                        else:
                            lines[cursorY] = lines[cursorY][:cursorX] + chr(event.key) + lines[cursorY][cursorX:]
                            cursorX += 1
                    except:
                        pass

        # draw text on the screen
        for line in range(len(lines)):
            text_surface = my_font.render(str(line)+"| " + lines[line].replace("\n", ""), False, text_color)
            screen.blit(text_surface, (0,line * text_surface.get_height()))
        
        # draw cursor
        cursor_num += 1
        if cursor_num % 6 <= 3:
            cursor_num = 0
            cursor_surface = my_font.render("|", False, text_color)
            text_surface = my_font.render(str(line)+"| " + lines[cursorY].replace("\n", "")[:cursorX], False, text_color)
            screen.blit(cursor_surface, (text_surface.get_width()-5, text_surface.get_height() * cursorY))

        print(lines)
        pygame.display.flip()
        screen.fill((0,0,0))