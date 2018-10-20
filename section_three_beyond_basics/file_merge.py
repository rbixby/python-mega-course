import glob2
from datetime import datetime

def merge_files():
    txt_files = glob2.glob("*/*.txt")
    file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
    with open(file_name, 'w') as merged_file:

        for t in txt_files:
            with open(t, 'r') as f:
                merged_file.write(f.read() + '\n')

if __name__ == "__main__":
    merge_files()
