from datetime import datetime

import clients
from window import *
from windowaviso import *
import sys, var, events

from windowcal import Ui_windowcal


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase ventana calendario
        '''
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual,mesactual,diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)

class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que instancia la ventana de aviso salir
        '''
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_Aviso()
        var.dlgaviso.setupUi(self)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de botón
        '''
        var.ui.btnCalendario.clicked.connect(events.Eventos.abrirCal)
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.selPago)
        '''
        Eventos de la barra de menús
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        '''
        Eventos de comboBox
        '''
        clients.Clientes.cargaProv_(self)
        var.ui.cmbPro.activated[str].connect(clients.Clientes.serProv)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())
