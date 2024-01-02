import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

class LeaveBalanceApp:
    def __init__(self, master, db):
        self.master = master
        self.master.title("Leave Balance App")

        self.db = db
        self.collection = db.leave_balances

        self.leave_balance = tk.DoubleVar()
        self.leave_balance.set(0.0)

        self.create_widgets()

    def create_widgets(self):
        # Leave Balance Label and Entry
        tk.Label(self.master, text="Leave Balance:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.master, textvariable=self.leave_balance, state="readonly", width=15).grid(row=0, column=1, padx=10, pady=10)

        # Deduct Leave Button
        tk.Button(self.master, text="Deduct Leave", command=self.deduct_leave).grid(row=1, column=0, columnspan=2, pady=10)

    def deduct_leave(self):
        try:
            leave_to_deduct = float(tk.simpledialog.askstring("Deduct Leave", "Enter leave to deduct:"))
            current_balance = self.leave_balance.get()

            if leave_to_deduct <= current_balance:
                new_balance = current_balance - leave_to_deduct
                self.leave_balance.set(new_balance)

                # Update MongoDB
                self.collection.update_one({}, {"$set": {"balance": new_balance}}, upsert=True)

                messagebox.showinfo("Leave Deducted", f"Leave deducted successfully!\nNew balance: {new_balance}")
            else:
                messagebox.showerror("Insufficient Leave Balance", "Not enough leave balance to deduct.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for leave deduction.")

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.leave_balance_db

    # Create Tkinter window
    root = tk.Tk()
    app = LeaveBalanceApp(root, db)
    root.mainloop()

if __name__ == "__main__":
    main()
    
