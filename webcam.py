from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO(
    r"C:\Users\Saideepu Balaraju\Desktop\DriverDrowsinessDataset\runs\detect\train\weights\best.pt"
)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Run detection
    results = model(frame, conf=0.5)

    # Draw bounding boxes and confidence scores
    annotated_frame = results[0].plot()

    # Print detections in terminal
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        print(
            f"Class: {model.names[class_id]} | "
            f"Confidence: {confidence:.4f}"
        )

    # Show webcam output
    cv2.imshow("Driver Drowsiness Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()