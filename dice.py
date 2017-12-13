
import random

print("Let's play dice!")
print("I'll give you a frequency distribution of your results.")
n = int(input("How many times shall we roll the dice? "))

data = []
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

for rolls in range(n):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    data.append(a + b)

for number in data:
    counts[number - 2] += 1

print("\nFrequency distribution chart\n")
print("In", n, "rolls of a pair of dice,")
dots = 2
for count in counts:
    print(dots, "was rolled", count, "times.")
    dots += 1
    
print("done")
print("Rolls:", len(data))

