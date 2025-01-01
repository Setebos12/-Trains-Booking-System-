# Trains Booking System 🚄🚃🚃🚃🚃🚃🚃🚃


## Contents

### System
The system communicates with files to update seat availability in trains.

The system creates one large graph of trains from individual train graphs.


### Pociągi
🚄 A train consists of 🚃 carriages and routes 🛤 that it operates.

🚃 A carriage has a seating arrangement, 💺 seats, and the routes 🛤🚃 that it operates.

💺 Seats have attributes such as (compartment, window-middle-aisle, bicycle, etc.).

🛤 A route has no loop in a directed graph with node data for arrival at the station and departure data from the station.

🛤🚃 A route in a carriage has edges representing seat reservations.

### User

🧍 Each user can book tickets.

## Dane

Data retrieved from portalpasportalpas(https://portalpasazera.pl/).


## Installation
