import tkinter as tk                       # Import Tkinter for GUI
from tkinter import messagebox             # Import messagebox for popups
from matplotlib.figure import Figure       # Import Figure for Matplotlib plotting
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Embed plots in Tkinter

# ---------------- Helper Function ---------------- #
def show_value(value):
    """
    Show a popup message with the current value of a widget.
    value: The value to display (string, number, boolean, etc.)
    """
    messagebox.showinfo("Widget Value", str(value))  # Show info dialog with value

# ---------------- Root Window ---------------- #
root = tk.Tk()                     # Create main window
root.title("Tkinter + Matplotlib Sample")  # Window title
root.geometry("600x500")           # Window size
root.configure(bg="lightblue")     # Background color

# ---------------- Label ---------------- #
tk.Label(
    root,
    text="Enter 3 numbers and check the box",
    bg="lightblue",
    fg="black",
    font=("Arial", 14)
).pack(pady=10)

# ---------------- Entries ---------------- #
entry_vars = [tk.StringVar(value="0") for _ in range(3)]  # 3 variables for Entry widgets
entries = []

for i in range(3):
    e = tk.Entry(
        root,
        textvariable=entry_vars[i],
        bg="white",
        fg="black",
        font=("Arial", 12),
        width=20,
        justify="center",
        relief="sunken"
    )
    e.pack(pady=5)
    entries.append(e)

# ---------------- Checkbutton ---------------- #
check_var = tk.BooleanVar(value=False)  # Track checkbox state
check = tk.Checkbutton(
    root,
    text="Check me!",
    variable=check_var,
    onvalue=True,
    offvalue=False,
    font=("Arial", 12),
    bg="white"
)
check.pack(pady=10)

# ---------------- Button to Show Values ---------------- #
def show_inputs():
    """
    Collect Entry and Checkbutton values and display them in a popup.
    """
    values = [v.get() for v in entry_vars]  # Get Entry values
    checkbox = check_var.get()              # Get Checkbutton value
    messagebox.showinfo("Values Entered", f"Entries: {values}\nCheckbox: {checkbox}")

tk.Button(
    root,
    text="Show Values",
    command=show_inputs,
    bg="green",
    fg="white",
    font=("Arial", 12)
).pack(pady=10)

# ---------------- Button to Plot Values ---------------- #
def plot_values():
    """
    Create a Matplotlib line plot of the 3 Entry values.
    """
    try:
        values = [float(v.get()) for v in entry_vars]  # Convert to floats
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter numeric values!")
        return

    # Create a new window for the plot
    plot_win = tk.Toplevel(root)
    plot_win.title("Matplotlib Plot")
    plot_win.geometry("500x400")

    # Create Matplotlib Figure and Axes
    fig = Figure(figsize=(5,4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([1,2,3], values, marker='o', linestyle='-', color='blue')  # Line plot
    ax.set_title("Entry Values Plot")
    ax.set_xlabel("Entry Number")
    ax.set_ylabel("Value")
    ax.grid(True)

    # Embed plot in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=plot_win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

tk.Button(
    root,
    text="Plot Values",
    command=plot_values,
    bg="orange",
    fg="white",
    font=("Arial", 12)
).pack(pady=10)

# ---------------- Run Mainloop ---------------- #
root.mainloop()  # Start Tkinter event loop
