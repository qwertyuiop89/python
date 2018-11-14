import webbrowser as wb
import pyautogui as pg
import time as t

points = 0
show = pg.confirm("which of these is my favorite tv show?", "choose one",["Hanna Montana", "The Office", "Dora The Explorer"])
if show == "Hanna Montana":
    pg.alert("correct")
    wb.open("https://www.youtube.com/watch?v=jtpK9uxTZhE")
    points += 5
elif show == "the office":
    pg.alert("correct")
    wb.open("https://www.youtube.com/watch?v=GfGN7bfohms")
    points += 5
elif show == "boy meets world":
    pg.alert("Wrong")
    wb.open("https://www.youtube.com/watch?v=3gOHvDP_vCs")
elif show == ("dora the explorer"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=JY8hiBbYHJY")
elif show == ("House hunters"):
    pg.alert ("wrong")
elif show == ("Jimmy Neutron"):
    pg.alert ("wrong")
else:
    pg.alert("it was Hanna Montana")
    wb.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

tests = pg.prompt("Do I like tests-")
if tests == "yes":
     pg.alert("wrong")
     wb.open("https://www.youtube.com/watch?v=lG7rBQIZ-vU")
elif tests == ("kind of"):
    pg.alert("wrong")
    wb.open("https://www.youtube.com/watch?v=p8XP7A7kvzM")
elif tests == ("I hate them"):
    pg.alert("wrong")
    wb.open("https://www.youtube.com/watch?v=xrympPev1RU")
elif tests == ("no"):
    pg.alert("correct")
    wb.open("https://www.youtube.com/watch?v=LnPXQjml7Sg")
    points += 5
elif tests == ("Fefe"):
    pg.alert ("wrong")
elif tests == ("Fefe"):
    pg.alert ("wrong")
else:
    pg.alert("it was no")
    wb.open("https://www.youtube.com/watch?v=jofNR_WkoCE")

book = pg.confirm("which of these is my favorite book?", "choose one",["Harry Potter", "Peppa Pig", "Green Eggs and Ham"])

if book == "Harry Potter":
    pg.alert("correct")
    wb.open("https://www.youtube.com/watch?v=Tx1XIm6q4r4")
    points += 5
elif book == ("peppa pig"):
    pg.alert ("correct")
    wb.open("https://www.youtube.com/watch?v=xrympPev1RU")
    points += 5
elif book == ("threads of time"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=IshQFFwW30U")
elif book == ("every book"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=IshQFFwW30U")
elif book ==("Green Eggs and Ham"):
    pg.alert ("wrong")
elif book == ("Red Firetruck"):
    pg.alert ("wrong")
else:
    pg.alert("it was Harry Potter")
    wb.open("https://www.youtube.com/watch?v=IshQFFwW30U")

game = pg.confirm("which of these is my favorite video game?", "choose one",["fortnite", "Mario Kart", "Grand Theft Auto"])
if game == "fortnite":
    pg.alert("correct")
    points += 5
    wb.open("https://www.youtube.com/watch?v=dwJL9AoFO_o")
elif game == ("pub G"):
    pg.alert ("wrong")
elif game == ("mario"):
    pg.alert ("wrong")
elif game == ("Wii lite"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=9MAKlMEl6fM")
elif game == ("Grand Theft auto"):
    pg.alert ("wrong")
elif game == ("Flappy Bird"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=9MAKlMEl6fM")
else:
    pg.alert("it was fortnite")
    wb.open("https://www.youtube.com/watch?v=ZyhrYis509A")

song = pg.confirm("which of these is my favorite Song?", "choose one",["Spongebob theme song", "God is a woman", "Mo Bamba"])
if song == "Spongebob theme song":
    pg.alert("correct")
    wb.open("https://www.youtube.com/watch?v=BiA-7xHM8zc")
elif song == ("God is a woman"):
    pg.alert ("wrong")
elif song == ("cheteau"):
    pg.alert ("wrong")
elif song == ("Fefe"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=")
elif song == ("Midsummer Madness"):
    pg.alert ("wrong")
elif song == ("Mo Bamba"):
    pg.alert ("wrong")
    wb.open("https://www.youtube.com/watch?v=98hmsn621")
else:
    pg.alert("it was Drunk Me")
    wb.open("https://www.youtube.com/watch?v=9MAKlMEl6fM")

pg.alert("your final score is " + str(points) + "/20")

    
