class CelsiusTemperatureSensor:
    def __init__(self):
        self._temperature = 25

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_celsius(self):
        return self._temperature


class FahrenheitTemperatureSensor:
    def __init__(self):
        self._temperature = 77

    def set_temperature(self, temperature):
        self._temperature = temperature

    def get_temperature_fahrenheit(self):
        return self._temperature


# TODO: Complete the TemperatureSensorAdapter class
class TemperatureSensorAdapter:
    def __init__(self, sensor):
        self.sensor = sensor
        self.sensor_type = type(sensor)

    def set_temperature(self, temperature):
        if self.sensor_type == FahrenheitTemperatureSensor:
            self.sensor.set_temperature(temperature)

        if self.sensor_type == CelsiusTemperatureSensor:
            c = (temperature - 32) * 5/9
            self.sensor.set_temperature(c)

        raise

    def get_temperature_celsius(self):
        if self.sensor_type == FahrenheitTemperatureSensor:
            temperature = self.sensor.get_temperature_fahrenheit()
            fahrenheit = (temperature * 9/5) + 32
            return fahrenheit
        if self.sensor_type == CelsiusTemperatureSensor:
            temperature = self.sensor.get_temperature_celsius()
            return temperature
        raise


def display_temperature(sensor):
    print(f"Temperature: {sensor.get_temperature_celsius():.2f} °C")


def test_temperature_sensor_adapter(
    adapter: TemperatureSensorAdapter,
    celsius_sensor: CelsiusTemperatureSensor,
    fahrenheit_sensor: FahrenheitTemperatureSensor
):
    adapter.set_temperature(100)
    fahrenheit_sensor.set_temperature(100)

    assert (
        abs(adapter.get_temperature_celsius() - 37.7778) < 0.0001
    ), "Adapter conversion is incorrect"

    celsius_sensor.set_temperature(0)
    adapter.set_temperature(32)
    assert (
        abs(celsius_sensor.get_temperature_celsius() -
            adapter.get_temperature_celsius()) < 0.0001
    ), "Adapter conversion is incorrect"

    print("All tests passed!")


if __name__ == "__main__":
    celsius_sensor = CelsiusTemperatureSensor()
    fahrenheit_sensor = FahrenheitTemperatureSensor()

    # TODO: Create an instance of the TemperatureSensorAdapter
    adapter = TemperatureSensorAdapter(celsius_sensor)

    display_temperature(celsius_sensor)
    if adapter:
        display_temperature(adapter)

    # TODO: Uncomment the test function call after implementing the adapter
    test_temperature_sensor_adapter(adapter, celsius_sensor, fahrenheit_sensor)
