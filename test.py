from ultralytics import YOLO

# Load trained model
model = YOLO(
    r"C:\Users\Saideepu Balaraju\Desktop\DriverDrowsinessDataset\runs\detect\train\weights\best.pt"
)

# Test image
results = model(
    r"C:\Users\Saideepu Balaraju\Downloads\gettyimages-1404571842-640x640.jpg",
    conf=0.1,
    save=True,
    show=True
)

# Print detections
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        print(
            f"Class: {model.names[class_id]} | "
            f"Confidence: {confidence:.4f}"
        )