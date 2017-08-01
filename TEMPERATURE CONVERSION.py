scale = input("Select (F) or (C): " )
temp = int(input("What is the temperature: " ))
def convert_temp(scale=None, temp=None):
    if scale == "F":
        return 'C', (temp - 32.0) * (5.0/9.0)
    elif scale == "C":
        return 'F', (temp * (9.0/5.0)) + 32.0
    else:
        print("Needs to be (F) or (C)!")
s, m = convert_temp(scale, temp)
print(temp, "degrees", scale, "is", m, "degrees", s)
