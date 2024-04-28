from main import CreatePredictor

#Predicts value for stock tomorrow on basis of values of today
Predictor=CreatePredictor()
print(Predictor)

print("Input Style\n1. Open \n2. High\n3. Low")
try:
    open=float(input("Enter Open stock value for today: "))
    high=float(input("Enter High stock value for today: "))
    low=float(input("Enter Low stock value for today: "))
except:
    print("Please enter input in specified format")
try:
    print("Stock value for tomorrow", float(Predictor.predict(open, high, low)[0]))
except:
    print("Please try again")