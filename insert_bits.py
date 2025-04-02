import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

def plot(x, y, x_name="time", y_name="data"):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)

    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(y_name + " as a graph of " + x_name)
    plt.grid()
    plt.show()


def read_wav_file(filename):
    rate, data = wav.read(filename)
    dt=1.0/rate
    # time=np.arange(0, len(data)*dt, dt)
    time = np.zeros(len(data))
    t=0
    for i in range(0, len(time)):
       time[i] = t
       t += dt
    return rate, data, time

def write_wav_file(filename, sample_rate, amp_axis):
    wav.write(filename, sample_rate, amp_axis.astype('int16'))

def get_time(rate,data):
    dt = 1.0 / rate
    return np.arange(0, len(data) * dt, dt)

def insert_func_into_data_section(time_axis, amp_axis, func):
    ams_out = np.zeros(len(time_axis))
    for i in range(time_axis.size):
        ams_out[i] = (func(time_axis[i]) + amp_axis[i])
    return ams_out

def insert_func_into_data_section_by_index(time_axis, amp_axis, func, initial_index, final_index):
    """
    this function returns nothing and changes the amp_axis itself
    """
    for i in range(initial_index, final_index):
        amp_axis[i] += func(time_axis[i])



def sin(t, freq = 300000, amp = 2000):
    return int(amp * np.sin(t*freq))
def cos(t, freq = 1, amp = 1):
    return int(amp * np.cos(t*freq))



if __name__ == '__main__':
    rate, data, time = read_wav_file('test_recording_1.wav')
    # plot(time, data)
    # print('rate = ', rate)
    new_data = insert_func_into_data_section(time, data, sin)
    # plot(time, new_data,y_name="new_amplitude")
    write_wav_file("test_recording_1_output.wav", rate, new_data)
