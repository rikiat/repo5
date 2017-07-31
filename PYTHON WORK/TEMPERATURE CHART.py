def toFarenheit(celsius):
    return (9.0/5.0) * celsius + 32

def toCelsius(farenheit):
    return (farenheit - 32) * (5.0 / 9.0)
for y in range(0,100):
    x = y / 2.0
    print("Celsius: ", x, ", Farenheit: ", toFarenheit(x))
