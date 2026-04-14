from ultralytics import YOLO

def main():
    model = YOLO('best.pt') # update path to your best.pt file

    results = model.predict(
        source='test_video2.mp4',                 
    
        show=True,
        save=True,
        conf=0.5
    )

if __name__ == '__main__':
    main()