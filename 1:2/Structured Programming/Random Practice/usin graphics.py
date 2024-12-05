from graphics import*

win = GraphWin("Celsius Converter",400,300)

win.setCoords(0.0,0.0,4.0,3.0)


Text(Point(1,2.5), "Celsius Temperature:").draw(win)
Text(Point(1,1), "Fahrenheit Temperature:").draw(win)

button = Text(Point(1.5,2.0),"Convert it")
button.draw(win)

input = Entry(Point(3,2.5),5)
input.setText("0.0")
input.draw(win)

fahrenheit = Text(Point(2.5,1),"")
fahrenheit.draw(win)
win.getMouse()

c = eval(input.getText())

f = 9/5*c+32

button.setText("Quit")
fahrenheit.setText(f)

win.getMouse()

