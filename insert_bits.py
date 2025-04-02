import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from finding_start import *
import soundfile as sf


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
    if data.ndim == 2:
        new_data = np.zeros(len(data))
        for i in range(len(data)):
            new_data[i] = data[i][0]#+data[i][1]
        data = new_data
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

def insert_func_into_data_section_by_time(time_axis, amp_axis, func, initial_time, final_time):
    '''

    :param time_axis:
    :param amp_axis:
    :param func:
    :param initial_time: the time we start
    :param final_time:
    :return:
    '''
    ams_out = amp_axis.copy()
    dt = time_axis[1] - time_axis[0]
    initial_ind = int(initial_time / dt)
    print("initial_ind = " + str(initial_ind))
    final_ind = int(final_time / dt)
    print("final_ind = " + str(final_ind))
    for i in range(initial_ind,final_ind):
        ams_out[i] = (func(time_axis[i]-initial_time) + amp_axis[i])
    return ams_out

def insert_func_into_data_section_by_index(time_axis, amp_axis, func, initial_index, final_index):
    """
    this function returns nothing and changes the amp_axis itself
    """
    for i in range(initial_index, final_index):
        amp_axis[i] += func(time_axis[i])



def sin(t, freq = 1, amp = 1000):
    return amp * np.sin(t*freq)
def cos(t, freq = 1, amp = 1):
    return amp * np.cos(t*freq)
def sin1(t, freq = 2 * np.pi, amp = 2000):
    return amp * np.sin(t*freq)
def cos1(t, freq = 50, amp = 1):
    return amp * np.cos(t*freq)



if __name__ == '__main__':
    rate, data, time = read_wav_file('song_2_shakira.wav')
    # plot(time, data)
    # print('rate = ', rate)
    plot(time, data)

    new_data = insert_func_into_data_section_by_time(time, data, sin1,0.6,1.6)
    plot(time, new_data,y_name="new_amplitude")

    #corr_func = find_bits(1, 5, time, new_data, [sin, cos, sin1, cos1])
    #print(corr_func)
    start_ind = find_start(1, time, new_data, cos1)
    print(start_ind)


    write_wav_file("song_2_shakira_out.wav", rate, data)
