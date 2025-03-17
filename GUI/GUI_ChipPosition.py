from PyQt5 import QtWidgets, QtGui, QtCore
from MoveBridge.hardware_interface import SHRCStage
from ChipPosition import SiChipPosition
import logging
from ophyd import Signal
import pyvisa

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI() 
    
    def initUI(self):
        """ Initializes the GUI"""
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Chip Positioner')
        layout = QtWidgets.QVBoxLayout()

        h_layout = QtWidgets.QHBoxLayout()
        self.x0_position = QtWidgets.QLabel('X0 Position:')
        self.x0_input = QtWidgets.QDoubleSpinBox()
        self.x0_input.setRange(-100, 100)
        self.x0_input.setValue(0)
        h_layout.addWidget(self.x0_position)
        h_layout.addWidget(self.x0_input)

        self.y0_pos = QtWidgets.QLabel('Y0 Position:')
        self.y0_input = QtWidgets.QDoubleSpinBox()
        self.y0_input.setRange(-100, 100) 
        self.y0_input.setValue(0)
        h_layout.addWidget(self.y0_pos)
        h_layout.addWidget(self.y0_input)

        self.z0_pos = QtWidgets.QLabel('Z0 Position:') 
        self.z0_input = QtWidgets.QDoubleSpinBox()
        self.z0_input.setRange(-100, 100)
        self.z0_input.setValue(0)
        h_layout.addWidget(self.z0_pos)
        h_layout.addWidget(self.z0_input)

        layout.addLayout(h_layout)

        h1_layout = QtWidgets.QHBoxLayout()
        self.x1_pos = QtWidgets.QLabel('X1 Position:')
        self.x1_input = QtWidgets.QDoubleSpinBox()
        self.x1_input.setRange(-100, 100)
        self.x1_input.setValue(0)
        h1_layout.addWidget(self.x1_pos)
        h1_layout.addWidget(self.x1_input)

        self.y1_pos = QtWidgets.QLabel('Y1 Position:')
        self.y1_input = QtWidgets.QDoubleSpinBox() 
        self.y1_input.setRange(-100, 100)
        self.y1_input.setValue(0)
        h1_layout.addWidget(self.y1_pos)
        h1_layout.addWidget(self.y1_input)

        self.z1_pos = QtWidgets.QLabel('Z1 Position:')
        self.z1_input = QtWidgets.QDoubleSpinBox()
        self.z1_input.setRange(-100, 100)
        self.z1_input.setValue(0)
        h1_layout.addWidget(self.z1_pos)
        h1_layout.addWidget(self.z1_input)

        self.x2_pos = QtWidgets.QLabel('X2 Position:')
        self.x2_input = QtWidgets.QDoubleSpinBox()
        self.x2_input.setRange(-100, 100)
        self.x2_input.setValue(0)
        h1_layout.addWidget(self.x2_pos)
        h1_layout.addWidget(self.x2_input)

        self.y2_pos = QtWidgets.QLabel('Y2 Position:')
        self.y2_input = QtWidgets.QDoubleSpinBox()
        self.y2_input.setRange(-100, 100)
        self.y2_input.setValue(0)
        h1_layout.addWidget(self.y2_pos)
        h1_layout.addWidget(self.y2_input)

        self.z2_pos = QtWidgets.QLabel('Z2 Position:')
        self.z2_input = QtWidgets.QDoubleSpinBox()
        self.z2_input.setRange(-100, 100)
        self.z2_input.setValue(0)
        h1_layout.addWidget(self.z2_pos)
        h1_layout.addWidget(self.z2_input)

        layout.addLayout(h1_layout)

        self.compute_button = QtWidgets.QPushButton('Compute')
        self.compute_button.clicked.connect(self.compute)
        layout.addWidget(self.compute_button)

        self.result_box = QtWidgets.QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)
        self.show()

        def load_settings(self): 
            """ Loads the settings"""
            self.chip_position = SiChipPosition()
            self.x0 = self.x0_input.value()
            self.y0 = self.y0_input.value()
            self.z0 = self.z0_input.value()
            self.x1 = self.x1_input.value()
            self.y1 = self.y1_input.value()
            self.z1 = self.z1_input.value()
            self.x2 = self.x2_input.value()
            self.y2 = self.y2_input.value()
            self.z2 = self.z2_input.value()
        def compute(self): 
            """Computes the transformation matrix"""
            self.load_settings()
            transformation_matrix = self.chip_position.calculate_transformation_matrix(self.x0, self.y0, self.z0, self.x1, self.y1, self.z1, self.x2, self.y2, self.z2)
            self.result_box.setText(str(transformation_matrix))
            


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())