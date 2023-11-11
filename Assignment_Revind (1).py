flight_array = []


#User System for the user_functionalities
def book_ticket(rows_data):
    book_num_rowA = (input("Enter the row number: "))
    book_num_seatA = (input("Enter the seat number: "))
    booked_sign = 'X'
    
    try:
        if not (book_num_rowA and book_num_seatA):
            print("Invalid Input")
        if (book_num_rowA and book_num_seatA):
            for i in range(len(rows_data)):
                for j in range(len(rows_data[i])):
                    if i == int(book_num_rowA)-1  and j == int(book_num_seatA):
                        if rows_data[i][j] == booked_sign:
                            print(f"Already Booked!")
                        elif rows_data[i][j] != booked_sign:
                            rows_data[i][j] = booked_sign
                            print(f"Seat {book_num_seatA} in a row {book_num_rowA} in a  booked successfully!")
        
    except:
        print(f"Inavlid Input! Enter the input in numbers")
def cancel_ticket(rows_data):
    booked_sign = "X"
    unbooked_sign = "*"
    row_num_book_A = int(input("Enter the row number: "))
    seat_num_book_A = int(input("Enter the seat number: "))
    for i in range(len(rows_data)):
        for j in range(len(rows_data[i])):
            if i == (row_num_book_A)-1 and j == seat_num_book_A:
                if rows_data[i][j] == unbooked_sign:
                    print(f"Already unbooked!")
                elif rows_data[i][j] == booked_sign:
                    rows_data[i][j] = unbooked_sign
                    print(f"Seat {seat_num_book_A} in a row {row_num_book_A} unbooked and cancelled successfully!")
def show_layout(seat_data_details):
    for i in seat_data_details:
        for j in i:
                print(j,end=" ")
        print()

def change_text(new_array):
    print()
    with open("Flight_Data_dictionary.txt", "w") as f:
        for i in new_array:
        # Convert the dictionary to a string for writing to the file
            line = str(i)
            f.write(line + '\n')



def change_layout(seats_data,rows_data):
    print()
    new_seat_array = ["seats"]
    new_seat_layout_array = []
    if seats_data and rows_data:
        seat_num = int(input("Enter the number of seats you want to add: "))
        for i in range(seat_num):
            seat_letters =  input(f"Enter the seats letter you want to give to seat{i+1}: ")
            new_seat_array.append(seat_letters)
        row_num  = int(input("How many rows you want to add into the flight company: "))
        sign = input("Enter a sign you want to give to your seats: ")
        for i in range(row_num):
            rows_array = [f"row{i+1}"]
            for j in range(seat_num):
                rows_array.append(sign)
            new_seat_layout_array.append(rows_array)
        if new_seat_array and new_seat_layout_array:
            seats_data = [new_seat_array]
            rows_data = [new_seat_layout_array]




def remove_flight():
    print()
 

def ask_company_user(user_input):
    new_array =[]
    seats_data_details = []
    f = open("Flight_Data_dictionary.txt","r")
    flight_input = input("Enter the Flight: ")
    print()
    for i in f:
        new_text = i.strip()
        elements = eval(new_text)
        new_array.append(elements)
        if flight_input in elements:
            print(elements)
            seats_data = elements[flight_input][f"Seats_names"]
            rows_data = elements[flight_input][f"seat_layout_array"]
            seats_data_details += seats_data + rows_data
            print(seats_data_details)
            if user_input:
                if user_input == 1:
                    show_layout(seats_data_details)
                    book_ticket(rows_data)
                    show_layout(seats_data_details)
                        
                elif user_input == 2:
                    show_layout(seats_data_details)
                    cancel_ticket(rows_data)
                    show_layout(seats_data_details)  
                else:
                    print(f"Invalid Input")
            


    change_text(new_array)        
        #change_text(new_array)          
def show_flights_text():
    print()
    try:
        f = open("Flight_Data_dictionary.txt","r")
        for i in f:
            new_text = i.strip()
            elements = eval(new_text)
            #for i in elements:
            for i in elements:
                for j in elements[i].values():
                    for k in j:
                        for j in k:
                            print(j,end= " ")
                        print()

    except:
            print(f"The Data not founded in the text file")
def user_system():
    print()
    #Event Control loop, so that when the user want to leave the user system or perform function with user system
    while True:
        print(f"Welcome User\n1. Book a Ticket\n2. Cancel a Booking\n3. Show a flights\n4. Exit the User System")
        user_input = input("Enter the corresponding number: ")
        #Conditional statements handle the user function execution and sub-function calls according to the input
        try:
            if not (user_input):
                print("Invalid Input")
            if user_input:
                if int(user_input) == 1:
                    user_input = 1
                    ask_company_user(user_input)
                    print()
                elif int(user_input) == 2:
                    user_input = 2
                    ask_company_user(user_input)
                elif int(user_input) == 3:
                    show_flights_text()
                    
                elif int(user_input) == 4:
                    print(f"You exit the User System")
                    #when the use enter number which assigned for leaving the user system, immediately break function stop while loop
                    break
            
        except:
            print(f"Invalid Input! Please Enter a number between 1-4")
