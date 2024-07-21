from calculator import CustomCalculator
from conversions import *
from matrix_operations import *
from statistical_calculations import *

# Créez une instance de la calculatrice
calculator = CustomCalculator()

while True:
    # Affiche le menu à chaque fois que vous voulez réaliser un calcul
    print("Welcome to the Custom Calculator. Here are the available options:")
    print("1. Basic operations (addition '+', subtraction '-', multiplication '*', division '/')")
    print("2. Trigonometric functions (cos, sin, tan) - Use 'mode:degrees' or 'mode:radians' to switch mode")
    print("3. Number system conversions (bin, dec, hex)")
    print("4. Advanced calculations (factorial 'fact', square root 'sqrt', logarithm 'log')")
    print("5. Use '_last' to reference the last result")
    print("6. Type 'exit' to quit the program")
    print("\n")

    user_input = input("Enter an expression (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    result = calculator.calculate(user_input)
    print("Result:", result)

# Exemples d'utilisation des modules
# Vous pouvez intégrer une interface utilisateur ici pour interagir avec les différents modules
