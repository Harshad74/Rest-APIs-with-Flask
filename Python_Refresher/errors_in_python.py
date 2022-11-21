def divide(dividend,divisor):
    if divisor==0:
        raise ZeroDivisionError("divisor cannot be zero")
    return dividend/divisor

grades=[]

print("welcome to the average grade program")
try:
    average=divide(sum(grades),len(grades))
except ZeroDivisionError as e:
    print("There are no grades in your list")
else:
    print(f"The average grade is {average}")
finally:
    print("Thank you")