def admin_system(flight_array):
    print()
    while True:
        try:
            print(f"Welcome Admin\n1. Add a Flight\n2. Modify a flight\n3. Remove a flight\n4. Exit the admin System")
            user_input = input("Enter the corresponding number: ")
            if int(user_input) == 1:
                add_flight(flight_array)
            elif int(user_input) == 2:
                modify_flight()
            elif int(user_input) == 3:
                remove_flight()
            elif int(user_input) == 4:
                print(f"You exit the admin system")
                break
            else:
                print(f"Invalid Input Selection")
        except:
            print("Invalid Input")
    
        print()
def add_flight(flight_array):
    print()
    seat_array = ["seats"]
    seat_layout_array= []
    
    try:
        company_name = input("Enter the name of the company you want to add: ")
        arrival_time = input("Enter the arrival time of the flight(just enter a number): ")
        departure_time = input("Enter the departure time of the flight(just enter the number): ")
        seat_num = int(input("Enter the number of seats you want to add: "))
        for i in range(seat_num):
            seat_letters =  input(f"Enter the seats letter you want to give to seat{i+1}: ")
            seat_array.append(seat_letters)
        row_num  = int(input("How many rows you want to add into the flight company: "))
        sign = input("Enter a sign you want to give to your seats: ")
        flight_company = [f"Flight_Company_Name:{company_name}"]
        flight_arrival_time = [f"flight_arrival_time: {arrival_time}"]
        flight_departure_time = [f"flight_departure_time: {departure_time}"]
        for i in range(row_num):
            rows_array = [f"row{i+1}"]
            for j in range(seat_num):
                rows_array.append(sign)
            seat_layout_array.append(rows_array)
        flight_array_details = [flight_company,flight_arrival_time, flight_departure_time,seat_array]
        flight_array += flight_array_details
        flight_array += seat_layout_array
        print(f"-"*50)
        show_flights(flight_array)
        print(f"{flight_array}")
        flight_dictionary(company_name,flight_company,flight_arrival_time,flight_departure_time,seat_array,seat_layout_array)
    except:
        print(f"Inavalid Input")        
def flight_dictionary(company_name,flight_company,flight_arrival_time,flight_departure_time,seat_array,seat_layout_array):
    print()
    flight_dict = {}
    try:
        if company_name:
            flight_dict_details = {f"Company_Flight_Name":[flight_company]
            ,f"flight_arrival_time": [flight_arrival_time]
            ,f"flight_departure_time": [flight_departure_time]
            ,f"Seat_layout": [[f"Seat_layout-{company_name}"]]
            ,f"Seats_names": [seat_array]
            ,f"seat_layout_array": seat_layout_array}
            flight_dict[company_name] = flight_dict_details
            print(flight_dict)
            text_flight_data(flight_dict)
        else:
            print(f"Data not founded")
    except:
        print(f"Data not added into the dictionary")
        print(flight_dict)
def text_flight_data(flight_dict):
    print()
    try:
        if flight_dict:
            f = open("Flight_Data_dictionary.txt","a")
            f.write(f"{flight_dict}\n")
            f.close
            print (f"flight data is entered in the text file as dictionary added successfully")
        else:
            print(f"Data not founded")
    except:
        print(f"Data is not exists and nothing is added")
def show_flights(flight_array):
    print()
    try:
        if flight_array:
            for i in flight_array:
                for j in i:
                    print(j,end= " ")
                print()
        else:
            print(f"No data is added to the flight array and data is not found in the array")
    except:
            print(f"The Data not founded!")
def modify_flight():
    print()
    try:
        print()
        print(f"modify function:\n1. Change Arrival and Departure time\n2. Change name of the flight\n3. Change layout of the flight")
        modify_input = input("Enter the corresponding number: ")
        if int(modify_input) == 1:
            modify_input = 1
               
        elif int(modify_input) == 2:
            modify_input = 2
           
        elif int(modify_input) == 3:
            modify_input = 3
           
            
    except:
        print("invalid input")


while True:
    print(f"Welcome to the Flight Management System\n\nUser System and Admin System are Available\n\nPlease Enter the name and the password to proceed further")
    print()
    name =  input("name: ")
    print()
    password = input("password: ")
    print()
    if name.lower() == "user" and password.lower() == "user123":
       user_system()
    elif name.lower() == "admin" and password.lower() == "admin123":
        admin_system(flight_array)
    else:
        print(f"Error!Wrong User of password. Try Again")
        print()