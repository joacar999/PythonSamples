###########################################################################
# Program that calculates the distribution of costs for a group of
# people who, # for example, pay different amounts for a joint dinner
###########################################################################
# Author: Jocke C and ChatGPT
# Copyright: No copyright. I created this togehter with help from chatGPT
# Email: joakim.carlsson@conciliodesign.se
###########################################################################

def split_costs():
    payments = {}

    # Number of participants
    n = int(input("How many people have made outlays? "))

    # Enter name and expense
    for i in range(n):
        name = input(f"Name of person {i+1}: ")
        amount = float(input(f"Expenses for {name} (SEK): "))
        payments[name] = amount

    # Total cost and share per person
    total = sum(payments.values())
    share = total / n

    # Calculate balances (positive = to be refunded, negative = to be paid)
    balances = {person: paid - share for person, paid in payments.items()}

    creditors = [(p, diff) for p, diff in balances.items() if diff > 0]
    debtors = [(p, -diff) for p, diff in balances.items() if diff < 0]

    transactions = []
    i, j = 0, 0

    while i < len(debtors) and j < len(creditors):
        debtor, debt = debtors[i]
        creditor, credit = creditors[j]

        amount = min(debt, credit)
        transactions.append(
            f"{debtor} pays {amount:.2f} SEK to {creditor}")

        debtors[i] = (debtor, debt - amount)
        creditors[j] = (creditor, credit - amount)

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    # --- Print ---
    print("=======================================2")
    print(f"Total cost: {total:.2f} SEK")
    print(f"Cost per person: {share:.2f} SEK\n")
    print("Transactions for settlement:")
    for t in transactions:
        print(" -", t)


# Run the function to split costs
split_costs()
