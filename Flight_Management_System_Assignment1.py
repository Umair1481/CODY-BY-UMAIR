#function having argument next text data call when the changes made in the text file and new text add to the exiting file
def change_text(new_text_data):
    try:
        print()
        #open file for the write mode
        with open("Flight_Data_dictionary.txt", "w") as f:
            #iterating over the text which is going to bhi write in file
            for i in new_text_data:
            # Convert the dictionary to a string for writing to the file
                line = str(i)
                f.write(line + '\n')
    except:
       print(f"Changed data is not added to the text file")
def book_ticket(flight_input,text_data):
    #array beneathe used to show the change before and after made by user
    current_seat_data = []
    #data is being fetched out by the user
    seats_data = text_data[flight_input][f"Seats_names"]
    rows_data = text_data[flight_input][f"seat_layout_array"]
    current_seat_data += seats_data + rows_data
    print(f"Company Flight {flight_input}-layout")
    show_layout(current_seat_data)
    book_num_row = int(input("Enter the row number: "))
    book_num_seat = int(input("Enter the seat number: "))
    booked_sign = 'X'
    try:
        for i in range(len(rows_data)):
            for j in range(len(rows_data[i])):
                if i == book_num_row-1  and j == book_num_seat:
                    if rows_data[i][j] == booked_sign:
                        print(f"Already Booked!")
                    elif rows_data[i][j] != booked_sign:
                        rows_data[i][j] = booked_sign
                        print(f"Seat {book_num_seat} in a row {book_num_row} in a  booked successfully!")
                        show_layout(current_seat_data)
                        break
    except:
        print(f"Nothing is booked! Input is Invalid")
#cancel function with the arguments flight name and text data from the text file handle the data of book       
def cancel_ticket(flight_input,text_data):
    #the same method used as in the above function but in that function we are only changing the booked sign 
    # into another sign 
    current_seat_data = []
    seats_data = text_data[flight_input][f"Seats_names"]
    rows_data = text_data[flight_input][f"seat_layout_array"]
    current_seat_data += seats_data + rows_data
    show_layout(current_seat_data)
    book_num_row = int(input("Enter the row number: "))
    book_num_seat = (input("Enter the seat number: "))
    booked_sign = 'X'
    unbooked_sign = "*"
    try:  
        for i in range(len(rows_data)):
            for j in range(len(rows_data[i])):
                if i == (book_num_row)-1  and j == int(book_num_seat):
                    if rows_data[i][j] != booked_sign:
                        print(f"Already unbooked!")
                    elif rows_data[i][j] == booked_sign:
                        rows_data[i][j] = unbooked_sign
                        print(f"Seat in column {book_num_seat} in a row {book_num_row} in a flight-{flight_input} unbooked adn successfully!")
        show_layout(current_seat_data)
    except:
        print(f"Nothing is cancelled! Input is Invalid")

#sub-function called when the changed made by the used in the 2d array layout rows and columns
def show_layout(current_seat_data):
    for i in current_seat_data:
        for j in i:
            print(j,end=" ")
        print()
#this fuunction read all the data in the text file , iterate over the text data and return the columns of details in the text file of the flight
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
def user():
    #Event Control loop, so that when the user want to leave the user system or perform function with user system
    while True:
        print(f"Welcome User\n1. Book a Ticket\n2. Cancel a Booking\n3. Show a flights\n4. Exit the User System")
        #Conditional statements handle the user function execution and sub-function calls according to the input
        try:
            user_input = int(input("Enter the corresponding number: "))
            if user_input < 3 and user_input != 0:
                flight_input = input(f"Enter the name of the flight_company: ")
                if flight_input:
                    #collection data is introduced in order to check the flight is exits in the data
                    collection_dict = {}
                    new_array =[]
                    f = open("Flight_Data_dictionary.txt","r")
                    for i in f:
                        new_text = i.strip()
                        text_data = eval(new_text)
                        new_array.append(text_data)
                        if flight_input in text_data:
                            if flight_input and user_input:
                                if user_input == 1:
                                    book_ticket(flight_input,text_data)
                                elif user_input == 2:
                                    cancel_ticket(flight_input,text_data)
                    change_text(new_array)
                    for i in new_array:
                        collection_dict.update(i)
                    if flight_input not in collection_dict:
                        print(f"The flight data is not exits in the data")
            elif user_input == 3:
                show_flights_text()
            elif user_input == 4:
                print(f"You exit the User System")
                #when the use enter number which assigned for leaving the user system, immediately break function stop while loop
                break
        except:
            print(f"Invalid Input! Please Enter a number between 1-4")
