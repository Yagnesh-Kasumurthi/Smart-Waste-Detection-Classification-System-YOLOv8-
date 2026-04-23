# detector.py

from ultralytics import YOLO

model = None


def load_model():
    global model
    print("🔄 Loading YOLO model...")
    model = YOLO("yolov8m.pt")  # 🔥 better accuracy than n
    print("✅ YOLO model loaded")
    return model


def detect(model, frame, conf_threshold=0.6):
    results = model(frame)

    detections = []

    for r in results:
        for box in r.boxes:
            conf = float(box.conf[0])

            if conf < conf_threshold:
                continue

            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            detections.append((label, (x1, y1, x2, y2), conf))

    return detections