import json

from load_data import load_data # import function to load JSON data

# Load JSON file
animals_data = load_data("animals_data.json")

# Generate animal information as an HTML string
output = " "
for animal in animals_data:
    if "name" in animal:
        output += f"Name: {animal['name']}\n"

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f"Diet: {animal['characteristics']['diet']}\n"

    if "locations" in animal and isinstance(animal["locations"], list) and animal["locations"]:
        output += f"Location: {animal['locations'][0]}\n"

    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f"Type: {animal['characteristics']['type']}\n"


# Read "animals_template.html"
with open("animals_template.html", "r") as template_file:
    template_content = template_file.read()

# Replace placeholder with generated animal info
updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# Write new content to animals.html
with open("animals.html", "w") as output_file:
    output_file.write(updated_html)

