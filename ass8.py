#Task 1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator is now at floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator is now at floor {self.current}")

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]

    def run_elevator(self, elevator_number, target_floor):
        print(f"\nRunning elevator {elevator_number} to floor {target_floor}")
        self.elevators[elevator_number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("\n🚨 Fire alarm! All elevators going to bottom floor...")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} moving to bottom...")
            elevator.go_to_floor(elevator.bottom)

def main():
    building = Building(1, 10, 2)

    building.run_elevator(0, 5)

    building.run_elevator(1, 7)

    building.fire_alarm()


if __name__ == "__main__":
    main()

#Task 2
class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_driven = 0

    def drive(self, hours):
        self.distance_driven += self.current_speed * hours

    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

import random
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nStatus of race: {self.name}")
        print(f"{'Car':10} {'Speed':6} {'Distance':8}")
        for car in self.cars:
            print(f"{car.name:10} {car.current_speed:6} {car.distance_driven:8}")

    def race_finished(self):
        return any(car.distance_driven >= self.distance for car in self.cars)

def main():
    cars = [Car(f"Car{i+1}", random.randint(100, 200)) for i in range(10)]

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1
        if hours % 10 == 0:
            race.print_status()

    race.print_status()
    print("\n🏁 The race is finished!")


if __name__ == "__main__":
    main()
