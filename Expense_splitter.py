def main():
    print("Welcome to the Expense Splitter!")
    num_people = int(input("Enter the number of people: "))
    amount = float(input("Enter the total amount: "))
    tip_rate = float(input("Enter the tip rate (e.g. 10%): "))
    
    def calculate_total(amount, tip_rate):
        return amount + (amount * tip_rate / 100)
    
    def split_bill(amount, num_people):
        return amount / num_people
    
    def display_receipt(amount, tip_rate, total_amount, split_amount):
        print("\n----- Receipt -----")
        print(f"Total Amount: ${amount:.2f}")
        print(f"Tip Rate: {tip_rate}%")
        print(f"Total Amount with Tip: ${total_amount:.2f}")
        print(f"Amount per Person: ${split_amount:.2f}")
        print("-------------------")
    
    total_amount = calculate_total(amount, tip_rate)
    split_amount = split_bill(total_amount, num_people)
    display_receipt(amount, tip_rate, total_amount, split_amount)

if __name__ == "__main__": 
    main()