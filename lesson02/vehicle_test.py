import unittest
from car import Car
from motorcycle import Motorcycle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "M5", 2023)
        self.moto = Motorcycle("Suzuki", "Hayabusa", 2023)

    def test_car_instance_check(self):
        self.assertIsInstance(self.car, Car)

    def car_wheels_check(self):
        self.assertEqual(self.car.get_num_wheels(), 4)

    def moto_wheels_check(self):
        self.assertEqual(self.moto.get_num_wheels(), 2)

    def car_speed_check(self):
        self.car.test_drive()
        self.assertEqual(self.car_speed_check(), 60)

    def moto_speed_check(self):
        self.moto.test_drive()
        self.assertEqual(self.moto_speed_check(), 75)

    def car_parking_check(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car_speed_check(), 0)

    def moto_parking_check(self):
        self.moto.test_drive()
        self.moto.park()
        self.assertEqual(self.moto_speed_check(), 0)


if __name__ == "__main__":
    unittest.main()
