'''

Archivo de eventos generales

'''

import sys

import var


class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception() as error:
            print('Error en módulo salir', error)

    def abrirCal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error en modulo abrir calendario', error)