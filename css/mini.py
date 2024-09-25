import tkinter as tk
from tkinter import ttk

# Function to switch between screens
def show_screen(screen_name):
    for screen in screens.values():
        screen.pack_forget()
    screens[screen_name].pack(expand=True, fill='both')

# Create the main window
root = tk.Tk()
root.title("Hostel Room Booking System")
root.geometry("400x600")

# Create screens with different background colors
welcome_screen = tk.Frame(root, bg="#f0f8ff")
login_screen = tk.Frame(root, bg="#ffebcd")
selection_screen = tk.Frame(root, bg="#e6e6fa")
details_screen = tk.Frame(root, bg="#ffe4e1")
block_screen = tk.Frame(root, bg="#f5f5dc")
na_room_details_screen = tk.Frame(root, bg="#d3d3d3")
details_screen_new = tk.Frame(root, bg="#ffe4c4")
success_screen = tk.Frame(root, bg="#faf0e6")
phub_screen = tk.Frame(root, bg="#e0ffff")
google_login_screen = tk.Frame(root, bg="#f0f8ff")  # New screen for Google login

# Welcome Screen
welcome_label = tk.Label(welcome_screen, text="HOSTEL ROOM BOOKING", font=("Arial", 24, "bold"), bg="#f0f8ff")
welcome_label.pack(pady=20)
get_started_button = tk.Button(welcome_screen, text="Get Started", command=lambda: show_screen('login_screen'), bg="#4CAF50", fg="white")
get_started_button.pack(pady=20)

# Login Screen
login_title = tk.Label(login_screen, text="Log In", font=("Arial", 24, "bold"), bg="#ffebcd")
login_title.pack(pady=20)
username_entry = tk.Entry(login_screen, width=30)
username_entry.insert(0, "Username")
username_entry.pack(pady=10)
password_entry = tk.Entry(login_screen, width=30, show='*')
password_entry.insert(0, "Password")
password_entry.pack(pady=10)
error_message = tk.Label(login_screen, text="", fg="red", bg="#ffebcd")
error_message.pack(pady=10)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username.startswith('05230') and len(username) == 8 and password == '456':
        error_message.config(text='')
        show_screen('selection_screen')
    else:
        error_message.config(text='Invalid username or password. Please try again.')

login_button = tk.Button(login_screen, text="Log In", command=validate_login, bg="#4682b4", fg="white")
login_button.pack(pady=20)

# Google Login Button
google_login_button = tk.Button(login_screen, text="Login Using Google", command=lambda: show_screen('google_login_screen'), bg="#DB4437", fg="white")
google_login_button.pack(pady=10)

# Google Login Screen
google_login_label = tk.Label(google_login_screen, text="Login with Google", font=("Arial", 24, "bold"), bg="#f0f8ff")
google_login_label.pack(pady=20)

google_account_options = [
    "phub.jnec@rub.edu.bt",
    "phub345@gmail.com",
    "student.jnec@rub.edu.bt",
    "Use another account"
]

# Create buttons for Google account options
for account in google_account_options:
    google_account_button = tk.Button(google_login_screen, text=account, width=30, command=lambda a=account: print(f"{a} selected"), bg="#f8f8f8")
    google_account_button.pack(pady=5)

# Button to proceed to the selection screen
next_button_google = tk.Button(google_login_screen, text="Next", command=lambda: show_screen('selection_screen'), bg="#34A853", fg="white")
next_button_google.pack(pady=20)

# Selection Screen (Boarding and Self Catering with Logout Button)
boarding_button = tk.Button(selection_screen, text="Boarding", command=lambda: show_screen('details_screen'), bg="#32cd32", fg="white")
boarding_button.pack(pady=10)

self_catering_button = tk.Button(selection_screen, text="Self Catering", command=lambda: show_screen('details_screen'), bg="#ffa07a", fg="white")
self_catering_button.pack(pady=10)

logout_button = tk.Button(selection_screen, text="Logout", command=lambda: show_screen('phub_screen'), bg="#dc143c", fg="white")
logout_button.pack(pady=30)

# Details Screen
details_label = tk.Label(details_screen, text="Add Your Detail", font=("Arial", 24, "bold"), bg="#ffe4e1")
details_label.pack(pady=10)

name_label = tk.Label(details_screen, text="Name:", bg="#ffe4e1")
name_label.pack(pady=5)
name_entry = tk.Entry(details_screen)
name_entry.pack(pady=5)

student_id_label = tk.Label(details_screen, text="Student ID:", bg="#ffe4e1")
student_id_label.pack(pady=5)
student_id_entry = tk.Entry(details_screen)
student_id_entry.pack(pady=5)

gender_label = tk.Label(details_screen, text="Gender:", bg="#ffe4e1")
gender_label.pack(pady=5)
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(details_screen, textvariable=gender_var, values=["Male", "Female"], state="readonly")
gender_dropdown.pack(pady=5)

course_label = tk.Label(details_screen, text="Course:", bg="#ffe4e1")
course_label.pack(pady=5)
course_var = tk.StringVar()
course_dropdown = ttk.Combobox(details_screen, textvariable=course_var, values=["DCSN", "DMPM", "DE", "DM"], state="readonly")
course_dropdown.pack(pady=5)

