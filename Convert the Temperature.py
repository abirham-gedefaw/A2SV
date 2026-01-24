class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result = []

        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00

        result.append(Kelvin)
        result.append(Fahrenheit)

        return result
