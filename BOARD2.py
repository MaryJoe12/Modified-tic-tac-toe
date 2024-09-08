import pygame
class BoardDim: 

    def __init__(self, size, xcor, ycor):
        self.size = size
        self.sqsize = size // DIM  #tamaño de cuadrado
        self.xcor = xcor
        self.ycor = ycor

WIDTH = 729 # 3^6 &
LINE_COLOR = (23, 145, 135) #&
CROSS_COLOR = (66, 66, 66) #& black
CIRCLE_COLOR = (239, 231, 200) #&
FADE = (28, 170, 156) #&
ALPHA = 100 #&
DIM = 3 #&

class Board:

    def __init__(self, dims=None, linewidth=15, ultimate=False): #listo
        self.squares = [ [0, 0, 0] for row in range(DIM)] #se hace la matriz
        self.dims = dims

        if not dims: #dimensiones
            self.dims = BoardDim(WIDTH, 0, 0)

        self.linewidth = linewidth
        self.offset = self.dims.sqsize * 0.2  #desplazar o ajustar la posición de un objeto o superficie en una pantalla. En otras palabras, es un valor que se suma a las coordenadas (x, y) de un objeto para cambiar su posición en la pantalla. 
        self.radius = (self.dims.sqsize // 2) * 0.7

        if ultimate: 
            self.create_ultimate()

        self.sepuedejugar = True


    def create_ultimate(self): #listo
        for row in range(DIM):
            for col in range(DIM):

                size = self.dims.sqsize
                xcor, ycor = self.dims.xcor + (col * self.dims.sqsize), self.dims.ycor + (row * self.dims.sqsize)
                dims = BoardDim(size=size, xcor=xcor, ycor=ycor)
                linewidth = self.linewidth - 7

                self.squares[row][col] = Board(dims=dims, linewidth=linewidth, ultimate=False)
    
    def render(self, surface):
        for row in range(DIM):
            for col in range(DIM):
                sqr = self.squares[row][col]

                if isinstance(sqr, Board): sqr.render(surface)
        
        # vertical lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.sqsize, self.dims.ycor),                  (self.dims.xcor + self.dims.sqsize, self.dims.ycor + self.dims.size), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor), (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor + self.dims.size), self.linewidth)
        
        # horizontal lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.sqsize),                  (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.sqsize), self.linewidth)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.size - self.dims.sqsize), (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.size - self.dims.sqsize), self.linewidth)

    def valid_sqr(self, xclick, yclick): #listo

        row = yclick // self.dims.sqsize
        col = xclick // self.dims.sqsize

        if row > 2: row %= DIM #residuo de la división
        if col > 2: col %= DIM

        sqr = self.squares[row][col] #que cuadro se va a marcar

        # base case
        if not isinstance(sqr, Board): #no es valida la casilla
            return sqr == 0 and self.sepuedejugar #significa que si es valida, da la señal de que si se puede

        # regresa que si es valida o que no lo es 
        return sqr.valid_sqr(xclick, yclick)

    def mark_sqr(self, xclick, yclick, player):
         row = yclick // self.dims.sqsize
         col = xclick // self.dims.sqsize

         if row > 2: row %= DIM
         if col > 2: col %= DIM

         sqr = self.squares[row][col]

         print('marking -> (', row, col, ')')

         # base case
         if not isinstance(sqr, Board):
             self.squares[row][col] = player
             return

         # recursive step
         sqr.mark_sqr(xclick, yclick, player)

    def draw_fig(self, surface, xclick, yclick):
         linewidth2=8
         row = yclick // self.dims.sqsize
         col = xclick // self.dims.sqsize

         if row > 2: row %= DIM
         if col > 2: col %= DIM

         sqr = self.squares[row][col]

         # base case
         if not isinstance(sqr, Board):

             # cross
             if sqr == 1:
                 # desc line
                 d1 = (self.dims.xcor + (col * self.dims.sqsize) + self.offset, 
                         self.dims.ycor + (row * self.dims.sqsize) + self.offset)
                 d2 = (self.dims.xcor + self.dims.sqsize * (1 + col) - self.offset, 
                         self.dims.ycor + self.dims.sqsize * (1 + row) - self.offset)
                 pygame.draw.line(surface, CROSS_COLOR, d1, d2, linewidth2)

                 # asc line
                 d1 = (self.dims.xcor + (col * self.dims.sqsize) + self.offset, 
                         self.dims.ycor + self.dims.sqsize * (1 + row) - self.offset)
                 d2 = (self.dims.xcor + self.dims.sqsize * (1 + col) - self.offset, 
                         self.dims.ycor + (row * self.dims.sqsize) + self.offset)
                 pygame.draw.line(surface, CROSS_COLOR, d1, d2, linewidth2)
             
             # circle
             elif sqr == 2:
                 center = (self.dims.xcor + self.dims.sqsize * (0.5 + col),
                           self.dims.ycor + self.dims.sqsize * (0.5 + row))

                 pygame.draw.circle(surface, CIRCLE_COLOR, center, self.radius, linewidth2)

             return

         # recursive step
         sqr.draw_fig(surface, xclick, yclick) #llamamos a la función para por si no llego a la casilla correcta ahora si llegue
        #se pone sqr para indicar que el que queremos marcar es el sqr escogido
        #llamada recursiva, en otras palabras llamar la función hasta que llegue al valor que queremos como un while.

    def manage_win(self, surface, winner, tablero=False): #qué se hace cuando gana alguien. Usamos las casillas no todo el tablero ya que tablero=False
        # blureamos el cuadro
        blur = pygame.Surface( (self.dims.size, self.dims.size) )
        blur.set_alpha( ALPHA )
        blur.fill( FADE )
        if tablero: #si hablamos de todo el tablero
            surface.blit(blur, (self.dims.xcor, self.dims.ycor))
            surface.blit(blur, (self.dims.xcor, self.dims.ycor))
            surface.blit(blur, (self.dims.xcor, self.dims.ycor)) 
        
        # dibujamos al ganador win
        if not tablero:
            # cross
            if winner == 1:
                # desc line
                #offset es para ajustar los valores
                d1= (self.dims.xcor + self.offset, 
                        self.dims.ycor + self.offset)
                d2 = (self.dims.xcor + self.dims.size - self.offset, 
                        self.dims.ycor + self.dims.size - self.offset)
                pygame.draw.line(surface, CROSS_COLOR, d1, d2, self.linewidth + 7)

                # asc line
                d1 = (self.dims.xcor + self.offset, 
                        self.dims.ycor + self.dims.size - self.offset)
                d2 = (self.dims.xcor + self.dims.size - self.offset, 
                        self.dims.ycor + self.offset)
                pygame.draw.line(surface, CROSS_COLOR, d1, d2, self.linewidth + 7)

            # circle
            if winner == 2:
                center = (self.dims.xcor + self.dims.size * 0.5,
                        self.dims.ycor + self.dims.size * 0.5)

                pygame.draw.circle(surface, CIRCLE_COLOR, center, self.dims.size * 0.4, self.linewidth + 7)

        # ya no se puede usar esa casilla
        self.sepuedejugar = False

    def check_draw_win(self, surface,): #ganaste o no la subcasilla. 
        #conseguimos la ubi de la matriz
        for row in range(DIM):
            for col in range(DIM):

                # de que cuadrito estamos hablando                   
                sqr = self.squares[row][col]

                if isinstance(sqr, Board) and sqr.sepuedejugar: #el cuadrito no esta apagado y los cuadritos existen en los tableros internos
                    winner = sqr.check_draw_win(surface) #lo vuelve a llamar hasta que saca algo
                    if winner: #cuando gana alguien
                        print("q")
                        self.squares[row][col] = winner
                        sqr.manage_win(surface, winner) #le mandamos quién gano

                # vertical wins
                for c in range(DIM):
                    if self.squares[0][c] == self.squares[1][c] == self.squares[2][c] != 0:
                        color = CROSS_COLOR if self.squares[0][c] == 1 else CIRCLE_COLOR
                        # draw win
                        d1 = (self.dims.xcor + self.dims.sqsize * (0.5 + c), 
                                self.dims.ycor + self.offset)
                        d2 = (self.dims.xcor + self.dims.sqsize * (0.5 + c), 
                                self.dims.ycor + self.dims.size - self.offset)
                        pygame.draw.line(surface, color, d1, d2, self.linewidth)

                        return self.squares[0][c]

                # horizontal wins
                for r in range(DIM):
                    if self.squares[r][0] == self.squares[r][1] == self.squares[r][2] != 0:
                        color = CROSS_COLOR if self.squares[r][0] == 1 else CIRCLE_COLOR
                        # draw win
                        d1 = (self.dims.xcor + self.offset, 
                                self.dims.ycor + self.dims.sqsize * (r + 0.5))
                        d2 = (self.dims.xcor + self.dims.size - self.offset, 
                                self.dims.ycor + self.dims.sqsize * (r + 0.5))
                        pygame.draw.line(surface, color, d1, d2, self.linewidth)

                        return self.squares[r][0]

                # diagonal wins
                # desc
                if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
                    color = CROSS_COLOR if self.squares[1][1] == 1 else CIRCLE_COLOR
                    # draw win
                    d1 = (self.dims.xcor + self.offset, 
                            self.dims.ycor + self.offset)
                    d2 = (self.dims.xcor + self.dims.size - self.offset, 
                            self.dims.ycor + self.dims.size - self.offset)
                    pygame.draw.line(surface, color, d1, d2, self.linewidth)

                    return self.squares[1][1]

                # asc
                if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
                    color = CROSS_COLOR if self.squares[1][1] == 1 else CIRCLE_COLOR
                    # draw win
                    d1 = (self.dims.xcor + self.offset, 
                            self.dims.ycor + self.dims.size - self.offset)
                    d2 = (self.dims.xcor + self.dims.size - self.offset, 
                            self.dims.ycor + self.offset)
                    pygame.draw.line(surface, color, d1, d2, self.linewidth)

                    return self.squares[1][1]

    def prueba(self, surface): #valida que se lleno 1 primer cuadro
     for row in range(DIM):
         for col in range(DIM):
             sqr = self.squares[row][col]
             if isinstance(sqr, Board) and sqr.sepuedejugar:
                winner = sqr.check_draw_win(surface)
                if winner:
                    self.squares[row][col] = winner
                    sqr.manage_win(surface, winner)
                    
                else:
                    # Check if the sub-board is full
                    if all(cell != 0 for row in sqr.squares for cell in row): # Sub-board is full
                        self.reset_board(row, col,surface, sqr)
                        
    def reset_board(self, row, col, surface, sqr):
        #reiniciar variables
        self.squares[row][col] = Board(dims=BoardDim(size=self.dims.sqsize, xcor=self.dims.xcor + col * self.dims.sqsize, ycor=self.dims.ycor + row * self.dims.sqsize), linewidth=self.linewidth, ultimate=False)
        #borrar fondo
        pygame.draw.rect(surface, (28, 170, 156), (sqr.dims.xcor, sqr.dims.ycor, sqr.dims.size, sqr.dims.size))
        sqr.render(surface) 
        
        # vertical lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.sqsize, self.dims.ycor),                  (self.dims.xcor + self.dims.sqsize, self.dims.ycor + self.dims.size),15)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor), (self.dims.xcor + self.dims.size - self.dims.sqsize, self.dims.ycor + self.dims.size), 15)
        
        # horizontal lines
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.sqsize),                  (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.sqsize),15)
        pygame.draw.line(surface, LINE_COLOR, (self.dims.xcor, self.dims.ycor + self.dims.size - self.dims.sqsize), (self.dims.xcor + self.dims.size, self.dims.ycor + self.dims.size - self.dims.sqsize), 15)
