import webbrowser as wb
import pyautogui as pg
import time as t
points=0
videogame = pg.prompt ("What is your favorite video game")
if videogame == "Fortnite":
    points += 10
    wb.open("https://www.youtube.com/watch?v=o8kPmRWvWVQ")
    t.sleep(3)
    pg.alert ("360 Ooga Booga Booga!!")
elif videogame == "Madden 19":
    points += 12
    wb.open("https://www.youtube.com/watch?v=Hw9DuUo77DI")
    t.sleep(3)
    pg.alert ("I used to like Madden, but 18 and 19 aren't that good.")
elif videogame == "Fifa 19":
    points += 10
    wb.open("https://www.youtube.com/watch?v=A2wABJyiHec")
    t.sleep(3)
    pg.alert ("I love playing with Juventus in that game!")
elif videogame == "NBA 2k19":
    points += 12
    wb.open("https://www.youtube.com/watch?v=wGKAbRsM8KA")
    t.sleep(3)
    pg.alert ("Ronnie overpriced everything!")
elif videogame == "Overwatch":
    points += 10
    wb.open("https://www.youtube.com/watch?v=K4cmlhpupn0")
    t.sleep(3)
    pg.alert ("Meh")
elif videogame == "Rocket League":
    points += 12
    wb.open("https://www.youtube.com/watch?v=EUB90qVA9sA")
    t.sleep(3)
    pg.alert ("I heard Jiedel plays that game.")
else:
    pg.alert ("Cool! I've heard of that game before!")

movie = pg.prompt ("What is your favorite movie?")
if movie == "Paul Blart Mall Cop 2":
    points += 11
    wb.open("https://www.youtube.com/watch?v=Bv0A2iINenA")
    t.sleep(3)
    pg.alert ("That is such a good film")
elif movie == "La La Land":
    points += 12
    wb.open("https://www.youtube.com/watch?v=waTDxRZ93Qc")
    t.sleep(3)
    pg.alert ("okay...")
elif movie == "Star Wars":
    points += 11
    wb.open("https://www.youtube.com/watch?v=waTDxRZ93Qc")
    t.sleep(3)
    pg.alert ("How many star wars movies have you seen?")
elif movie == "Spider Man":
    points += 12
    wb.open("https://www.youtube.com/watch?v=yCVOCSlzQno")
    pg.alert ("i saw that movie right it came out. It was so good!")
    t.sleep(3)
elif movie == "Iron Man 2":
    points += 11
    wb.open("https://www.youtube.com/watch?v=BoohRoVA9WQ")
    t.sleep(3)
    pg.alert ("Meh")
elif movie == "Cinderella":
    points += 12
    wb.open("https://www.youtube.com/watch?v=cL-RjWKtZrM")
    t.sleep(3)
    pg.alert ("How old you?")
else:
    pg.alert("Cool, I've heard of that before, but I never watched it...")

food = pg.prompt ("What is your food?")
if food == "Chicken parm":
    points += 11
    wb.open("https://www.youtube.com/watch?v=IUdLlhTmenc")
    t.sleep(3)
    pg.alert ("chicken parm you taste so good")
elif food == "Steak":
    points += 12
    wb.open("https://www.youtube.com/watch?v=iq1WzNrGN6k")
    t.sleep(3)
    pg.alert ("I love steak")
elif food == "Cake":
    points += 11
    wb.open("https://www.youtube.com/watch?v=EOQeU_6vbeg")
    t.sleep(3)
    pg.alert ("Chocolate cake is the best")
elif food == "Pizza":
    points += 12
    wb.open("https://www.youtube.com/watch?v=sv3TXMSv6Lw")
    t.sleep(3)
    pg.alert ("pizza is so good")
elif food == "Pasta":
    points += 11
    wb.open("https://www.youtube.com/watch?v=Q000EqwO-4w")
    t.sleep(3)
    pg.alert ("alfredo is the best")
elif food == "Veggie Plater":
    points += 12
    wb.open("https://www.youtube.com/watch?v=lKwN7ShllDs")
    t.sleep(3)
    pg.alert ("mr. kucher  loves veggie platers")
else:
    pg.alert ("I like that food too")

sport = pg.prompt ("What is your favorite sport?")
if sport == "Basketball":
    points += 13
    wb.open("https://www.instagram.com/mitchell.center/")
    pg.alert ("Follow @mitchell.center on IG for the best mitchell and basketball content.")
    t.sleep(3)
elif sport == "Football":
    points += 12
    wb.open("https://www.youtube.com/watch?v=zCH5VppLT9U")
    t.sleep(3)
    pg.alert ("I love watching football on youtube")
elif sport == "Soccer":
    points += 11
    wb.open("https://www.youtube.com/watch?v=yYjD78X1d9Q")
    t.sleep(3)
    pg.alert ("fifa 17 is really good")
elif sport == "golf":
    points += 3
    wb.open("https://www.youtube.com/watch?v=_lyAEL4Wqao")
    t.sleep(3)
    pg.alert ("dude perfect made a great golf video. ")
elif sport == "Baseball":
    points += 4
    wb.open("https://www.youtube.com/watch?v=XUOmkQPa7kk")
    t.sleep(3)
    pg.alert ("watch mlb highbaseball iq moments")
elif sport == "Curling":
    points += 10
    wb.open("https://www.youtube.com/watch?v=2rQzRMSR1x0")
    t.sleep(3)
    pg.alert ("the 2010 curling final was insane!")
else:
    pg.alert("Interesting choice!")

subject = pg.prompt ("What is your favorite subject?")
if subject == "Math":
    points += 12
    wb.open ("https://www.youtube.com/watch?v=-wkr_vf18cw")
    t.sleep(3)
    pg.alert ("math is great!")
elif subject == "Science":
    points += 11
    wb.open ("https://www.youtube.com/watch?v=wwOY6RgrDKQ")
    t.sleep(3)
    pg.alert ("how's your bridge coming along")
elif subject == "Comp Sci":
    points += 12
    wb.open ("https://www.youtube.com/watch?v=L9LkNAedP9U")
    t.sleep(3)
    pg.alert ("Too bad it's only once a week")
elif subject == "Foreign Language":
    points += 11
    wb.open ("https://www.youtube.com/watch?v=_cjV3gbex1E")
    t.sleep(3)
    pg.alert ("muy bien")
elif subject == "English":
    points += 12
    wb.open ("https://www.youtube.com/results?search_query=of++mice+and+men")
    t.sleep(3)
    pg.alert ("Do you like of mice and men")
elif subject == "History":
    points += 11
    wb.open ("https://www.youtube.com/watch?v=VfOR1XCMf7A")
    t.sleep(3)
    pg.alert ("the 20s ROARED!")
else:
    pg.alert("")


pg.alert("You scored: " + str(points))

    



