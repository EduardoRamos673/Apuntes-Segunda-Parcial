#Metodo de practica 1
from guizero import App

app = App(title="Hello world")
app.display();

"""Importa la clase App de la biblioteca Guizero.
Crea una instancia de la clase App con el título "Hello world".
Llama al método display() para mostrar la ventana de la aplicación en pantalla."""
#Metodo de practica 2
from guizero import App, Text, PushButton

app = App("ICI App")
message = Text(app, text="Welcome to the ICI App!")

app.display()
"""Importa las clases App, Text, y PushButton de la biblioteca Guizero.
Crea una instancia de la clase App con el título "ICI App".
Crea un objeto Text dentro de la aplicación con el texto "Welcome to the ICI App!".
Llama al método display() para mostrar la ventana de la aplicación en pantalla."""


#Metodo de practica 3
from guizero import App, Text, PushButton

app = App("ICI App")

message = Text(app, text="Welcome to the ICI App!")
button = PushButton(app, text="Click me!")

app.display()
"""Importa las clases App, Text, y PushButton de la biblioteca Guizero.
Crea una instancia de la clase App con el título "ICI App".
Crea un objeto Text dentro de la aplicación con el texto "Welcome to the ICI App!".
Crea un botón (PushButton) con el texto "Click me!".
Llama al método display() para mostrar la ventana de la aplicación en pantalla."""

#Metodo de practica 4
from guizero import App, Text, PushButton

def say_hello():
    message_2.value = "ICI Rocks!"
    
app = App("ICI App")

message = Text(app, text="Welcome to the ICI App!")
message_2 = Text(app)
button = PushButton(app, text="Click me!", command=say_hello)
app.display()
"""Importa las clases App, Text, y PushButton de la biblioteca Guizero.
Define una función llamada say_hello que cambia el valor de message_2 a "ICI Rocks!".
Crea una instancia de la clase App con el título "ICI App".
Crea un objeto Text con el texto "Welcome to the ICI App!".
Crea otro objeto Text llamado message_2.
Crea un botón con el texto "Click me!" y lo asocia a la función say_hello cuando se hace clic en él.
Llama al método display() para mostrar la ventana de la aplicación en pantalla."""
#Metodo de practica 5
from guizero import App, Text, PushButton

def say_hello():
    message_2.value = "ICI Rocks!"
    
app = App("ICI App")

message = Text(app, text="Welcome to the ICI App!")
message_2 = Text(app)
button = PushButton(app, text="Click me!", command=say_hello)
app.display()

#Metodo de practica 6
from guizero import App, Text, PushButton, TextBox

def say_hello():
    app.info("Saludos", text= f"Hola {name.value}")
    #message_2.value = "Hola " + name.value
    
app = App(title="ICI App")

message = Text(app, text="¿Como te llamas?", color="Red")
name = TextBox(app, width=30, height=1, multiline=True)
message_2 = Text(app)
button = PushButton(app, text="Click me!", command=say_hello)

app.display()

#Metodo de practica 7
from guizero import App, Text, PushButton, TextBox

def say_hello():
    app.info("Suma", text=f"La suma es: {int(num_1.value)+int(num_2.value)}")
    
app = App(title="ICI App")

message = Text(app, text="Ingrese el primer numero")
num_1 = TextBox(app, width=30)
message_2= Text(app, text="Ingrese el segundo numero")
num_2 = TextBox(app, width=30)
button = PushButton(app, text="Click me!", command=say_hello)

app.display()