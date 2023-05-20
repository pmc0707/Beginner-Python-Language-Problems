GAME_WIDTH =700
GAME_HEIGHT =700
SPEED=50
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOUR="#00FF00"
FOOD_COLOUR="#FF0000"
BACKGROUND_COLOUR="#000000"




class Snake:
    pass

class Food:
    pass
def next_turn():
    pass
def change_direction(new_direction):
    pass
def check_collisions():
    pass
def game_over():
    pass

window = ()
window.title("snake game")
window.resizable(False, False)
scroe=0
direction ="down"
label=label(window,text="Score:{}".format(score),font=('consolas',40))
label.pack()
canvas = canvas(window,bg=BACKGROUND_COLOUR,height=GAME_HEIGHT,width=GAME_WIDTH)
window.update()
window.mainloop()