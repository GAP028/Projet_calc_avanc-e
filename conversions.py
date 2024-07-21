import math

# Fonctions de conversion pour les angles
def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

def radians_to_degrees(radians):
    return radians * (180 / math.pi)

# Fonctions de conversion pour les distances
def convert_km_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_km(miles):
    return miles / 0.621371

# Ajoutez ici d'autres fonctions de conversion pour les distances...

# Fonctions de conversion pour les températures
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32

# Fonctions de conversion pour les durées
def convert_duration(duration, from_unit, to_unit):
    conversion_factors = {
        "years": 365 * 24 * 60 * 60,
        "months": 30 * 24 * 60 * 60,
        "weeks": 7 * 24 * 60 * 60,
        "days": 24 * 60 * 60,
        "hours": 60 * 60,
        "minutes": 60,
        "seconds": 1
    }
    from_factor = conversion_factors.get(from_unit)
    to_factor = conversion_factors.get(to_unit)
    if from_factor is None or to_factor is None:
        return None
    return duration * from_factor / to_factor
