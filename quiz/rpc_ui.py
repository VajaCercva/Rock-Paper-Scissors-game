from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random


class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(540, 394)
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(16)
        window.setFont(font)
        window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/ChatGPT Image Jun 4, 2025, 09_21_38 PM.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        window.setWindowIcon(icon)
        window.setStyleSheet("background-color: black;")

        self.window = window
        self.player_score = 0
        self.ai_score = 0

        self.your_points = QtWidgets.QLabel(window)
        self.your_points.setGeometry(QtCore.QRect(10, 0, 171, 41))
        font_points = QtGui.QFont()
        font_points.setFamily("Rockwell")
        font_points.setPointSize(16)
        self.your_points.setFont(font_points)
        self.your_points.setStyleSheet("color: orange; background-color: transparent;")
        self.your_points.setObjectName("your_points")

        self.AI_points = QtWidgets.QLabel(window)
        self.AI_points.setGeometry(QtCore.QRect(390, 0, 151, 41))
        self.AI_points.setFont(font_points)
        self.AI_points.setStyleSheet("color: orange; background-color: transparent;")
        self.AI_points.setObjectName("AI_points")

        self.start_btn = QtWidgets.QPushButton(window)
        self.start_btn.setGeometry(QtCore.QRect(210, 200, 111, 31))
        self.start_btn.setFont(font_points)
        self.start_btn.setStyleSheet("color: red; background-color: rgb(103, 102, 102); border: 1px solid white;")
        self.start_btn.setObjectName("start_btn")

        self.choose_label = QtWidgets.QLabel(window)
        self.choose_label.setGeometry(QtCore.QRect(170, 120, 201, 41))
        self.choose_label.setFont(font_points)
        self.choose_label.setStyleSheet("color: white; background-color: transparent;")
        self.choose_label.setAlignment(QtCore.Qt.AlignCenter)
        self.choose_label.setText("What you choose?")
        self.choose_label.setVisible(False)

        self.rock_btn = QtWidgets.QPushButton(window)
        self.rock_btn.setGeometry(QtCore.QRect(80, 180, 111, 41))
        self.rock_btn.setFont(font_points)
        self.rock_btn.setText("Rock")
        self.rock_btn.setStyleSheet("background-color: gray; color: white;")
        self.rock_btn.setVisible(False)

        self.paper_btn = QtWidgets.QPushButton(window)
        self.paper_btn.setGeometry(QtCore.QRect(210, 180, 111, 41))
        self.paper_btn.setFont(font_points)
        self.paper_btn.setText("Paper")
        self.paper_btn.setStyleSheet("background-color: gray; color: white;")
        self.paper_btn.setVisible(False)

        self.scissors_btn = QtWidgets.QPushButton(window)
        self.scissors_btn.setGeometry(QtCore.QRect(340, 180, 111, 41))
        self.scissors_btn.setFont(font_points)
        self.scissors_btn.setText("Scissors")
        self.scissors_btn.setStyleSheet("background-color: gray; color: white;")
        self.scissors_btn.setVisible(False)

        self.result_label = QtWidgets.QLabel(window)
        self.result_label.setGeometry(QtCore.QRect(140, 240, 260, 41))
        self.result_label.setFont(font_points)
        self.result_label.setStyleSheet("color: yellow; background-color: transparent;")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label.setVisible(False)

        self.replay_btn = QtWidgets.QPushButton(window)
        self.replay_btn.setGeometry(QtCore.QRect(210, 300, 111, 41))
        self.replay_btn.setFont(font_points)
        self.replay_btn.setText("Replay")
        self.replay_btn.setStyleSheet("background-color: green; color: white;")
        self.replay_btn.setVisible(False)


        self.start_btn.clicked.connect(self.show_game_options)
        self.rock_btn.clicked.connect(lambda: self.play("Rock"))
        self.paper_btn.clicked.connect(lambda: self.play("Paper"))
        self.scissors_btn.clicked.connect(lambda: self.play("Scissors"))
        self.replay_btn.clicked.connect(self.reset_game)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Rock Paper Scissors"))
        self.your_points.setText(_translate("window", "Your points: 0/3"))
        self.AI_points.setText(_translate("window", "AI points: 0/3"))
        self.start_btn.setText(_translate("window", "START!"))

    def show_game_options(self):
        self.start_btn.setVisible(False)
        self.choose_label.setVisible(True)
        self.rock_btn.setVisible(True)
        self.paper_btn.setVisible(True)
        self.scissors_btn.setVisible(True)
        self.result_label.setVisible(True)

    def play(self, player_choice):
        ai_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = ""

        if player_choice == ai_choice:
            result = f"Draw! AI also chose {ai_choice}."
        elif (player_choice == "Rock" and ai_choice == "Scissors") or \
             (player_choice == "Paper" and ai_choice == "Rock") or \
             (player_choice == "Scissors" and ai_choice == "Paper"):
            self.player_score += 1
            result = f"You win! AI chose {ai_choice}."
        else:
            self.ai_score += 1
            result = f"You lose! AI chose {ai_choice}."

        self.result_label.setText(result)
        self.your_points.setText(f"Your points: {self.player_score}/3")
        self.AI_points.setText(f"AI points: {self.ai_score}/3")

        if self.player_score == 3 or self.ai_score == 3:
            winner = "You win the game!" if self.player_score == 3 else "AI wins the game!"
            self.result_label.setText(winner)
            self.rock_btn.setEnabled(False)
            self.paper_btn.setEnabled(False)
            self.scissors_btn.setEnabled(False)
            self.replay_btn.setVisible(True)

    def reset_game(self):
        self.player_score = 0
        self.ai_score = 0
        self.your_points.setText("Your points: 0/3")
        self.AI_points.setText("AI points: 0/3")
        self.result_label.setText("")
        self.rock_btn.setEnabled(True)
        self.paper_btn.setEnabled(True)
        self.scissors_btn.setEnabled(True)
        self.replay_btn.setVisible(False)

        self.result_label.setVisible(True)
        self.choose_label.setVisible(True)
        self.rock_btn.setVisible(True)
        self.paper_btn.setVisible(True)
        self.scissors_btn.setVisible(True)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
