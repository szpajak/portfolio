import copy
import os
import sys
import time
from PyQt6 import QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont, QMovie
from PyQt6.uic import loadUi


# from GUI
from MainWindow import Ui_MainWindow as Ui_MainWindow
from SecondWindow import Ui_Dialog
from LoadingWindow import Ui_MainWindow as Ui_Load
from ErrorWindow import Ui_MainWindow as Ui_Error
from InfoWindow import Ui_MainWindow as Ui_Info
from algorythm import Population, Fixtures, Genetic, Team, Match
import pyqtgraph as pg
import pyqtgraph.canvas

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.second = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)

        self.spinBox_12.valueChanged.connect(self.update_spinBox_12)
        self.spinBox_13.valueChanged.connect(self.update_spinBox_13)
        self.spinBox_8.valueChanged.connect(self.update_spinBox_8)
        self.spinBox_9.valueChanged.connect(self.update_spinBox_9)
        self.spinBox_10.valueChanged.connect(self.update_spinBox_10)
        self.spinBox_11.valueChanged.connect(self.update_spinBox_11)

        self.checkBox_11.stateChanged.connect(self.checkBox_11_changed)
        self.checkBox_12.stateChanged.connect(self.checkBox_12_changed)

        self.population_size = self.spinBox_12.value()
        self.generation_size = self.spinBox_13.value()
        self.tournament_size = self.spinBox_8.value()
        self.elite_size = self.spinBox_9.value()
        self.percent_muted = self.spinBox_10.value()
        self.mut_rate = self.spinBox_11.value()

    def check(self):
        if ((self.checkBox_11.checkState() != Qt.CheckState.Checked and
                    self.checkBox_12.checkState() != Qt.CheckState.Checked) or
                    ((self.checkBox_13.checkState() != Qt.CheckState.Checked and
                    self.checkBox_14.checkState() != Qt.CheckState.Checked and
                    self.checkBox_15.checkState() != Qt.CheckState.Checked and
                    self.checkBox_16.checkState() != Qt.CheckState.Checked) and
                    (self.percent_muted > 0 or self.mut_rate > 0))):
            self.error = ErrorWindow()
            self.error.show()
            return
        if (self.checkBox_13.checkState() != Qt.CheckState.Checked and
                self.checkBox_14.checkState() != Qt.CheckState.Checked and
                self.checkBox_15.checkState() != Qt.CheckState.Checked and
                self.checkBox_16.checkState() != Qt.CheckState.Checked) or self.percent_muted == 0 or self.mut_rate == 0:
            self.info_window = InfoWindow()
            self.info_window.show()
            self.info_window.pushButton.clicked.connect(self.info_window_button)
            self.info_window.pushButton_2.clicked.connect(self.info_window.close)
        else:
            self.second_window()

    def second_window(self):
        self.second = SecondWindow(obj=self)
        if self.second.correct:
            self.second.show()
            self.plot_window = PlotWindow(obj=self)
            self.plot_window.show()
        else:

            self.error = ErrorWindow()
            self.error.show()
    def update_spinBox_12(self):
        self.population_size = self.spinBox_12.value()

    def update_spinBox_13(self):
        self.generation_size = self.spinBox_13.value()

    def update_spinBox_8(self):
        self.tournament_size = self.spinBox_8.value()

    def update_spinBox_9(self):
        self.elite_size = self.spinBox_9.value()

    def update_spinBox_10(self):
        self.percent_muted = self.spinBox_10.value()

    def update_spinBox_11(self):
        self.mut_rate = self.spinBox_11.value()

    def checkBox_11_changed(self, state):

        # Jeśli checkbox 1 jest zaznaczony, odznacz checkbox 2
        if state == 2:
            self.checkBox_12.setChecked(False)

    def checkBox_12_changed(self, state):

        # Jeśli checkbox 2 jest zaznaczony, odznacz checkbox 1
        if state == 2:
            self.checkBox_11.setChecked(False)

    def info_window_button(self):
        self.info_window.close()
        self.second_window()


