import numpy as np


def get_consensus(ss):
    # define characters
    chars = np.array(['A', 'C', 'G', 'T'])

    # transform ss to numpy
    lines = np.array(ss.upper().split('\n'))
    lines = lines[lines != '']
    np1 = np.array([[*line.strip()] for line in lines])
    rows_np1, cols_np1 = np1.shape

    # define count matrix
    np_count = np.zeros((len(chars), cols_np1), dtype=int)

    for i, char in enumerate(chars):
        char_count = np.char.count(np1, char)
        result = np.sum(char_count, axis=0)
        np_count[i] = result

    return np_count


if __name__ == '__main__':
    ss = "ATCGATGC\n" + "GTACaCGC\n" + "ACTACAGC\n" + "CtCAATTC\n" + "CTGgATTC"
    count = get_consensus(ss)
    print(count)
