import pygame
import snake

# 520, 530  560, 570
pygame.init()
screen = pygame.display.set_mode((800, 800))

bkg = pygame.Surface((800, 800))
bkg.fill((50, 50, 50))

cores = [
    (255, 255, 255),
    (5, 155, 255),
    (255, 159, 64),
    (255, 62, 62),
    (113, 255, 113)
]

id_cor = 0

play_image = pygame.image.load('assets/backInicio.png')

ex = pygame.Surface((83, 21))
ex.fill(cores[id_cor])

pos_img_x = 0
pos_img_y = 0

sair = False
while not sair:

    pygame.display.update()
    screen.fill(0)

    screen.blit(bkg, (0, 0))
    screen.blit(play_image, (pos_img_x, pos_img_y))
    screen.blit(ex, (365, 533))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sair = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pos_m_x = mouse_pos[0]
            pos_m_y = mouse_pos[1]
            if (292 < pos_m_x < 470) and (295 < pos_m_y < 405):
                snake.init(cores[id_cor])
                pygame.quit()
                sair = True
            if (520 < pos_m_x < 560) and (530 < pos_m_y < 570):
                max_c = len(cores)-1
                if id_cor+1 > max_c:
                    id_cor = 0
                else:
                    id_cor += 1
                ex.fill(cores[id_cor])
