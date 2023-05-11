from PyQt5.QtWidgets import *
from gui import *
import csv


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Passpro(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        """
        Function that hides certain widgets, and initializes certain variables
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.username = ''
        self.back_val = 0

        self.web_add_search_line.hide()
        self.pass_add_line.hide()
        self.choice_add_2.hide()
        self.web_search_button.hide()
        self.acc_resp_label.hide()
        self.add_search_output.hide()
        self.welcome_label.hide()
        self.choice_add.hide()
        self.choice_search.hide()
        self.user_add_line.hide()
        self.back_button.hide()
        self.pass_display_label.hide()

        self.login_button.clicked.connect(lambda: self.login())
        self.create_acc_button.clicked.connect((lambda: self.create_acc()))
        self.choice_add.clicked.connect(lambda: self.choice(0))
        self.choice_search.clicked.connect(lambda: self.choice(1))
        self.choice_add_2.clicked.connect(lambda: self.add())
        self.web_search_button.clicked.connect(lambda: self.search())
        self.back_button.clicked.connect(lambda: self.back(self.back_val))

    def login(self):
        """
        This function checks for usernames and passwords saved in accounts.csv, and lets then asks the user whether they'd like to add or search for a website if a given username and password are correct
        if not, it tells the user the account does not exist.
        :return:
        """
        user_list = []
        self.username = str(self.user_line.text().lower())
        password = str(self.pass_line.text())
        with open("accounts.csv", "r", newline='') as accounts:
            reader = csv.reader(accounts)
            for line in reader:
                user_list.append(line[0])
                if line[0] == self.username and line[1] == password:
                    self.add_search_output.hide()
                    self.login_button.hide()
                    self.create_acc_button.hide()
                    self.user_line.hide()
                    self.pass_line.hide()
                    self.user_label.hide()
                    self.pass_label.hide()

                    self.welcome_label.show()
                    self.choice_add.show()
                    self.choice_search.show()
                    self.back_button.show()

                    self.back_val = 1

                    self.welcome_label.setText(f"Welcome {self.username}, would you like to add or search for a website?")

                if self.username not in user_list:
                    self.add_search_output.setText("Account does not exist.")
                    self.add_search_output.show()

    def create_acc(self):
        """
        This function handles the creation of a new account, and lets users know if a given username is taken
        :return:
        """
        user_list = []
        username = str(self.user_line.text().lower())
        password = str(self.pass_line.text())
        with open("accounts.csv", "r+", newline='') as accounts:
            writer = csv.writer(accounts)
            for line in accounts:
                user_list.append(line.split(',')[0])
            if username in user_list:
                self.add_search_output.setText("Username taken, please try another.")
                self.add_search_output.show()
            else:
                writer.writerow([username, password])
                self.add_search_output.setText("Account created! Please log in.")
                self.add_search_output.show()

    def choice(self, value):
        """
        This function shows certain widgets based on a given value, determined by a choice of buttons to push
        :param value: This determines the choice that the user chose, which shows certain widgets
        :return:
        """
        if value == 0:
            self.welcome_label.hide()
            self.choice_add.hide()
            self.choice_search.hide()

            self.web_add_search_line.setText("Website")
            self.user_add_line.setText("Username")
            self.pass_add_line.setText("Password")
            self.back_val = 2

            self.web_add_search_line.show()
            self.pass_add_line.show()
            self.user_add_line.show()
            self.choice_add_2.show()
            self.back_button.show()
        else:
            self.welcome_label.hide()
            self.choice_add.hide()
            self.choice_search.hide()

            self.web_add_search_line.setText("Website")
            self.back_val = 2

            self.web_add_search_line.show()
            self.web_search_button.show()
            self.back_button.show()

    def add(self):
        """
        This function allows a user to save a given website, username, and password to their accounts file
        :return:
        """
        website = str(self.web_add_search_line.text().lower())
        username = str(self.user_add_line.text().lower())
        password = str(self.pass_add_line.text())
        with open(f"{self.username}.csv", 'a', newline='') as user_file:
            writer = csv.writer(user_file)
            writer.writerow([website, password, username])
            self.add_search_output.setText("Website username and password saved!")
            self.add_search_output.show()

    def search(self):
        """
        This function allows a user to search through their personal file for a given website, which then shows the username and password for said website if it exists in their file
        :return:
        """
        with open(f"{self.username}.csv", 'a', newline="") as user_file:
            #this is done to create a file if a user file hasn't been created yet
            pass
        web_names = []
        website = str(self.web_add_search_line.text().lower())
        with open(f"{self.username}.csv", 'r', newline="") as user_file:
            reader = csv.reader(user_file)
            for line in reader:
                web_names.append(line[0])
                if line[0] == website:
                    self.add_search_output.setText(f"The username for {website} is {line[2]}.")
                    self.pass_display_label.setText(f"The password for {website} is {line[1]}.")
                    self.add_search_output.show()
                    self.pass_display_label.show()
                if website not in web_names:
                    self.add_search_output.setText(f"{website} was not found.")
                    self.add_search_output.show()
                    self.pass_display_label.hide()
            if len(web_names) == 0:
                self.add_search_output.setText(f"You have no websites saved!")
                self.add_search_output.show()

    def back(self, value):
        """
        This function provides code for the back button
        :param value: this value determines what stage the GUI is at, the number determines what the back function needs to hide and show.
        :return:
        """
        if value == 1:
            self.add_search_output.show()
            self.login_button.show()
            self.create_acc_button.show()
            self.user_line.show()
            self.pass_line.show()
            self.user_label.show()
            self.pass_label.show()

            self.welcome_label.hide()
            self.choice_add.hide()
            self.choice_search.hide()
            self.back_button.hide()

            self.user_line.setText("")
            self.pass_line.setText("")
            self.add_search_output.setText("")
        elif value == 2:
            self.back_val = 1
            self.welcome_label.show()
            self.choice_add.show()
            self.choice_search.show()

            self.web_add_search_line.hide()
            self.pass_add_line.hide()
            self.choice_add_2.hide()
            self.web_search_button.hide()
            self.add_search_output.hide()
            self.user_add_line.hide()
            self.pass_display_label.hide()

            self.add_search_output.setText("")
