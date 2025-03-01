import cv2
import os
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


def run(root: str = 'samples') -> None:
    make_fresh_tsv()

    print(f"{Fore.CYAN}> Preparing to scan '{root}/'{Fore.RESET}\n----")

    out = open('out.tsv', 'a')

    for file in os.listdir(root):
        path = os.path.join(root, file)

        results = scan_qr_code(path)
        scouter = results.split('\t')[0]
        print(f"{Fore.YELLOW}[ OK ] Read scouting data from {scouter}{Fore.RESET}")

        write_results(results, out)

    print(f"\n{Fore.GREEN}Done! Output table is at 'out.tsv'{Fore.RESET}")
