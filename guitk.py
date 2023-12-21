import tkinter as tk
from tkinter import filedialog, simpledialog
import os


def get_custom_weight(saved_weight):
    if saved_weight:
        message = f"Naciśnij Enter, aby użyć zapisanej masy ciała {saved_weight}kg, lub wprowadź nową wartość masy ciała: "
    else:
        message = "Naciśnij Enter, aby użyć domyślnej masy ciała 70kg, lub wprowadź nową wartość masy ciała: "

    return simpledialog.askfloat("Custom Weight", message)


# Example usage within a Tkinter function
def your_tkinter_function():
    saved_weight = 'xd'
    custom_weight = get_custom_weight(saved_weight)

    if custom_weight is not None:
        print(f"Użyto masy ciała: {custom_weight}kg")
    else:
        print("No valid weight provided or operation cancelled")


def option1_selected():
    label.config(text="Tu bedzie miejsce do wgrywania plików")
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        print("Selected files:")
        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            print(file_path)
            print(file_name)
            # check if xml: dializy.process_xml_file(file_path, file_name)


def option2_selected():
    label.config(text="Tu bedzie miejsce do pobierania plików")
    your_tkinter_function()


root = tk.Tk()
root.title("Dializy")
root.geometry("600x400")

# Sidebar frame
sidebar = tk.Frame(root, width=200, bg='lightgrey')
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Labels for options in sidebar
option1 = tk.Label(sidebar, text="Wybierz pliki", bg='lightgrey', padx=10, pady=5, cursor='hand2')
option1.pack()
option1.bind("<Button-1>", lambda event: option1_selected())

option2 = tk.Label(sidebar, text="Pobierz pliki", bg='lightgrey', padx=10, pady=5, cursor='hand2')
option2.pack()
option2.bind("<Button-1>", lambda event: option2_selected())

# Main content area
main_content = tk.Frame(root, width=400, height=400, bg='white')
main_content.pack_propagate(False)
main_content.pack(expand=True, fill=tk.BOTH)

# Label to display selected option
label = tk.Label(main_content, text="Wybierz opcję z menu", padx=10, pady=10)
label.pack()

root.mainloop()
