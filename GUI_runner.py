import tkinter as tk
from tkinter import ttk
import GUI_functions as gf
from GUI_functions import validate_numeric_input, reset_parameters

# For clarity in Windows
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    print('warning: not setting dpi awareness')

###-----VARIABLES-----###
Title = 'scriber fab'
window_width = 800
window_height = 400

def create_frames(root):
    frame_run = ttk.Frame(root, relief='solid', borderwidth=1)
    frame_specs = ttk.LabelFrame(root, text="Specs", relief='solid', borderwidth=1)
    frame_estimates = ttk.Frame(root, relief='solid', borderwidth=1)
    frame_help = ttk.Frame(root, relief='solid', borderwidth=1)

    # Place frames using grid
    root.grid_rowconfigure(0, weight=2)
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    frame_run.grid(row=0, column=1, rowspan=2, sticky='nsew')
    frame_specs.grid(row=0, column=0, sticky='nsew')
    frame_estimates.grid(row=1, column=0, sticky='nsew')
    frame_help.grid(row=1, column=1, sticky='nsew')

    return frame_run, frame_specs, frame_estimates, frame_help

def set_frame_titles(frame_run, frame_estimates, frame_help):
    frame_run_label = ttk.Label(frame_run, text="Run")
    frame_run_label.pack(padx=10, pady=10)

    frame_estimates_label = ttk.Label(frame_estimates, text="Estimates")
    frame_estimates_label.pack(padx=10, pady=10)

    frame_help_label = ttk.Label(frame_help, text="Help")
    frame_help_label.pack(padx=10, pady=10)

def add_parameters(root, frame_specs):
    # Default values for parameters
    default_values = {
        "Wafer Diameter": 4,
        "Chip Length": 1,
        "Chip Width": 2,
        "Scribe Speed": 0.5
    }

    # Dictionary to store entry widgets and unit selectors
    entries = {}
    unit_selectors = {}

    # Add parameter labels, entry boxes, and unit selectors to the "Specs" frame
    parameters = [
        ("Wafer Diameter", 4),
        ("Chip Length", 1),
        ("Chip Width", 2),
        ("Scribe Speed", 0.5)
    ]

    for i, (param, default_value) in enumerate(parameters):
        label = ttk.Label(frame_specs, text=param)
        label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
        
        entry = ttk.Entry(frame_specs, validate='key', validatecommand=(root.register(validate_numeric_input), '%P'))
        entry.insert(0, str(default_value))
        entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
        entries[param] = entry
        
        if param != "Scribe Speed":
            unit_selector = ttk.Combobox(frame_specs, values=["cm", "in"])
            if param != "Wafer Diameter":
                unit_selector.set("cm") #default 1 x 1 cm chips
            else:
                unit_selector.set("in")#wafer diameter default to 4 inches
            unit_selector.grid(row=i, column=2, padx=10, pady=5, sticky='w')
            unit_selectors[param] = unit_selector

    # Add RESET button
    reset_button = ttk.Button(frame_specs, text="RESET", command=lambda: reset_parameters(entries, unit_selectors, default_values))
    reset_button.grid(row=len(parameters), column=0, columnspan=3, padx=10, pady=10)

    return entries

def start_gui():
    ###-----GUI CODE-----###
    root = tk.Tk() #create the main window
    root.title(Title) #set the title of the window
    #find screen dimensions & center
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    root.attributes('-alpha',1)#set transparency

    frame_run, frame_specs, frame_estimates, frame_help = create_frames(root)
    set_frame_titles(frame_run, frame_estimates, frame_help)
    entries = add_parameters(root, frame_specs)

    # Function to get the current values of the parameters
    def get_parameter_values():
        return {param: entries[param].get() for param in entries}

    # Expose the get_parameter_values function to be accessible from main.py
    root.get_parameter_values = get_parameter_values

    # Start the main loop
    root.mainloop()

    return root, get_parameter_values