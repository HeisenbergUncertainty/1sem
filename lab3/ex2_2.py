import turtle

def norm(): 
    turtle.penup()
    turtle.backward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180) 
    
def zero():
    for _ in range(2):
        turtle.forward(50)
        turtle.right(90)  
        turtle.forward(100)
        turtle.right(90)  
        
def one():
    turtle.penup()
    turtle.right(90) 
    turtle.forward(50)
    turtle.pendown()    
    turtle.left(135)
    turtle.forward(71)
    turtle.right(135)
    turtle.forward(100)
    
    norm()
    
def four():
    turtle.right(90) 
    turtle.forward(50)
    for _ in range(2):
        turtle.left(90) 
        turtle.forward(50) 
    turtle.right(180) 
    turtle.forward(100)
    
    norm()
    
def seven():
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(71)
    turtle.left(45)
    turtle.forward(50)
    
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    norm()
    
#def draw_number(n):
    #if n == '0':
        #zero()
    #elif n == '1':
        #one()
    #elif n == '4':
        #four()
    #elif n == '7':
        #seven()
    #else:
        #print('nope')
    
    
data = ['zero()', 'one()', 2, 3, 'four()', 5, 6, 'seven()'] 
turtle.shape('turtle')

turtle.penup()
turtle.goto(-350, 300)
turtle.pendown()
nums = list(map(int, '141700'))
for x in nums:
    turtle.pendown()
    eval(data[x])
    turtle.penup()        
    turtle.forward(60)
    turtle.pendown()
    