# same logic used in the admin system to handle the data as used in the user data       
def admin():
    print()
    while True:
        print(f"Welcome Admin\n1. Add a Flight\n2. Modify a flight\n3. Remove a flight\n4. Exit the admin System")
        try:
            admin_input = int(input("Enter the corresponding number: "))
            if admin_input == 1 and admin_input != 0:
                company_name = input("Enter the name of the flight You want to add: ")
                new_array =[]
                collection_dict ={}
                f = open("Flight_Data_dictionary.txt","r")
                #iterating over the exiting data in the text file
                for i in f:
                    new_text = i.strip()
                    #strip function remove all the new line character from the strings in exiting file
                    #eval function used to convert data from the string into elements or separated data for the list
                    text_data = eval(new_text)
                    new_array.append(text_data)
                for i in new_array:
                    collection_dict.update(i)
                if company_name not in collection_dict:
                    add_flight(company_name)
                else:
                    print(f"The company named {company_name} is already exits in data")
            elif admin_input == 2:
                print()
                print(f"modify function:\n1. Change Arrival and Departure time\n2. Change name of the flight\n3. Change layout of the flight")
                try:
                    modify_input = int(input("Enter the corresponding number: "))
                    flight_input = input("Enter the name of the flight You want to modify: ")
                    new_array =[]
                    collection_dict = {}
                    f = open("Flight_Data_dictionary.txt","r")
                    for i in f:
                        new_text = i.strip()
                        text_data = eval(new_text)
                        new_array.append(text_data)
                        if flight_input in text_data:
                            if flight_input and modify_input:
                                if modify_input == 1:
                                    change_times(flight_input,text_data)
                                elif modify_input == 2:
                                    change_name(flight_input,text_data)
                                elif modify_input == 3:
                                    new_layout(flight_input,text_data)
                    change_text(new_array)
                    for i in new_array:
                        collection_dict.update(i)
                    if flight_input not in collection_dict:
                        print(f"The flight data with the named {flight_input} is not exits in the data")
                except:
                    print(f"Invalid Input")
            elif admin_input == 3:
                flight_input = input("Enter the name of the flight You want to remove: ")
                new_array =[]
                collection_dict = {}
                f = open("Flight_Data_dictionary.txt","r")
                for i in f:
                    new_text = i.strip()
                    text_data = eval(new_text)
                    new_array.append(text_data)
                    if flight_input in text_data:
                        if flight_input and admin_input:
                            if admin_input == 3:
                                remove_flight(flight_input,text_data)
                change_text(new_array)
                for i in new_array:
                    collection_dict.update(i)
                if flight_input not in collection_dict:
                    print(f"The flight data is not exits or removed from the data")
            elif admin_input == 4:
                print(f"You exit the admin System")
                #when the use enter number which assigned for leaving the user system, immediately break function stop while loop
                break
        except:
            print(f"Invalid Input! Please Enter a number between 1-4")
#Add function used to add flight daat, also it adds a the data into the text file and dictionary both as well
# This function also used show the when data in the text file saved in the text file.
def add_flight(company_name):    
    flight_add = []
    seat_array = ["seats"]
    seat_layout_array= []
    try:
        arrival_time = int(input("Enter the arrival time of the flight(just enter a number): "))
        departure_time = int(input("Enter the departure time of the flight(just enter the number): "))
        seat_num = int(input("Enter the number of seats you want to add: "))
        for i in range(seat_num):
            seat_letters =  input(f"Enter the seats letter you want to give to seat{i+1}: ").upper()
            seat_array.append(seat_letters)
        row_num  = int(input("How many rows you want to add into the flight company: "))
        sign = input("Enter a sign you want to give to your seats: ")
        flight_company = [f"Flight_Company_Name:{company_name}"]
        flight_arrival_time = [f"flight_arrival_time: {arrival_time}:00"]
        flight_departure_time = [f"flight_departure_time: {departure_time}:00"]
        for i in range(row_num):
            rows_array = [f"row{i+1}"]
            for j in range(seat_num):
                rows_array.append(sign)
            seat_layout_array.append(rows_array)
        flight_array_details = [flight_company,flight_arrival_time, flight_departure_time,seat_array]
        flight_add += flight_array_details
        flight_add += seat_layout_array
        print(f"-"*50)
        print(f"{flight_add}")
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
#This function shows the data when the new file added
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
#This function changes the time of file data
def change_times(flight_input,text_data):
    times_data = []
    arrival_data = text_data[flight_input][f"flight_arrival_time"]  
    departurture_data = text_data[flight_input][f"flight_departure_time"]
    #times data is the 2d array so that it become a 2d array and we can change both the names
    times_data += arrival_data + departurture_data
    new_arrival = input("Enter the new arrival time you want to add: ")
    new_departure = input("Enter the new departure time you want to add: ")
    #times data also changes when the user make changes into it
    print(f"The previous times for the flights")
    show_times(times_data)
    for i in range(len(times_data)):
        for j in range(len(times_data[i])):
            if times_data[0][0] != f"flight_arrival_time: {new_arrival}:00":    
                times_data[0][0] = f"flight_arrival_time: {new_arrival}:00"
            if times_data[1][0] != f"flight_departure_time: {new_departure}:00":
                times_data[1][0] = f"flight_departure_time: {new_departure}:00"
    print(f"The new times for the flights")
    show_times(times_data)
    #similar logic is applied on the sub-functions
