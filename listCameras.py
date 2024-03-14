import cv2

def print_available_cameras():
    for i in range(10):  # Check up to 10 devices
        cap = cv2.VideoCapture(i)
        if not cap.isOpened():
            break
        print(f"Camera {i}: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}x{cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
        cap.release()

if __name__ == "__main__":
    print_available_cameras()
