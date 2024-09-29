import os
import shutil


def dynamic_interval_sampling(frames, desired_num_samples):
    total_frames = len(frames)
    interval = max(1, total_frames // desired_num_samples)
    return frames[::interval]


inp = "Vandalism"
out = inp + "_Sampled"

input_dir = os.path.join(os.getcwd(), inp)
output_dir = os.path.join(os.getcwd(), out)

os.makedirs(output_dir, exist_ok=True)

for root, dirs, files in os.walk(input_dir):
    for dir in dirs:
        input_folder = os.path.join(root, dir)

        # List all files (frames) in the current folder
        frames = os.listdir(input_folder)

        print(f"Length of samples in {dir} is: {len(frames)}")

        # Sample frames using dynamic interval
        sampled_frames = dynamic_interval_sampling(frames, 20)

        # Ensure output directory exists
        output_folder = os.path.join(output_dir, dir)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Move sampled frames to output directory
        for frame in sampled_frames:
            frame_path = os.path.join(input_folder, frame)
            output_frame_path = os.path.join(output_folder, frame)
            # print(f"Copying frame {frame_path} to {output_frame_path}")
            shutil.copy(frame_path, output_frame_path)
            print(f"Frame {frame} copied to {output_frame_path}")
