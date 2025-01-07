# Train Booking System 🚅🚃🚃🚃🚃🚃🚃🚃

## Overview
The **Train Booking System** is an application designed for booking and managing train reservations.

---

## Features

### **System**
- **Graph-based Train Management**:
  - Combines individual train graphs into a unified network for efficient route planning.
  - Handles direct and indirect route searches with dynamic transfer handling.
- **Seat Reservation**:
  - Updates seat availability dynamically upon booking or cancellation.
  - Supports various seat attributes such as window, aisle, compartment, and bicycle storage.


### **Trains**
- **Carriages**:
  - Contain seating arrangements with detailed features.
  - Manage routes and reserved seats dynamically.
- **Routes**:
  - Directed graphs representing station-to-station connections.
  - Includes precise arrival and departure data for better planning.

### **Users**
- **Account Management**:
  - Each user is assigned a unique ID.
  - Enables personalized booking and ticket management.
- **Ticket Management**:
  - Users can book, view, and cancel tickets easily.

---

## Installation

### **Requirements**
- Python 3.8 or newer
- Main Libraries: PySide6, NetworkX, Matplotlib

### **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/train-booking-system.git
   cd train-booking-system
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Refresh train data (optional):
   ```bash
   python refresh_data.py
   ```
4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

### **Login**
1. Enter your unique user ID (default user id: 0).
2. Click `Enter` to access your account.

### **Search for Trains**
1. Provide departure and arrival stations.
2. Select the travel date and time.
3. Choose direct or indirect routes.

### **Book a Seat**
1. Browse available trains and carriages.
2. Select a seat and confirm your booking.

### **Manage Tickets**
- View all booked tickets in the `Tickets` section.
- Remove unwanted tickets with a single click.

---



## Data Sources
- Train data retrieved from [Portal Pasażera](https://portalpasazera.pl/).

---

## Author
- Krzysztof Rutkowski

