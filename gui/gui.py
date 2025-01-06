from PySide6.QtWidgets import QApplication, QMainWindow, QCompleter, QListWidgetItem, QTableWidgetItem, QPushButton, QListWidget
from PySide6.QtCore import QDate, QTime, Qt
from PySide6.QtGui import QPixmap
from gui.ui_trains import Ui_Trains
from System.system import System, UserSystem, RouteError, InvalidStationError
from datetime import datetime
from io import BytesIO
from networkx import draw_circular
from matplotlib import pyplot as plt
from PIL.ImageQt import ImageQt
from PIL import Image


def plot_route(route, departure_station, arrival_station):
    G = route.routes
    path = route.stations_between(departure_station, arrival_station)
    node_colors = [
        "green" if node == departure_station else
        "red" if node == arrival_station else
        "yellow" if node in path else
        "skyblue"
        for node in G.nodes
    ]

    plt.figure(figsize=(4.5, 4.5))
    draw_circular(G, with_labels=True, node_color=node_colors, font_weight="bold", node_size=450, font_size=5)
    plt.title("Routes Visualization")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    buffer.seek(0)
    return buffer


class TrainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Trains()
        self.ui.setupUi(self)

        self.user_system = UserSystem(System())

        self.selected_train = None
        self.selected_carriage = None
        self.selected_seat = None

        self._initialize_ui()
        self._set_completer()

    def _initialize_ui(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.Search.clicked.connect(self._button_search)
        self.ui.listWidget.itemDoubleClicked.connect(self._select_train)
        self.ui.Carriages.itemClicked.connect(self._select_carriage)
        self.ui.Home.clicked.connect(self._go_home)
        self.ui.SeatsLook.itemClicked.connect(self._seat_clicked)
        self.ui.Booker.clicked.connect(self._Booker)
        self.ui.Tickets.clicked.connect(self._Go_ticket)
        self.ui.Enter.clicked.connect(self._user)
        self._set_date_and_time_limits()

    def _set_date_and_time_limits(self):
        self.ui.dateEdit.setMinimumDate(QDate.currentDate())
        self.ui.dateEdit.setMaximumDate(QDate.currentDate().addMonths(6))
        self.ui.timeEdit.setMinimumTime(QTime.currentTime())
        self.ui.timeEdit.setMaximumTime(QTime(23, 59, 59))

    def _user(self):
        user_id = self.ui.Logger.text()
        if user_id:
            self.user_system.change_current_user(user_id)
            self.ui.IDshow.setText(f"Your ID: {user_id}")

    def _Go_ticket(self):
        self.ui.ListTicket.clear()
        user_id = self.user_system.monitor_user.user_id
        user = self.user_system.system.get_user(user_id)
        tickets = user.tickets
        self.ui.stackedWidget.setCurrentIndex(1)

        for ticket in tickets:
            item = QListWidgetItem(str(ticket))
            item.ticket = ticket
            self.ui.ListTicket.addItem(item)
        self.ui.ListTicket.itemClicked.connect(self._show_ticket_options)

    def _show_ticket_options(self, item):
        if not item.ticket:
            return

        self._clear_button()
        button = QPushButton("Remove Ticket")
        button.ticket = item.ticket
        self.ui.page_2.layout().addWidget(button)
        button.clicked.connect(self._remove_ticket)

    def _remove_ticket(self):
        button = self.sender()
        ticket = button.ticket
        user_id = self.user_system.monitor_user.user_id
        self.user_system.system.remove_ticket(ticket, user_id)
        self._Go_ticket()
        button.deleteLater()

    def _go_home(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def _button_search(self):
        self.ui.info.clear()
        departure = self.ui.Departure.text()
        arrival = self.ui.Arrival.text()
        datatime_time = self.get_time()

        self.user_system.monitor_user.arrival = arrival
        self.user_system.monitor_user.deparute = departure

        try:
            if self.ui.checkBox.isChecked():
                info = self.user_system.system.check_direct_connection(
                    departure, arrival, datatime_time)
                if not info:
                    raise ValueError(f"No Train from {departure} to {arrival}")
                self._populate_train_list(info, departure, arrival)
            else:
                info = self.user_system.system.check_no_direct_connections(
                    departure, arrival, datatime_time)
                if not info:
                    raise ValueError(f"No Train from {departure} to {arrival}")
                self._populate_no_direct_train_list(info, departure, arrival)

            self.ui.stackedWidget.setCurrentIndex(3)
        except (RouteError, InvalidStationError, ValueError) as e:
            self.ui.info.setText(str(e))

    def _populate_train_list(self, trains, departure, arrival):
        self.ui.listWidget.clear()
        for train_id in trains:
            self._add_train_item(train_id, departure, arrival)

    def _populate_no_direct_train_list(self, connections, departure, arrival):
        self.ui.listWidget.clear()
        for train1_id, train2_id, transfer, wait_time in connections:
            transfer_info = f"Transfer at {transfer}\nWait time: {str(wait_time)[:-3]}"
            self._add_info_item(transfer_info)
            self._add_train_item(train1_id, departure, transfer)
            self._add_train_item(train2_id, transfer, arrival)

    def _add_info_item(self, info_text):
        item = QListWidgetItem(info_text)
        item.setFlags(Qt.ItemFlag.NoItemFlags)
        self.ui.listWidget.addItem(item)

    def _add_train_item(self, train_id, departure, arrival):
        route = self.user_system.system.get_train_route(train_id)
        info = route.info_route(departure, arrival)
        item_text = f"Train {train_id}: {departure} -> {arrival}\n{info}"

        item = QListWidgetItem(item_text)
        item.route = route.id
        item.train = self.user_system.system.trains[train_id[1]]
        item.dep_arr = (departure, arrival)
        self.ui.listWidget.addItem(item)

    def _Booker(self):
        if self.user_system.monitor_user.check_if_all_not_none():
            self.user_system.book_seat_data()
            if self.ui.checkBox.isChecked():
                self._Go_ticket()
            else:
                self.ui.stackedWidget.setCurrentIndex(3)
            self.user_system.monitor_user.seat_id = None

    def _select_train(self, item):
        if not item.flags() & Qt.ItemFlag.ItemIsEnabled:
            return

        self.user_system.monitor_user.route_id = item.route
        self.user_system.monitor_user.train_id = item.train.id
        self.user_system.monitor_user.arrival = item.dep_arr[1]
        self.user_system.monitor_user.deparute = item.dep_arr[0]
        self.user_system.monitor_user.seat_id = None

        self._prepare_carriages_view(item.train, item.route)
        self.ui.stackedWidget.setCurrentIndex(0)

    def _prepare_carriages_view(self, train, route_id):
        self.ui.SeatsLook.clear()
        self.ui.Carriages.clear()
        self.display_route(train.routes[route_id])

        for carriage in train.carriages.values():
            carriage_item = QListWidgetItem(f"Carriage {carriage.id}")
            carriage_item.carriage = carriage
            self.ui.Carriages.addItem(carriage_item)

    def _select_carriage(self, item):
        self.user_system.monitor_user.seat_id = None
        self.selected_carriage = item.carriage
        self.user_system.monitor_user.carriage_id = item.carriage.id

        departure = self.user_system.monitor_user.deparute
        arrival = self.user_system.monitor_user.arrival
        r_data = self._get_r_data()
        available_seats = item.carriage.list_all_available_seats(departure, arrival, self.user_system.monitor_user.route_id, r_data)
        self._populate_seats_view(available_seats, item.carriage)

    def _populate_seats_view(self, seats, carriage):
        carriage_look = carriage.get_carriage_look(seats)
        self.ui.SeatsLook.setRowCount(len(carriage_look))
        self.ui.SeatsLook.setColumnCount(len(carriage_look[0])) if carriage_look else 0

        for row, row_data in enumerate(carriage_look):
            for col, seat_info in enumerate(row_data):
                self._add_seat_item(row, col, seat_info, carriage)

    def _add_seat_item(self, row, col, seat_info, carriage):
        seat_item = QTableWidgetItem(seat_info)
        if seat_info.startswith("S"):
            seat_item.id = seat_info[1:-1]
            seat_item.seat = carriage.seats[str(seat_item.id)]
        else:
            seat_item.id = None
            seat_item.seat = None

        if seat_info.endswith("F"):
            seat_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        else:
            seat_item.setFlags(Qt.ItemFlag.NoItemFlags)

        self.ui.SeatsLook.setItem(row, col, seat_item)

    def _seat_clicked(self, item):
        if item.flags() == Qt.ItemFlag.NoItemFlags:
            return
        self.selected_seat = item.seat
        self.user_system.monitor_user.seat_id = item.id
        carriage_id = self.user_system.monitor_user.carriage_id
        add_info = ""
        if item.seat:
            add_info = str(item.seat)
        self.ui.summary.setText(f"Carriage: {carriage_id} Seat: {item.id}\n {add_info}")

    def _set_completer(self):
        completer = QCompleter(self.user_system.system.all_stations)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.Arrival.setCompleter(completer)
        self.ui.Departure.setCompleter(completer)

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

    def _clear_button(self):
        for i in reversed(range(self.ui.page_2.layout().count())):
            widget = self.ui.page_2.layout().itemAt(i).widget()
            if widget and not isinstance(widget, QListWidget):
                self.ui.page_2.layout().takeAt(i)
                widget.deleteLater()

    def display_route(self, route):
        buffer = plot_route(route, self.user_system.monitor_user.deparute, self.user_system.monitor_user.arrival)
        image = Image.open(buffer)
        pixmap = QPixmap.fromImage(ImageQt(image))
        self.ui.labelplot.setPixmap(pixmap)

    def _get_r_data(self):
        r_data = {}
        if self.ui.corridor_middle_window.isChecked():
            wmc = self.ui.CMW1.value()
            r_data['window_middle_corridor'] = wmc

        if self.ui.Table.isChecked():
            table = self.ui.Table1.isChecked()
            r_data['table'] = table

        if self.ui.Compartemnts.isChecked():
            compartments = self.ui.Compartemnts1.isChecked()
            r_data['compartments'] = compartments

        return r_data


def guiMain(args):
    app = QApplication(args)
    window = TrainWindow()
    window.show()
    return app.exec()
