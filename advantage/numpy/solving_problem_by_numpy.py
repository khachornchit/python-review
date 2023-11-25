import numpy as np


def get_consensus(chars, ss):
    # Transform ss to numpy
    lines = np.array(ss.upper().split('\n'))
    np1 = np.array([list(line) for line in lines])
    rows_np1, cols_np1 = np1.shape

    # Define count matrix
    np_count = np.zeros((len(chars), cols_np1), dtype=int)

    for i, char in enumerate(chars):
        np_count[i] = np.sum(np1 == char, axis=0)

    return np_count


def final_output(chars, count_matrix):
    rows, cols = count_matrix.shape
    output = []

    for i in range(cols):
        col = count_matrix[:, i]
        max_indices = np.where(col == np.max(col))[0]
        result = '/'.join(chars[index] for index in max_indices)
        output.append(result)

    return output


if __name__ == '__main__':
    chars = np.array(['A', 'C', 'G', 'T'])
    # ss = "ATCGATGC\n" + "GTACaCGC\n" + "ACTACAGC\n" + "CtCAATTC\n" + "CTGgATTC"
    ss = ("ATCGATGC\n" + "GTACaCCC\n" + "ACTACATC\n" + "CtCAATAC")

    count = get_consensus(chars, ss)
    print(final_output(chars, count))
