# main.py

import cv2
import os
import time
from config import *
from detector import load_model, detect
from utils import log_event, generate_filename, ensure_directory


def main():
    print("🚀 Starting High Accuracy Waste Detection...")

    ensure_directory(SAVE_PATH)

    model = load_model()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Camera not accessible")
        return

    print("📷 Camera started. Press 'q' to quit")

    last_saved_time = 0
    COOLDOWN = 5

    previous_labels = []
    stable_count = 0

    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            break

        detections = detect(model, frame)

        filtered_detections = []

        for label, box, conf in detections:

            # ✅ Allowed classes filter
            if label not in ALLOWED_CLASSES:
                continue

            (x1, y1, x2, y2) = box

            # ✅ Size filter
            frame_area = frame.shape[0] * frame.shape[1]
            box_area = (x2 - x1) * (y2 - y1)

            if box_area < 0.01 * frame_area:
                continue

            # ✅ Strict confidence filtering
            if label == "bottle" and conf < 0.7:
                continue

            if label == "cell phone" and conf < 0.65:
                continue

            filtered_detections.append((label, box, conf))

        # 🧠 Temporal stability
        current_labels = [label for label, _, _ in filtered_detections]

        if current_labels == previous_labels:
            stable_count += 1
        else:
            stable_count = 0

        previous_labels = current_labels

        # 🎨 Draw boxes
        for label, box, conf in filtered_detections:
            (x1, y1, x2, y2) = box

            category = WASTE_CATEGORIES.get(label, "Not Waste")

            color = COLOR_WASTE if category != "Not Waste" else COLOR_PERSON

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            text = f"{label} ({category}) {conf:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # 🚨 Save only when stable + cooldown
        current_time = time.time()

        waste_detected = any(
            label in WASTE_CATEGORIES for label, _, _ in filtered_detections
        )

        if waste_detected and stable_count > 5 and (current_time - last_saved_time > COOLDOWN):

            filename = generate_filename()
            filepath = os.path.join(SAVE_PATH, filename)

            cv2.imwrite(filepath, frame)
            log_event(LOG_FILE, f"Waste detected: {filename}")

            print(f"♻️ Saved: {filename}")

            last_saved_time = current_time

        cv2.imshow("High Accuracy Waste Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()