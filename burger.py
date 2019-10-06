# -*- coding: utf-8 -*-
"""
Created on Fri May 17 09:43:54 2019

@author: 0715334
"""
#i used these in my game
import random as r
import time
import turtle as t

#this sets up the world
t.setup(960,640)
world = t.Screen()
world.bgcolor("orange")

#this creates the turtle called order
#this turtle displays instructions and coustomers orders
order = t.Turtle()
order.ht()
order.penup()
order.setpos(-220,230)
order.speed(0)

#there is a dragging and get pos function for each ingredient
#all of these functions do the same thing they just are used for different ingredients
#dragging lets you drag the turtle without the program breaking
#i found this function online
def draggingbottom(x, y):
    bottom.ondrag(None)
    bottom.setheading(bottom.towards(x, y))
    bottom.goto(x, y)
    bottom.ondrag(draggingbottom)
#getpos finds the coordinates of the ingredient
# if the position is on the plate it will be added to the list and a stamp of the ingredient is left on the plate
def getposbottom(x,y):
    x = bottom.xcor() 
    if (220<x <310):#this is where the plate is
        burger.append("bun")#this adds the ingredient to the list that holds the new burger
        bottom.stamp()#this makes the stamp on the plate
    bottom.setpos(bunp)#this makes the turtle go back to its place
    bottom.setpos(bunp)
        
        
def draggingpatty(x, y):
    patty.ondrag(None)
    patty.setheading(patty.towards(x, y))
    patty.goto(x, y)
    patty.ondrag(draggingpatty)
def getpospatty(x,y):
    x = patty.xcor()
    if (220<x <310):
        burger.append("patty")
        patty.stamp()
    patty.setpos(pattyp)

def draggingcheese(x, y):
    cheese.ondrag(None)
    cheese.setheading(cheese.towards(x, y))
    cheese.goto(x, y)
    cheese.ondrag(draggingcheese)
def getposcheese(x,y):
    x = cheese.xcor()
    if (220<x <310):
        burger.append("cheese")
        cheese.stamp()
        cheese.setpos(cheesep)

def dragginglettuce(x, y):
    lettuce.ondrag(None)
    lettuce.setheading(lettuce.towards(x, y))
    lettuce.goto(x, y)
    lettuce.ondrag(dragginglettuce)
def getposlettuce(x,y):
    x = lettuce.xcor()
    if (220<x <310):
        burger.append("lettuce")
        lettuce.stamp()
        lettuce.setpos(lettucep)

def draggingmustard(x, y):
    mustard.ondrag(None)
    mustard.setheading(mustard.towards(x, y))
    mustard.goto(x, y)
    mustard.ondrag(draggingmustard)
def getposmustard(x,y):
    x = mustard.xcor()
    if (220<x <310):
        burger.append("mustard")
        mustard.stamp()
        mustard.setpos(mustardp)
        
def draggingmayo(x, y):
    mayo.ondrag(None)
    mayo.setheading(mayo.towards(x, y))
    mayo.goto(x, y)
    mayo.ondrag(draggingmayo)
def getposmayo(x,y):
    x = mayo.xcor()
    if (220<x <310):
        burger.append("mayo")
        mayo.stamp()
        mayo.setpos(mayop)
        
def draggingonion(x, y):
    onion.ondrag(None)
    onion.setheading(onion.towards(x, y))
    onion.goto(x, y)
    onion.ondrag(draggingonion)
def getposonion(x,y):
    x = onion.xcor()
    if (220<x <310):
        burger.append("onion")
        onion.stamp()
        onion.setpos(onionp)
        
def draggingtomato(x, y):
    tomato.ondrag(None)
    tomato.setheading(tomato.towards(x, y))
    tomato.goto(x, y)
    tomato.ondrag(draggingtomato)
def getpostomato(x,y):
    x = tomato.xcor()
    if (220<x <310):
        burger.append("tomato")
        tomato.stamp()
        tomato.setpos(tomatop) 
        
#this function makes the turtle,order,print a list
#for each ingredient the turtle writes the ingredient and moves down to write the next ingredient
#this function is used to print orders and to print the burger the player makes
def printorder(ordernum):
    for x in ordernum:
        order.write(x,font =('Fixedsys' , 22, 'bold'))
        orderx = order.xcor()#finds the x coordinate
        ordery= order.ycor()#find the current y coordinate
        order.goto(orderx,(ordery-20))#then moves down 20 pixels before looping again
    

