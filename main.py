import sys
import os
from PySide2 import *
import psutil
from multiprocessing import cpu_count
import datetime
from qt_material import *
import shutil 
import platform
import PySide2extn
from time import time, sleep
from ui_interface import *
platforms = {
'linux' : 'Linux',
'linux1' : 'Linux',
'linux2' : 'Linux',
'darwin' : 'OS X',
'win32' : 'Windows'
}
class WorkerSignals(QObject):
    #--
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)
class Worker(QRunnable):
    #--
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress
    @Slot()
    def run(self):
        #--
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)   
        finally:
            self.signals.finished.emit()   
class MainWindow(QMainWindow):
    def __init__(self): 
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        apply_stylesheet(app, theme='dark_cyan.xml')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/feather/airplay.svg"))
        self.setWindowTitle("MInsight")
        QSizeGrip(self.ui.size_grip)
        self.ui.minimizeWindowButton.clicked.connect(lambda: self.showMinimized())
        self.ui.closeWindowButton.clicked.connect(lambda: self.close())
        self.ui.restoreWindowButton.clicked.connect(lambda: self.restore_or_maximize_window())
        self.ui.cpu_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu_page))        
        self.ui.battery_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery_info))
        self.ui.system_inf_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_info))
        self.ui.activity_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activities))
        self.ui.storage_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        self.ui.sensors_page_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
        self.ui.networks_page_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network))
        def moveWindow(e):
            if self.isMaximized() == False:  
                if e.buttons() == Qt.LeftButton:  
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)
        self.show()
        self.threadpool = QThreadPool()
        self.psutil_thread()
        self.system_info()
        self.processes()
        self.storage()
        self.sensors()
        self.networks()
    def psutil_thread(self):
        worker = Worker(self.cpu_ram)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(worker)
        battery_worker = Worker(self.battery)
        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(battery_worker)
    def print_output(self, s):
        print(s)
    def thread_complete(self):
        print("THREAD COMPLETE!")
    def progress_fn(self, n):
        print("%d%% done" % n)
    def applyButtonStyle(self):
        for w in self.ui.left_side_menu.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                w.setStyleSheet("border-bottom: none;")
        self.sender().setStyleSheet("border-bottom: 2px solid")
        return
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restoreWindowButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))
        else:
            self.showMaximized()
            self.ui.restoreWindowButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))
    def slideLeftMenu(self):
        width = self.ui.side_menu_frame.width()
        if width == 40:
            newWidth = 200
        else:
            newWidth = 40
        self.animation = QPropertyAnimation(self.ui.side_menu_frame, b"minimumWidth") 
        self.animation.setDuration(250)
        self.animation.setStartValue(width) 
        self.animation.setEndValue(newWidth) 
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
    def battery(self, progress_callback):
        while True:
            batt = psutil.sensors_battery()
            if not hasattr(psutil, "sensors_battery"):
                self.ui.battery_status.setText("Platform not supported")
            if batt is None:
                self.ui.battery_status.setText("No battery installed")
            if batt.power_plugged:
                self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
                self.ui.battery_time_left.setText("N/A")
                if batt.percent < 100:
                    self.ui.battery_status.setText("Charging")
                else:
                    self.ui.battery_status.setText("Fully Charged")  
                self.ui.battery_plugged.setText("Yes")
            else:
                self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
                self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
                if batt.percent < 100:
                    self.ui.battery_status.setText("Discharging")
                else:
                    self.ui.battery_status.setText("Fully Charged")         
                self.ui.battery_plugged.setText("No")
            self.ui.battery_usage.rpb_setMaximum(100) 
            self.ui.battery_usage.rpb_setValue(batt.percent)
            self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
            self.ui.battery_usage.rpb_setLineColor((255, 30, 99)) 
            self.ui.battery_usage.rpb_setPieColor((45, 74, 83)) 
            self.ui.battery_usage.rpb_setTextColor((255, 255, 255))
            self.ui.battery_usage.rpb_setInitialPos('West') 
            self.ui.battery_usage.rpb_setTextFormat('Percentage')
            self.ui.battery_usage.rpb_setLineWidth(15)
            self.ui.battery_usage.rpb_setPathWidth(15)
            self.ui.battery_usage.rpb_setLineCap('RoundCap')
            sleep(1)
    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)
    def cpu_ram(self, progress_callback):
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam / (1024 * 1024 * 1024)
            self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))
            availRam = 1.0
            availRam = psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024 * 1024 * 1024)
            self.ui.available_ram.setText(str("{:.4f}".format(availRam) + ' GB'))
            ramUsed = 1.0
            ramUsed = psutil.virtual_memory()[3] * ramUsed
            ramUsed = ramUsed / (1024 * 1024 * 1024)
            self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + ' GB'))
            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4] * ramFree
            ramFree = ramFree / (1024 * 1024 * 1024)
            self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + ' GB'))
            core = cpu_count()
            self.ui.cpu_count.setText(str(core))
            ramUsages = str(psutil.virtual_memory()[2]) + '%'
            self.ui.ram_usage.setText(str("{:.4f}".format(totalRam) + ' GB'))
            cpuPer = psutil.cpu_percent()
            self.ui.cpu_per.setText(str(cpuPer) + " %")
            cpuMainCore = psutil.cpu_count(logical=False)
            self.ui.cpu_main_core.setText(str(cpuMainCore))
            self.ui.cpu_percentage.rpb_setMaximum(100) 
            self.ui.cpu_percentage.rpb_setValue(cpuPer)
            self.ui.cpu_percentage.rpb_setBarStyle('Hybrid2')
            self.ui.cpu_percentage.rpb_setLineColor((255, 30, 99))
            self.ui.cpu_percentage.rpb_setPieColor((45, 74, 83))
            self.ui.cpu_percentage.rpb_setTextColor((255, 255, 255)) 
            self.ui.cpu_percentage.rpb_setInitialPos('West')
            self.ui.cpu_percentage.rpb_setTextFormat('Percentage')
            self.ui.cpu_percentage.rpb_setTextFont('Arial')        
            self.ui.cpu_percentage.rpb_setLineWidth(15)
            self.ui.cpu_percentage.rpb_setPathWidth(15)
            self.ui.cpu_percentage.rpb_setLineCap('RoundCap')
            self.ui.ram_percantage.spb_setMinimum((0, 0, 0))
            self.ui.ram_percantage.spb_setMaximum((totalRam, totalRam, totalRam))  
            self.ui.ram_percantage.spb_setValue((availRam, ramUsed, ramFree))
            self.ui.ram_percantage.spb_lineColor(((6,233,38), (6,201,233), (233,6,201)))
            self.ui.ram_percantage.spb_setInitialPos(('West', 'West', 'West'))
            self.ui.ram_percantage.spb_lineWidth(15)
            self.ui.ram_percantage.spb_setGap(15)
            self.ui.ram_percantage.spb_lineStyle(('SolidLine', 'SolidLine', 'SolidLine'))
            self.ui.ram_percantage.spb_lineCap(('RoundCap', 'RoundCap', 'RoundCap'))
            self.ui.ram_percantage.spb_setPathHidden(True)
            sleep(1)
    def system_info(self):
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.ui.system_date.setText(str(time))  
        date = datetime.datetime.now().strftime("%Y-%m-%d")          
        self.ui.system_time.setText(str(date))
        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_sytem.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())
    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            try:        
                process = psutil.Process(x)
                self.create_table_widget(rowPosition, 0, str(process.pid), "tableWidget")
                self.create_table_widget(rowPosition, 1, process.name(), "tableWidget")
                self.create_table_widget(rowPosition, 2, process.status(), "tableWidget")
                self.create_table_widget(rowPosition, 3, str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')), "tableWidget")
                suspend_btn = QPushButton(self.ui.tableWidget)
                suspend_btn.setText('Suspend')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.tableWidget.setCellWidget(rowPosition, 4, suspend_btn)
                resume_btn = QPushButton(self.ui.tableWidget)
                resume_btn.setText('Resume')
                resume_btn.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition, 5, resume_btn)
                terminate_btn = QPushButton(self.ui.tableWidget)
                terminate_btn.setText('Terminate')
                terminate_btn.setStyleSheet("color: orange")
                self.ui.tableWidget.setCellWidget(rowPosition, 6, terminate_btn)
                kill_btn = QPushButton(self.ui.tableWidget)
                kill_btn.setText('Kill')
                kill_btn.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition, 7, kill_btn)
            except Exception as e:
                print(e)
        self.ui.activity_search.textChanged.connect(self.findName)
    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 1)
            self.ui.tableWidget.setRowHidden(row, name not in item.text().lower())
    def storage(self):
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            rowPosition = self.ui.storageTable.rowCount()
            self.ui.storageTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, x.device, "storageTable")
            self.create_table_widget(rowPosition, 1, x.mountpoint, "storageTable")
            self.create_table_widget(rowPosition, 2, x.fstype, "storageTable")
            self.create_table_widget(rowPosition, 3, x.opts, "storageTable")
            if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
                self.create_table_widget(rowPosition, 4, str(x.maxfile), "storageTable")
                self.create_table_widget(rowPosition, 5, str(x.maxpath), "storageTable")
            else:
                self.create_table_widget(rowPosition, 4, "Function not available on " + platforms[sys.platform], "storageTable")
                self.create_table_widget(rowPosition, 5, "Function not available on " + platforms[sys.platform], "storageTable")
            disk_usage = shutil.disk_usage(x.mountpoint)
            self.create_table_widget(rowPosition, 6, str((disk_usage.total / (1024 * 1024 * 1024))) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 7, str((disk_usage.free / (1024 * 1024 * 1024))) + " GB", "storageTable")
            self.create_table_widget(rowPosition, 8, str((disk_usage.used / (1024 * 1024 * 1024))) + " GB", "storageTable")
            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressBar = QProgressBar(self.ui.storageTable)
            progressBar.setObjectName(u"progressBar")
            progressBar.setValue(full_disk)
            self.ui.storageTable.setCellWidget(rowPosition, 9, progressBar)
    def sensors(self):
        if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':           
            for x in psutil.sensors_temperatures():
                for y in psutil.sensors_temperatures()[x]:
                    rowPosition = self.ui.sensorTable.rowCount()
                    self.ui.sensorTable.insertRow(rowPosition)
                    self.create_table_widget(rowPosition, 0, x, "sensorTable")
                    self.create_table_widget(rowPosition, 1, y.label, "sensorTable")
                    self.create_table_widget(rowPosition, 2, str(y.current), "sensorTable")
                    self.create_table_widget(rowPosition, 3, str(y.high), "sensorTable")
                    self.create_table_widget(rowPosition, 4, str(y.critical), "sensorTable")
                    temp_per = (y.current / y.high) * 100
                    progressBar = QProgressBar(self.ui.sensorTable)
                    progressBar.setObjectName(u"progressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensorTable.setCellWidget(rowPosition, 5, progressBar)
        else:
            global platforms
            rowPosition = self.ui.sensorTable.rowCount()
            self.ui.sensorTable.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, "Function not supported on " + platforms[sys.platform], "sensorTable")
            self.create_table_widget(rowPosition, 1, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 2, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 3, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 4, "N/A", "sensorTable")
            self.create_table_widget(rowPosition, 5, "N/A", "sensorTable")
    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()
        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)
        qtablewidgetitem.setText(text);
    def networks(self):
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()
            rowPosition = self.ui.net_stats_table.rowCount()
            self.ui.net_stats_table.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, x, "net_stats_table")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "net_stats_table")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "net_stats_table")
            self.create_table_widget(rowPosition, 3, str(z[x].speed), "net_stats_table")
            self.create_table_widget(rowPosition, 4, str(z[x].mtu), "net_stats_table")
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)
            rowPosition = self.ui.net_io_table.rowCount()
            self.ui.net_io_table.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, x, "net_io_table")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "net_io_table")
            self.create_table_widget(rowPosition, 2, str(z[x].bytes_recv), "net_io_table")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "net_io_table")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "net_io_table")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "net_io_table")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "net_io_table")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "net_io_table")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "net_io_table")
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()
            for y in z[x]:  
                rowPosition = self.ui.net_addresses_table.rowCount()
                self.ui.net_addresses_table.insertRow(rowPosition)
                self.create_table_widget(rowPosition, 0, str(x), "net_addresses_table")
                self.create_table_widget(rowPosition, 1, str(y.family), "net_addresses_table")
                self.create_table_widget(rowPosition, 2, str(y.address), "net_addresses_table")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "net_addresses_table")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "net_addresses_table")
                self.create_table_widget(rowPosition, 5, str(y.ptp), "net_addresses_table")
        for x in psutil.net_connections():
            z = psutil.net_connections()
            rowPosition = self.ui.net_connections_table.rowCount()
            self.ui.net_connections_table.insertRow(rowPosition)
            self.create_table_widget(rowPosition, 0, str(x.fd), "net_connections_table")
            self.create_table_widget(rowPosition, 1, str(x.family), "net_connections_table")
            self.create_table_widget(rowPosition, 2, str(x.type), "net_connections_table")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "net_connections_table")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "net_connections_table")
            self.create_table_widget(rowPosition, 5, str(x.status), "net_connections_table")
            self.create_table_widget(rowPosition, 6, str(x.pid), "net_connections_table")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())