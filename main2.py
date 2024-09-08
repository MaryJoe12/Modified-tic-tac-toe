import pygame
import sys
from BOARD2 import *
from game2 import Game

pygame.init()
#constantes
WIDTH = 729 # 3^6 &
HEIGHT = 729 #&
BG_COLOR = (28, 170, 156) #verde
test_font= pygame.font.Font(None,30) #escribir, tamaño 30
test_font2= pygame.font.Font(None,50) #escribir, tamaño 50

class Main:

    def __init__(self):
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) ) #display
        pygame.display.set_caption('TIC TAC TOE') #titulo de la pagina
        self.game = Game(ultimate=True) #tipo de juego #llamando clase de game2

    def mainloop(self):

        screen = self.screen
        game = self.game
        screen.fill( BG_COLOR ) #colorear todo de verde
        game.render_board(screen) #llamar a la función del archivo game2 el render_board
        #el anuncio de turno
        text_surface = test_font.render("Turn X", False, "Black")
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 25))
        pygame.draw.rect(screen, (255, 255, 255), text_rect)  #blanco
        screen.blit(text_surface, text_rect.topleft)
        pygame.display.update()

        while True:

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN and game.playing:
                    xclick, yclick = event.pos  #posición del mouse

                    if game.board.valid_sqr(xclick, yclick): #se va al board2. Si es valida la casilla prosigue
                        game.board.mark_sqr(xclick, yclick, game.player)#para poner que la casilla es de x jugador, no se puede poner en el de arriba porque tiene llamada recursiva
                        game.board.draw_fig(screen, xclick, yclick) #dibujamos el simbolito
                        game.board.prueba(screen) 

                        # se gano todo el juego
                        winner = game.board.check_draw_win(screen) 
                        
                        if winner: #si hay numerito es verdadero
                            game.board.manage_win(screen, winner, tablero=True)# todo el tablero 
                            game.ultimate_winner(screen, winner)
                            

                        else:
                            game.next_turn(screen)

                # keypress
                if event.type == pygame.KEYDOWN: #presionar la r para reinciar
                    if event.key == pygame.K_r:
                        game.restart()
                        self.screen.fill( BG_COLOR )
                        game.render_board(screen)
                        game.playing=True
                        main.mainloop()

                # quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
        
            pygame.display.update()
      

gameon=False
main = Main()
main.screen.fill((255, 255, 255)) #color blanco
try:
    f=open("inicio.txt", "r") #lector de archivo
    a=f.read()
    bien= test_font2.render(str(a), False, "Black")
finally:
  if f:
    f.close()
bienvenido=test_font2.render("Click space to start",  False, "Black")
bien_rect=bien.get_rect(center=(340,250))
bienvenido_rect= bienvenido.get_rect(center=(340,330))
main.screen.blit(bien,bien_rect)
main.screen.blit(bienvenido, bienvenido_rect)
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            gameon= True
        if gameon:
            main.mainloop()
        if event.type == pygame.QUIT: #cerrar el codigo
            pygame.quit()
            sys.exit()
