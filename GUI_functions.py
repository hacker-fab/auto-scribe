#By Adwoa Asare
#Start Date: 10/12/2024
#Last Updated: 10/14/2024
### 
import tkinter as tk
def validate_numeric_input(P):
    if P == "" or P.replace('.', '', 1).isdigit():
        return True
    return False

# Function to reset parameters to default values
def reset_parameters(entries, unit_selectors, default_values):
    for param, default_value in default_values.items():
        entries[param].delete(0, tk.END)
        entries[param].insert(0, str(default_value))
        if param in unit_selectors:
            if param != "Wafer Diameter":
                unit_selectors[param].set("cm")
            else:
                unit_selectors[param].set("in")