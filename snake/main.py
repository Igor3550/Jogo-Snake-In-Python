import pygame
import snake

pygame.init()
screen = pygame.display.set_mode((800, 800))

bkg = pygame.Surface((800, 800))
bkg.fill((50, 50, 50))

play_image = pygame.image.load('assets/play.png')
comp = play_image.get_rect()
x = (comp[2]//2)
y = (comp[3]//2)
pos_img_x = (380-x)
pos_img_y = (350-y)
print(x, y)

sair = False
while not sair:

    pygame.display.update()
    screen.fill(0)

    screen.blit(bkg, (0, 0))
    screen.blit(play_image, (pos_img_x, pos_img_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sair = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pos_m_x = mouse_pos[0]
            pos_m_y = mouse_pos[1]
            if (292 < pos_m_x < 470) and (295 < pos_m_y < 405):
                print('mao na venta!')
                snake.init()
                pygame.quit()
                sair = True
