import pytest
from car import Car
from track import Track

def test_car_drive_and_fuel():
    car = Car(7)
    car.fill_up(50)
    car.drive(100)
    assert car.remaining_fuel() == 43.0

def test_car_not_enough_fuel():
    car = Car(10)
    car.fill_up(5)
    with pytest.raises(ValueError):
        car.drive(100)

def test_track_consumption():
    t = Track(15, 2)
    t.fill_up(100)
    t.drive(100)
    assert t.remaining_fuel() == 70.0

def test_invalid_inputs():
    c = Car(7)
    with pytest.raises(ValueError):
        c.fill_up(-5)
    with pytest.raises(ValueError):
        c.drive(-100)
