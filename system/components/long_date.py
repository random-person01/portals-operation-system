from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

def long_date():
    print(now.toString(Qt.ISODate))
    print(now.toString(Qt.DefaultLocaleLongDate))
    datetime = QDateTime.currentDateTime()
    print(datetime.toString())
    time = QTime.currentTime()
    print(time.toString(Qt.DefaultLocaleLongDate))
