import tkinter
import csv


class MyApp:
    def __init__(self, root):
        self.root = root
        # This button will be used to add todos
        self.add_button = tkinter.Button(self.root, text="+ Add New TODO", command=lambda: self.entry_box("Add Button"))
        self.add_button.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)

        # This frame will contain Checkboxes
        self.checkbutton_frame = tkinter.Frame(self.root, border=1, relief="sunken", bg="white")
        self.checkbutton_frame.grid(row=1, column=0, sticky="nsew", pady=10, padx=10)

        # This button will be used to delete todos
        self.delete_button = tkinter.Button(self.root, text="Delete TODO", command=lambda: self.entry_box("Del Button"))
        self.delete_button.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)

        # When the user opens this application initial() function will show todos from "Stored_Todo.csv" file
        self.stored_todo()

    # This function will read file
    def stored_todo(self):
        # :todo_dict: will contain todos from "Stored_Todo.csv" file as {"Workout": "True")
        todo_dict = {}
        with open("Stored_Todo.csv", "r") as to_read:
            csv_reader = csv.DictReader(to_read, fieldnames=["todo_text", "checkbox_value"])
            for dictionary in csv_reader:
                if dictionary != {"todo_text": "todo_text", "checkbox_value": "checkbox_value"}:
                    todo_dict.update({dictionary["todo_text"]: dictionary["checkbox_value"]})

        # Looping through every item in todo_dict
        for todo, checkbox in todo_dict.items():
            checkbutton_value = tkinter.BooleanVar()    # To get or set value we need a tkinter variable
            checkbutton_value.set(checkbox)     # Setting an initial value

            # Creating check buttons
            checkbutton = tkinter.Checkbutton(self.checkbutton_frame, text=todo, font="arial 15 bold",
                                              variable=checkbutton_value, anchor="w")
            checkbutton.pack(fill="both", padx=10, pady=10)
            # Giving a command to check buttons
            # Passing arguments in write() function using lambda
            # Using local variables stored_value and stored_text to store checkbutton_value and checkbutton text
            checkbutton.config(command=lambda stored_value=checkbutton_value, stored_text=checkbutton.cget("text"):
                               self.write(stored_value.get(), stored_text))

    # This function will create an entry box, it will be called from add_button or delete_button
    def entry_box(self, from_where):
        todo_text = tkinter.StringVar()     # To get or set value we need a tkinter variable
        todo_entry = tkinter.Entry(self.root, textvariable=todo_text, font="arial 15 bold")

        # :from_where: will contain "Add Button" or "Del Button"
        if from_where == "Add Button":
            todo_entry.grid(row=0, column=0, sticky="nsew", pady=10, padx=10)
            todo_entry.bind("<Return>", lambda event: self.checkbox(todo_text.get()))

        elif from_where == "Del Button":
            todo_entry.grid(row=2, column=0, sticky="nsew", pady=10, padx=10)
            todo_entry.bind("<Return>", lambda event: self.delete_todo(todo_text.get()))

    # This function will create check buttons it will be called from entry_box() function
    def checkbox(self, todo_text):
        checkbutton_value = tkinter.BooleanVar()    # To get or set value we need a tkinter variable
        checkbutton = tkinter.Checkbutton(self.checkbutton_frame, text=todo_text, font="arial 15 bold",
                                          variable=checkbutton_value, anchor="w")
        checkbutton.pack(fill="both", padx=10, pady=10)

        # Giving a command to check buttons
        # Passing arguments in write() function using lambda
        # :stored_value: is a local variable that will contain checkbutton_value
        # :stored_text: is also a local variable that will contain checkbutton text
        # The reason we are using local variables so that the value doesn't change
        checkbutton.config(command=lambda stored_value=checkbutton_value, stored_text=checkbutton.cget("text"):
                           self.write(stored_value.get(), stored_text))

        # Creating a lambda function and calling it
        lam = (lambda stored_value=checkbutton_value, stored_text=checkbutton.cget("text"):
               self.write(stored_value.get(), stored_text))
        lam()

    # This function will write something to "Stored_Todo.csv" file, it will be called from checkbox() function
    def write(self, value, text):
        # Opening "Stored_Todo.csv" file and appending todo_text and checkbox_value to it
        with open("Stored_Todo.csv", "a", newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=["todo_text", "checkbox_value"])
            # Writing header only once
            if file.tell() == 0:
                csv_writer.writeheader()
            csv_writer.writerow({"todo_text": text, "checkbox_value": value})

        # :todo_dict: will contain todos it will contain in this format, "todo_text" as keys and checkbox_value as value
        #   {"Morning Workout": "True"}
        # The reason we are adding todos in this format, is because dictionaries doesn't contain duplicate values
        # So if there's a "to do" inputted twice then it will not be added
        todo_dict = {}
        with open("Stored_Todo.csv", "r") as to_read:
            csv_reader = csv.DictReader(to_read, fieldnames=["todo_text", "checkbox_value"])
            for dictionary in csv_reader:
                # Not adding the header to todo_dict
                if dictionary != {"todo_text": "todo_text", "checkbox_value": "checkbox_value"}:
                    todo_dict.update({dictionary["todo_text"]: dictionary["checkbox_value"]})

        # Writing todo_dict to "Stored_Todo.csv" file again
        with open("Stored_Todo.csv", "w", newline="") as write_file:
            csv_writer = csv.DictWriter(write_file, fieldnames=["todo_text", "checkbox_value"])
            if write_file.tell() == 0:
                csv_writer.writeheader()
            for todo, checkbox in todo_dict.items():
                csv_writer.writerow({"todo_text": todo, "checkbox_value": checkbox})

        # Refreshing "to do" page
        MyApp(self.root)

    # This function will delete a "to do" it will be called from entry_box() function
    def delete_todo(self, todo_text):
        # Reading "Stored_Todo.csv" file in this format, {"Morning Workout": True}
        todo_dict = {}
        with open("Stored_Todo.csv", "r") as to_read:
            csv_reader = csv.DictReader(to_read, fieldnames=["todo_text", "checkbox_value"])
            for dictionary in csv_reader:
                if dictionary != {"todo_text": "todo_text", "checkbox_value": "checkbox_value"}:
                    todo_dict.update({dictionary["todo_text"]: dictionary["checkbox_value"]})

        # Looping through every item in todo_dict
        # If todo_text != "to do" that means add everything that is not equal to todo_text
        new_todo_dict = {}
        for todo, checkbox in todo_dict.items():
            if todo_text != todo:
                new_todo_dict.update({todo: checkbox})

        # Writing new_todo_dict to "Stored_Todo.csv" file again
        with open("Stored_Todo.csv", "w", newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=["todo_text", "checkbox_value"])
            if file.tell() == 0:
                csv_writer.writeheader()
            for t, c in new_todo_dict.items():
                csv_writer.writerow({"todo_text": t, "checkbox_value": c})

        # Refreshing "to do" page
        MyApp(self.root)


if __name__ == "__main__":
    main_window = tkinter.Tk()
    main_window.geometry("300x400")
    main_window.title("TODO")

    # Filling checkbutton_frame to our main_window
    main_window.grid_rowconfigure(index=1, weight=1)
    main_window.grid_columnconfigure(index=0, weight=1)

    my_app = MyApp(main_window)

    main_window.mainloop()
