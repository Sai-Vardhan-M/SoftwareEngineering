# Read and process multiple weather scenarios from file
with open("weather_input.txt", "r") as file:
    for line in file:
        a, b, c, x = map(float, line.strip().split())
        y = a * x**2 + b * x + c
        print(f"Weather Model: For coefficients a={a}, b={b}, c={c} at hour {x}, temperature = {y:.2f}°C")
