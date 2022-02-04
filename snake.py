from turtle import Turtle
STATING_POSITIONS=[(0,0),(-20, 0),(-40, 0)] # all constant must be capitial 
MOVE_SNAKE_PACES=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
        def __init__(self) -> None:
            self.turtles=[]
            self.create_snake()

        def create_snake(self):
            # #step 1 create a snake body
            for position in STATING_POSITIONS:
                self.add_segment(position)

        def add_segment(self,position):
                new_turtle=Turtle("square")
                new_turtle.penup()
                new_turtle.color("white")
                new_turtle.goto(position)
                self.turtles.append(new_turtle)

        def move_forward(self):
            #step 2: Move the snake 
                for steps in range(len(self.turtles) - 1, 0, -1):
                    new_x=self.turtles[steps-1].xcor()
                    new_y=self.turtles[steps-1].ycor()
                    self.turtles[steps].goto(new_x,new_y)
                    #all turtles went to the same position which is at (0,0) cordinate
                self.turtles[0].forward(MOVE_SNAKE_PACES)
        # we are moving the head of the snake 
        def up(self):
            if self.turtles[0].heading()!= DOWN:
                self.turtles[0].setheading(UP)
        
        def down(self):
            if self.turtles[0].heading()!= UP:
                self.turtles[0].setheading(DOWN)

        def left(self):
            if self.turtles[0].heading()!= RIGHT:
                self.turtles[0].setheading(LEFT)

        def right(self):
            if self.turtles[0].heading()!= LEFT:
                self.turtles[0].setheading(RIGHT)



        

    # step 7 : extent the snake whenever he eats the food
        def extent(self):
            self.add_segment(self.turtles[-1].position())
            # last position se add hota jaa rha hai
