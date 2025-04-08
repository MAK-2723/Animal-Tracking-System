import cv2
import threading
from detection import detect_animals, load_model
import numpy as np

class CameraStream:
    """Handles real-time video capture and processing."""
    def __init__(self, camera_index=0, model_path="yolov8.pt"):
        self.camera_index = camera_index
        self.model = load_model(model_path)
        self.cap = cv2.VideoCapture(self.camera_index)
        self.running = False

    def start(self):
        """Starts the camera stream in a separate thread."""
        self.running = True
        threading.Thread(target=self.capture_frames, daemon=True).start()

    def stop(self):
        """Stops the camera stream."""
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()

    def capture_frames(self):
        """Captures video frames and processes them for detection."""
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                break
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert for YOLO compatibility
            detections = detect_animals(frame_rgb, self.model)
            self.display_results(frame, detections)

    def display_results(self, frame, detections):
        """Displays the detection results on the video feed."""
        for detection in detections:
            x1, y1, x2, y2 = detection["bbox"]
            label = f"{detection['species']} ({detection['confidence']*100:.1f}%)"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        cv2.imshow("Animal Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop()

if __name__ == "__main__":
    stream = CameraStream()
    stream.start()