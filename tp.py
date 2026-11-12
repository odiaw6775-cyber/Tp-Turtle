import turtle

# Création de la tortue
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("#87CEEB")  # ciel bleu

def aller(x, y):
    """Place la tortue à (x, y) sans dessiner."""
    t.penup()
    t.goto(x, y)
    t.pendown()

def petale(taille, couleur):
    """Dessine un pétale rempli."""
    t.color(couleur)
    t.begin_fill()
    t.circle(taille, 60)
    t.left(120)
    t.circle(taille, 60)
    t.left(120)
    t.end_fill()

def fleur(x, y, taille, couleur):
    """Dessine une fleur : tige, pétales et cœur."""
    # Tige
    aller(x, y)
    t.setheading(270)  # la tortue regarde vers le bas
    t.color("green")
    t.pensize(3)
    t.forward(taille * 2)
    t.pensize(1)

    # Pétales
    aller(x, y)
    for i in range(8):
        t.setheading(i * 45)  # 8 pétales : 360 / 8 = 45°
        petale(taille, couleur)

    # Cœur de la fleur
    aller(x, y)
    t.color("yellow")
    t.begin_fill()
    t.circle(taille * 0.35)
    t.end_fill()

# Soleil
aller(-220, 170)
t.color("yellow")
t.begin_fill()
t.circle(45)
t.end_fill()

# Sol
aller(-300, -150)
t.setheading(0)
t.color("green")
t.begin_fill()
t.forward(600)
t.right(90)
t.forward(200)
t.right(90)
t.forward(600)
t.right(90)
t.forward(200)
t.end_fill()

# Jardin de fleurs
positions = [(-200, -80), (-100, -100), (0, -70), (100, -95), (200, -80)]
couleurs = ["red", "orange", "magenta", "purple", "pink"]

for i in range(len(positions)):
    x, y = positions[i]
    fleur(x, y, 30 + i * 3, couleurs[i])

turtle.done()