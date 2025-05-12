"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""
# These ratios are always the same

MERCURY_RATIO = 0.376
VENUS_RATIO = 0.889
MARS_RATIO = 0.378
JUPITER_RATIO = 2.36
SATURN_RATIO = 1.081
URANUS_RATIO = 0.815
NEPTUNE_RATIO = 1.14 

def main():
    earth_weight = input("Enter a weight on Earth:")
    planet = input("Enter a planet: ")
    earth_weight_float = float(earth_weight)

    planet_weight = earth_weight_float

    if planet == "Mercury": 
        planet_weight = earth_weight_float * MERCURY_RATIO
    elif planet == "Venus":
        planet_weight = earth_weight_float * VENUS_RATIO
    elif planet == "Mars":
        planet_weight = earth_weight_float * MARS_RATIO
    elif planet == "Jupiter":
        planet_weight = earth_weight_float * JUPITER_RATIO
    elif planet == "Saturn":
        planet_weight = earth_weight_float * SATURN_RATIO
    elif planet == "Uranus":
        planet_weight = earth_weight_float * URANUS_RATIO
    elif planet == "Neptune":
        planet_weight = earth_weight_float * NEPTUNE_RATIO
    
    planet_weight = round(planet_weight, 2)
    print("The equivalent weight on", planet, ":", planet_weight)

if __name__ == "__main__":
    main()
