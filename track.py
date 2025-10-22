class Track:
    def __init__(self, fuel_consumption_per_100km_per_trailer: float, trailers: int):
        if fuel_consumption_per_100km_per_trailer <= 0 or trailers < 0:
            raise ValueError("Invalid input values for consumption or trailers")
        self.consumption_per_trailer = fuel_consumption_per_100km_per_trailer
        self.trailers = trailers
        self.fuel = 0

    def fill_up(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount of fuel must be positive")
        self.fuel += amount

    def drive(self, distance_km: float):
        if distance_km <= 0:
            raise ValueError("Distance must be positive")
        total_consumption = self.consumption_per_trailer * self.trailers
        fuel_needed = (distance_km / 100) * total_consumption
        if fuel_needed > self.fuel:
            raise ValueError("Not enough fuel to drive this distance")
        self.fuel -= fuel_needed

    def remaining_fuel(self):
        return round(self.fuel, 2)
