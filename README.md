# Diagnosis of Acute Lymphoblastic Leukemia (ALL) using Image Processing

This project detects Acute Lymphoblastic Leukemia (ALL) from microscopic images of peripheral blood smears using image processing techniques. The application is built using OpenCV for image analysis and Tkinter for a user-friendly interface.

## Features
- Load blood smear images from your computer
- Convert images to HSV color space for better segmentation
- Apply color-based filtering to isolate potential leukemia cells
- Display both original and processed images

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/ALL-Diagnosis.git
   cd ALL-Diagnosis
   ```
2. **Install dependencies**:
   ```sh
   pip install opencv-python numpy pillow
   ```
3. **Run the application**:
   ```sh
   python leukemia_diagnosis_gui.py
   ```

## Usage
1. Click the "Load Image" button to select a blood smear image.
2. The original image and processed version will be displayed side by side.
3. The processing highlights potential leukemia cells using color segmentation.

## Screenshot
![Processed Image](screenshot.png)

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy
- Pillow (for Tkinter image handling)

## Contributing
Feel free to open issues or submit pull requests!

## License
This project is licensed under the MIT License.
