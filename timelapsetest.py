import cv2
import datetime
import time



def upload_to_youtube(video_file, title, description, category, keywords, privacy_status):
    args = argparser.parse_args(["--file=" + video_file, "--title=" + title, "--description=" + description,
                                 "--category=" + category, "--keywords=" + keywords, "--privacyStatus=" + privacy_status])
    youtube = get_authenticated_service(args)
    try:
        initialize_upload(youtube, args)
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred:\n{e.content}")

def concatenate_videos(video1_path, video2_path, output_path):
    # Open the input videos
    video1 = cv2.VideoCapture(video1_path)
    video2 = cv2.VideoCapture(video2_path)

    # Get the properties of the input videos
    width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video1.get(cv2.CAP_PROP_FPS)

    # Create a VideoWriter object for the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Read and write frames from the first video
    while True:
        ret, frame = video1.read()
        if not ret:
            break
        out.write(frame)

    # Read and write frames from the second video
    while True:
        ret, frame = video2.read()
        if not ret:
            break
        out.write(frame)

    # Release resources
    video1.release()
    video2.release()
    out.release()

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


            video1_path = "timelapse.avi"  # Replace with the path to your first video
            video2_path = f"dailyCapture_{datetime.datetime.now().strftime('%Y-%m-%d')}.avi"
            output_path = "timelapse.avi"  # Replace with the desired output path

            concatenate_videos(video1_path, video2_path, output_path)

            print("Video concatenation completed.")

            upload_to_youtube(output_path, "My Concatenated Video", "Description", "22", "keyword1,keyword2", "private")


            break
        else:
            # If it's not time yet, wait for a minute before checking again
            time.sleep(60)

