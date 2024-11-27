from expertsystem import ExpertSystem

# Define the rules for the expert system
class WeatherExpertSystem(ExpertSystem):
    def __init__(self):
        super().__init__()

    def rules(self):
        # Rule 1: If the temperature is above 30°C, it's a hot day
        self.add_rule(lambda temp: temp > 30, "It's a hot day.")
        
        # Rule 2: If the temperature is below 0°C, it's a freezing day
        self.add_rule(lambda temp: temp < 0, "It's a freezing day.")
        
        # Rule 3: If the temperature is between 0°C and 30°C, it's a moderate day
        self.add_rule(lambda temp: 0 <= temp <= 30, "It's a moderate day.")

# Create an instance of the weather expert system
weather_system = WeatherExpertSystem()

# Ask for user input and evaluate the weather
temperature = float(input("Enter the current temperature: "))
result = weather_system.run(temperature)
print(result)
