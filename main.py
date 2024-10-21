# By Adwoa Asare
# Start Date: 10/12/2024
# Last Updated: 10/14/2024
### This is the main file for operating the automated scriber from a GUI
import GUI_runner

def main():
    # Start the GUI and get the root and get_parameter_values function
    root, get_parameter_values = GUI_runner.start_gui()

    # Access the up-to-date values of the parameters
    parameter_values = get_parameter_values()
    print(parameter_values)

if __name__ == "__main__":
    main()