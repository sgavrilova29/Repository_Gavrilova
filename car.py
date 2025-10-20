class Car:
    def __init__(self, fuel_consumption_per_100km: float):
        self.fuel_consumption = fuel_consumption_per_100km  # L/100km
        self.fuel = 0.0  # current fuel in liters

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