class SecondWindow(QtWidgets.QMainWindow, Ui_Dialog):

    def __init__(self, *args, obj=None, **kwargs):
        super(SecondWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.club_logos = os.listdir("main/grafiki/club_logos")
        m_window = obj

        tournament_type = ""
        if m_window.checkBox_11.checkState() == Qt.CheckState.Checked:
            tournament_type = "Ranking"
        elif m_window.checkBox_12.checkState() == Qt.CheckState.Checked:
            tournament_type = "Tournament"

        mut_type = []
        if m_window.checkBox_13.checkState() == Qt.CheckState.Checked:
            mut_type.append("Round")
        if m_window.checkBox_14.checkState() == Qt.CheckState.Checked:
            mut_type.append("Host")
        if m_window.checkBox_15.checkState() == Qt.CheckState.Checked:
            mut_type.append("Hour2")
        if m_window.checkBox_16.checkState() == Qt.CheckState.Checked:
            mut_type.append("Hour1")

        f = Fixtures()
        f.PL_fixtures(False)
        f.initiate_match_times()
        f.complete_the_cost_matrix(0)
        f.penalty_fun()
        f.objective_function()
        global p
        p = Population()
        self.correct = p.finish(population_size=m_window.population_size, generation_size=m_window.generation_size,
                 tournament_size=m_window.tournament_size, tournament_type=tournament_type,
                 elite_percent=m_window.elite_size/100, mut_type=mut_type,
                 percent_muted=m_window.percent_muted/100, mut_rate=m_window.mut_rate/100)
        if not self.correct:
            return
        self.label_2.setText(f"{p.best}")

        for i in range(0,19):
            first_rnd = Ui_Dialog.round(self, i+1)
            rematch_rnd = Ui_Dialog.round(self, i+20)
            sorted_first = sorted(p.best_fix.first_game[i], key=lambda x: x.time)
            sorted_rematch = sorted(p.best_fix.rematch[i], key=lambda x: x.time)
            k = 0
            for i in range(0, len(first_rnd) // 2):
                first_rnd[k].setPixmap(QtGui.QPixmap(f"main/grafiki/club_logos/{sorted_first[i].team1.path}"))
                rematch_rnd[k].setPixmap(QtGui.QPixmap(f"main/grafiki/club_logos/{sorted_rematch[i].team1.path}"))
                k += 1
                first_rnd[k].setPixmap(QtGui.QPixmap(f"main/grafiki/club_logos/{sorted_first[i].team2.path}"))
                rematch_rnd[k].setPixmap(QtGui.QPixmap(f"main/grafiki/club_logos/{sorted_rematch[i].team2.path}"))
                k += 1


class PlotWindow(QtWidgets.QMainWindow):
    def __init__(self, obj=None):
        super().__init__()
        m_window = obj
        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)
        self.plot_graph.setBackground("w")
        generation_size = list(range(1, m_window.generation_size+1))
        y_wartosci = [obiekt.objective_function() for obiekt in p.all_generation]
        best = [p.best] * m_window.generation_size
        self.plot_graph.setTitle("Wykres funkcji celu", size="20pt", color="black", font_family="Century Gothic")
        pen = pg.mkPen(color=(255, 0, 0), width=8)
        self.plot_graph.plot(
            generation_size,
            y_wartosci,
            pen=pen)

        styles = {"color": "black", "font-size": "18px", "font-family": "Century Gothic"}
        self.plot_graph.setLabel("left", "Wartość funkcji celu", **styles)
        self.plot_graph.setLabel("bottom", "Ilość iteracji", **styles)
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setXRange(1, m_window.generation_size)

        pen2 = pg.mkPen(color=(0, 255, 0), width=5)
        self.plot_graph.plot(generation_size, best, pen=pen2)
        self.setWindowTitle('Wykres przebiegu funkcji celu')
        self.setWindowIcon(QIcon('main/grafiki/logo.png'))


class LoadingWindow(QtWidgets.QMainWindow, Ui_Load):
    def __init__(self, *args, **kwargs):
        super(LoadingWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)


class ErrorWindow(QtWidgets.QMainWindow, Ui_Error):
    def __init__(self, *args, **kwargs):
        super(ErrorWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


class InfoWindow(QtWidgets.QMainWindow, Ui_Info):
    def __init__(self, *args, **kwargs):
        super(InfoWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()


# Funkcja samodzielnie napisana i dodawana do automatycznie generowanego pliku SecondWindow.py

# def round(self, round_num):
#     if round_num == 1:
#         return [self.Team_H_1_Sob1330, self.Team_A_1_Sob1330, self.Team_H_1_Sob1600_1, self.Team_A_1_Sob1600_1,
#                 self.Team_H_1_Sob1600_2, self.Team_A_1_Sob1600_2, self.Team_H_1_Sob1600_3, self.Team_A_1_Sob1600_3,
#                 self.Team_H_1_Sob1600_4, self.Team_A_1_Sob1600_4, self.Team_H_1_Sob1600_5, self.Team_A_1_Sob1600_5,
#                 self.Team_H_1_Sob1830, self.Team_A_1_Sob1830, self.Team_H_1_Nie1500, self.Team_A_1_Nie1500,
#                 self.Team_H_1_Nie1730, self.Team_A_1_Nie1730, self.Team_H_1_Nie2100, self.Team_A_1_Nie2100]
#     if round_num == 2:
#         return [self.Team_H_1_Sob1330_38, self.Team_A_1_Sob1330_38,
#                 self.Team_H_1_Sob1600_186, self.Team_A_1_Sob1600_186,
#                 self.Team_H_1_Sob1600_187, self.Team_A_1_Sob1600_187, self.Team_H_1_Sob1600_188,
#                 self.Team_A_1_Sob1600_188,
#                 self.Team_H_1_Sob1600_189, self.Team_A_1_Sob1600_189, self.Team_H_1_Sob1600_190,
#                 self.Team_A_1_Sob1600_190,
#
#                 self.Team_H_1_Sob1830_38, self.Team_A_1_Sob1830_38, self.Team_H_1_Nie1500_38,
#                 self.Team_A_1_Nie1500_38,
#                 self.Team_H_1_Nie1730_38, self.Team_A_1_Nie1730_38, self.Team_H_1_Nie2100_38,
#                 self.Team_A_1_Nie2100_38]
#     if round_num == 3:
#         return [self.Team_H_1_Sob1330_2, self.Team_A_1_Sob1330_2, self.Team_H_1_Sob1600_7,
#                 self.Team_A_1_Sob1600_7,
#                 self.Team_H_1_Sob1600_8, self.Team_A_1_Sob1600_8, self.Team_H_1_Sob1600_9,
#                 self.Team_A_1_Sob1600_9,
#                 self.Team_H_1_Sob1600_10, self.Team_A_1_Sob1600_10, self.Team_H_1_Sob1600_6,
#                 self.Team_A_1_Sob1600_6,
#                 self.Team_H_1_Sob1830_2, self.Team_A_1_Sob1830_2, self.Team_H_1_Nie1500_2,
#                 self.Team_A_1_Nie1500_2,
#                 self.Team_H_1_Nie1730_2, self.Team_A_1_Nie1730_2, self.Team_H_1_Nie2100_2,
#                 self.Team_A_1_Nie2100_2]
#     if round_num == 4:
#         return [self.Team_H_1_Sob1330_3, self.Team_A_1_Sob1330_3, self.Team_H_1_Sob1600_12,
#                 self.Team_A_1_Sob1600_12,
#                 self.Team_H_1_Sob1600_13, self.Team_A_1_Sob1600_13, self.Team_H_1_Sob1600_14,
#                 self.Team_A_1_Sob1600_14,
#                 self.Team_H_1_Sob1600_15, self.Team_A_1_Sob1600_15, self.Team_H_1_Sob1600_11,
#                 self.Team_A_1_Sob1600_11,
#                 self.Team_H_1_Sob1830_3, self.Team_A_1_Sob1830_3, self.Team_H_1_Nie1500_3,
#                 self.Team_A_1_Nie1500_3,
#                 self.Team_H_1_Nie1730_3, self.Team_A_1_Nie1730_3, self.Team_H_1_Nie2100_3,
#                 self.Team_A_1_Nie2100_3]
#     if round_num == 5:
#         return [self.Team_H_1_Sob1330_4, self.Team_A_1_Sob1330_4,
#                 self.Team_H_1_Sob1600_17, self.Team_A_1_Sob1600_17,
#                 self.Team_H_1_Sob1600_18, self.Team_A_1_Sob1600_18, self.Team_H_1_Sob1600_19,
#                 self.Team_A_1_Sob1600_19,
#                 self.Team_H_1_Sob1600_20, self.Team_A_1_Sob1600_20, self.Team_H_1_Sob1600_16,
#                 self.Team_A_1_Sob1600_16,
#
#                 self.Team_H_1_Sob1830_4, self.Team_A_1_Sob1830_4, self.Team_H_1_Nie1500_4, self.Team_A_1_Nie1500_4,
#                 self.Team_H_1_Nie1730_4, self.Team_A_1_Nie1730_4, self.Team_H_1_Nie2100_4, self.Team_A_1_Nie2100_4]
#
#     if round_num == 6:
#         return [self.Team_H_1_Sob1330_5, self.Team_A_1_Sob1330_5,
#                 self.Team_H_1_Sob1600_22, self.Team_A_1_Sob1600_22,
#                 self.Team_H_1_Sob1600_23, self.Team_A_1_Sob1600_23, self.Team_H_1_Sob1600_24,
#                 self.Team_A_1_Sob1600_24,
#                 self.Team_H_1_Sob1600_25, self.Team_A_1_Sob1600_25, self.Team_H_1_Sob1600_21,
#                 self.Team_A_1_Sob1600_21,
#                 self.Team_H_1_Sob1830_5, self.Team_A_1_Sob1830_5, self.Team_H_1_Nie1500_5, self.Team_A_1_Nie1500_5,
#                 self.Team_H_1_Nie1730_5, self.Team_A_1_Nie1730_5, self.Team_H_1_Nie2100_5, self.Team_A_1_Nie2100_5]
#
#     if round_num == 7:
#         return [self.Team_H_1_Sob1330_6, self.Team_A_1_Sob1330_6,
#                 self.Team_H_1_Sob1600_27, self.Team_A_1_Sob1600_27,
#                 self.Team_H_1_Sob1600_28, self.Team_A_1_Sob1600_28, self.Team_H_1_Sob1600_29,
#                 self.Team_A_1_Sob1600_29,
#                 self.Team_H_1_Sob1600_30, self.Team_A_1_Sob1600_30, self.Team_H_1_Sob1600_26,
#                 self.Team_A_1_Sob1600_26,
#
#                 self.Team_H_1_Sob1830_6, self.Team_A_1_Sob1830_6, self.Team_H_1_Nie1500_6, self.Team_A_1_Nie1500_6,
#                 self.Team_H_1_Nie1730_6, self.Team_A_1_Nie1730_6, self.Team_H_1_Nie2100_6, self.Team_A_1_Nie2100_6]
#
#     if round_num == 8:
#         return [self.Team_H_1_Sob1330_7, self.Team_A_1_Sob1330_7,
#                 self.Team_H_1_Sob1600_32, self.Team_A_1_Sob1600_32,
#                 self.Team_H_1_Sob1600_33, self.Team_A_1_Sob1600_33, self.Team_H_1_Sob1600_34,
#                 self.Team_A_1_Sob1600_34,
#                 self.Team_H_1_Sob1600_35, self.Team_A_1_Sob1600_35, self.Team_H_1_Sob1600_31,
#                 self.Team_A_1_Sob1600_31,
#                 self.Team_H_1_Sob1830_7, self.Team_A_1_Sob1830_7, self.Team_H_1_Nie1500_7, self.Team_A_1_Nie1500_7,
#                 self.Team_H_1_Nie1730_7, self.Team_A_1_Nie1730_7, self.Team_H_1_Nie2100_7, self.Team_A_1_Nie2100_7]
#
#     if round_num == 9:
#         return [self.Team_H_1_Sob1330_8, self.Team_A_1_Sob1330_8,
#                 self.Team_H_1_Sob1600_37, self.Team_A_1_Sob1600_37,
#                 self.Team_H_1_Sob1600_38, self.Team_A_1_Sob1600_38, self.Team_H_1_Sob1600_39,
#                 self.Team_A_1_Sob1600_39,
#                 self.Team_H_1_Sob1600_40, self.Team_A_1_Sob1600_40, self.Team_H_1_Sob1600_36,
#                 self.Team_A_1_Sob1600_36,
#
#                 self.Team_H_1_Sob1830_8, self.Team_A_1_Sob1830_8, self.Team_H_1_Nie1500_8, self.Team_A_1_Nie1500_8,
#                 self.Team_H_1_Nie1730_8, self.Team_A_1_Nie1730_8, self.Team_H_1_Nie2100_8, self.Team_A_1_Nie2100_8]
#     if round_num == 10:
#         return [self.Team_H_1_Sob1330_9, self.Team_A_1_Sob1330_9,
#                 self.Team_H_1_Sob1600_42, self.Team_A_1_Sob1600_42,
#                 self.Team_H_1_Sob1600_43, self.Team_A_1_Sob1600_43, self.Team_H_1_Sob1600_44,
#                 self.Team_A_1_Sob1600_44,
#                 self.Team_H_1_Sob1600_45, self.Team_A_1_Sob1600_45, self.Team_H_1_Sob1600_41,
#                 self.Team_A_1_Sob1600_41,
#
#                 self.Team_H_1_Sob1830_9, self.Team_A_1_Sob1830_9, self.Team_H_1_Nie1500_9, self.Team_A_1_Nie1500_9,
#                 self.Team_H_1_Nie1730_9, self.Team_A_1_Nie1730_9, self.Team_H_1_Nie2100_9, self.Team_A_1_Nie2100_9]
#
#     if round_num == 11:
#         return [self.Team_H_1_Sob1330_10, self.Team_A_1_Sob1330_10,
#                 self.Team_H_1_Sob1600_47, self.Team_A_1_Sob1600_47,
#                 self.Team_H_1_Sob1600_48, self.Team_A_1_Sob1600_48, self.Team_H_1_Sob1600_49,
#                 self.Team_A_1_Sob1600_49,
#                 self.Team_H_1_Sob1600_50, self.Team_A_1_Sob1600_50, self.Team_H_1_Sob1600_46,
#                 self.Team_A_1_Sob1600_46,
#
#                 self.Team_H_1_Sob1830_10, self.Team_A_1_Sob1830_10, self.Team_H_1_Nie1500_10,
#                 self.Team_A_1_Nie1500_10,
#                 self.Team_H_1_Nie1730_10, self.Team_A_1_Nie1730_10, self.Team_H_1_Nie2100_10,
#                 self.Team_A_1_Nie2100_10]
#
#     if round_num == 12:
#         return [self.Team_H_1_Sob1330_11, self.Team_A_1_Sob1330_11,
#                 self.Team_H_1_Sob1600_52, self.Team_A_1_Sob1600_52,
#                 self.Team_H_1_Sob1600_53, self.Team_A_1_Sob1600_53, self.Team_H_1_Sob1600_54,
#                 self.Team_A_1_Sob1600_54,
#                 self.Team_H_1_Sob1600_55, self.Team_A_1_Sob1600_55, self.Team_H_1_Sob1600_51,
#                 self.Team_A_1_Sob1600_51,
#
#                 self.Team_H_1_Sob1830_11, self.Team_A_1_Sob1830_11, self.Team_H_1_Nie1500_11,
#                 self.Team_A_1_Nie1500_11,
#                 self.Team_H_1_Nie1730_11, self.Team_A_1_Nie1730_11, self.Team_H_1_Nie2100_11,
#                 self.Team_A_1_Nie2100_11]
#
#     if round_num == 13:
#         return [self.Team_H_1_Sob1330_12, self.Team_A_1_Sob1330_12,
#                 self.Team_H_1_Sob1600_56, self.Team_A_1_Sob1600_56,
#                 self.Team_H_1_Sob1600_57, self.Team_A_1_Sob1600_57, self.Team_H_1_Sob1600_58,
#                 self.Team_A_1_Sob1600_58,
#                 self.Team_H_1_Sob1600_59, self.Team_A_1_Sob1600_59, self.Team_H_1_Sob1600_60,
#                 self.Team_A_1_Sob1600_60,
#
#                 self.Team_H_1_Sob1830_12, self.Team_A_1_Sob1830_12, self.Team_H_1_Nie1500_12,
#                 self.Team_A_1_Nie1500_12,
#                 self.Team_H_1_Nie1730_12, self.Team_A_1_Nie1730_12, self.Team_H_1_Nie2100_12,
#                 self.Team_A_1_Nie2100_12]
#
#     if round_num == 14:
#         return [self.Team_H_1_Sob1330_13, self.Team_A_1_Sob1330_13,
#                 self.Team_H_1_Sob1600_65, self.Team_A_1_Sob1600_65,
#                 self.Team_H_1_Sob1600_61, self.Team_A_1_Sob1600_61, self.Team_H_1_Sob1600_62,
#                 self.Team_A_1_Sob1600_62,
#                 self.Team_H_1_Sob1600_63, self.Team_A_1_Sob1600_63, self.Team_H_1_Sob1600_64,
#                 self.Team_A_1_Sob1600_64,
#
#                 self.Team_H_1_Sob1830_13, self.Team_A_1_Sob1830_13, self.Team_H_1_Nie1500_13,
#                 self.Team_A_1_Nie1500_13,
#                 self.Team_H_1_Nie1730_13, self.Team_A_1_Nie1730_13, self.Team_H_1_Nie2100_13,
#                 self.Team_A_1_Nie2100_13]
#
#     if round_num == 15:
#         return [self.Team_H_1_Sob1330_14, self.Team_A_1_Sob1330_14,
#                 self.Team_H_1_Sob1600_68, self.Team_A_1_Sob1600_68,
#                 self.Team_H_1_Sob1600_69, self.Team_A_1_Sob1600_69, self.Team_H_1_Sob1600_66,
#                 self.Team_A_1_Sob1600_66,
#                 self.Team_H_1_Sob1600_67, self.Team_A_1_Sob1600_67, self.Team_H_1_Sob1600_70,
#                 self.Team_A_1_Sob1600_70,
#
#                 self.Team_H_1_Sob1830_14, self.Team_A_1_Sob1830_14, self.Team_H_1_Nie1500_14,
#                 self.Team_A_1_Nie1500_14,
#                 self.Team_H_1_Nie1730_14, self.Team_A_1_Nie1730_14, self.Team_H_1_Nie2100_14,
#                 self.Team_A_1_Nie2100_14]
#
#     if round_num == 16:
#         return [self.Team_H_1_Sob1330_15, self.Team_A_1_Sob1330_15,
#                 self.Team_H_1_Sob1600_72, self.Team_A_1_Sob1600_72,
#                 self.Team_H_1_Sob1600_73, self.Team_A_1_Sob1600_73, self.Team_H_1_Sob1600_74,
#                 self.Team_A_1_Sob1600_74,
#                 self.Team_H_1_Sob1600_71, self.Team_A_1_Sob1600_71, self.Team_H_1_Sob1600_75,
#                 self.Team_A_1_Sob1600_75,
#
#                 self.Team_H_1_Sob1830_15, self.Team_A_1_Sob1830_15, self.Team_H_1_Nie1500_15,
#                 self.Team_A_1_Nie1500_15,
#                 self.Team_H_1_Nie1730_15, self.Team_A_1_Nie1730_15, self.Team_H_1_Nie2100_15,
#                 self.Team_A_1_Nie2100_15]
#     if round_num == 17:
#         return [self.Team_H_1_Sob1330_16, self.Team_A_1_Sob1330_16,
#                 self.Team_H_1_Sob1600_76, self.Team_A_1_Sob1600_76,
#                 self.Team_H_1_Sob1600_77, self.Team_A_1_Sob1600_77, self.Team_H_1_Sob1600_78,
#                 self.Team_A_1_Sob1600_78,
#                 self.Team_H_1_Sob1600_79, self.Team_A_1_Sob1600_79, self.Team_H_1_Sob1600_80,
#                 self.Team_A_1_Sob1600_80,
#
#                 self.Team_H_1_Sob1830_16, self.Team_A_1_Sob1830_16, self.Team_H_1_Nie1500_16,
#                 self.Team_A_1_Nie1500_16,
#                 self.Team_H_1_Nie1730_16, self.Team_A_1_Nie1730_16, self.Team_H_1_Nie2100_16,
#                 self.Team_A_1_Nie2100_16]
#
#     if round_num == 18:
#         return [self.Team_H_1_Sob1330_17, self.Team_A_1_Sob1330_17,
#                 self.Team_H_1_Sob1600_81, self.Team_A_1_Sob1600_81,
#                 self.Team_H_1_Sob1600_82, self.Team_A_1_Sob1600_82, self.Team_H_1_Sob1600_83,
#                 self.Team_A_1_Sob1600_83,
#                 self.Team_H_1_Sob1600_84, self.Team_A_1_Sob1600_84, self.Team_H_1_Sob1600_85,
#                 self.Team_A_1_Sob1600_85,
#
#                 self.Team_H_1_Sob1830_17, self.Team_A_1_Sob1830_17, self.Team_H_1_Nie1500_17,
#                 self.Team_A_1_Nie1500_17,
#                 self.Team_H_1_Nie1730_17, self.Team_A_1_Nie1730_17, self.Team_H_1_Nie2100_17,
#                 self.Team_A_1_Nie2100_17]
#
#     if round_num == 19:
#         return [self.Team_H_1_Sob1330_18, self.Team_A_1_Sob1330_18,
#                 self.Team_H_1_Sob1600_86, self.Team_A_1_Sob1600_86,
#                 self.Team_H_1_Sob1600_87, self.Team_A_1_Sob1600_87, self.Team_H_1_Sob1600_88,
#                 self.Team_A_1_Sob1600_88,
#                 self.Team_H_1_Sob1600_89, self.Team_A_1_Sob1600_89, self.Team_H_1_Sob1600_90,
#                 self.Team_A_1_Sob1600_90,
#
#                 self.Team_H_1_Sob1830_18, self.Team_A_1_Sob1830_18, self.Team_H_1_Nie1500_18,
#                 self.Team_A_1_Nie1500_18,
#                 self.Team_H_1_Nie1730_18, self.Team_A_1_Nie1730_18, self.Team_H_1_Nie2100_18,
#                 self.Team_A_1_Nie2100_18]
#
#     if round_num == 20:
#         return [self.Team_H_1_Sob1330_19, self.Team_A_1_Sob1330_19,
#                 self.Team_H_1_Sob1600_91, self.Team_A_1_Sob1600_91,
#                 self.Team_H_1_Sob1600_92, self.Team_A_1_Sob1600_92, self.Team_H_1_Sob1600_93,
#                 self.Team_A_1_Sob1600_93,
#                 self.Team_H_1_Sob1600_94, self.Team_A_1_Sob1600_94, self.Team_H_1_Sob1600_95,
#                 self.Team_A_1_Sob1600_95,
#
#                 self.Team_H_1_Sob1830_19, self.Team_A_1_Sob1830_19, self.Team_H_1_Nie1500_19,
#                 self.Team_A_1_Nie1500_19,
#                 self.Team_H_1_Nie1730_19, self.Team_A_1_Nie1730_19, self.Team_H_1_Nie2100_19,
#                 self.Team_A_1_Nie2100_19]
#
#     if round_num == 21:
#         return [self.Team_H_1_Sob1330_20, self.Team_A_1_Sob1330_20,
#                 self.Team_H_1_Sob1600_96, self.Team_A_1_Sob1600_96,
#                 self.Team_H_1_Sob1600_97, self.Team_A_1_Sob1600_97, self.Team_H_1_Sob1600_98,
#                 self.Team_A_1_Sob1600_98,
#                 self.Team_H_1_Sob1600_99, self.Team_A_1_Sob1600_99, self.Team_H_1_Sob1600_100,
#                 self.Team_A_1_Sob1600_100,
#
#                 self.Team_H_1_Sob1830_20, self.Team_A_1_Sob1830_20, self.Team_H_1_Nie1500_20,
#                 self.Team_A_1_Nie1500_20,
#                 self.Team_H_1_Nie1730_20, self.Team_A_1_Nie1730_20, self.Team_H_1_Nie2100_20,
#                 self.Team_A_1_Nie2100_20]
#
#     if round_num == 22:
#         return [self.Team_H_1_Sob1330_21, self.Team_A_1_Sob1330_21,
#                 self.Team_H_1_Sob1600_101, self.Team_A_1_Sob1600_101,
#                 self.Team_H_1_Sob1600_102, self.Team_A_1_Sob1600_102, self.Team_H_1_Sob1600_103,
#                 self.Team_A_1_Sob1600_103,
#                 self.Team_H_1_Sob1600_104, self.Team_A_1_Sob1600_104, self.Team_H_1_Sob1600_105,
#                 self.Team_A_1_Sob1600_105,
#
#                 self.Team_H_1_Sob1830_21, self.Team_A_1_Sob1830_21, self.Team_H_1_Nie1500_21,
#                 self.Team_A_1_Nie1500_21,
#                 self.Team_H_1_Nie1730_21, self.Team_A_1_Nie1730_21, self.Team_H_1_Nie2100_21,
#                 self.Team_A_1_Nie2100_21]
#     if round_num == 23:
#         return [self.Team_H_1_Sob1330_22, self.Team_A_1_Sob1330_22,
#                 self.Team_H_1_Sob1600_106, self.Team_A_1_Sob1600_106,
#                 self.Team_H_1_Sob1600_107, self.Team_A_1_Sob1600_107, self.Team_H_1_Sob1600_108,
#                 self.Team_A_1_Sob1600_108,
#                 self.Team_H_1_Sob1600_109, self.Team_A_1_Sob1600_109, self.Team_H_1_Sob1600_110,
#                 self.Team_A_1_Sob1600_110,
#
#                 self.Team_H_1_Sob1830_22, self.Team_A_1_Sob1830_22, self.Team_H_1_Nie1500_22,
#                 self.Team_A_1_Nie1500_22,
#                 self.Team_H_1_Nie1730_22, self.Team_A_1_Nie1730_22, self.Team_H_1_Nie2100_22,
#                 self.Team_A_1_Nie2100_22]
#
#     if round_num == 24:
#         return [self.Team_H_1_Sob1330_23, self.Team_A_1_Sob1330_23,
#                 self.Team_H_1_Sob1600_111, self.Team_A_1_Sob1600_111,
#                 self.Team_H_1_Sob1600_112, self.Team_A_1_Sob1600_112, self.Team_H_1_Sob1600_113,
#                 self.Team_A_1_Sob1600_113,
#                 self.Team_H_1_Sob1600_114, self.Team_A_1_Sob1600_114, self.Team_H_1_Sob1600_115,
#                 self.Team_A_1_Sob1600_115,
#
#                 self.Team_H_1_Sob1830_23, self.Team_A_1_Sob1830_23, self.Team_H_1_Nie1500_23,
#                 self.Team_A_1_Nie1500_23,
#                 self.Team_H_1_Nie1730_23, self.Team_A_1_Nie1730_23, self.Team_H_1_Nie2100_23,
#                 self.Team_A_1_Nie2100_23]
#     if round_num == 25:
#         return [self.Team_H_1_Sob1330_24, self.Team_A_1_Sob1330_24,
#                 self.Team_H_1_Sob1600_116, self.Team_A_1_Sob1600_116,
#                 self.Team_H_1_Sob1600_117, self.Team_A_1_Sob1600_117, self.Team_H_1_Sob1600_118,
#                 self.Team_A_1_Sob1600_118,
#                 self.Team_H_1_Sob1600_119, self.Team_A_1_Sob1600_119, self.Team_H_1_Sob1600_120,
#                 self.Team_A_1_Sob1600_120,
#
#                 self.Team_H_1_Sob1830_24, self.Team_A_1_Sob1830_24, self.Team_H_1_Nie1500_24,
#                 self.Team_A_1_Nie1500_24,
#                 self.Team_H_1_Nie1730_24, self.Team_A_1_Nie1730_24, self.Team_H_1_Nie2100_24,
#                 self.Team_A_1_Nie2100_24]
#
#     if round_num == 26:
#         return [self.Team_H_1_Sob1330_25, self.Team_A_1_Sob1330_25,
#                 self.Team_H_1_Sob1600_121, self.Team_A_1_Sob1600_121,
#                 self.Team_H_1_Sob1600_122, self.Team_A_1_Sob1600_122, self.Team_H_1_Sob1600_123,
#                 self.Team_A_1_Sob1600_123,
#                 self.Team_H_1_Sob1600_124, self.Team_A_1_Sob1600_124, self.Team_H_1_Sob1600_125,
#                 self.Team_A_1_Sob1600_125,
#
#                 self.Team_H_1_Sob1830_25, self.Team_A_1_Sob1830_25, self.Team_H_1_Nie1500_25,
#                 self.Team_A_1_Nie1500_25,
#                 self.Team_H_1_Nie1730_25, self.Team_A_1_Nie1730_25, self.Team_H_1_Nie2100_25,
#                 self.Team_A_1_Nie2100_25]
#     if round_num == 27:
#         return [self.Team_H_1_Sob1330_26, self.Team_A_1_Sob1330_26,
#                 self.Team_H_1_Sob1600_126, self.Team_A_1_Sob1600_126,
#                 self.Team_H_1_Sob1600_127, self.Team_A_1_Sob1600_127, self.Team_H_1_Sob1600_128,
#                 self.Team_A_1_Sob1600_128,
#                 self.Team_H_1_Sob1600_129, self.Team_A_1_Sob1600_129, self.Team_H_1_Sob1600_130,
#                 self.Team_A_1_Sob1600_130,
#
#                 self.Team_H_1_Sob1830_26, self.Team_A_1_Sob1830_26, self.Team_H_1_Nie1500_26,
#                 self.Team_A_1_Nie1500_26,
#                 self.Team_H_1_Nie1730_26, self.Team_A_1_Nie1730_26, self.Team_H_1_Nie2100_26,
#                 self.Team_A_1_Nie2100_26]
#     if round_num == 28:
#         return [self.Team_H_1_Sob1330_27, self.Team_A_1_Sob1330_27,
#                 self.Team_H_1_Sob1600_131, self.Team_A_1_Sob1600_131,
#                 self.Team_H_1_Sob1600_132, self.Team_A_1_Sob1600_132, self.Team_H_1_Sob1600_133,
#                 self.Team_A_1_Sob1600_133,
#                 self.Team_H_1_Sob1600_134, self.Team_A_1_Sob1600_134, self.Team_H_1_Sob1600_135,
#                 self.Team_A_1_Sob1600_135,
#
#                 self.Team_H_1_Sob1830_27, self.Team_A_1_Sob1830_27, self.Team_H_1_Nie1500_27,
#                 self.Team_A_1_Nie1500_27,
#                 self.Team_H_1_Nie1730_27, self.Team_A_1_Nie1730_27, self.Team_H_1_Nie2100_27,
#                 self.Team_A_1_Nie2100_27]
#
#     if round_num == 29:
#         return [self.Team_H_1_Sob1330_28, self.Team_A_1_Sob1330_28,
#                 self.Team_H_1_Sob1600_136, self.Team_A_1_Sob1600_136,
#                 self.Team_H_1_Sob1600_137, self.Team_A_1_Sob1600_137, self.Team_H_1_Sob1600_138,
#                 self.Team_A_1_Sob1600_138,
#                 self.Team_H_1_Sob1600_139, self.Team_A_1_Sob1600_139, self.Team_H_1_Sob1600_140,
#                 self.Team_A_1_Sob1600_140,
#
#                 self.Team_H_1_Sob1830_28, self.Team_A_1_Sob1830_28, self.Team_H_1_Nie1500_28,
#                 self.Team_A_1_Nie1500_28,
#                 self.Team_H_1_Nie1730_28, self.Team_A_1_Nie1730_28, self.Team_H_1_Nie2100_28,
#                 self.Team_A_1_Nie2100_28]
#     if round_num == 30:
#         return [self.Team_H_1_Sob1330_29, self.Team_A_1_Sob1330_29,
#                 self.Team_H_1_Sob1600_141, self.Team_A_1_Sob1600_141,
#                 self.Team_H_1_Sob1600_142, self.Team_A_1_Sob1600_142, self.Team_H_1_Sob1600_143,
#                 self.Team_A_1_Sob1600_143,
#                 self.Team_H_1_Sob1600_144, self.Team_A_1_Sob1600_144, self.Team_H_1_Sob1600_145,
#                 self.Team_A_1_Sob1600_145,
#
#                 self.Team_H_1_Sob1830_29, self.Team_A_1_Sob1830_29, self.Team_H_1_Nie1500_29,
#                 self.Team_A_1_Nie1500_29,
#                 self.Team_H_1_Nie1730_29, self.Team_A_1_Nie1730_29, self.Team_H_1_Nie2100_29,
#                 self.Team_A_1_Nie2100_29]
#
#     if round_num == 31:
#         return [self.Team_H_1_Sob1330_30, self.Team_A_1_Sob1330_30,
#                 self.Team_H_1_Sob1600_146, self.Team_A_1_Sob1600_146,
#                 self.Team_H_1_Sob1600_147, self.Team_A_1_Sob1600_147, self.Team_H_1_Sob1600_148,
#                 self.Team_A_1_Sob1600_148,
#                 self.Team_H_1_Sob1600_149, self.Team_A_1_Sob1600_149, self.Team_H_1_Sob1600_150,
#                 self.Team_A_1_Sob1600_150,
#
#                 self.Team_H_1_Sob1830_30, self.Team_A_1_Sob1830_30, self.Team_H_1_Nie1500_30,
#                 self.Team_A_1_Nie1500_30,
#                 self.Team_H_1_Nie1730_30, self.Team_A_1_Nie1730_30, self.Team_H_1_Nie2100_30,
#                 self.Team_A_1_Nie2100_30]
#     if round_num == 32:
#         return [self.Team_H_1_Sob1330_31, self.Team_A_1_Sob1330_31,
#                 self.Team_H_1_Sob1600_151, self.Team_A_1_Sob1600_151,
#                 self.Team_H_1_Sob1600_152, self.Team_A_1_Sob1600_152, self.Team_H_1_Sob1600_153,
#                 self.Team_A_1_Sob1600_153,
#                 self.Team_H_1_Sob1600_154, self.Team_A_1_Sob1600_154, self.Team_H_1_Sob1600_155,
#                 self.Team_A_1_Sob1600_155,
#
#                 self.Team_H_1_Sob1830_31, self.Team_A_1_Sob1830_31, self.Team_H_1_Nie1500_31,
#                 self.Team_A_1_Nie1500_31,
#                 self.Team_H_1_Nie1730_31, self.Team_A_1_Nie1730_31, self.Team_H_1_Nie2100_31,
#                 self.Team_A_1_Nie2100_31]
#
#     if round_num == 33:
#         return [self.Team_H_1_Sob1330_32, self.Team_A_1_Sob1330_32,
#                 self.Team_H_1_Sob1600_156, self.Team_A_1_Sob1600_156,
#                 self.Team_H_1_Sob1600_157, self.Team_A_1_Sob1600_157, self.Team_H_1_Sob1600_158,
#                 self.Team_A_1_Sob1600_158,
#                 self.Team_H_1_Sob1600_159, self.Team_A_1_Sob1600_159, self.Team_H_1_Sob1600_160,
#                 self.Team_A_1_Sob1600_160,
#
#                 self.Team_H_1_Sob1830_32, self.Team_A_1_Sob1830_32, self.Team_H_1_Nie1500_32,
#                 self.Team_A_1_Nie1500_32,
#                 self.Team_H_1_Nie1730_32, self.Team_A_1_Nie1730_32, self.Team_H_1_Nie2100_32,
#                 self.Team_A_1_Nie2100_32]
#     if round_num == 34:
#         return [self.Team_H_1_Sob1330_33, self.Team_A_1_Sob1330_33,
#                 self.Team_H_1_Sob1600_161, self.Team_A_1_Sob1600_161,
#                 self.Team_H_1_Sob1600_162, self.Team_A_1_Sob1600_162, self.Team_H_1_Sob1600_163,
#                 self.Team_A_1_Sob1600_163,
#                 self.Team_H_1_Sob1600_164, self.Team_A_1_Sob1600_164, self.Team_H_1_Sob1600_165,
#                 self.Team_A_1_Sob1600_165,
#
#                 self.Team_H_1_Sob1830_33, self.Team_A_1_Sob1830_33, self.Team_H_1_Nie1500_33,
#                 self.Team_A_1_Nie1500_33,
#                 self.Team_H_1_Nie1730_33, self.Team_A_1_Nie1730_33, self.Team_H_1_Nie2100_33,
#                 self.Team_A_1_Nie2100_33]
#
#     if round_num == 35:
#         return [self.Team_H_1_Sob1330_34, self.Team_A_1_Sob1330_34,
#                 self.Team_H_1_Sob1600_166, self.Team_A_1_Sob1600_166,
#                 self.Team_H_1_Sob1600_167, self.Team_A_1_Sob1600_167, self.Team_H_1_Sob1600_168,
#                 self.Team_A_1_Sob1600_168,
#                 self.Team_H_1_Sob1600_169, self.Team_A_1_Sob1600_169, self.Team_H_1_Sob1600_170,
#                 self.Team_A_1_Sob1600_170,
#
#                 self.Team_H_1_Sob1830_34, self.Team_A_1_Sob1830_34, self.Team_H_1_Nie1500_34,
#                 self.Team_A_1_Nie1500_34,
#                 self.Team_H_1_Nie1730_34, self.Team_A_1_Nie1730_34, self.Team_H_1_Nie2100_34,
#                 self.Team_A_1_Nie2100_34]
#     if round_num == 36:
#         return [self.Team_H_1_Sob1330_35, self.Team_A_1_Sob1330_35,
#                 self.Team_H_1_Sob1600_171, self.Team_A_1_Sob1600_171,
#                 self.Team_H_1_Sob1600_172, self.Team_A_1_Sob1600_172, self.Team_H_1_Sob1600_173,
#                 self.Team_A_1_Sob1600_173,
#                 self.Team_H_1_Sob1600_174, self.Team_A_1_Sob1600_174, self.Team_H_1_Sob1600_175,
#                 self.Team_A_1_Sob1600_175,
#
#                 self.Team_H_1_Sob1830_35, self.Team_A_1_Sob1830_35, self.Team_H_1_Nie1500_35,
#                 self.Team_A_1_Nie1500_35,
#                 self.Team_H_1_Nie1730_35, self.Team_A_1_Nie1730_35, self.Team_H_1_Nie2100_35,
#                 self.Team_A_1_Nie2100_35]
#
#     if round_num == 37:
#         return [self.Team_H_1_Sob1330_36, self.Team_A_1_Sob1330_36,
#                 self.Team_H_1_Sob1600_176, self.Team_A_1_Sob1600_176,
#                 self.Team_H_1_Sob1600_177, self.Team_A_1_Sob1600_177, self.Team_H_1_Sob1600_178,
#                 self.Team_A_1_Sob1600_178,
#                 self.Team_H_1_Sob1600_179, self.Team_A_1_Sob1600_179, self.Team_H_1_Sob1600_180,
#                 self.Team_A_1_Sob1600_180,
#
#                 self.Team_H_1_Sob1830_36, self.Team_A_1_Sob1830_36, self.Team_H_1_Nie1500_36,
#                 self.Team_A_1_Nie1500_36,
#                 self.Team_H_1_Nie1730_36, self.Team_A_1_Nie1730_36, self.Team_H_1_Nie2100_36,
#                 self.Team_A_1_Nie2100_36]
#     if round_num == 38:
#         return [self.Team_H_1_Sob1330_37, self.Team_A_1_Sob1330_37,
#                 self.Team_H_1_Sob1600_181, self.Team_A_1_Sob1600_181,
#                 self.Team_H_1_Sob1600_182, self.Team_A_1_Sob1600_182, self.Team_H_1_Sob1600_183,
#                 self.Team_A_1_Sob1600_183,
#                 self.Team_H_1_Sob1600_184, self.Team_A_1_Sob1600_184, self.Team_H_1_Sob1600_185,
#                 self.Team_A_1_Sob1600_185,
#
#                 self.Team_H_1_Sob1830_37, self.Team_A_1_Sob1830_37, self.Team_H_1_Nie1500_37,
#                 self.Team_A_1_Nie1500_37,
#                 self.Team_H_1_Nie1730_37, self.Team_A_1_Nie1730_37, self.Team_H_1_Nie2100_37,
#                 self.Team_A_1_Nie2100_37]
#     else:
#         print("ERROR")