import numpy as np


def get_consensus(chars, ss):
    # transform ss to numpy
    lines = np.array(ss.upper().split('\n'))
    np1 = np.array([[*line] for line in lines])
    rows_np1, cols_np1 = np1.shape

    # define count matrix
    np_count = np.zeros((len(chars), cols_np1), dtype=int)

    for i, char in enumerate(chars):
        char_count = np.char.count(np1, char)
        output = np.sum(char_count, axis=0)
        np_count[i] = output

    return np_count


def final_output(chars, count):
    max_values_per_column = np.max(count, axis=0)
    print(max_values_per_column)


if __name__ == '__main__':
    chars = np.array(['A', 'C', 'G', 'T'])
    ss = "ATCGATGC\n" + "GTACaCGC\n" + "ACTACAGC\n" + "CtCAATTC\n" + "CTGgATTC"

    count = get_consensus(chars, ss)
    final_output(chars, count)

    # print(count)
