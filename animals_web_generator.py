import json
from load_data import load_data # import function to load JSON data

# Load JSON file
animals_data = load_data("animals_data.json")

# Iterate through the list of animals
for animal in animals_data:
    details = []  # Store available fields for printing

    if "name" in animal:
        details.append(f"Name: {animal['name']}")

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        details.append(f"Diet: {animal['characteristics']['diet']}")

    if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
        details.append(f"Location: {animal['locations'][0]}")

    if "characteristics" in animal and "type" in animal["characteristics"]:
        details.append(f"Type: {animal['characteristics']['type']}")

    # Print details only if there are any
    if details:
        print("\n".join(details))
        print()