#these are empty lists that can be filled when an burger is ordered or when it is being made
whichb = []
burger = []
   
#these are the different types of burgers that can be ordered
order1 = ["bun","patty","cheese","lettuce","mustard","bun"]
order2 = ["bun","patty","mayo","lettuce","onion","mayo","bun"]
order3 = ["bun","tomato","onion","lettuce","patty","lettuce","onion","tomato","bun"]
order4 = ["bun","patty","cheese","patty","cheese","patty","cheese","mayo","bun"]
#this function picks a random burger and checks if the player makes it correctly
#it also gives points for if the player makes the burger correctly
def makeorder():
    order.setpos(-300,230)
    #this records the start time and is used find how long it takes to make the burger
    start = time.time()
    #global variables defined outside the function
    global whichb
    global burger
    global tscore
    
    #this randomly selects an order
    ordernum = r.randint(1,4)
    #here, the order turtle writes customer's order on the screen using the printorder function
    order.write("**NEW ORDER**",font =('Fixedsys' , 22, 'bold'))
    order.goto(-300,200)
    #it also adds the randomly selected order to the list called "which b"
    #whichb contains whatever order is randomly selected and is used to compare to the players burger
    if ordernum == 1:
        printorder(order1)
        whichb.extend(order1)
    if ordernum == 2:
        printorder(order2)
        whichb.extend(order1)
    if ordernum == 3:
        printorder(order3)
        whichb.extend(order3)
    if ordernum == 4:
        printorder(order4)
        whichb.extend(order4)
#this moves the order turtle back after it has moved to print the list
    order.setpos(-300,220)
#this is how the player makes a burger
#the program waits untill the burger the player makes is as big as the order
#the same functions are used for each ingredient turtle
    while len(burger) < len(whichb):
        bottom.ondrag(draggingbottom)#this function is used with the turtle function ondrag it allows the turtle to be dragged without the program crashing 
        bottom.onrelease(getposbottom)#when the player stops dragging an ingredient getpos runs so if the ingredient is on the tray it gets added to the burger
        patty.ondrag(draggingpatty)
        patty.onrelease(getpospatty)
        cheese.ondrag(draggingcheese)
        cheese.onrelease(getposcheese)
        lettuce.ondrag(dragginglettuce)
        lettuce.onrelease(getposlettuce)
        mustard.ondrag(draggingmustard)
        mustard.onrelease(getposmustard)
        mayo.ondrag(draggingmayo)
        mayo.onrelease(getposmayo)
        onion.ondrag(draggingonion)
        onion.onrelease(getposonion)
        tomato.ondrag(draggingtomato)
        tomato.onrelease(getpostomato)
   
    
    #this records the time now and subtracts it from the start time
    #then it has the time it took the make the burger
    end = time.time()
    ttime = end - start
    ttime = round(ttime)
    
    #this moves order turtle
    order.setpos(170,230)
    order.write("YOUR BURGER",font =('Fixedsys' , 22, 'bold'))
    #now the order turtle can write down the burger the player made so it can be compared to the order
    order.setpos(200,200)
    printorder(burger)
    #this shows the player how long it took to make the burger
    order.write("Made in "+str(ttime)+" seconds",font =('Fixedsys' , 22, 'bold'))
    time.sleep(3)#this makes the program pause so we can read it
    #then the order turtle gets put back and the text is cleared
    order.clear()
    order.setpos(-300,220)

    #this compares the burger the player made to the one that is ordered
    if burger == whichb:
        order.write("perfect",font =('Fixedsys' , 22, 'bold'))
        tscore = tscore + 20
        #this adds points for making a correct burger
        if ttime < 100:
            addtpoints = 100 - ttime
            tscore = addtpoints
        #this adds points for making a fast burger
    else:
        order.write("incorrect order",font =('Fixedsys' , 22, 'bold'))
        if ttime < 50:
            addtpoints = 50 - ttime
            tscore = addtpoints
            #this adds points for a fast burger
    #this clears the lists that have been made 
    burger.clear()
    whichb.clear()
    #this clears the stamps that have been made on the red tray
    bottom.clearstamps()
    patty.clearstamps()
    cheese.clearstamps()
    lettuce.clearstamps()
    mustard.clearstamps()
    mayo.clearstamps()
    onion.clearstamps()
    tomato.clearstamps()
    

