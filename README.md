# 🧠 Smart Waste Detection & Classification System (YOLOv8)

## 📌 Overview

This project is an AI-based system that detects and classifies waste in real-time using computer vision. It leverages YOLOv8 for object detection and identifies different types of waste such as recyclable, organic, hazardous, and general waste.

The system is designed as a step towards building intelligent monitoring solutions for cleaner public environments.

---

## 🚀 Features

* 🎥 Real-time object detection using webcam
* ♻️ Waste classification into multiple categories
* 🧾 Automatic image capture on detection
* 🗂️ Logging of detected waste events
* ⚡ Lightweight and fast using YOLOv8
* 🧠 Extendable for future features like throw detection

---

## 🛠️ Tech Stack

* Python
* OpenCV
* YOLOv8 (Ultralytics)
* NumPy

---

## 📂 Project Structure

```
Waste-Detection/
│
├── main.py              # Main execution file
├── detector.py          # YOLO model loading & detection
├── config.py            # Configuration (classes, paths)
├── utils.py             # Helper functions
│
├── outputs/             # Saved images & logs (ignored in git)
├── models/              # Pretrained models (ignored in git)
│
├── README.md
├── LICENSE
├── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/waste-detection.git
cd waste-detection
```

### 2. Install dependencies

```
pip install ultralytics opencv-python numpy
```

### 3. Run the project

```
python main.py
```

---

## 📸 Sample Output

(Add screenshots here)

Example:

* Detected object: Bottle → Plastic Waste
* Detected object: Banana → Organic Waste

---

## ⚠️ Notes

* Dataset and trained models are not included due to size constraints.
* The system uses a pretrained YOLO model and can be further improved with custom training.
* Accuracy depends on lighting, camera angle, and dataset quality.

---

## 🔮 Future Improvements

* 🎯 Detect actual “waste throwing” actions
* 📊 Add dashboard for analytics
* 🧠 Improve accuracy using custom-trained models
* 🌐 Deploy as a web or mobile application

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Yagnesh Kasumurthi

---

## ⭐ Acknowledgements

* YOLOv8 by Ultralytics
* OpenCV community
