from ultralytics import YOLO

model=YOLO("yolov8n.pt")
model.train(data="dataset.yaml",epochs=50,imgsz=640,batch=16,device= "cpu")
model.export(format="onnx")

#Evaluate model
#metrics=model.val()
#print(metrics)
