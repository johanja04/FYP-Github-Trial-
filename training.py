from ultralytics import YOLO

def main():
    # nano is the fastest model to run on a laptop
    model = YOLO('yolov8n.pt') 

    # training
    results = model.train(
        data='data.yaml',
        imgsz=640,      # 640x640 yolo standard
        batch=8,       # crashes at 16 on vscode
        name='cricket_ball_model_v2',
        device='cpu'
    )

    # 3. Validation
    metrics = model.val()
    print(f"Maps: {metrics.box.map}") # Mean Average Precision

if __name__ == '__main__':
    main()