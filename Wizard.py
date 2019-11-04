from PyQt5.QtWidgets import *


def createIntroPage():
    page = QWizardPage()
    page.setTitle("Introduction")

    label = QLabel(
            "This wizard will help you register your copy of Super Product "
            "Two.")
    label.setWordWrap(True)

    layout = QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


def createRegistrationPage():
    page = QWizardPage()
    page.setTitle("Registration")
    page.setSubTitle("Please fill both fields.")

    nameLabel = QLabel("Name:")
    nameLineEdit = QLineEdit()

    emailLabel = QLabel("Email address:")
    emailLineEdit = QLineEdit()

    layout = QGridLayout()
    layout.addWidget(nameLabel, 0, 0)
    layout.addWidget(nameLineEdit, 0, 1)
    layout.addWidget(emailLabel, 1, 0)
    layout.addWidget(emailLineEdit, 1, 1)
    page.setLayout(layout)

    return page


def createConclusionPage():
    page = QWizardPage()
    page.setTitle("Conclusion")

    label = QLabel("You are now successfully registered. Have a nice day!")
    label.setWordWrap(True)

    layout = QVBoxLayout()
    layout.addWidget(label)
    page.setLayout(layout)

    return page


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    wizard = QWizard()
    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage())
    wizard.addPage(createConclusionPage())

    wizard.setWindowTitle("Trivial Wizard")
    wizard.show()

    sys.exit(app.exec_())
