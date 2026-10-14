
import os
import math
from datetime import datetime

cafeName = "SIX-FOUR-FIVE CAFE"

salesFile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sales_log.txt")

monthNames = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

threeSize = [
    "Americano", "Cafe Mocha", "Cafe Latte", "Caramel Macchiato",
    "Salted Caramel Macchiato", "White Chocolate Mocha", "Spanish Latte",
    "French Vanilla Latte", "Caramel Latte", "Vanilla Latte",
    "Brown Sugar Espresso", "Six Four Five Latte", "Sea Salt Latte",
    "Dirty Matcha", "Matcha Latte", "Vanilla Milk", "Chocolate Milk",
    "White Chocolate Matcha", "Chamomile Tea"
]

threeSizesPrice = [
    [100, 105, 120], [120, 135, 150], [105, 115, 130],
    [120, 140, 155], [120, 140, 160], [120, 135, 150],
    [115, 130, 145], [120, 135, 150], [120, 140, 160],
    [115, 130, 145], [115, 130, 145], [130, 145, 160],
    [130, 145, 160], [140, 155, 170], [120, 145, 160],
    [110, 120, 130], [110, 120, 130], [140, 155, 170],
    [80, 90, 100]
]

twoSize = [
    "White Americano", "Strawberry Milk", "Strawberry White Chocolate",
    "Mocha", "Caramel", "Salted Caramel", "Coffee Jelly",
    "White Chocolate Mocha (Blended)", "Matcha", "Strawberry",
    "Java Chip", "Cookies and Cream", "Peppermint Mocha",
    "Strawberry Matcha", "Strawberry Black Tea", "Lychee Soda",
    "Blueberry Soda", "Green Apple Soda"
]

twoSizePrice = [
    [160, 175], [120, 130], [135, 145], [150, 165],
    [150, 165], [150, 165], [155, 165], [165, 175],
    [150, 165], [120, 135], [165, 180], [170, 185],
    [185, 200], [165, 180], [90, 100], [90, 100],
    [90, 100], [90, 100]
]

regularSize = [
    "Cheesy Eggdesal", "Classic Burger", "Cheese Burger",
    "645 Burger", "Classic Tuna", "645 Tuna Sandwich",
    "Plain Fries", "Flavored Fries", "Chocolate Chip Cookie",
    "Smore's Cookie", "Chocolate Crinkles", "House Blend Iced Tea"
]

regularSizePrice = [
    [50], [50], [60], [75], [75], [105],
    [50], [70], [35], [50], [15], [95]
]

drinkAddons = [
    "Shot", "Milk", "Sugar Syrup", "Oat Milk", "Syrup",
    "Strawberry", "White Chocolate", "Whip Cream",
    "Coffee Jelly", "Crushed Oreo", "Chocolate Chips"
]

drinkAddonPrice = [35, 15, 15, 50, 20, 15, 30, 20, 20, 20, 20]

foodAddons = ["Cheese", "Egg", "Coleslaw"]
foodAddonPrice = [10, 20, 20]

friesFlavors = ["Cheese", "BBQ", "Sour Cream", "Sweet Corn"]

menu_list = threeSize + twoSize + regularSize
menu_price = threeSizesPrice + twoSizePrice + regularSizePrice

width = 46

showMenu = True
programRunning = True

