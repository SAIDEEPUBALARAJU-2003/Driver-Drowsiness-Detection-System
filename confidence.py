from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model("path_to_image.jpg")

for r in results:
    for box in r.boxes:
        print(
            f"Class: {model.names[int(box.cls[0])]}, "
            f"Confidence: {float(box.conf[0]):.4f}"
        )