#this welcomes the player and starts them at lvl 1
level = 1
tscore = 0
#this lets the player choose to play
order.write("welcome to papa chloe's burgeria\nhere you make burgers by dragging ingredients to the red tray\nyou can earn points by correctly making customer's orders\nyou also earn points for making the orders quickly",font = ('Fixedsys' , 18, 'bold'))
play = world.textinput("play?","do you want to play(y/n)")
while play == "y" :
    #these are the turtles for each ingredient
    #each turtle has a different shape,color,size,position which is made here
      
    bottom = t.Turtle()
    bottom.speed(0)
    bottom.penup()
    bottom.shapesize(3,3)
    bottom.color("#f0c98e")
    bottom.pencolor("black")
    bottom.shape("circle")
    bunp = (-50,-100)
    bottom.setpos(bunp)
    bottom.write("bun",align="center",font =('Fixedsys' , 22, 'bold'))

    patty = t.Turtle()
    patty.speed(0)
    patty.penup()
    patty.shapesize(3,3)
    pattyp =(-150,-100)
    patty.setpos(pattyp)
    patty.color("#48240a")
    patty.pencolor("black")
    patty.shape("circle")
    patty.write("patty",align="center",font =('Fixedsys' , 22, 'bold'))

    cheese = t.Turtle()
    cheese.speed(0)
    cheese.penup()
    cheese.shapesize(3,3)
    cheesep = (-250,-100)
    cheese.setpos(cheesep)
    cheese.color("#ffd43c")
    cheese.pencolor("black")
    cheese.shape("square")
    cheese.write("cheese",align="center",font =('Fixedsys' , 22, 'bold'))

    lettuce = t.Turtle()
    lettuce.speed(0)
    lettuce.penup()
    lettucep = (-350,-100)
    lettuce.shapesize(3,3)
    lettuce.setpos(lettucep)
    lettuce.color("#A6D785")
    lettuce.pencolor("black")
    lettuce.shape("square")
    lettuce.write("lettuce",align="center",font =('Fixedsys' , 22, 'bold'))

    mustard = t.Turtle()
    mustard.speed(0)
    mustard.penup()
    mustardp = (-50,-250)
    mustard.shapesize(3,3)
    mustard.setpos(mustardp)
    mustard.color("#feca1d")
    mustard.pencolor("black")
    mustard.write("mustard",align="center",font =('Fixedsys' , 22, 'bold'))
    mustard.shape("circle")

    mayo = t.Turtle()
    mayo.penup()
    mayo.speed(0)
    mayop = (-150,-250)
    mayo.shapesize(3,3)
    mayo.setpos(mayop)
    mayo.color("#fffde9")
    mayo.pencolor("black")
    mayo.shape("square")
    mayo.write("mayo",align="center",font =('Fixedsys' , 22, 'bold'))

    onion = t.Turtle()
    onion.penup()
    onion.speed(0)
    onionp = (-250,-250)
    onion.setpos(onionp)
    onion.shapesize(3,3)
    onion.color("#fdfffc")
    onion.shape("circle")
    onion.pencolor("black")
    onion.write("onion",align="center",font =('Fixedsys' , 22, 'bold'))

    tomato = t.Turtle()
    tomato.speed(0)
    tomato.penup()
    tomatop = (-350,-250)
    tomato.shapesize(3,3)
    tomato.setpos(tomatop)
    tomato.color("red")
    tomato.pencolor("black")
    tomato.shape("circle")
    tomato.write("tomato",align="center",font =('Fixedsys' , 22, 'bold'))

    plate = t.Turtle()
    plate.speed(0)
    plate.penup()
    plate.shapesize(7, 7)
    plate.color("red")
    plate.shape("square")
    plate.pencolor("white")
    plate.setpos(260,-170)

    order.setpos(-300,220)
    order.write("you have reached level " + str(level),font =('Fixedsys' , 22, 'bold'))
    z = 0
    while level != z:#this part prints stats to the game like what level and what score
        order.clear()
        order.setpos(-300,270)
        order.write("Score:"+ str(round(tscore)),font =('Fixedsys' , 22, 'bold'))
        order.setpos(-300,250)
        order.write("You are on level "+str(level),font =('Fixedsys' , 22, 'bold'))
        makeorder()
        z = z +1
    if tscore >= 65:#this lets the player move on to a new level
        level = level +1
if play != "y" or "n":#this runs in case the player does not input the right thing
    play = world.textinput("play?","do you want to play(y/n)")