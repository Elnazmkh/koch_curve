
import turtle as tt


# recursive function to draw 1/3 of koch curve
def koch_curve(length, depth):

    if depth == 0:
        tt.forward(length)
        return
    else:
        koch_curve(length /3, depth -1)
        tt.left(60)
        koch_curve(length /3, depth -1)
        tt.right(120)
        koch_curve(length /3, depth -1)
        tt.left(60)
        koch_curve(length /3, depth -1)

# ------------------------------

tt.speed(20)

#draw the whole curve
for i in range(3):
    koch_curve(200, 3)
    tt.right(120)

tt.TurtleScreen._RUNNING = True