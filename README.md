# 🧙 Invisible Cloak - Harry Potter Effect

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-orange)
![Real-time](https://img.shields.io/badge/Real--Time-Vision-green)

Create magical invisibility effects using computer vision and color masking.



## ✨ Features
- Real-time background replacement
- Dual-range color detection
- Morphological noise reduction
- Webcam integration
- Customizable color ranges

## 🚀 Quick Start

```bash
git clone https://github.com/yourusername/invisible-cloak.git
cd invisible-cloak
pip install -r requirements.txt
python invisible_cloak.py
```
## 🧰 How It Works
## 🔍 Color Masking
```python
# Detect red color (two ranges for hue wrap-around)
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
```
## 🖼️ Background Handling
```python
# Capture initial background
for i in range(30):
    ret, background = cap.read()
```
## ✨ Effect Composition
```python
# Combine masked areas
output = cv2.add(
    cv2.bitwise_and(background, background, mask=mask_inv),
    cv2.bitwise_and(frame, frame, mask=mask)
```

## 🛠 Customization Parameters

| Parameter          | Default Value       | Description                  |
|--------------------|---------------------|------------------------------|
| **MORPH_OPEN**     | `(5,5) kernel`      | Kernel size for noise removal |
| **LOWER_RED**      | `[0,120,70]`       | Lower HSV threshold (Range 1) |
| **UPPER_RED**      | `[10,255,255]`     | Upper HSV threshold (Range 1) |
| **LOWER_RED2**     | `[170,120,70]`     | Lower HSV threshold (Range 2) |
| **UPPER_RED2**     | `[180,255,255]`    | Upper HSV threshold (Range 2) |
| **BACKGROUND_FRAMES** | `30`            | Frames for background capture |

### 💡 Adjustment Tips:
```python
# Example: Change noise reduction kernel
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7,7), np.uint8))

# Example: Modify red detection range
lower_red1 = np.array([0,100,50])  # More sensitive
upper_red1 = np.array([15,255,255]) # Wider range






