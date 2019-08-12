## Summary

This is Project is meant to demonstrate the simple use of variables in Python, how to perform calculations and how to build a simple GUI.

### Requirements

* We will use the PyPi Package appJar to create a simple GUI for Python Programming

#### Step 1

* build a simple calculator as you like
* we will use a small operation that calculates taxes from a number
* ask the user for input, calculate the solution and print it out

<details>
<summary>Solution</summary>

<p>

```
taxes = 1.19

brutto = input('Put in the Billing Amount including Taxes')

result = float(brutto)/taxes

print('This is the Billing Amount without taxes')

```

Pretty easy right :-)

</p>
</details>

#### Step 2

* now let's build something more exciting out of this
* add the appJar Package to the project, comment out what you've done for a moment
* create a gui window with appJar
* open up the GUI

<details>
<summary>Solution</summary>

<p>

```
from appJar import gui

app = gui("Brutto Netto Rechner", "400x200")

app.go()

```

This creates a simple window. 
</p>
</details>

#### Step 3

* we want to replace the command line input by an input field
* moreover we need a button for performing the calculation

<details>
<summary>Solution</summary>

<p>

```
# set Title
app.addLabel('title', 'Brutto Netto Rechner')
app.setLabelBg('title', 'white')

# set input
app.addLabelEntry("Bruttopreis")

# create button
app.addButton("Calculate", calculate)

```

This actually should produce an error. Why? We have not declared a function called calculate yet...

</p>
</details>

#### Step 4

* create a function called calculate 
* be careful and create it before the button creation (try it out, if you don't know why)
* run a print event in that function

<details>
<summary>Solution</summary>

<p>

```
# function to run on button click
def calculate():
    print('Clicked Button!')

```
Have a Look at your console.
</p>
</details>

#### Step 5

* we are missing on two things: the calculation AND the output
* get the users input from the Bruttopreis Label and save it to a variable
* use your code from before to calculate the result
* create a label in the function that shows the result

<details>
<summary>Solution</summary>

<p>

```
# function to run on button click
def calculate():
    brutto = app.getEntry("Bruttopreis")
    result = float(brutto)/1.19
    app.addLabel('Solution', result)

```

Aaand your done!
</p>
</details>

Check the brutto_netto_rechner.py file for the complete solution.

### Useful Links

* http://appjar.info/
* https://www.pythonforbeginners.com/basics/python-variables
* https://realpython.com/python-data-types/