import json
import os


class DataSaver:
    def __init__(self, directory="output_files"):
        self.directory = directory

    def save_data_to_json(self, data, query):
        try:
            # Create directory if it doesn't exist
            if not os.path.exists(self.directory):
                os.makedirs(self.directory)

            # Create a file path based on the query name
            file_path = os.path.join(self.directory, f"{query}.json")

            # Load existing data from the file if it exists
            existing_data = []
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    existing_data = json.load(file)

            # Append new data to existing data
            existing_data.extend([item.__dict__ for item in data])

            # Save combined data to JSON file
            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)

        except OSError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
