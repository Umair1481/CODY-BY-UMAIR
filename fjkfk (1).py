flight_array = []

#User System for the user_functionalities
def book_ticket(rows,data):
    book_num_rowA = (input("Enter the row number: "))
    book_num_seatA = (input("Enter the seat number: "))
    booked_sign = 'X'
    
    try:
        if not (book_num_rowA and book_num_seatA):
            print("Invalid Input")
        if (book_num_rowA and book_num_seatA):
            for i in range(len(rows)):
                for j in range(len(rows[i])):
                    if i == int(book_num_rowA)-1  and j == int(book_num_seatA):
                        if rows[i][j] == booked_sign:
                            print(f"Already Booked!")
                        elif rows[i][j] != booked_sign:
                            rows[i][j] = booked_sign
                            print(f"Seat {book_num_seatA} in a row {book_num_rowA} in a  booked successfully!")
        show_layout(data)
    except:
        print(f"Inavlid Input! Enter the input in numbers")
def cancel_ticket(rows,data):
    booked_sign = "3"
    unbooked_sign = "*"
    row_num_book_A = int(input("Enter the row number: "))
    seat_num_book_A = int(input("Enter the seat number: "))
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i == (row_num_book_A)-1 and j == seat_num_book_A:
                if rows[i][j] == unbooked_sign:
                    print(f"Already Cancelled and unbooked!")
                elif rows[i][j] == booked_sign:
                    rows[i][j] = unbooked_sign
                    print(f"Seat {seat_num_book_A} in a row {row_num_book_A} unbooked and cancelled successfully!")
    show_layout(data)
def show_layout(data):
    for i in data:
        for j in i:
            for k in j:
                print(k,end=" ")
            print()
def change_text(new_array):
    print()
    with open("Flight_Data_dictionary.txt", "w") as f:
        for i in new_array:
        # Convert the dictionary to a string for writing to the file
            line = str(i)
            f.write(line + '\n') 
def ask_company():
    user_input = int(input("Enter the number: "))
    new_array =[]
    f = open("Flight_Data_dictionary.txt","r")
    flight_input = input("Enter the Flight: ")
    for i in f:
        new_text = i.strip()
        elements = eval(new_text)
        new_array.append(elements)
        if flight_input in elements:
            data = [elements[flight_input][f"Seats_names_{flight_input}"]]
            print(data)
            if data:
                rows = elements[flight_input][f"seat_layout_array_{flight_input}"]
                data.append(rows)
                if rows:
                    if user_input == 1:
                        book_ticket(rows,data)
                    elif user_input == 2:
                        cancel_ticket(rows,data)
            
                
            change_text(new_array)
ask_company()
