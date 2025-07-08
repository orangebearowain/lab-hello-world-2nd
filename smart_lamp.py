from dataclasses import dataclass, field

@dataclass
class SmartLamp:
    name: str
    color: str = "white"
    brightness: int = 100
    is_on: bool = field(default=False, init=False)

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_brightness(self, percent: int):
        if 0 <= percent <= 100:
            self.brightness = percent
        else:
            print("Brightness should be between 0 and 100.")

    def set_color(self, new_color: str):
        self.color = new_color

    def status(self):
        on_off = "ON" if self.is_on else "OFF"
        return f"{self.name} [{on_off}]: {self.brightness}% brightness, {self.color}"

if __name__ == "__main__":
    desk_lamp = SmartLamp(name="Desk Lamp", color="orange", brightness=50)
    night_stand = SmartLamp(name="Night-Stand", color="yellow", brightness=70)

    desk_lamp.turn_on()
    night_stand.turn_on()

    print(desk_lamp.status()) 
    print(night_stand.status())  