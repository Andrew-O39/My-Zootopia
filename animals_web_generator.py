import json

from load_data import load_data # import function to load JSON data

def serialize_animal(animal_obj):
    output = '' # Start with an empty string
    output += '<li class="cards__item">\n' # Add opening <li> tag
    output += f'<div class="card__title">{animal_obj.get("name", "Unknown Animal")}</div>\n' # Add title
    output += '<p class="card__text">\n'

    # Diet
    if animal_obj.get("characteristics") and "diet" in animal_obj["characteristics"]:
        output += f'<strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}<br/>\n'

    # Location
    if isinstance(animal_obj.get("locations"), list) and animal_obj["locations"]:
        output += f'<strong>Location:</strong> {animal_obj["locations"][0]}<br/>\n'

    # Type
    if animal_obj.get("characteristics") and "type" in animal_obj["characteristics"]:
        output += f'<strong>Type:</strong> {animal_obj["characteristics"]["type"]}<br/>\n'

    output += '</p>\n'  # Close <p> tag
    output += '</li>\n' # Close <li> tag

    return output # Return the complete HTML string for the animal


def main():
    # Load JSON file
    animals_data = load_data("animals_data.json")

    # Generate all animals' information as <li> items
    output = ""  # Initialize an empty string to store all animals' HTML
    for animal in animals_data:
        output += serialize_animal(animal)  # Append each animal's HTML

    # Read "animals_template.html" file
    with open("animals_template.html", "r") as template_file:
        template_content = template_file.read()

    # Replace placeholder with generated animal information
    updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # Write new content to "animals.html"
    with open("animals.html", "w") as output_file:
        output_file.write(updated_html)

