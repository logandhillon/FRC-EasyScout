import cv2
import os
from typing import Callable, List
from colorama import Fore


def getResource(res):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "res", res)


def scan_qr_code(image_path):
    image = cv2.imread(image_path)
    qr_code_detector = cv2.QRCodeDetector()
    decoded_text, points, _ = qr_code_detector.detectAndDecode(image)

    if points is not None:
        return decoded_text
    else:
        return None


def make_fresh_tsv():
    with open(getResource("base.tsv"), 'r') as f:
        contents = f.read()

    with open(getResource("base.tsv"), 'w') as f:
        f.write(contents)

    print("[ OK ] Created fresh copy of 'base.tsv'")


def write_results(results: str, out):
    out.write('\n')
    out.write(results)


def scan_dir(callback: Callable[[List[List[str]]], None], target: str = 'samples') -> None:
    """Scans an optionally given directory for scouting codes, and parses them via the callback.

    Args:
        callback ((2d-str-array) -> void): callback for codes to be parsed via after scanning is complete
        target (str?): directory to scan (default='samples')
    """

    print(f"{Fore.CYAN}> Preparing to scan '{target}/'{Fore.RESET}\n----")

    data = []

    for file in os.listdir(target):
        try:
            qr_data = scan_qr_code(os.path.join(target, file))
            scouter = qr_data.split('\t')[0]
            data.append(qr_data)
            print(f"{Fore.YELLOW}[ OK ] Read scouting data from {Fore.MAGENTA}{scouter}{Fore.RESET}")
        except:
            print(f"{Fore.RED}[FAIL] Cannot read {file}! Skipping this file...{Fore.RESET}")

    print("Sending compiled data to callback...")
    callback(data)
