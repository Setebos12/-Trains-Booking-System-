from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter
from PySide6.QtWidgets import QListWidgetItem, QTableWidgetItem, QPushButton
from PySide6.QtWidgets import QListWidget
from PySide6.QtCore import QDate, QTime, Qt
from ui_trains import Ui_Trains
import sys
from System.system import System, read_all_trains
from System.system import RouteError, InvalidStationError
from datetime import datetime
from io import BytesIO
from networkx import draw_circular
from matplotlib import pyplot as plt
from PIL.ImageQt import ImageQt
from PySide6.QtGui import QPixmap
from PIL import Image


def plot_route(route, departure_station, arrival_station):
    G = route.routes

    path = route.stations_between(departure_station, arrival_station)
    node_colors = []
    for node in G.nodes:
        if node == departure_station:
            node_colors.append("green")
        elif node == arrival_station:
            node_colors.append("red")
        elif node in path:
            node_colors.append("yellow")
        else:
            node_colors.append("skyblue")

    plt.figure(figsize=(4.5, 4.5))
    draw_circular(G, with_labels=True, node_color=node_colors, font_weight="bold", node_size=450, font_size=5)
    plt.title("Routes Visualization")

    buff = BytesIO()
    plt.savefig(buff, format="png")
    plt.close()
    buff.seek(0)
    return buff


class TrainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Trains()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(2)
        self._set_data()
        self.ui.Search.clicked.connect(self._button_search)
        self.ui.listWidget.itemDoubleClicked.connect(self._select_train)
        self.ui.Carriages.itemClicked.connect(self._select_carriage)
        self.ui.Home.clicked.connect(self._go_home)
        self.ui.SeatsLook.itemClicked.connect(self._seat_clicked)
        self.ui.Booker.clicked.connect(self._Booker)
        self.ui.Tickets.clicked.connect(self._Go_ticket)
        self.ui.Enter.clicked.connect(self._user)
        self.system = System(read_all_trains())
        self._set_completer()
        self.selected_train = None
        self.selected_carriage = None
        self.selected_seat = None
        self.route = None

    def _user(self):
        get_id = self.ui.Logger.text()
        if not len(get_id):
            return
        self.system.change_current_user(get_id)
        self.ui.IDshow.setText(f"Your id {get_id}")

    def _Go_ticket(self):
        self.ui.ListTicket.clear()
        user_id = self.system.monitor_user.user_id
        tickets = self.system.users[user_id].tickets
        self.ui.stackedWidget.setCurrentIndex(1)

        for ticket in tickets:
            item = QListWidgetItem(str(ticket))
            item.ticket = ticket
            self.ui.ListTicket.addItem(item)
        self.ui.ListTicket.itemClicked.connect(self._show_ticket_options)

    def _show_ticket_options(self, item):
        if item.ticket is None:
            return

        self._clear_button()
        ticket = item.ticket
        button = QPushButton("Remove Ticket")
        button.ticket = ticket
        self.ui.page_2.layout().addWidget(button)
        button.clicked.connect(self._remove_ticket)

    def _remove_ticket(self):
        button = self.sender()
        ticket = button.ticket
        self.system.remove_ticket(ticket)
        self._go_home()
        button.deleteLater()

    def _set_data(self):
        self.ui.dateEdit.setMinimumDate(QDate.currentDate().addYears(-4))
        self.ui.dateEdit.setMaximumDate(QDate.currentDate().addYears(1))
        self.ui.timeEdit.setMinimumTime(QTime.currentTime())
        self.ui.timeEdit.setMaximumTime(QTime(23, 59, 59))

    def _go_home(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def get_time(self):
        datatime = self.ui.dateEdit.date()
        time = self.ui.timeEdit.time()
        datatime_time = datetime(
            datatime.year(),
            datatime.month(),
            datatime.day(),
            time.hour(),
            time.minute(),
            time.second()
        )
        return datatime_time

    def _button_search(self):
        self.ui.info.clear()
        departure = self.ui.Departure.text()
        arrival = self.ui.Arrival.text()
        datatime_time = self.get_time()
        try:
            self.system.monitor_user.arrival = arrival
            self.system.monitor_user.deparute = departure
        except:
            self.ui.info.setText("Log first")
            return

        if self.ui.checkBox.isChecked():
            try:
                info = self.system.check_direct_connection(
                    departure, arrival, datatime_time)
                if not len(info):
                    raise ValueError(f"No Train from {departure} to {arrival}")
                self.train_list(info, departure, arrival)
                self.ui.stackedWidget.setCurrentIndex(3)
            except RouteError as e:
                self.ui.info.setText(f"{str(e)}")
            except InvalidStationError as e:
                self.ui.info.setText(f"{str(e)}")
            except ValueError as e:
                self.ui.info.setText(f"{str(e)}")
        else:
            try:
                info = self.system.check_no_direct_connections(
                    departure, arrival, datatime_time)
                if not len(info):
                    raise ValueError(f"No Train from {departure} to {arrival}")
                self.no_direct_train_list(info, departure, arrival)
                self.ui.stackedWidget.setCurrentIndex(3)
            except RouteError as e:
                self.ui.info.setText(f"{str(e)}")
            except InvalidStationError as e:
                self.ui.info.setText(f"{str(e)}")
            except ValueError as e:
                self.ui.info.setText(f"{str(e)}")

    def no_direct_train_list(self, ids, departure, arrival):
        self.ui.listWidget.clear()
        for trains_info in ids:
            train1_id = trains_info['train1']
            train2_id = trains_info['train2']
            transfer = trains_info['station']
            time_wait = trains_info['time_wait']
            transfer_info = f"Transfer at {transfer}\n time_wait {str(time_wait)[:-3]}"
            info_item = QListWidgetItem(transfer_info)
            info_item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.ui.listWidget.addItem(info_item)
            self.add_train_item(train1_id, departure, transfer)
            self.add_train_item(train2_id, transfer, arrival)


    def train_list(self, ids, departure, arrival):
        self.ui.listWidget.clear()
        for train_id in ids:
            self.add_train_item(train_id, departure, arrival)

    def add_train_item(self, train_id, departure, arrival):
        route = self.system.get_train_route(train_id)

        info = route.info_route(departure, arrival)
        item_text = (
            f"Pociąg {train_id}: {departure} -> {arrival}\n"
            f"{info}"
        )
        item = QListWidgetItem(item_text)
        item.t = item_text
        item.route = route.id
        item.train = self.system.trains[train_id[1]]
        item.dep_arr = departure, arrival
        self.ui.listWidget.addItem(item)

    def display_route(self, route):
        buffer = plot_route(route, self.system.monitor_user.deparute,
                            self.system.monitor_user.arrival)
        image = Image.open(buffer)
        qt_pixmap = QPixmap.fromImage(ImageQt(image))

        self.ui.labelplot.setPixmap(qt_pixmap)

    def _Booker(self):
        if self.selected_seat and self.selected_carriage and self.selected_train:

            print(f"Rezerwacja dla pociągu {self.selected_train.id}, wagonu {self.selected_carriage.id}, siedzenia {self.selected_seat.data['id']}")
            self.system.book_seat_data()
            if self.ui.checkBox.isChecked():
                self._Go_ticket()
            else:
                self.ui.stackedWidget.setCurrentIndex(3)

    def _select_train(self, item):
        if item.flags() == Qt.ItemFlag.NoItemFlags:
            return
        self.ui.SeatsLook.clear()
        self.ui.summary.setText("Choose Sit My friend")
        self.selected_train = item.train
        self.route = item.route
        self.system.monitor_user.route_id = item.route
        self.system.monitor_user.train_id = item.train.id
        self.system.monitor_user.arrival = item.dep_arr[1]
        self.system.monitor_user.deparute = item.dep_arr[0]
        self.ui.Carriages.clear()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.display_route(self.selected_train.routes[self.system.monitor_user.route_id])
        for carriage in item.train.carriages.values():
            carriage_item = QListWidgetItem(f"Carriage {str(carriage.id)}")
            carriage_item.carriage = carriage
            carriage_item.route = item.route
            carriage_item.train = item.train.id
            self.ui.Carriages.addItem(carriage_item)
        self.ui.label.setText(item.t)

    def _select_carriage(self, item):
        self.ui.SeatsLook.clear()
        self.selected_carriage = item.carriage
        self.system.monitor_user.carriage_id = item.carriage.id
        departure = self.ui.Departure.text()
        arrival = self.ui.Arrival.text()
        r_data = self._get_r_data()
        seats = item.carriage.list_all_availabe_seats(departure, arrival, item.route, r_data)
        carriage_look = item.carriage.get_carriage_look(seats)
        self.ui.SeatsLook.setRowCount(len(carriage_look))
        self.ui.SeatsLook.setColumnCount(len(carriage_look[0])) if carriage_look else 0
        for row in range(len(carriage_look)):
            for col in range(len(carriage_look[row])):
                seat_item = QTableWidgetItem(carriage_look[row][col])
                if carriage_look[row][col][0] == 'S':
                    seat_item.id = carriage_look[row][col][1:-1]
                    seat_item.seat = item.carriage.seats[str(seat_item.id)]
                else:
                    seat_item.id = None
                    seat_item.seat = None
                if carriage_look[row][col][-1] == 'F':
                    seat_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
                else:
                    seat_item.setFlags(Qt.ItemFlag.NoItemFlags)

                seat_item.carriage_id = item.carriage.id
                seat_item.route = item.route
                seat_item.train = item.train
                self.ui.SeatsLook.setItem(row, col, seat_item)

    def _seat_clicked(self, item):
        if item.flags() == Qt.ItemFlag.NoItemFlags:
            return
        self.selected_seat = item.seat
        self.system.monitor_user.seat_id = item.id
        add_info = ""
        if item.seat:
            add_info = str(item.seat)
        self.ui.summary.setText(f"Carriage: {item.carriage_id} Seat: {item.id}\n {add_info}")

    def _set_completer(self):
        completer = QCompleter(self.system.all_stations)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.Arrival.setCompleter(completer)
        self.ui.Departure.setCompleter(completer)

    def _get_r_data(self):
        r_data = {}
        if self.ui.corridor_middle_window.isChecked():
            wmc = self.ui.CMW1.value()
            r_data['window_middle_corridor'] = wmc

        if self.ui.Table.isChecked():
            table = self.ui.Table1.isChecked()
            r_data['table'] = table

        if self.ui.Compartemnts1.isChecked():
            compartments = self.ui.Compartemnts1.isChecked()
            r_data['compartments'] = compartments

        return r_data

    def _clear_button(self):
        for i in reversed(range(self.ui.page_2.layout().count())):
            widget = self.ui.page_2.layout().itemAt(i).widget()
            if widget is not None and not isinstance(widget, QListWidget):
                self.ui.page_2.layout().takeAt(i)  # Usuń widget z układu
                widget.deleteLater()


def guiMain(args):
    app = QApplication(args)
    window = TrainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    guiMain(sys.argv)
