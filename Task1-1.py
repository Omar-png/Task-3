#Task: Weather Advisor

Temp = float(input('Please input the current Temperature in Celsius') )
if Temp >= 30:
    print("It's a hot day. Stay hydrated!")
elif Temp >= 20:
    print("It's a warm day. Enjoy the weather!")
elif Temp >= 10:
    print("It's a cool day. Wear a jacket!")
elif Temp < 10:
    print("It's a cold day. Stay warm!")
else: print('please enter a proper value')
    