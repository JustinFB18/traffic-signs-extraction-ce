import os
import json

# Mapping folder names to labels
folder_to_label = {
    'informative_signal': 'informative',
    'prevention_sign': 'preventive',
    'regulation_sign': 'regulation'
}
# Base path where the folders are located
base_path = 'signs'  

# Process each folder and update JSON files
for folder_name, label in folder_to_label.items():
    folder_path = os.path.join(base_path, folder_name)

    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            json_path = os.path.join(folder_path, filename)

            # Load the JSON file
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for shape in data.get('shapes', []):
                shape['label'] = label

            # Save the modified JSON back to the file
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

print("Labels are updated successfully in JSON files.")
