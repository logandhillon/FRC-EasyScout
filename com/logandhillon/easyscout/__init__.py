import cv2
import os
from colorama import Fore


def scan_qr_code(image_path):
    image = cv2.imread(image_path)
    qr_code_detector = cv2.QRCodeDetector()
    decoded_text, points, _ = qr_code_detector.detectAndDecode(image)

    if points is not None:
        return decoded_text
    else:
        return None


def make_fresh_tsv():
    with open('res/base.tsv', 'r') as f:
        contents = f.read()

    with open('out.tsv', 'w') as f:
        f.write(contents)

    print("Created fresh copy of 'base.tsv'")


def write_results(results: str, out):
    out.write('\n')
    out.write(results)


def main() -> None:
    make_fresh_tsv()

    root = 'samples'
    out = open('out.tsv', 'a')

    for file in os.listdir(root):
        path = os.path.join(root, file)
        print(f"Scanning '{path}'")

        results = scan_qr_code(path)
        scouter = results.split('\t')[0]
        print(f"{Fore.YELLOW}Read scouting data from {scouter}{Fore.RESET}")

        write_results(results, out)

    print(f"{Fore.GREEN}Done! Output table is at 'out.tsv'{Fore.RESET}")
