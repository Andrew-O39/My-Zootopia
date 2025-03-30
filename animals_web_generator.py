import json

from load_data import load_data # import function to load JSON data

# Load JSON file
animals_data = load_data("animals_data.json")

# Generate animal information as a single <ul> list with <li> items

output = "<ul class='cards'>\n"
for animal in animals_data:
    output += "<li class='cards__item'>\n"

    if "name" in animal:
        output += f"<div class='card__title'>{animal['name']}</div>\n"

    output += "<p class='card__text'>\n"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"

    if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
        output += f" <strong>Location:</strong> {animal['locations'][0]}<br/>\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"

    output += "</p>\n  </li>\n"
output += "</ul>\n"

# Read "animals_template.html"
with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

# Replace placeholder with generated animal info
updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new content to animals.html
with open("animals.html", "w") as output_file:
    output_file.write(updated_html)

