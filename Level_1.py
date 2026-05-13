#Create a temperature converter that handles both Celsius to
#Fahrenheit and Fahrenheit to Celsius


def c2f(cel):
    fah=(cel * 9/5) + 32  #equation of celcius to farenheit
    return fah

def f2c(fah):
    cel=(fah - 32) * 5/9  #//equation of farenheit to celcius
    return cel

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

temp= int(input("Enter 1 / 2: ")) #choose an option


if temp == 1: #choise based on option 1
    val= float(input("Enter the temperature: "))
    print(c2f(val), "°F")

elif temp == 2: #choise based on option 2
    val= float(input("Enter the temperature: "))
    print(f2c(val), "°C")