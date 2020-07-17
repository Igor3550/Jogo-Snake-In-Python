# importando as blibiotecas usadas
from random import randint  # biblioteca para gerar valores aleatorios
from time import sleep  # lib para dar um tempo na execução

import pygame  # biblioteca para janela e objetos e tudo mais
import sys  # biblioteca do systema

atual_state = 0
snake = object
apple = object


def init(cor=(255, 255, 255)):
    global atual_state
    global snake
    global apple

    # definindo os objetos
    class Apple:  # atribuições e funções do objeto 'Apple'
        def __init__(self):
            self.body = pygame.Surface((10, 10))
            self.body.fill((255, 0, 0))
            self.pos = self.new_pos()

        def new_pos(self):  # retornar uma nova posição
            self.pos = (randint(20, 780), randint(20, 780))
            self.pos = ((self.pos[0] // 10) * 10, (self.pos[1] // 10) * 10)
            return self.pos

        def draw(self, collided=False):  # desenhar a 'Apple'
            if collided:  # se colidiu desenhar em uma nova posição
                self.pos = self.new_pos()
                snake.pos.append((snake.pos[-1][0], snake.pos[-1][1]))
            screen.blit(self.body, self.pos)

    class Snake:  # atribuições e funções do objeto 'Snake'
        def __init__(self):
            self.body = pygame.Surface((10, 10))
            self.body.fill(cor)
            self.pos = [(300, 300), (310, 300), (320, 300)]
            self.direct = 1

        def draw(self):  # desenhar na tela

            for pos in self.pos:
                screen.blit(self.body, pos)

        def move(self, direct):  # mudar a direção da 'Snake'
            if direct == RIGHT:  # direita
                if self.direct == LEFT:  # se a direção anterior for 'esquerda' ele inverte as posições de cada segmento
                    self.pos.sort(reverse=True)
                    self.direct = 1
                else:
                    self.pos[0] = (self.pos[0][0] + 10, self.pos[0][1])
                    self.direct = 1
            if direct == LEFT:
                if self.direct == RIGHT:
                    self.pos.sort()
                    self.direct = 3
                else:
                    self.pos[0] = (self.pos[0][0] - 10, self.pos[0][1])
                    self.direct = 3
            if direct == UP:
                if self.direct == DOWN:
                    self.pos.sort()
                    self.direct = 0
                else:
                    self.pos[0] = (self.pos[0][0], self.pos[0][1] - 10)
                    self.direct = 0
            if direct == DOWN:
                if self.direct == UP:  # se a direção anterior for 'para cima' ele inverte as posições de cada segmento
                    self.pos.sort(reverse=True)
                    self.direct = 2
                else:
                    self.pos[0] = (self.pos[0][0], self.pos[0][1] + 10)
                    self.direct = 2
            for p in range(len(self.pos) - 1, 0, -1):
                self.pos[p] = (self.pos[p - 1][0], self.pos[p - 1][1])

    def desenha_espera_iniciar():  # desenhando a tela de espera para iniciar
        score = pygame.Rect(5, 5, 100, 100)
        score_surface = pygame.Surface((110, 110))
        score_surface.fill((50, 50, 50))

        pygame.draw.rect(score_surface, (0, 50, 200), score)
        screen.blit(texto, pos_texto)
        screen.blit(score_surface, (350, 350))

    def desenha_espera_perdeu(pon=0):  # desenhando a tela de espera para recomeçar quando perde
        score_font = pygame.font.SysFont('arial black', 15)
        ponts_text = str(pon)
        score_text1 = score_font.render('Pontuação:', True, (50, 50, 50))
        score_text2 = score_font.render(ponts_text, True, (50, 50, 50))
        score_text3 = score_font.render('Recorde:', True, (50, 50, 50))
        score_text4 = score_font.render(str(record), True, (50, 50, 50))
        score = pygame.Rect(5, 5, 100, 100)
        score_surface = pygame.Surface((110, 110))
        score_surface.fill((50, 50, 50))
        pygame.draw.rect(score_surface, (0, 50, 200), score)
        screen.blit(texto, pos_texto)
        screen.blit(perde_text, (275, 225))
        score_surface.blit(score_text1, (8, 5))
        score_surface.blit(score_text2, (50, 25))
        score_surface.blit(score_text3, (18, 50))
        score_surface.blit(score_text4, (50, 70))

        screen.blit(score_surface, (350, 350))

    def espera(pon=0, pontuacao=False, perd=False):  # desenha a 'Snake' se movimentando só
        global atual_state
        if perd:  # se tiver pedido da um tempo antes de mudar de tela
            atual_state = verify(atual_state)

        if pontuacao:  # mostrar ou não a pontuação e o recorde
            desenha_espera_perdeu(pon)
        else:
            desenha_espera_iniciar()

        # pegar a posição do primeiro segmento
        (x, y) = (snake.pos[-1][0], snake.pos[-1][1])

        # definindo pontos de colisão para mudar a direção
        p1 = (580, 300)
        p2 = (600, 580)
        p3 = (220, 600)
        p4 = (200, 220)
        p5 = (580, 200)

        direc = snake.direct  # direção atual
        snake.move(direc)  # mover na direção atual

        # alterando a direção se colidir em algum ponto de colisão
        if (x, y) == p1:
            snake.move(DOWN)
        if (x, y) == p2:
            snake.move(LEFT)
        if (x, y) == p3:
            snake.move(UP)
        if (x, y) == p4:
            snake.move(RIGHT)
        if (x, y) == p5:
            snake.move(DOWN)

    def jogando():  # mudar a direção de acordo com a tecla pressionada
        direct = snake.direct  # direção atual
        comandos = pygame.key.get_pressed()  # pegar qual tecla foi pressionada

        # alterando a direção
        if comandos[pygame.K_UP]:
            direct = UP
        if comandos[pygame.K_DOWN]:
            direct = DOWN
        if comandos[pygame.K_RIGHT]:
            direct = RIGHT
        if comandos[pygame.K_LEFT]:
            direct = LEFT

        snake.move(direct)  # chama a função '.move' do objeto alterando a direção

    def perdeu(p=0):  # reinicianndo todos os objetos
        global snake
        global apple
        apple = Apple()
        snake = Snake()
        espera(p, True)

    def verify(state):  # verificar: se perdeu da um tempo antes de reiniciar
        if state == states['PERDEU']:
            c = 0
            while c < 2:
                sleep(1)
                c += 1
            state = states['JOGAR']
        elif state == states['JOGAR']:
            state = states['JOGANDO']
        return state

    # função para tocar um audio
    def audio(som):
        if som == sound['espera']:
            som.set_volume(0.2)
            som.play()
        else:
            som.set_volume(1)
            som.play()

    # Iniciando código principal

    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption('Snake')

    # definindo estados do jogo
    states = {
        'JOGAR': 0,
        'JOGANDO': 1,
        'PERDEU': 2
    }

    # definindo alguns textos
    textos = {
        'Iniciar': 'Pressione as setas para iniciar!',
        'Perdeu': 'Perdeu playboy!'
    }
    # definindo alguns titulos de sons
    sound = {
        'espera': pygame.mixer.Sound('assets/ini.wav'),
        'perdeu': pygame.mixer.Sound('assets/perdeu.wav'),
        'ponto': pygame.mixer.Sound('assets/ponto.wav')
    }

    # configurando fontes e textos
    font = pygame.font.SysFont('arial black', 20)
    texto = font.render(textos['Iniciar'], True, (50, 50, 50), (0, 0, 0))
    perde_text = font.render(textos['Perdeu'], True, (50, 50, 50), (0, 0, 0))
    pos_texto = texto.get_rect()
    pos_texto = 235, 250

    # variáveis de controle
    pontos = 0
    ponts = 0
    record = 0
    som_espera = True
    perde = False

    # definindo o estado atual
    atual_state = states['JOGAR']

    # definindo as direções
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    # definindo os objetos
    snake = Snake()
    apple = Apple()

    fps = pygame.time.Clock()  # variável para definir os frames por segundo
    FPS = 20
    sair = False  # variável de controle para encerrar

    # loop principal do game
    while not sair:

        fps.tick(FPS)  # configurando o FPS

        pygame.display.update()  # atualizando a tela a cada frame
        screen.fill(0)  # limpando a tela a cada frame

        snake.draw()  # desenha a snake

        # estado espera
        if atual_state == states['JOGAR']:  # estado de espera para iniciar ou recomeçar
            if perde:  # muda a tela de espera
                espera(ponts, True)
            else:
                espera()

            if som_espera:
                audio(sound['espera'])
                som_espera = False

            for event in pygame.event.get():  # verificar se alguma tecla foi pressionada
                if event.type == pygame.QUIT:  # se o evento foi de sair o jogo encerra
                    sair = True
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  # se alguma tecla foi pressionada muda o estado de jogo
                    atual_state = states['JOGANDO']

        # estado perdeu
        elif atual_state == states['PERDEU']:  # muda a tela para a tela de espera quando perder
            audio(sound['perdeu'])
            som_espera = True
            espera(perd=True)
            perde = True  # quando perder pela primeira vez muda a tela de espera
            ponts = pontos  # 'pontos' zera toda vez que perde 'ponts' é enviada para ser mostrada na tela

            if ponts > record:  # se 'ponts' for maior que 'record' então ele recebe o valor de 'ponts'
                record = ponts

            perdeu(ponts)
            pontos = 0

        # estado jogando
        elif atual_state == states['JOGANDO']:

            jogando()
            apple.draw()
            snake_head = snake.pos[0]  # definido o primeiro segmento

            # definindo colisões
            if snake_head[0] < 0 or snake_head[0] >= 800:  # se colidiu com as paredes verticais (esquerda e direita)
                atual_state = states['PERDEU']
            if snake_head[1] < 0 or snake_head[1] >= 800:  # se colidiu com as paredes horizontais (cima e baixo)
                atual_state = states['PERDEU']

            if snake.pos[0] == apple.pos:  # colisão com a 'Apple'
                pontos += 1  # adiciona um novo ponto
                audio(sound['ponto'])
                apple.draw(True)  # desenha a 'apple' em uma nova posição

            for i in range(len(snake.pos) - 1, 1, -1):  # verificar colisão com o próprio 'corpo' da snake
                if snake.pos[0] == snake.pos[i]:
                    atual_state = states['PERDEU']

        # verificar evento de encerrar o jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sair = True
