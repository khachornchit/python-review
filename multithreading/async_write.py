import threading
import time


class FileWriterThread(threading.Thread):
    def __init__(self, text, output_file):
        threading.Thread.__init__(self)
        self.text = text
        self.output_file = output_file

    def run(self):
        with open(self.output_file, "a") as file:
            file.write(self.text + '\n')
            time.sleep(2)
        print("Finished background file write to " + self.output_file)


def get_user_input():
    return input("Enter a string to store: ")


def print_calculation_result():
    print("100 + 400 =", 100 + 400)


def main():
    user_message = get_user_input()
    background_writer = FileWriterThread(user_message, 'out.txt')
    background_writer.start()

    print("The program can continue while it writes in another thread")
    print_calculation_result()

    background_writer.join()
    print("Waited until thread was complete")


if __name__ == "__main__":
    main()
