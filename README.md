# traffic-signs-extraction-ce

This project is part of the Computer Engineering Application Project course at TEC. It is designed to provide a software platform for background extraction and semantic element identification, specifically for traffic signs.

## Project Structure and File Explanations

- **dataset_builder.py**: Builds a dataset from JSON annotations (created with LabelMe) for different categories of traffic signs. It processes the JSON files, exports images and labels, and organizes them into a dataset structure for training.
- **numbers_to_labels.py**: Updates the label fields in JSON annotation files to use semantic labels based on their folder/category.
- **requirements.txt**: Lists the required Python packages. The main dependency is `labelme` (used for annotation and export).
- **training-dpt.ipynb**: Jupyter notebook for training a deep learning model (DPT) for semantic segmentation or background extraction. Includes steps for environment setup, data loading, and model training.
- **vtti-unified-notebook.ipynb**: Jupyter notebook for video frame extraction and processing, this is the main code who generate the cloud points file (.pcd).

## How to Use This Repository

### 1. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 2. Prepare Your Data

- Organize your raw images and annotation JSON files in a folder structure like:
  - `signs/informative_signal/`
  - `signs/prevention_sign/`
  - `signs/regulation_sign/`
- Each folder should contain images and their corresponding LabelMe JSON files.

### 3. Update Labels in JSON Files

Run the following script to update the `label` fields in all JSON files according to their category:

```bash
python numbers_to_labels.py
```

### 4. Build the Dataset

Run the dataset builder script to process the JSON files and export the images and labels into a dataset structure:

```bash
python dataset_builder.py
```

This will create a `dataset/` folder with subfolders for each category, containing the processed images and label files.

### 5. Train the Model

Open `training-dpt.ipynb` in Jupyter Notebook or VS Code and follow the steps to train the DPT model on your dataset.

### 6. Cloud Point Generation

Use `vtti-unified-notebook.ipynb` to extract frames from videos and generate point cloud files (.pcd) based on semantic segmentation and monocular depth estimation.


## Notes
- Ensure you have [LabelMe](https://github.com/wkentaro/labelme) installed and available in your PATH for dataset export.
- The scripts assume a specific folder structure for input data. Adjust paths as needed for your setup.
- For large datasets, the processing scripts use parallel execution to speed up annotation export.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.