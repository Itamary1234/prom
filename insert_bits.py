import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from finding_start import *
from CONSTANTS import *

def plot(x, y, x_name="time", y_name="data"):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y)

    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(y_name + " as a graph of " + x_name)
    plt.grid()
    plt.show()

def plot_file(file_path):
    rate, coded_amps, time_axis = read_wav_file(file_path)
    plot(time_axis, coded_amps)


def read_wav_file(filename):
    rate, data = wav.read(filename)
    if data.ndim == 2:
        new_data = np.zeros(len(data))
        for i in range(len(data)):
            new_data[i] = data[i][0]#+data[i][1]
        data = new_data
    # data = np.zeros(len(data))
    data = data.astype(np.float64)
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


    time_slice = time_axis[initial_ind:final_ind] - initial_time

    # Checking if func is tuple, for cos correlation
    if isinstance(func, tuple):
        func = func[0]
    try:
        amp_axis[initial_ind:final_ind] += func(time_slice)
    except FloatingPointError:
        print("FloatingPointError, initial_time = " + initial_time+", final_time = " + final_time)
        amp_axis[initial_ind:final_ind] = 0


def insert_bits_as_sound(time_axis, amp_axis, initial_time, information):
    '''
    this function changes amps itself
    :param initial_time:
    :param time_axis:
    :param amp_axis:
    :param information: array of the bits [0,1,0,1,1,...]
    :param func_array: all the function matching the bits
    :param t_bit: time of each bit
    :return: nothing
    '''
    current_time = initial_time
    for bit in information:
        # now we insert the mini_bits
        for mini_index in range(BIT_LENGTH):
            #we want the index of the mini bit and then the index of the bit and then the sin func
            f1 = MINI_BIT_FUNCTION_ARRAY1[mini_index][bit][0]
            f2 = MINI_BIT_FUNCTION_ARRAY2[mini_index][bit][0]
            f3 = MINI_BIT_FUNCTION_ARRAY3[mini_index][bit][0]
            insert_func_into_data_section_by_time(time_axis, amp_axis, f1, current_time, current_time + T_MINI_BIT)
            insert_func_into_data_section_by_time(time_axis, amp_axis, f2, current_time, current_time + T_MINI_BIT)
            insert_func_into_data_section_by_time(time_axis, amp_axis, f3, current_time, current_time + T_MINI_BIT)
            current_time = current_time + T_MINI_BIT



    # this is the code before mini_bits
    # current_time = initial_time
    # for bit in information:
    #     f = FUNCTION_ARRAY[bit]
    #     insert_func_into_data_section_by_time(time_axis, amp_axis, f, current_time, current_time + T_BIT)
    #     current_time = current_time + T_BIT


def encrypt(time_axis, amp_axis, information : list):
    '''
    this function changes amps itself to contain the message
    :param time_axis:
    :param amp_axis:
    :param information: bits to encode
    :return:
    '''
    # insert_func_into_data_section_by_time(time_axis, amp_axis, test_func, 3.5, 4)
    insert_func_into_data_section_by_time(time_axis, amp_axis, start_func, INITIAL_TIME, INITIAL_TIME + T_WORD)
    insert_bits_as_sound(time_axis, amp_axis, INITIAL_TIME + T_WORD, information)

