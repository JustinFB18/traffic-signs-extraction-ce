import os
import subprocess
import shutil
from concurrent.futures import ProcessPoolExecutor, as_completed

# Configuration
INPUT_BASE_PATH = 'signs'
OUTPUT_BASE_PATH = 'dataset'
CATEGORIES = ['informative_signal', 'prevention_sign', 'regulation_sign']

def process_json(json_path, input_folder, output_folder):
    base_name = os.path.splitext(os.path.basename(json_path))[0]
    temp_output_folder = os.path.join(input_folder, base_name)

    subprocess.run(
        ['labelme_export_json', json_path],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    expected_files = {
        'img.png': f'{base_name}_img.png',
        'label.png': f'{base_name}_label.png',
        'label_viz.png': f'{base_name}_label_viz.png',
        'label_names.txt': f'{base_name}_label_names.txt'
    }

    for original, renamed in expected_files.items():
        src = os.path.join(temp_output_folder, original)
        dst = os.path.join(output_folder, renamed)
        if os.path.exists(src):
            shutil.move(src, dst)

    if os.path.isdir(temp_output_folder):
        shutil.rmtree(temp_output_folder)

    return f"==> Processed: {json_path}"


if __name__ == '__main__':
    # Create output folders if needed
    for category in CATEGORIES:
        os.makedirs(os.path.join(OUTPUT_BASE_PATH, category), exist_ok=True)

    # Build tasks
    tasks = []
    for category in CATEGORIES:
        input_folder = os.path.join(INPUT_BASE_PATH, category)
        output_folder = os.path.join(OUTPUT_BASE_PATH, category)
        for file in os.listdir(input_folder):
            if file.endswith('.json'):
                json_path = os.path.join(input_folder, file)
                tasks.append((json_path, input_folder, output_folder))

    # Determine number of workers
    max_workers = os.cpu_count() // 2
    print(f"🔄 Starting parallel processing of {len(tasks)} JSON files with {max_workers} workers...")

    # Execute in parallel
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_json, *args) for args in tasks]
        for future in as_completed(futures):
            print(future.result())

    print(f"\nAll files processed and saved to: {OUTPUT_BASE_PATH}")
