# numberA and numberB
# subtract numberB from numberA
# print the result

numberA = float(input("First number: "))
numberB = float(input("Second number: "))
sub = numberA - numberB

print("Result: " + str(sub))

if sub < 0:
    print("Negative Number.")
else:
    print("Positive Number.")
