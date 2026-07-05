from ultralytics import YOLO
import cv2
from datetime import datetime

model = YOLO(
    r"C:\Users\Saideepu Balaraju\Desktop\DriverDrowsinessDataset\runs\detect\train\weights\best.pt"
)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5)

    annotated_frame = results[0].plot()

    # Save confidence scores
    with open("confidence_log.txt", "a") as f:
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            line = (
                f"{datetime.now()} | "
                f"{model.names[class_id]} | "
                f"{confidence:.4f}\n"
            )

            print(line.strip())
            f.write(line)

    cv2.imshow("Driver Drowsiness Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()