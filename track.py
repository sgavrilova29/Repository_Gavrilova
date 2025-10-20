class Track:
    def __init__(self, fuel_per_100km_per_trailer: float, trailers_count: int):
        self.fuel_consumption = fuel_per_100km_per_trailer * trailers_count
        self.fuel = 0.0

    def fill_up(self, liters: float):
        if liters < 0:
            raise ValueError("Fuel amount cannot be negative")
        self.fuel += liters

    def drive(self, distance_km: float):
        if distance_km < 0:
            raise ValueError("Distance cannot be negative")
        needed = self.fuel_consumption * distance_km / 100
        if needed > self.fuel:
            raise ValueError("Not enough fuel to drive this distance")
        self.fuel -= needed

    def remaining_fuel(self) -> float:
        return round(self.fuel, 2)
