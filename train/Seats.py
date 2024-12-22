class Seat:
    def __init__(self, id: int, compartments: bool, window_middle_corridor: int, table: bool = False, bike: bool = False, pregnat: bool = False, invalid: bool = False) -> None:
        self.data = {
            "id": id,
            "compartments": bool(compartments),
            "window_middle_corridor": int(window_middle_corridor) % 3,
            "table": bool(table),
            "bike": bool(bike),
            "pregnat": bool(pregnat),
            "invalid": bool(invalid),
        }

    def check_requirments(self, r_data: dict) -> bool:
        for key in r_data:
            if r_data[key] is None:
                continue
            if r_data.get(key, -1) != self.data.get(key, 0):
                return False
        return True