year_label = tk.Label(details_screen, text="Year:", bg="#ffe4e1")
year_label.pack(pady=5)
year_var = tk.StringVar()
year_dropdown = ttk.Combobox(details_screen, textvariable=year_var, values=["First Year", "Second Year"], state="readonly")
year_dropdown.pack(pady=5)

next_button = tk.Button(details_screen, text="Next", command=lambda: show_screen('block_screen'), bg="#8a2be2", fg="white")
next_button.pack(pady=10)

# Block Selection Screen
block_label = tk.Label(block_screen, text="Select the Block", font=("Arial", 24, "bold"), bg="#f5f5dc")
block_label.pack(pady=10)

n_block_button = tk.Button(block_screen, text="N Block", command=lambda: show_screen('na_room_details_screen'), bg="#00bfff", fg="white")
n_block_button.pack(pady=5)

j_block_button = tk.Button(block_screen, text="J Block", command=lambda: show_screen('na_room_details_screen'), bg="#ff69b4", fg="white")
j_block_button.pack(pady=5)

d_block_button = tk.Button(block_screen, text="D Block", command=lambda: show_screen('na_room_details_screen'), bg="#ff8c00", fg="white")
d_block_button.pack(pady=5)

# Na Room Details Screen
na_room_details_label = tk.Label(na_room_details_screen, text="Na Room Details", font=("Arial", 24, "bold"), bg="#d3d3d3")
na_room_details_label.pack(pady=10)

ground_floor_label = tk.Label(na_room_details_screen, text="Ground Floor Rooms:", font=("Arial", 18), bg="#d3d3d3")
ground_floor_label.pack(pady=5)

ground_floor_rooms = [
    "Room 1-2",
    "Room 3-4",
    "Room 5-6",
    "Room 7-8",
    "Room 9-10",
    "Room 11-12",
    "Room 13-14",
    "Room 15-16"
]

for room in ground_floor_rooms:
    room_label = tk.Label(na_room_details_screen, text=room, bg="#d3d3d3")
    room_label.pack()

first_floor_label = tk.Label(na_room_details_screen, text="First Floor Rooms:", font=("Arial", 18), bg="#d3d3d3")
first_floor_label.pack(pady=5)

first_floor_rooms = [
    "Room 17-18",
    "Room 19-20",
    "Room 21-22",
    "Room 23-24",
    "Room 25-26",
    "Room 27-28",
    "Room 29-30",
    "Room 31-32"
]

for room in first_floor_rooms:
    room_label = tk.Label(na_room_details_screen, text=room, bg="#d3d3d3")
    room_label.pack()

proceed_button = tk.Button(na_room_details_screen, text="Proceed", command=lambda: show_screen('details_screen_new'), bg="#4682b4", fg="white")
proceed_button.pack(pady=10)

# Add Total, Booked, Available buttons
total_button = tk.Button(na_room_details_screen, text="Total", command=lambda: print("Total Rooms"), bg="black", fg="white")
total_button.pack(pady=5)

booked_button = tk.Button(na_room_details_screen, text="Booked", command=lambda: print("Booked Rooms"), bg="black", fg="white")
booked_button.pack(pady=5)

available_button = tk.Button(na_room_details_screen, text="Available", command=lambda: print("Available Rooms"), bg="black", fg="white")
available_button.pack(pady=5)

# New Detail Screen with Rectangle Placeholders
new_details_label = tk.Label(details_screen_new, text="New Detail Screen", font=("Arial", 24, "bold"), bg="#ffe4c4")
new_details_label.pack(pady=10)

# Create rectangles with specified contents
details = ["Phub", "Female", "05230124", "DCSN", "Second Year", "Na Block"]
rectangle_height = 50  # Fixed height for rectangles
for detail in details:
    rectangle_frame = tk.Frame(details_screen_new, width=300, height=rectangle_height, bg="lightgrey", bd=2, relief="solid")
    rectangle_frame.pack(pady=5)
    detail_label = tk.Label(rectangle_frame, text=detail, bg="lightgrey")
    detail_label.pack(expand=True, fill='both')

next_button_new = tk.Button(details_screen_new, text="Next", command=lambda: show_screen('success_screen'), bg="#8a2be2", fg="white")
next_button_new.pack(pady=10)

# Success Screen
success_label = tk.Label(success_screen, text="Booking Successful!", font=("Arial", 24, "bold"), bg="#faf0e6")
success_label.pack(pady=20)
success_message = tk.Label(success_screen, text="Thank you for booking with us!", bg="#faf0e6")
success_message.pack(pady=10)

# Phub Screen
phub_label = tk.Label(phub_screen, text="Phub", font=("Arial", 24, "bold"), bg="#e0ffff")
phub_label.pack(pady=20)

# Button to return to the welcome screen
return_button = tk.Button(phub_screen, text="Return to Welcome", command=lambda: show_screen('welcome_screen'), bg="#4682b4", fg="white")
return_button.pack(pady=10)

# Create a dictionary to hold all screens
screens = {
    'welcome_screen': welcome_screen,
    'login_screen': login_screen,
    'selection_screen': selection_screen,
    'details_screen': details_screen,
    'block_screen': block_screen,
    'na_room_details_screen': na_room_details_screen,
    'details_screen_new': details_screen_new,
    'success_screen': success_screen,
    'phub_screen': phub_screen,
    'google_login_screen': google_login_screen  # Adding Google login screen to the dictionary
}

# Show the welcome screen initially
show_screen('welcome_screen')

# Run the application
root.mainloop()
