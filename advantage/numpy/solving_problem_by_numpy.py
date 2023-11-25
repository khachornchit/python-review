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


def final_output(chars, count_matrix):
    compare_matrix = np.max(count, axis=0)
    rows, cols = count_matrix.shape
    output = []

    def get_char():
        max_index = np.argmax(col_transpose)
        max_value = col_transpose[max_index]
        target_index = np.where(col_transpose == max_value)
        result = [chars[index] for index in target_index]
        return '/'.join(result[0])

    for i in range(cols):
        col = count_matrix[:, i:i + 1]
        col_transpose = np.transpose(col)[0]
        output.append(get_char())

    return output


if __name__ == '__main__':
    chars = np.array(['A', 'C', 'G', 'T'])
    ss = "ATCGATGC\n" + "GTACaCGC\n" + "ACTACAGC\n" + "CtCAATTC\n" + "CTGgATTC"

    count = get_consensus(chars, ss)
    output = final_output(chars, count)

    print(output)
