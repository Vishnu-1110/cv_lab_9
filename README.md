# Computer Vision Lab 9 — Gaussian Noise

This project demonstrates how to add **Gaussian noise** to a grayscale image using Python, OpenCV, NumPy, and Matplotlib.

## Objective

To add Gaussian noise to an image and compare the original image with the noisy image.

## Libraries Used

- Python
- OpenCV
- NumPy
- Matplotlib

## Python Code

The complete program is available in [cv_lab_9.py](cv_lab_9.py).

## How It Works

The program:

1. Reads the input image in grayscale.
2. Generates Gaussian noise using NumPy.
3. Uses a mean of **0** and standard deviation of **25**.
4. Adds the noise to the original image.
5. Clips pixel values to the valid range of 0–255.
6. Displays the original and noisy images side by side.

### Gaussian Noise

Gaussian noise is random noise whose values follow a normal distribution. It can be used to simulate sensor noise and other variations that may occur in digital images.

## How to Run

Install the required libraries:

```bash
pip install opencv-python numpy matplotlib
```

Place the input image in the project folder as:

```text
images2.jpg
```

Run:

```bash
python cv_lab_9.py
```

**No Google Colab or Google Drive connection is required.**

## Output

The output contains:

- Original Image
- Noisy Image (Gaussian Noise)

### Output Image

![Gaussian Noise Output](output.png)

## Result

Gaussian noise is added to the original grayscale image, producing the noisy image shown in the output.

## Author

**Vishnu Vardhan**

GitHub: [Vishnu-1110](https://github.com/Vishnu-1110)
