import os
import librosa
import numpy as np
import matplotlib.pyplot as plt

filename = os.getenv('FILENAME')
filename_noext = os.getenv('FILENAME_NOEXT')

current_dir = os.path.dirname(os.path.abspath(__file__))
audio_dir = os.path.join(current_dir, 'separated', 'htdemucs', filename_noext)
graph_dir = os.path.join(current_dir, 'graphs', filename_noext)

os.makedirs(audio_dir, exist_ok=True)
os.makedirs(graph_dir, exist_ok=True)

audio_files = [os.path.join(audio_dir, f) for f in os.listdir(audio_dir) if f.endswith(('.flac', '.mp3', '.wav'))]

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

window_size = 10
frame_length = 1024
hop_length = 512

plt.figure(figsize=(18, 6))

for file_path in audio_files:
    y, sr = librosa.load(file_path, sr=None, mono=False, res_type='kaiser_best')
    left_channel = y[0, :]
    right_channel = y[1, :]

    num_frames = 1 + (min(len(left_channel), len(right_channel)) - frame_length) // hop_length
    panning = np.zeros(num_frames)

    for i in range(num_frames):
        start = i * hop_length
        end = start + frame_length
        
        left_energy = np.sum(left_channel[start:end] ** 2)
        right_energy = np.sum(right_channel[start:end] ** 2)
        total_energy = left_energy + right_energy

        panning[i] = (right_energy - left_energy) / (total_energy + 1e-6)

    avg_panning = moving_average(panning, window_size)
    avg_time = librosa.frames_to_time(np.arange(len(avg_panning)), hop_length=hop_length, sr=sr)

    label = os.path.splitext(os.path.basename(file_path))[0]
    plt.plot(avg_time, avg_panning, label=label)

plt.legend(loc='upper right') 
plt.gca().invert_yaxis()    
plt.yticks([-1, 0, 1], ['Left', 'Center', 'Right'])
plt.ylabel('Panning')
duration_sec = len(left_channel) / sr
plt.xticks(np.arange(0, duration_sec, 15),
        [(f"{int(t // 60):02d}:{int(t % 60):02d}") for t in np.arange(0, duration_sec, 15)])
plt.xlim(avg_time[0], avg_time[-1])
plt.xlabel("Time")
plt.tight_layout()
plt.title("Average Panning Over Time")

plot_filename = os.path.join(graph_dir, 'combined_lineplot.png')
plt.savefig(plot_filename)
