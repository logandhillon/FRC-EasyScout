import com.logandhillon.easyscout as easyscout
from com.logandhillon.easyscout.gui import start_gui
import sys

if __name__ == "__main__":
    if "--no-gui" in sys.argv:
        easyscout.run()
    else:
        start_gui()
