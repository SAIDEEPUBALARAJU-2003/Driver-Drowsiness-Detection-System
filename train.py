from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data=r"C:\Users\Saideepu Balaraju\Desktop\DriverDrowsinessDataset\data.yaml",
    epochs=100,
    imgsz=640,
    batch=8,
    device="cpu",
    patience=20,
    workers=2
)