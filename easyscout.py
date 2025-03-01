from colorama import Fore
import com.logandhillon.easyscout as easyscout
from com.logandhillon.easyscout.gui import start_gui
import sys


def scan_indep(results):
    with open('out.tsv', 'a') as out:
        easyscout.write_results(results, out)
        print(f"{Fore.GREEN}[DONE] 🎉 Output table is at 'out.tsv'{Fore.RESET}")


if __name__ == "__main__":
    if "--no-gui" in sys.argv:
        easyscout.scan_dir(callback=scan_indep)
    else:
        start_gui()
