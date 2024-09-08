import pygame
from BOARD2 import Board

pygame.init()
WIDTH = 729 # 3^6 &
HEIGHT = 729 #&
CROSS_COLOR = (66, 66, 66) #&
CIRCLE_COLOR = (239, 231, 200) #&
test_font= pygame.font.Font(None,30)


class Game:

    def __init__(self, ultimate=False): #modo de juego
        self.ultimate = ultimate
        self.board = Board(ultimate=ultimate) #dibuja el tablero
        self.player = 1
        self.playing = True
        pygame.font.init()

    def render_board(self, surface):
        self.board.render(surface)

    def next_turn(self, screen):
        if self.player == 1:
            self.player = 2 
            text_surface = test_font.render("Turn O", False, "Black")
            
        else:
            self.player= 1
         
            text_surface = test_font.render("Turn X", False, "Black")
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 25))
        pygame.draw.rect(screen, (255, 255, 255), text_rect)
    # Dibujar el nuevo texto en la pantalla
        screen.blit(text_surface, text_rect.topleft)

        
    def ultimate_winner(self, surface, winner):
        print('ULTIMATE WINNER! ->', winner)

        if winner == 1:
            color = CROSS_COLOR
            # desc
            di = (WIDTH // 2 - 110, HEIGHT // 2 - 110)
            df = (WIDTH // 2 + 110, HEIGHT // 2 + 110)
            # asc
            d2i = (WIDTH // 2 - 110, HEIGHT // 2 + 110)
            d2f = (WIDTH // 2 + 110, HEIGHT // 2 - 110)
            # draw
            pygame.draw.line(surface, color, di, df, 22)
            pygame.draw.line(surface, color, d2i, d2f, 22)

        else:
            color = CIRCLE_COLOR
            # center
            center = (WIDTH // 2, HEIGHT // 2   )
            pygame.draw.circle(surface, color, center, WIDTH // 4, 22)
        
        font2= pygame.font.Font(None,50) 
        reincia= font2.render("Click R to restart", 1, color)
        reinciar_rect=reincia.get_rect(center=(729// 2, 25))
        pygame.draw.rect(surface, (28, 170, 156), reinciar_rect)
        surface.blit(reincia, reinciar_rect)
        font = pygame.font.SysFont('monospace', 64)
        gano = font.render('ULTIMATE WINNER!', 1, color)
        surface.blit(gano, (WIDTH // 2 - gano.get_rect().width // 2, HEIGHT // 2 + 220))
        

        self.playing = False #marca que se acabo el juego

    def restart(self):
        self.__init__(self.ultimate)