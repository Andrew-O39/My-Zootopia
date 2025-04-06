import json

def load_data(file_path):
  """ Loads a JSON file """
  try:
    with open(file_path, 'r') as handle:
      data = json.load(handle)
      return data
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    return None
  except json.JSONDecodeError as e:
    print(f"Error: Failed to decode JSON in '{file_path}': {e}")
    return None
  except Exception as e:
    print(f"Unexpected error while loading '{file_path}': {e}")
    return None