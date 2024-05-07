import cv2
import datetime
import time

def capture_video(duration_seconds=60):
    # Open the default camera (usually the built-in webcam)
    cap = cv2.VideoCapture(0)

    # Get current date for the output filename
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    output_filename = f"dailyCapture_{current_date}.avi"

    # Set the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (640, 480))

    # Record video for the specified duration
    start_time = time.time()
    while time.time() - start_time < duration_seconds:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('Recording', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":

    # Set the scheduled time for recording (in 24-hour format)
    scheduled_time = datetime.time(13, 37)

    while True:
        # Get the current time
        current_time = datetime.datetime.now().time()

        # Check if it's time to start recording
        if current_time.hour == scheduled_time.hour and current_time.minute == scheduled_time.minute:
            print(f"Recording video at {current_time}")
            capture_video()
            print("Video recording completed.")
            break
        else:
            # If it's not time yet, wait for a minute before checking again
            time.sleep(60)
