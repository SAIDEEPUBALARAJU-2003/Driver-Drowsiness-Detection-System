from ultralytics import YOLO

model = YOLO(
    r"C:\Users\Saideepu Balaraju\Desktop\DriverDrowsinessDataset\runs\detect\train\weights\last.pt"
)

model.train(resume=True)