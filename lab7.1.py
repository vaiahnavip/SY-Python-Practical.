text = input("Enter the email / text :")

symbols = ('@', '.', '!')

print("------symbol count-----")

for symbol in symbols : 
    count = text.count(symbol)
    print(f"'{symbol}'{count}time(s)")
    