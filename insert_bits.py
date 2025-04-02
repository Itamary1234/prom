import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from finding_start import *


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
    dt = time_axis[1] - time_axis[0]
    initial_ind = int(initial_time / dt)
    final_ind = int(final_time / dt)
    for i in range(initial_ind,final_ind):
        amp_axis[i] = (func(time_axis[i]-initial_time) + amp_axis[i])

def insert_func_into_data_section_by_index(time_axis, amp_axis, func, initial_index, final_index):
    """
    this function returns nothing and changes the amp_axis itself
    """
    for i in range(initial_index, final_index):
        amp_axis[i] += func(time_axis[i])



def start_func(t):
    return 531 * np.sin(t * 2 * np.pi)
def func0(t):
    return 299 * np.sin(t*1031)
def func1(t):
    return 307 * np.sin(t*1474)
def func2(t):
    return 347 * np.sin(t*1221)
def func3(t):
    return 273 * np.sin(t*1741)


def encode_information(time_axis, amp_axis, initial_time, information, func_array=None, t_bit = 0.2):
    '''
    this function changes amps itself
    :param time_axis:
    :param amp_axis:
    :param initial_time: the time to start sending the bits
    :param information: array of the bits [0,1,2,2,3...]
    :param func_array: all the function matching the bits
    :param t_bit: time of each bit
    :return: nothing
    '''
    if func_array is None:
        func_array = [func0, func1, func2, func3]
    current_time = initial_time
    for bit in information:
        f = func_array[bit]
        insert_func_into_data_section_by_time(time_axis, amp_axis, f, current_time, current_time + t_bit)
        current_time = current_time + t_bit


def encrypt(time_axis, amp_axis):
    '''
    this function changes amps itself to contain the message
    :param time_axis:
    :param amp_axis:
    :return:
    '''
    message_array = arr = [0] * 13 + [1] * 13 + [2] * 12 + [3] * 12
    insert_func_into_data_section_by_time(time_axis, amp_axis, start_func, 5.3, 6.3)
    encode_information(time_axis, amp_axis, 6.3,message_array)

if __name__ == '__main__':
    for i in range(13):
        print(1,end=",")
    rate, data, time = read_wav_file('song_2_shakira.wav')
    # plot(time, data)
    # print('rate = ', rate)
    plot(time, data)
    encrypt(time, data)
    plot(time, data,"new")

    # new_data = insert_func_into_data_section_by_time(time, data, sin1,3.6,4.6)

    # plot(time, new_data,y_name="new_amplitude")
    #
    #
    # start_ind = rec_find_start(1, time, new_data, sin1, 10000)
    # print(start_ind)
    #
    #
    # write_wav_file("song_2_shakira_out.wav", rate, data)