def show_times(times_data):
    for i in times_data:
        for j in i:
            print(j,end=" ")
        print()
def change_name(flight_input,text_data):
    print()
    name_data = text_data[flight_input][f"Company_Flight_Name"] 
    if name_data:
        new_name = input("Enter the new name of the flight: ").lower()
        if new_name:
            name_data[0] = [f"flight_arrival_time: {new_name}"]
            if {flight_input}:
                text_data[new_name] = text_data.pop(flight_input)
            print(f"The company named {flight_input} is changed now and does not exits in the record")

def new_layout(flight_input,text_data):
    print()
    previous_layout = []
    new_seat_array = ["seat"]
    new_seat_layout_array = []
    change_layout = []
    seats_data = text_data[flight_input][f"Seats_names"]
    rows_data = text_data[flight_input][f"seat_layout_array"]      
    previous_layout += seats_data + rows_data
    print(f"The previous layout for the {flight_input}")
    show_previous_layout(previous_layout)
    seat_num = int(input("Enter the number of new seats you want to add: "))
    for i in range(seat_num):
        seat_letters =  input(f"Enter the seats new letter you want to give to seat{i+1}: ").upper()
        new_seat_array.append(seat_letters)
    row_num  = int(input("How many new rows you want to add into the flight company: "))
    row_name = input("Enter the new name of rows: ").capitalize()
    sign = input("Enter a new sign you want to give to your seats: ")
    for i in range(row_num):
        rows_array = [f"{row_name}{i+1}"]
        for j in range(seat_num):
            rows_array.append(sign)
        new_seat_layout_array.append(rows_array)
    change_seats(flight_input,text_data,new_seat_array,change_layout)
    change_rows(flight_input,text_data,new_seat_layout_array,change_layout)
    print(f"The new layout for the {flight_input}")
    show_change_layout(change_layout)
def show_previous_layout(previous_layout):
    for i in previous_layout:
        for j in i:
            print(j,end = " ")
        print()
def change_seats(flight_input,text_data,new_seat_array,change_layout):
    seats_data = text_data[flight_input][f"Seats_names"]
    if seats_data and new_seat_array:
        seats_data[0] = new_seat_array
        change_layout += seats_data
def change_rows(flight_input,text_data,new_seat_layout_array,change_layout):
    rows_data = text_data[flight_input][f"seat_layout_array"]  
    if rows_data:
        rows_data.clear()
        rows_data += new_seat_layout_array
        change_layout += rows_data
def show_change_layout(change_layout):
    for i in change_layout:
        for j in i:
            print(j,end= " ")
        print()
def remove_flight(flight_input,text_data):
    if text_data:
       del text_data[flight_input]
       print(f"The {flight_input} is removed from the flight records")
while True:
    print(f"Welcome to the Flight Management System\n\nUser System and Admin System are Available\n\nPlease Enter the name and the password to proceed further")
    print()
    name =  input("name: ")
    print()
    password = input("password: ")
    print()
    if name.lower() == "user" and password.lower() == "user123":
       user()
    elif name.lower() == "admin" and password.lower() == "admin123":
        admin()
    else:
        print(f"Error!Wrong User of password. Try Again")
        print()
