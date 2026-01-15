def convert_temp(temperature, Fahrenheit=False):
    if Fahrenheit:
        if temperature < -459.67:
            return None
        celsius = (5/9) * (temperature - 32)
        return round (celsius, 2)
    else:
        if temperature < -273.15:
            return None
        fahrenheit_val = (9/5) * temperature + 32
        return round (fahrenheit_val, 2)
    
if __name__ == "__main__":
    print(convert_temp(20))
    print(convert_temp(-10))
    print(convert_temp(68, Fahrenheit=True))
    print(convert_temp(-100, Fahrenheit=True))
    print(convert_temp(-280))
    print(convert_temp(-460, Fahrenheit=True))