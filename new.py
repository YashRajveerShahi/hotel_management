
class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")

        self.guests = []
        self.reservations = []

        # Labels
        tk.Label(self.root, text="Guest Name:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="Room Number:").grid(row=1, column=0, padx=10, pady=10)

        # Entry fields
        self.guest_name_entry = tk.Entry(self.root)
        self.guest_name_entry.grid(row=0, column=1, padx=10, pady=10)
        self.room_number_entry = tk.Entry(self.root)
        self.room_number_entry.grid(row=1, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Add Guest", command=self.add_guest).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="Book Room", command=self.book_room).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        tk.Button(self.root, text="Display Reservations", command=self.display_reservations).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def add_guest(self):
        guest_name = self.guest_name_entry.get()
        if guest_name:
            self.guests.append(guest_name)
            messagebox.showinfo("Success", f"Guest '{guest_name}' added successfully!")
            self.guest_name_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a guest name.")

    def book_room(self):
        guest_name = self.guest_name_entry.get()
        room_number = self.room_number_entry.get()

        if guest_name and room_number:
            self.reservations.append((guest_name, room_number))
            messagebox.showinfo("Success", f"Room '{room_number}' booked for '{guest_name}'.")
            self.guest_name_entry.delete(0, tk.END)
            self.room_number_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter both guest name and room number.")

    def display_reservations(self):
        if self.reservations:
            reservations_info = "\n".join([f"Guest: {guest}, Room: {room}" for guest, room in self.reservations])
            messagebox.showinfo("Reservations", reservations_info)
        else:
            messagebox.showinfo("Reservations", "No reservations yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
