from typing import Dict


class Seat:
    def __init__(self, id: int, compartments: bool,
                 window_middle_corridor: int,
                 table: bool = False,
                 bike: bool = False,
                 pregnat: bool = False,
                 invalid: bool = False) -> None:
        """
        Initializes a Seat object with attributes.

        Args:
            id (int): Seat ID.
            compartments (bool): Whether the seat is in a compartment.
            window_middle_corridor (int): Position type (0: window, 1: middle, 2: corridor).
            table (bool): Whether the seat has a table.
            bike (bool): Whether the seat has space for a bike.
            pregnant (bool): Whether the seat is reserved for pregnant passengers.
            invalid (bool): Whether the seat is reserved for disabled passengers.
        """
        self.data = {
            "id": str(id),
            "compartments": bool(compartments),
            "window_middle_corridor": int(window_middle_corridor) % 3,
            "table": bool(table),
            "bike": bool(bike),
            "pregnat": bool(pregnat),
            "invalid": bool(invalid),
        }

    def check_requirments(self, r_data: Dict) -> bool:
        """
        Checks if the seat meets given requirements.

        Args:
            r_data (dict): Dictionary of seat requirements.

        Returns:
            bool: True if requirements are met, False otherwise.
        """
        for key in r_data:
            if r_data[key] is None:
                continue
            if r_data.get(key, -1) != self.data.get(key, 0):
                return False
        return True

    def seat_repr(self) -> Dict:
        return self.data

    def __str__(self) -> str:
        window_corridor_map = {0: "window", 1: "middle", 2: "corridor"}
        if self.data["window_middle_corridor"] in window_corridor_map:
            temp = self.data["window_middle_corridor"]
            self.data["window_middle_corridor"] = window_corridor_map[
                self.data["window_middle_corridor"]
            ]
        true_data = [
            f"{key}: {value}\n" for key, value in self.data.items() if value
        ]
        self.data["window_middle_corridor"] = temp
        return ', '.join(true_data) if true_data else "No true data available"
