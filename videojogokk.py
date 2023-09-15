import pygame
from sys import exit
from random import randint

def mostrar_score():
    tempo = int(pygame.time.get_ticks() / 1000) - tempo_inicial
    texto_surface = teste_fonte.render(f'{tempo}', False, 'brown')
    texto_rect = texto_surface.get_rect(center = (400, 50))
    screen.blit(texto_surface, texto_rect)
    return tempo

def inimigos_movement(inimigos_list):
    if inimigos_list:
        for inimigos_rect in inimigos_list:
            inimigos_rect.x -= 5
            
            if inimigos_rect.bottom == 300:
                screen.blit(pudim_surface, inimigos_rect)
            else:
                screen.blit(macaron_surface, inimigos_rect)

        inimigos_list = [inimigos for inimigos in inimigos_list if inimigos.x > -100]

        return inimigos_list
    else:
        return []

def colisoes(player, obstaculo):
    if obstaculo:
        for inimigos_rect in obstaculo:
            if player.colliderect(inimigos_rect):
                return False
    return True

def player_animacao():
    global player_surface, player_index

    if player_rect.bottom < 300:
        player_surface = player_pulo
    else:
        player_index += 0.1
        if player_index >= len(player_andar): 
            player_index = 0
        player_surface = player_andar[int(player_index)]

# Inicia o Pygame:
pygame.init()
# Cria uma tela com os parâmetros (width, height):
screen = pygame.display.set_mode((800, 400))
# Define o nome do programa no display:
pygame.display.set_caption("Onodera's Confession")
# Cria uma variável que permite limitar o framerate máximo:
clock = pygame.time.Clock()
# Cria uma fonte com os parâmetros (fonte_padrão/'caminho_da_fonte_importada', tamanho_da_fonte):
teste_fonte = pygame.font.Font('font/Pixeltype.ttf', 50)
# Variável que determina que o jogo está ativo
jogo_ativo = False
tempo_inicial = 0
pontos = 0

# Cria uma variável surface (também pode ser de texto ou cor, mas com outros comandos):
ceu_surface = pygame.image.load('graphics/ceu.png').convert()
terra_surface = pygame.image.load('graphics/ground2.png').convert()

# Criando inimigos
# Pegue a imagem do inimigo e defina a posição inicial dele (definir posição agora é feito por função)
# Inimigo terrestre
pudim_andar_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
pudim_andar_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
pudim_andar = [pudim_andar_1,pudim_andar_2]
pudim_andar_index = 0
pudim_surface = pudim_andar[pudim_andar_index]

# Inimigo aéreo
macaron_andar_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
macaron_andar_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
macaron_andar = [macaron_andar_1,macaron_andar_2]
macaron_andar_index = 0
macaron_surface = macaron_andar[macaron_andar_index]

inimigos_rect_list = []

# Criando o player
player_andar_1 = pygame.image.load('graphics/Player/onodera_run_1.png').convert_alpha()
player_andar_2 = pygame.image.load('graphics/Player/onodera_run_2.png').convert_alpha()
player_pulo = pygame.image.load('graphics/Player/onodera_jump.png').convert_alpha()
#Configurações da animação
player_andar = [player_andar_1, player_andar_2]
player_index = 0
player_surface = player_andar[player_index]
# Ponha um retângulo ao redor de uma surface (parâmetros: esquerda, cima, largura, altura):
player_rect = player_surface.get_rect(midbottom = (200, 300))
# Variável para gravidade:
player_gravity = 0

#Para a tela inicial:
onodera = pygame.image.load('graphics/Player/onodera_jump.png').convert_alpha()
onodera = pygame.transform.rotozoom(onodera, 0, 2)
onodera_rect = onodera.get_rect(center = (400, 200))

titulo = teste_fonte.render("Onodera's Confession", False, 'brown')
titulo_rect = titulo.get_rect(center = (400, 70))

mensagem = teste_fonte.render("Press Space to start", False, 'brown')
mensagem_rect = mensagem.get_rect(center = (400, 330))

timer_obstaculo = pygame.USEREVENT + 1
pygame.time.set_timer(timer_obstaculo, 1500)

pudim_animacao_timer = pygame.USEREVENT + 2
pygame.time.set_timer(pudim_animacao_timer, 500)

macaron_animacao_timer = pygame.USEREVENT + 3
pygame.time.set_timer(macaron_animacao_timer, 200)

# Música
bg_soundtrack = pygame.mixer.Sound('audio/music.mp3')
bg_soundtrack.set_volume(0.9)
bg_soundtrack.play(loops = -1)

# Efeitos
som_de_pulo = pygame.mixer.Sound('audio/jump.mp3')
som_de_pulo.set_volume(0.5)

# While que impede o programa de fechar a menos que o usuário entre em um "evento de saída":
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if jogo_ativo:    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom >=300:
                    player_gravity = -20
                    som_de_pulo.play()

            # Se um botão estiver pressionado e ele for a barra de espaço, pulinho
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=300:
                    player_gravity = -20
                    som_de_pulo.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                jogo_ativo = True
                tempo_inicial = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.MOUSEBUTTONDOWN:
                jogo_ativo = True
                tempo_inicial = int(pygame.time.get_ticks() / 1000)

        if jogo_ativo:
            if event.type == timer_obstaculo:
                if randint(0,2):
                    inimigos_rect_list.append(pudim_surface.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    inimigos_rect_list.append(macaron_surface.get_rect(midbottom = (randint(900, 1100), 210)))

            if event.type == pudim_animacao_timer:
                if pudim_andar_index == 0: pudim_andar_index = 1
                else: pudim_andar_index = 0
                pudim_surface = pudim_andar[pudim_andar_index]

            if event.type == macaron_animacao_timer:
                if macaron_andar_index == 0: macaron_andar_index = 1
                else: macaron_andar_index = 0
                macaron_surface = macaron_andar[macaron_andar_index]

    if jogo_ativo:
        # Copia o conteúdo de uma surface pra outra (como colocar elementos visuais no display)
        # A ordem dos screen.blit afeta a "layer" em que as surfaces serão apresentadas
        # Os parâmetros são (nome_da_variavel_surface, (posição x, posição y)):
        screen.blit(ceu_surface, (0, 0))
        screen.blit(terra_surface, (0, 300))
        pontos = mostrar_score()

        # Gravidade :0
        player_gravity += 1
        player_rect.y += player_gravity
        # Cria um limite de onde o player pode chegar (barra a gravidade):
        if player_rect.bottom >=300:
            player_rect.bottom = 300
        # Roda a animação
        player_animacao()
        # Junta duas variáveis:
        screen.blit(player_surface, player_rect)

        # Movimento dos inimigos
        inimigos_rect_list = inimigos_movement(inimigos_rect_list)

        jogo_ativo = colisoes(player_rect, inimigos_rect_list)

    else:
        screen.fill("Pink")
        screen.blit(onodera, onodera_rect)
        inimigos_rect_list.clear()
        player_rect.midbottom = (200, 300)
        player_gravity = 0

        pontos_msg = teste_fonte.render(f'Total de pontos: {pontos}', False, 'brown')
        pontos_msg_rect = pontos_msg.get_rect(center = (400, 330))
        screen.blit(titulo, titulo_rect)
        if pontos == 0:
            screen.blit(mensagem, mensagem_rect)
        else:
            screen.blit(pontos_msg, pontos_msg_rect)

    # Atualiza a tela e mostra as atualizações que acontecem nela:
    pygame.display.update()
    # Limita o framerate máximo em 60fps
    clock.tick(60)