from appJar import gui

# could be made dynamic input
taxes = 1.19

# create GUI
app = gui("Brutto Netto Rechner", "400x200")
app.setFont(18)


# set Title
app.addLabel('title', 'Brutto Netto Rechner')
app.setLabelBg('title', 'white')

# set input
app.addLabelEntry("Bruttopreis")

# function to run on button click
def calculate():
    brutto = app.getEntry("Bruttopreis")
    result = float(brutto)/1.19
    app.addLabel('Solution', result)

# create button
app.addButton("Calculate", calculate)

app.go()