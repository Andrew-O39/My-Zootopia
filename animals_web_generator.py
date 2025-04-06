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
    try:
        # Load JSON file
        animals_data = load_data("animals_data.json")
    except FileNotFoundError:
        print("Error: 'animals_data.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to parse 'animals_data.json'. Is 'animals_data.json' a valid JSON file?")
        return
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
        return

    if not animals_data or not isinstance(animals_data, list):
        print("Error: No valid animal data found in 'animals_data.json'.")
        return

    # Generate HTML for all animals
    output_lines = []
    for animal in animals_data:
        output_lines.append(serialize_animal(animal)) # Append each animal's HTML
    output = ''.join(output_lines)

    try:
        # Read "animals_template.html" file
        with open("animals_template.html", "r") as template_file:
            template_content = template_file.read()
    except FileNotFoundError:
        print("Error: 'animals_template.html' file not found.")
        return
    except Exception as e:
        print(f"Unexpected error while reading template: {e}")
        return

    # Replace placeholder with generated animal information
    if "__REPLACE_ANIMALS_INFO__" not in template_content:
        print("Warning: Placeholder '__REPLACE_ANIMALS_INFO__' not found in template.")
        return
    updated_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    try:
        # Write new content to "animals.html"
        with open("animals.html", "w") as output_file:
            output_file.write(updated_html)
        print("Successfully generated 'animals.html'")
    except Exception as e:
        print(f"Error: Failed to write 'animals.html': {e}")

# Run the main program
if __name__ == "__main__":
    main()