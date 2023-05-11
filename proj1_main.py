from passpro import *


def main():
    app = QApplication([])
    window = Passpro()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

