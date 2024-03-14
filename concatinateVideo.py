import cv2

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

if __name__ == "__main__":
    video1_path = "test1.avi"  # Replace with the path to your first video
    video2_path = "test2.avi"  # Replace with the path to your second video
    output_path = "concatTest.avi"  # Replace with the desired output path

    concatenate_videos(video1_path, video2_path, output_path)
