class Car:
    def __init__(self, fuel_consumption_per_100km: float):
        if fuel_consumption_per_100km <= 0:
            raise ValueError("Fuel consumption must be positive")
        self.fuel_consumption = fuel_consumption_per_100km
        self.fuel = 0

    def fill_up(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount of fuel must be positive")
        self.fuel += amount

    def drive(self, distance_km: float):
        if distance_km <= 0:
            raise ValueError("Distance must be positive")
        fuel_needed = (distance_km / 100) * self.fuel_consumption
        if fuel_needed > self.fuel:
            raise ValueError("Not enough fuel to drive this distance")
        self.fuel -= fuel_needed

    def remaining_fuel(self):
        return round(self.fuel, 2)
