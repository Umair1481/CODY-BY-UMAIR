def change_times(times_data):
    new_arrival = input("Enter the new arrival time you want to add: ")
    new_departure = input("Enter the new departure time you want to add: ")
    for i in range(len(times_data)):
        for j in range(len(times_data[i])):
            if times_data[0][0] != f"flight_arrival_time: {new_arrival}":    
                times_data[0][0] = f"flight_arrival_time: {new_arrival}"
            if times_data[1][0] != f"flight_arrival_time: {new_departure}":
                times_data[1][0] = f"flight_arrival_time: {new_departure}"
def change_name(name_data,elements,flight_input):
    print()
    if name_data:
        new_name = input("Enter the new name of the flight: ")
        if new_name:
            name_data[0] = [f"flight_arrival_time: {new_name}"]
            if {flight_input}:
                elements[new_name] = elements.pop(flight_input)
            print(elements)
def remove_flight(elements,flight_input):
    if elements:
       del elements[flight_input]
       


    
    
    
            
def new_layout(new_seat_array,new_seat_layout_array):
    print()
    seat_num = int(input("Enter the number of new seats you want to add: "))
    for i in range(seat_num):
        seat_letters =  input(f"Enter the seats new letter you want to give to seat{i+1}: ")
        new_seat_array.append(seat_letters)
    row_num  = int(input("How many new rows you want to add into the flight company: "))
    row_name = input("Enter the new name of rows: ")
    sign = input("Enter a new sign you want to give to your seats: ")
    for i in range(row_num):
        rows_array = [f"{row_name}{i+1}"]
        for j in range(seat_num):
            rows_array.append(sign)
        new_seat_layout_array.append(rows_array)
def change_seats(seats_data,new_seat_array):
    if seats_data and new_seat_array:
        seats_data[0] = new_seat_array
    
def change_rows(rows_data,new_seat_layout_array):
        if rows_data:
            rows_data.clear()
            rows_data += new_seat_layout_array
def show_times(times_data):
    for i in times_data:
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
modify_input = int(input("Enter a number: "))
def ask_company_admin(modify_input):
    new_array =[]
    times_data = []
    new_seat_array = ["seats"]
    new_seat_layout_array = []
    
    f = open("Flight_Data_dictionary.txt","r")
    flight_input = input("Enter the Flight: ")
    for i in f:
        new_text = i.strip()
        elements = eval(new_text)
        new_array.append(elements)
        if flight_input in elements:     
            name_data = elements[flight_input][f"Company_Flight_Name"] 
            arrival_data = elements[flight_input][f"flight_arrival_time"]  
            departurture_data = elements[flight_input][f"flight_departure_time"]
            seats_data = elements[flight_input][f"Seats_names"]  
            rows_data = elements[flight_input][f"seat_layout_array"]   
            times_data += arrival_data + departurture_data
            if modify_input:
                if modify_input == 1:
                    print()
                    show_times(times_data)
                    change_times(times_data)  
                    
                elif modify_input == 2:
                    new_layout(new_seat_array,new_seat_layout_array)
                    change_seats(seats_data,new_seat_array)
                    change_rows(rows_data,new_seat_layout_array)
                elif modify_input == 3:        
                    change_name(name_data,elements,flight_input)                    
                    remove_flight(elements,flight_input)                
    change_text(new_array) 
ask_company_admin(modify_input)       