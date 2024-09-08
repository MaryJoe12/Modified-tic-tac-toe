import turtle

# Código para la configuración de la ventana:
window = turtle.Screen()
window.title("Este está más fácil que el gato :) ")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

def dibujar_fondo():
    for i in range(-400, 400, 20):
        for j in range(-300, 300, 20):
            cuadro = turtle.Turtle()
            cuadro.speed(0)
            cuadro.shape("square")
            cuadro.color("grey")
            cuadro.shapesize(stretch_wid=0.2, stretch_len=0.2)
            cuadro.penup()
            cuadro.goto(i, j)

# Dibujar el fondo de cuadros al inicio
dibujar_fondo()

# Variables iniciales para los marcadores
marcadorA = 0
marcadorB = 0

# Código para el físico del jugador A
jugadorA = turtle.Turtle()
jugadorA.speed(2)
jugadorA.shape("square")
jugadorA.color("white")
jugadorA.up()
jugadorA.goto(-350, 0)
jugadorA.shapesize(stretch_wid=8, stretch_len=2)

# Código para el físico del jugador B
jugadorB = turtle.Turtle()
jugadorB.speed(2)
jugadorB.shape("square")
jugadorB.color("white")
jugadorB.up()
jugadorB.goto(350, 0)
jugadorB.shapesize(stretch_wid=8, stretch_len=2)

# Código para el físico de la pelota:
Pelota = turtle.Turtle()
Pelota.speed(2)
Pelota.shape("turtle")
Pelota.color("purple")
Pelota.up()
Pelota.dx = 10
Pelota.dy = 10

# Código para la línea divisora:
division = turtle.Turtle()
division.color("red")
division.pensize(5)
division.goto(0, 600)
division.goto(0, -600)

# Código para el marcador
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Jugador A: 0                   Jugador B: 0", align="center", font=("Courier"))

# Función para el movimiento del jugador A:
def jugadorA_arriba():
    a = jugadorA.ycor()
    a += 45
    jugadorA.sety(a)

def jugadorA_abajo():
    b = jugadorA.ycor()
    b -= 45
    jugadorA.sety(b)

# Función para el movimiento del jugador B:
def jugadorB_arriba():
    c = jugadorB.ycor()
    c += 45
    jugadorB.sety(c)

def jugadorB_abajo():
    d = jugadorB.ycor()
    d -= 45
    jugadorB.sety(d)

# Código para enlazar las funciones con el teclado:
window.listen()
window.onkeypress(jugadorA_arriba, "w")
window.onkeypress(jugadorA_abajo, "s")
window.onkeypress(jugadorB_arriba, "Up")
window.onkeypress(jugadorB_abajo, "Down")

# Ciclo principal del juego (mientras el juego esté activo, este ciclo seguirá corriendo)
while True:
    window.update()
    Pelota.setx(Pelota.xcor() + Pelota.dx)
    Pelota.sety(Pelota.ycor() + Pelota.dy)

    # Bordes arriba y abajo
    if Pelota.ycor() > 290:
        Pelota.dy *= -1
    if Pelota.ycor() < -290:
        Pelota.dy *= -1

    # Bordes derecha e izquierda y puntos
    if Pelota.xcor() > 390:
        Pelota.goto(0, 0)
        Pelota.dx *= -1
        marcadorA += 1
        pen.clear()
        pen.write("Jugador A: {}         Jugador B: {}".format(marcadorA, marcadorB), align="center",
                  font=("Courier"))

    if Pelota.xcor() < -390:
        Pelota.goto(0, 0)
        Pelota.dx *= -1
        marcadorB += 1
        pen.clear()
        pen.write("Jugador A: {}         Jugador B: {}".format(marcadorA, marcadorB), align="center",
                  font=("Courier"))

    # Configuración del choque entre la pelota y los jugadores
    if ((Pelota.xcor() > 340 and Pelota.xcor() < 350)
            and (Pelota.ycor() < jugadorB.ycor() + 50 and Pelota.ycor() > jugadorB.ycor() - 50)):
        Pelota.dx *= -1

    if ((Pelota.xcor() < -340 and Pelota.xcor() > -350)
            and (Pelota.ycor() < jugadorA.ycor() + 50 and Pelota.ycor() > jugadorA.ycor() - 50)):
        Pelota.dx *= -1


  

           