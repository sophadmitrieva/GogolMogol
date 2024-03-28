import pygame

pygame.init()

display_width = 800
display_height = 400

display = pygame.display.set_mode((display_width, display_height))
background = pygame.image.load("fon.png")

pygame.display.set_caption("GogolMogol")
pygame.display.set_icon(pygame.image.load("gogol.png"))

gogol_width = 120  # Gogol without water
gogol_height = 225
just_gogol = pygame.image.load("gogol.png")

gogol_close = pygame.image.load("Gogol_close.png")  # Gogol without water and  with closed eyes
gogol_close_water = pygame.image.load("Gogol_close_water.png")  # with water and closed eyes
gogol_water_open = pygame.image.load("Gogol_water_open.png")  # with water and opened eyes

current_image = just_gogol
current_coordinates = current_image.get_rect(center=(gogol_width, gogol_height))  # what I see now

mops_height = 450
mops_width = 350
speed_mops = mops_height - 300
mops = pygame.image.load("mops.png")
mops_rect = mops.get_rect(center=(mops_width, mops_height))
needed_click = 0  # Один клик для мопса

mops_lapa = pygame.image.load("lapa.png")
lapa_width = 200
lapa_height = 450

cursor = pygame.image.load("cursor_img.png")
cursor_img = cursor
pygame.mouse.set_visible(False)
cursor_img_rect = cursor_img.get_rect()

square = pygame.image.load("square.png")
speed_square = 1
square_hover = pygame.image.load("square_hold.png")
directions = True #change the direction of the square

FONT = pygame.font.Font("FORTEXTS.ttf", 20)
text = FONT.render('Press left mouse button bro', True, (198, 156, 219))

game = True
press_button = True
animation_done = False

GOGOL_EVENT = pygame.USEREVENT + 1  # timer
GOGOL_EVENT_2 = pygame.USEREVENT + 2
LAPA_EVENT = pygame.USEREVENT + 3
MOPS_EVENT = pygame.USEREVENT + 4
timer1_works = True
game_begining = False

while game:
    display.blit(background, (0, 0))

    if game_begining:
        cursor_img = square

    display.blit(current_image, current_coordinates)

    mops_rect = mops.get_rect(center=(mops_width, mops_height))
    display.blit(mops, mops_rect)

    mops_lapa_rect = mops_lapa.get_rect(center=(lapa_width, lapa_height))
    display.blit(mops_lapa, mops_lapa_rect)

    cursor_img_rect.center = pygame.mouse.get_pos()  # update position mouse
    display.blit(cursor_img, cursor_img_rect)

    if press_button:
        display.blit(text, (display_width // 4, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if mops_height > 250 and needed_click == 0:
                mops_height -= speed_mops
                needed_click += 1
                press_button = False
            elif lapa_height > 250 and needed_click == 1:
                lapa_height -= speed_mops
                needed_click += 1
            elif needed_click == 2:
                lapa_height -= 20
                lapa_width -= 110
                needed_click += 1
                pygame.time.set_timer(LAPA_EVENT, 3500)
                pygame.time.set_timer(MOPS_EVENT, 5000)

            if needed_click == 3:
                current_image = gogol_close
                pygame.time.set_timer(GOGOL_EVENT, 1500)

        if event.type == GOGOL_EVENT:
            current_image = gogol_close_water
            pygame.time.set_timer(GOGOL_EVENT_2, 1500)

        if event.type == GOGOL_EVENT_2:
            current_image = gogol_water_open # ???

        if event.type == LAPA_EVENT:
            lapa_height += 150
            lapa_width += 3000

        if event.type == MOPS_EVENT:
            mops_height = 500
            mops_width = 600
            game_begining = True

    pygame.display.flip()

    pygame.display.update()
