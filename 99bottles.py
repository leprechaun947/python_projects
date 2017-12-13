# Ninety nine bottles of beer on the wall

tens = ["ninety", "eighty", "seventy", "sixty", "fifty", "forty", "thirty", "twenty", ""]
teens = ["nineteen", "eighteen", "seventeen", "sixteen", "fifteen", "fourteen", "thirteen", "twelve", "eleven", "ten more"]
units = ["nine", "eight", "seven", "six", "five", "four", "three", "two", "one", ""]

countdown = []

count = 99
while count > 0:
    for ten in tens:
        if count < 20 and count > 9:
            for teen in teens:
                num = (teen)
                countdown.append(num)
                count -= 1
        else:
            for unit in units:
                num = (ten + " " + unit)
                countdown.append(num)
                count -= 1

    for unit in units:
        if count == 0:
            num = ("no more")
            countdown.append(num)
        else:
            num = (unit + " more")
            countdown.append(num)
        count -= 1

for i in range(99): 
    num1 = countdown[0]
    num2 = countdown[1]
    bot1 = bot2 = "bottles"
    if num1 == "two more":
        bot1, bot2 = "bottles", "bottle"
    if num1 == "one more":
        bot1, bot2 = "bottle", "bottles"
    print("{} {} of beer on the wall, {} {} of beer;\nTake one down and pass it round, {} {} of beer on the wall.".format(num1.capitalize(), bot1, num1, bot1, num2, bot2))
    print()
    del countdown[0]
print("No more bottles of beer on the wall, no more bottles of beer;\nGo to the store and get some more, ninety nine bottles of beer on the wall.")
