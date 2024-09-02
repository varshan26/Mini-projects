print("Weclome to the tip calculator!");
bill = float(input("Enter the overall bill: "));
tip = int(input("How much would you like to tip? 10, 12 or 15?:"));
split = int(input("How many people split the bill?: "));

value = ((bill * (tip/100)) + bill);
value = round(value/split);

print("Each person should pay: ",value," $");
