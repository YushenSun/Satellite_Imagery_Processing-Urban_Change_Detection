# Satellite Imagery Processing - Urban Change Detection

## Overview

This repository contains the implementation of a project focused on processing satellite imagery to detect urban changes over time. The project leverages advanced geospatial techniques and image processing algorithms to analyze satellite images, identifying areas of urban expansion, infrastructure development, and other significant changes.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Description

The aim of this project is to develop a pipeline that can process satellite imagery to detect and analyze urban changes over time. This is particularly useful for urban planners, environmental monitoring agencies, and researchers who need to monitor urban growth, deforestation, or other land use changes.

Key objectives include:

- **Image Preprocessing**: Prepare satellite images by applying various preprocessing techniques such as normalization, noise reduction, and alignment.
- **Change Detection**: Implement algorithms to detect and quantify changes in urban areas across different time periods.
- **Visualization**: Create visual representations of the detected changes to facilitate interpretation and decision-making.

## Features

- **Multi-temporal Image Analysis**: Analyze images from different time periods to detect changes in urban areas.
- **Automated Change Detection**: Automatically identify and quantify changes using machine learning and image processing techniques.
- **Customizable Analysis**: The analysis pipeline can be adjusted to focus on specific types of changes or regions of interest.
- **Visualization Tools**: Generate maps and visual summaries of detected changes for easy interpretation.

## Installation

To set up the project, clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/YushenSun/Satellite-Imagery-Processing.git
cd Satellite-Imagery-Processing
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Ensure that additional geospatial libraries like GDAL, Rasterio, and OpenCV are installed:

```bash
pip install gdal rasterio opencv-python
```

## Usage

### Preprocessing Images

To preprocess satellite images before analysis:

```bash
python preprocess.py --input=path_to_input_image --output=path_to_output_image
```

This script will normalize and align the input images to prepare them for change detection analysis.

### Detecting Changes

To detect changes in urban areas between different time periods:

```bash
python detect_changes.py --before=path_to_earlier_image --after=path_to_later_image --output=path_to_change_map
```

This command will produce a map highlighting areas where significant changes have occurred.

### Visualization

To visualize the detected changes:

```bash
python visualize.py --change_map=path_to_change_map --output=path_to_visualization
```

This will generate a visual representation of the detected changes, making it easier to understand the extent and nature of urban development.

## Results

The results of this project include detailed maps showing areas of urban expansion, infrastructure development, or other land-use changes. Example outputs can be found in the `results/` directory.

### Example Outputs

- **Urban Expansion Map**: Shows areas where significant urban development has occurred over time.
- **Deforestation Detection**: Identifies areas where forests have been cleared, making way for urban or agricultural development.

## Technologies

- **Geospatial Analysis**: GDAL, Rasterio, Shapely
- **Image Processing**: OpenCV, NumPy
- **Machine Learning**: Scikit-learn (for change detection)
- **Visualization**: Matplotlib, Plotly

## Contributing

Contributions are welcome! If you have ideas for improving the project, adding new features, or fixing bugs, feel free to contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, feedback, or suggestions, please contact:

- **Yushen Sun**
- [LinkedIn](https://www.linkedin.com/in/syushen/)
- [Email](mailto:sun.yushen@gmail.com)
