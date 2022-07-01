import sys
import os

from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6 import uic
from tkinter import messagebox


class Dialogo(QDialog):
    # AusInUS = 2
    # UKInUS = 0.5
    # AusInUS = 3
    # UKInUS = 1.5

    def init(self):
        ruta = os.path.dirname(os.path.abspath(file)) + r"..\vista\WireFrameEditarAsignatura.ui"
        QDialog.init(self)
        uic.loadUi(ruta, self)


        self.btnGuardar.clicked.connect(self.EditarAsignatura)
        self.btnCancelar.clicked.connect(self.exit_app)

    def EditarAsignatura(self):
        NuevoNombreAsignatura = self.lineEditAsignatura.text()
        if(NuevoNombreAsignatura == nombreAsignatura):
            resultado = messagebox.askquestion("Quiere cambiar el nombre de l asignatura", "¿Está seguro que desea cambiar el nombre?")
            if resultado == "yes":
                nombreAsignatura = NuevoNombreAsignatura
            if resultado == "no":
                messagebox.showinfo('Mensaje Informativo', 'No se edito la asignatura')
                nombreAsignatura = nombreAsignatura



    def exit_app(self): #Si se presiona el boton cancelar la aplicacion mostrara un mensaje Salir
        resultado = messagebox.askquestion("Salir", "¿Está seguro que desea salir?")
        if resultado == "yes":
            # exit(0)
            quit(0)


if name == 'main':
    app = QApplication(sys.argv)
    dialogo = Dialogo()
    dialogo.show()
    app.exec()