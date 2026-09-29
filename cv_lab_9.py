import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "images2.jpg"

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if img is None:
    raise FileNotFoundError(
        f"Image not found or could not be loaded at: {image_path}"
    )

print(f"Successfully loaded image: {image_path} with shape {img.shape}")

# Gaussian noise
mean = 0
std_dev = 25
noise = np.random.normal(mean, std_dev, img.shape)

# Add noise and keep pixel values in the valid range
noisy_image = np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)

# Display original and noisy images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(noisy_image, cmap="gray")
plt.title("Noisy Image (Gaussian Noise)")
plt.axis("off")

plt.tight_layout()
plt.show()
