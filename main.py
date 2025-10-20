from car import Car
from track import Track

if __name__ == "__main__":
    car = Car(7)
    track = Track(15, 2)

    car.fill_up(100)
    track.fill_up(300)

    car.drive(500)
    track.drive(500)

    print(f"Car remaining fuel: {car.remaining_fuel()} L")
    print(f"Track remaining fuel: {track.remaining_fuel()} L")
