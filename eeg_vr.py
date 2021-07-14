import pandas as pd
import re


def load_data(vr_filepath, eeg_filepath):
    vr_data = pd.read_csv(vr_filepath)
    # eeg_data = None

    with open(eeg_filepath, "r") as eeg_file:
        line = "#"
        csv_start = 0
        while line[0] == "#":
            print(line)
            csv_start = eeg_file.tell()
            line = eeg_file.readline()

        eeg_file.seek(csv_start)
        eeg_data = pd.read_csv(eeg_file)

    return vr_data, eeg_data


if __name__ == "__main__":
    vr_filepath = "C:/Users/Jack Sullivan/UnityProjects/mind-wandering-vr/mind-wandering-141829.csv"
    eeg_filepath = "C:/Users/Jack Sullivan/Downloads/DSI-24/baseline_VR_625_raw.csv"

    vr_data, eeg_data = load_data(vr_filepath, eeg_filepath)

    print(eeg_data)