while programRunning:

    if showMenu:
        print("================ MENU ================")
        print("--- 12oz Hot / 16oz Cold / 20oz Cold ---")

        for i in range(len(menu_list)):

            if i == len(threeSize):
                print("--- 16oz Cold / 20oz Cold ---")

            if i == len(threeSize) + len(twoSize):
                print("--- One size only ---")

            print(f"{i + 1}. {menu_list[i]}: {menu_price[i]}")

        print("======================================")
        showMenu = False

    print("")
    print("================")
    print("      645")
    print("================")
    print("1. New Order")
    print("2. Monthly Sales Report")
    print("3. Annual Sales Report")
    print("4. Show Menu Again")
    print("5. Exit")

    choice = input("Choose (1-5): ").strip()

    if choice == "1":

        orderList = []
        isOrdering = True
        isCancelled = False

        print("Type the item NUMBER or NAME.")
        print("Type 0 to cancel the order.")

        while isOrdering:

            orderInput = input("Enter your order: ").strip()

            if orderInput == "0":
                print("Order cancelled.")
                orderList = []
                isCancelled = True
                isOrdering = False
                continue

            index = -1

            if orderInput.isdigit():

                number = int(orderInput)

                if number >= 1 and number <= len(menu_list):
                    index = number - 1

            else:

                for i in range(len(menu_list)):

                    if menu_list[i].lower() == orderInput.lower():
                        index = i
                        break

            if index == -1:
                print("Item not found in the menu.")
                continue

            validAmount = False

            while not validAmount:

                try:
                    orderAmount = int(input("Amount: "))

                    if orderAmount > 0:
                        validAmount = True
                    else:
                        print("Enter a valid amount.")

                except ValueError:
                    print("Please enter a whole number.")

            if index < len(threeSize):

                sizeNames = ["12oz Hot", "16oz Cold", "20oz Cold"]

            elif index < len(threeSize) + len(twoSize):

                sizeNames = ["16oz Cold", "20oz Cold"]

            elif menu_list[index] == "House Blend Iced Tea":

                sizeNames = ["20oz Cold"]

            else:

                sizeNames = ["Regular"]

            if len(sizeNames) == 1:

                orderSize = 1

            else:

                print("Sizes:")

                for n in range(len(sizeNames)):
                    print(
                        f"{n + 1}. {sizeNames[n]} - "
                        f"PHP {menu_price[index][n]:,.2f}"
                    )

                validSize = False

                while not validSize:

                    try:
                        orderSize = int(input(
                            f"Enter your size (1-{len(sizeNames)}): "
                        ))

                        if orderSize >= 1 and orderSize <= len(sizeNames):
                            validSize = True
                        else:
                            print("Invalid size.")

                    except ValueError:
                        print("Please enter a whole number.")

            flavor = ""

            if menu_list[index] == "Flavored Fries":

                print("Flavors:")

                for n in range(len(friesFlavors)):
                    print(f"{n + 1}. {friesFlavors[n]}")

                validFlavor = False

                while not validFlavor:

                    try:
                        flavorNumber = int(input("Choose ONE flavor: "))

                        if flavorNumber >= 1 and flavorNumber <= len(friesFlavors):

                            flavor = friesFlavors[flavorNumber - 1]
                            validFlavor = True

                        else:
                            print("Invalid flavor number.")

                    except ValueError:
                        print("Please enter a whole number.")

            addons = []

            if index < len(threeSize) + len(twoSize) or menu_list[index] == "House Blend Iced Tea":

                addonNames = drinkAddons
                addonPrices = drinkAddonPrice

            else:

                addonNames = foodAddons
                addonPrices = foodAddonPrice

            validAnswer = False

            while not validAnswer:

                answer = input("Add-ons? (y/n): ").strip().lower()

                if answer == "y" or answer == "yes":
                    validAnswer = True
                    addMore = True

                elif answer == "n" or answer == "no":
                    validAnswer = True
                    addMore = False

                else:
                    print("Please type y or n.")

            if addMore:

                print("Available Add-ons:")

                for n in range(len(addonNames)):
                    print(
                        f"{n + 1}. {addonNames[n]} - "
                        f"PHP {addonPrices[n]:,.2f}"
                    )

                choosingAddons = True

                while choosingAddons:

                    try:
                        number = int(input("Add-on number (0 = done): "))

                    except ValueError:
                        print("Please enter a whole number.")
                        continue

                    if number == 0:
                        choosingAddons = False
                        continue

                    if number < 1 or number > len(addonNames):
                        print("Invalid add-on number.")
                        continue

                    validQuantity = False

                    while not validQuantity:

                        try:
                            quantity = int(input("Add-on quantity: "))

                            if quantity > 0:
                                validQuantity = True
                            else:
                                print("Enter a valid amount.")

                        except ValueError:
                            print("Please enter a whole number.")

                    addons.append([
                        addonNames[number - 1],
                        addonPrices[number - 1],
                        quantity
                    ])

                    print(
                        f"Added add-on: {addonNames[number - 1]} "
                        f"x{quantity}"
                    )

            orderList.append([
                index,
                orderSize,
                orderAmount,
                addons,
                flavor
            ])

            print("Added Order!")
            print("------------")

            validAnswer = False

            while not validAnswer:

                answer = input(
                    "Do you want to add another order? (y/n): "
                ).strip().lower()

                if answer == "y" or answer == "yes":
                    validAnswer = True

                elif answer == "n" or answer == "no":
                    validAnswer = True
                    isOrdering = False

                else:
                    print("Please type y or n.")

        if len(orderList) > 0 and not isCancelled:

            itemsTotal = 0
            addonsTotal = 0

            for index, size, amount, addons, flavor in orderList:

                itemsTotal += menu_price[index][size - 1] * amount

                for addonName, addonPrice, addonQty in addons:
                    addonsTotal += addonPrice * addonQty

            total = itemsTotal + addonsTotal

            print("Order Finished")
            print("================")
            print(f"Items subtotal  : PHP {itemsTotal:,.2f}")
            print(f"Add-ons subtotal: PHP {addonsTotal:,.2f}")
            print(f"TOTAL           : PHP {total:,.2f}")
            print("================")

            validCash = False
            cancelledPayment = False

            while not validCash:

                try:
                    cash = float(input("Cash received (0 = cancel order): "))

                    if not math.isfinite(cash):
                        print("Please enter a valid amount.")
                        continue

                    cash = round(cash, 2)

                    if cash == 0:
                        print("Order cancelled.")
                        cancelledPayment = True
                        validCash = True

                    elif cash < 0:
                        print("Cash cannot be negative.")

                    elif cash < total:
                        print(
                            "Not enough cash. Short by "
                            f"PHP {total - cash:,.2f}"
                        )

                    else:
                        validCash = True

                except ValueError:
                    print("Please enter a valid amount.")

            if not cancelledPayment:

                change = round(cash - total, 2)

                now = datetime.now()

                sales = []

                if os.path.exists(salesFile):

                    with open(salesFile, "r", encoding="utf-8") as file:

                        for line in file:

                            parts = line.strip().split(" | ")

                            if len(parts) == 3:
                                sales.append(parts)

                orderNumber = "645-" + str(len(sales) + 1).zfill(4)

                with open(salesFile, "a", encoding="utf-8") as file:

                    file.write(
                        now.strftime("%Y-%m-%d %H:%M:%S")
                        + " | "
                        + orderNumber
                        + " | "
                        + str(total)
                        + "\n"
                    )

                print("")
                print("=" * width)
                print(cafeName.center(width))
                print("COFFEE  -  SIZZLING".center(width))
                print("=" * width)

                print("Order No: " + orderNumber)
                print("Date    : " + now.strftime("%Y-%m-%d %I:%M %p"))
                print("-" * width)

                for index, size, amount, addons, flavor in orderList:

                    unitPrice = menu_price[index][size - 1]

                    print(menu_list[index])

                    if index < len(threeSize):

                        sizeNames = [
                            "12oz Hot", "16oz Cold", "20oz Cold"
                        ]

                    elif index < len(threeSize) + len(twoSize):

                        sizeNames = [
                            "16oz Cold", "20oz Cold"
                        ]

                    elif menu_list[index] == "House Blend Iced Tea":

                        sizeNames = ["20oz Cold"]

                    else:

                        sizeNames = ["Regular"]

                    detail = (
                        f"  {sizeNames[size - 1]} "
                        f" {amount} x PHP {unitPrice:,.2f}"
                    )

                    right = f"PHP {unitPrice * amount:,.2f}"

                    spaces = width - len(detail) - len(right)

                    if spaces < 1:
                        spaces = 1

                    print(detail + " " * spaces + right)

                    if flavor != "":
                        print("  Flavor: " + flavor)

                    for addonName, addonPrice, addonQty in addons:

                        left = f"  + {addonName} x{addonQty}"
                        right = f"PHP {addonPrice * addonQty:,.2f}"

                        spaces = width - len(left) - len(right)

                        if spaces < 1:
                            spaces = 1

                        print(left + " " * spaces + right)

                print("-" * width)

                receiptItems = "Items subtotal"
                receiptAddons = "Add-ons subtotal"
                receiptTotal = "TOTAL"
                receiptCash = "Cash received"
                receiptChange = "Change"

                right = f"PHP {itemsTotal:,.2f}"
                print(receiptItems + " " * max(1, width - len(receiptItems) - len(right)) + right)

                right = f"PHP {addonsTotal:,.2f}"
                print(receiptAddons + " " * max(1, width - len(receiptAddons) - len(right)) + right)

                right = f"PHP {total:,.2f}"
                print(receiptTotal + " " * max(1, width - len(receiptTotal) - len(right)) + right)

                print("-" * width)

                right = f"PHP {cash:,.2f}"
                print(receiptCash + " " * max(1, width - len(receiptCash) - len(right)) + right)

                right = f"PHP {change:,.2f}"
                print(receiptChange + " " * max(1, width - len(receiptChange) - len(right)) + right)

                print("=" * width)
                print(
                    "Thank you for ordering at Six-Four-Five Cafe!".center(width)
                )
                print("")

    elif choice == "2":

        validYear = False

        while not validYear:

            try:
                year = int(input("Enter year (example 2026): "))
                validYear = True

            except ValueError:
                print("Please enter a valid year.")

        validMonth = False

        while not validMonth:

            try:
                month = int(input("Enter month (1-12): "))

                if month >= 1 and month <= 12:
                    validMonth = True
                else:
                    print("Month must be 1 to 12.")

            except ValueError:
                print("Please enter a valid month.")

        totalSales = 0
        count = 0

        if os.path.exists(salesFile):

            with open(salesFile, "r", encoding="utf-8") as file:

                for line in file:

                    parts = line.strip().split(" | ")

                    if len(parts) != 3:
                        continue

                    try:
                        saleYear = int(parts[0][0:4])
                        saleMonth = int(parts[0][5:7])
                        saleTotal = float(parts[2])

                    except ValueError:
                        continue

                    if saleYear == year and saleMonth == month:

                        totalSales += saleTotal
                        count += 1

        print("================")
        print(f"MONTHLY SALES - {monthNames[month - 1]} {year}")

        if count == 0:
            print("No sales recorded for this month.")

        else:
            print(f"Total sales  : PHP {totalSales:,.2f}")
            print(f"Transactions : {count}")

        print("================")

    elif choice == "3":

        validYear = False

        while not validYear:

            try:
                year = int(input("Enter year (example 2026): "))
                validYear = True

            except ValueError:
                print("Please enter a valid year.")

        monthTotals = [0] * 12
        monthCounts = [0] * 12

        if os.path.exists(salesFile):

            with open(salesFile, "r", encoding="utf-8") as file:

                for line in file:

                    parts = line.strip().split(" | ")

                    if len(parts) != 3:
                        continue

                    try:
                        saleYear = int(parts[0][0:4])
                        saleMonth = int(parts[0][5:7])
                        saleTotal = float(parts[2])

                    except ValueError:
                        continue

                    if saleYear == year and saleMonth >= 1 and saleMonth <= 12:

                        monthTotals[saleMonth - 1] += saleTotal
                        monthCounts[saleMonth - 1] += 1

        print("================")
        print(f"ANNUAL SALES - {year}")

        if sum(monthCounts) == 0:

            print("No sales recorded for this year.")

        else:

            for m in range(12):

                word = "transaction" if monthCounts[m] == 1 else "transactions"

                print(
                    f"{monthNames[m].ljust(10)} "
                    f"{('PHP ' + format(monthTotals[m], ',.2f')).rjust(16)} "
                    f"({monthCounts[m]} {word})"
                )

            print("----------------")

            print(f"Total sales  : PHP {sum(monthTotals):,.2f}")
            print(f"Transactions : {sum(monthCounts)}")

        print("================")

    elif choice == "4":

        showMenu = True

    elif choice == "5":

        print("Goodbye!")
        programRunning = False

    else:

        print("Invalid choice. Please type 1 to 5.")
