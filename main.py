# You need to write a Python script that has the ability to read an audio file (.wav format) and do the following: - done
# - print summary report - length of the audio, sampling frequency - done
# - show a graph of the audio signal - done
# - split the audio into 5-second chunks and save them to the disk. - done



import matplotlib.pyplot as plt
import numpy as np
import wave


def read_file(path):
    raw = wave.open(path)
    return raw


def summary_report(raw):
    sampling_frame_rate = raw.getframerate()
    no_of_frames = raw.getnframes()
    length_of_audio = no_of_frames / float(sampling_frame_rate)
    return length_of_audio, sampling_frame_rate


def plot_audio_signal(raw):
    sampling_frame_rate = raw.getframerate()
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype ="int16")
    time = np.linspace(0, len(signal) / sampling_frame_rate, num = len(signal))
     
    plt.figure(1)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal)
    plt.show()


def split_five_seconds(raw, length_of_audio, sampling_frame_rate, output_folder_file):
    parameters = raw.getparams()
    no_of_frames = raw.getnframes()
    split_time_chunks = 5 * sampling_frame_rate
    start_frame = 0

    for i in range(0, no_of_frames, split_time_chunks):

        if i == no_of_frames:
            break

        end_frame = (i + split_time_chunks)
        output_file = output_folder_file + "/" +str(i) + "_" + str(i + split_time_chunks) + ".wav"
        print(output_file)


        with wave.open(output_file, 'wb') as split_file:
            split_file.setparams(parameters)
            raw.setpos(start_frame)
            split_file.writeframes(raw.readframes(end_frame - start_frame))


        start_frame = end_frame

    raw.close()
    print("Successfully Splitted Audio in different chunks")


if __name__ == "__main__":

    folder_file = "Audio_Files/"
    input_folder_file = input("Enter your folder path and audio file path. For Eg: Folder_Name/test.wav\n")
    raw = read_file(folder_file + input_folder_file)
    print("File Successfully Read")

    length_of_audio, sampling_frame_rate = summary_report(raw)
    print("Length of the Audio = ", str(length_of_audio) + " Seconds")
    print("Sampling Frame Rate = ", sampling_frame_rate)

    plot_audio_signal(raw)

    output_folder_file = folder_file + input_folder_file.split("/")[0]
    split_five_seconds(raw, length_of_audio, sampling_frame_rate, output_folder_file)


