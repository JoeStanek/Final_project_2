from passpro import *


def main():
    app = QApplication([])
    window = Passpro()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

# use | pyuic5 -x name.ui -o name.py | to import the ui file