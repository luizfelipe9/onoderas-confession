    #if player_rect.colliderect(lesma_rect):
    #    print ("BRUH")

    #mouse_pos = pygame.mouse.get_pos()

    #if player_rect.collidepoint((mouse_pos)):
    #    print (pygame.mouse.get_pressed())

#-----------------------------------------------------------

#pygame.draw.rect(screen, 'Pink', texto_rect)
#pygame.draw.rect(screen, 'Pink', texto_rect, 10)
#screen.blit(texto_surface, texto_rect)

#-----------------------------------------------------------

# Cria uma surface de texto com os parâmetros (Texto, anti-aliasing - não use em pixel art -, cor)
#texto_surface = teste_fonte.render('(=UwU=)', False, 'brown')
#texto_rect = texto_surface.get_rect(center = (400, 50))

#-----------------------------------------------------------

# if(lesma_rect.right <= 0):
#     lesma_rect.left = 800
# # Puxa a posição inicial da lesma e diminui a posição dela em 1 para a lesma andar sozinha
# lesma_rect.x -= 5
# screen.blit(lesma_surface, lesma_rect)