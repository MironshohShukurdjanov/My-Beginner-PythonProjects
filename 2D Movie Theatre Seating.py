# Initial 5x5 seating chart (all seats are available)
seating_chart = [["A" for _ in range(5)] for _ in range(5)]


def display_seating(chart):
    print("Seating Chart:")
    for row in chart:
        print(" ".join(row))
    print()


while True:
    display_seating(seating_chart)

    # Ask the user to book a seat or quit
    user_input = input("Enter row and column to book a seat (e.g., '1 2'), or 'q' to quit: ")

    if user_input.lower() == "q":
        print("Exiting program. Goodbye!")
        break

    try:
        # Parse row and column input
        row, col = map(int, user_input.split())

        # Check if the seat is valid and available
        if seating_chart[row][col] == "A":
            seating_chart[row][col] = "B"  # Book the seat
            print(f"Seat at row {row}, column {col} has been booked.\n")
        else:
            print(f"Seat at row {row}, column {col} is already booked. Try another seat.\n")
    except (ValueError, IndexError):
        print("Invalid input! Please enter a valid row and column (e.g., '1 2').\n")