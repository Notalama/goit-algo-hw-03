import turtle

def koch_curve(t, order, size):
    """
    Рекурсивно малює криву Коха.

    Args:
      t: Об'єкт черепахи.
      order: Рівень рекурсії (порядок кривої Коха).
      size: Довжина відрізка.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    """
    Малює сніжинку Коха.

    Args:
      order: Рівень рекурсії.
      size: Розмір сніжинки.
    """
    w = turtle.Screen()
    w.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size * 3**0.5 / 6)  # Центрування сніжинки
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    w.mainloop()

if __name__ == "__main__":
    order = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    draw_koch_snowflake(order)
