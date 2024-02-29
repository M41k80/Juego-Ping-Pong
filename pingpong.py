import turtle

## pantalla

wn = turtle.Screen()
wn.title("pingpong by @m41k80")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

### goles
goles_jugador_1 = 0
goles_jugador_2 = 0

## jugador 1
jugador_1 = turtle.Turtle()
jugador_1.speed(0)
jugador_1.shape("square")
jugador_1.color("blue")
jugador_1.shapesize(stretch_wid=5, stretch_len=1)
jugador_1.penup()
jugador_1.goto(-350, 0)



## jugador 2
jugador_2 = turtle.Turtle()
jugador_2.speed(0)
jugador_2.shape("square")
jugador_2.color("red")
jugador_2.shapesize(stretch_wid=5, stretch_len=1)
jugador_2.penup()
jugador_2.goto(350, 0)

## pelota

pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.shapesize(stretch_wid=1, stretch_len=1)
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 1
pelota.dy = -1

###Marcadores

marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 260)
marcador.write("JUGADOR 1: 0    JUGADOR 2: 0", 
               align="center", font=("Arial", 22, "normal"))


### texto victoria
text_victoria = turtle.Turtle()
text_victoria.speed(0)
text_victoria.color("orange")
text_victoria.hideturtle()
text_victoria.goto(0, -0)

### funciones

def jugador_1_up():
    y = jugador_1.ycor()
    y += 20
    jugador_1.sety(y)
    
def jugador_1_down():
    y = jugador_1.ycor()
    y -= 20
    jugador_1.sety(y)
    
    

def jugador_2_up():
    y = jugador_2.ycor()
    y += 20
    jugador_2.sety(y)
    
def jugador_2_down():
    y = jugador_2.ycor()
    y -= 20
    jugador_2.sety(y)
    
### enlace de teclado

wn.listen()
wn.onkeypress(jugador_1_up, "w")
wn.onkeypress(jugador_1_down, "s")
wn.onkeypress(jugador_2_up, "Up")
wn.onkeypress(jugador_2_down, "Down")



#inicio

while True:
    wn.update()
    
    #movimiento de la pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    
    #checkeo de el borde
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
    
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1    
        
        
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        goles_jugador_1 += 1
        marcador.clear()
        marcador.write("JUGADOR 1: {}    JUGADOR 2: {}".format(goles_jugador_1, goles_jugador_2), 
               align="center", font=("Arial", 22, "normal"))
        
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1
        goles_jugador_2 += 1
        marcador.clear()
        marcador.write("JUGADOR 1: {}    JUGADOR 2: {}".format(goles_jugador_1, goles_jugador_2), 
               align="center", font=("Arial", 22, "normal"))
    
    
    ### ganador
    
    if goles_jugador_1 == 5:
        text_victoria.write("JUGADOR 1  !!! GANASTE",
                      align="center", font=("Arial", 30, "normal"))
        
    if goles_jugador_2 == 5:
        text_victoria.write("JUGADOR 2  !!! GANASTE",
                      align="center", font=("Arial", 30, "normal"))
        
           
           
        
    ## cuando pega la pelota
    
    if (pelota.xcor() > 340 and pelota.xcor() < 350) \
        and (pelota.ycor() < jugador_2.ycor() + 40 \
            and pelota.ycor() > jugador_2.ycor() -40):
        pelota.setx(340)
        pelota.dx *= -1
        
    if (pelota.xcor() < -340 and pelota.xcor() > -350) \
        and (pelota.ycor() < jugador_1.ycor() + 40 \
            and pelota.ycor() > jugador_1.ycor() -40):
        pelota.setx(-340)
        pelota.dx *= -1