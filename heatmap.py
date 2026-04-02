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

if filename and filename.endswith(('.flac', '.mp3', '.wav')):
    additional_file_path = os.path.join(current_dir, filename)
    if os.path.exists(additional_file_path):
        audio_files.append(additional_file_path)

window_size = 8192
hop_length = 512
bins = np.linspace(-1, 1, 100)

for file_path in audio_files:
    data, sampling_rate = librosa.load(file_path, mono=False, sr=None)
    D_left = np.abs(librosa.stft(data[0], n_fft=window_size, hop_length=hop_length))
    D_right = np.abs(librosa.stft(data[1], n_fft=window_size, hop_length=hop_length))

    mask = D_left >= D_right
    panning_values = np.where(mask, 1 - (D_right / (D_left + 1e-10)), -1 + (D_left / (D_right + 1e-10)))
    panning_values[(D_left == 0) & (D_right == 0)] = 0

    panning_timesteps = np.apply_along_axis(lambda x: np.histogram(x, bins=bins, density=True)[0], 0, panning_values)

    plt.figure(figsize=(15, 5))
    plt.imshow(panning_timesteps, aspect='auto', cmap='cividis', interpolation='hanning', vmax=2.5, extent=[0, D_left.shape[1] * hop_length / sampling_rate, -1, 1])
    
    plt.gca().invert_yaxis()
    plt.yticks([-1, 0, 1], ["Left", "Center", "Right"])
    plt.ylabel('Panning')
    
    duration_sec = librosa.get_duration(y=data[0], sr=sampling_rate)
    times = np.arange(0, duration_sec, 15)
    labels = [f"{int(t // 60):02d}:{int(t % 60):02d}" for t in times]
    plt.xticks(times, labels)

    plt.xlabel('Time (s)')
    plt.title('Panning Heatmap')

    plot_filename = os.path.join(graph_dir, os.path.splitext(os.path.basename(file_path))[0] + '_heatmap.png')
    plt.savefig(plot_filename)