from finding_bits import *
from insert_bits import *


def test():
    rate, data, time = read_wav_file('test_recording_1.wav')
    # plot(time, data)
    # print('rate = ', rate)
    new_data = insert_func_into_data_section(time, data, cos)
    plot(time, new_data,y_name="new_amplitude")

    corr_func = find_bits(1, 5, time, new_data, [sin, cos, sin1,cos1])
    assert corr_func == cos