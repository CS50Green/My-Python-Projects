# My TODO
## Description

Assalamualaikum World!

This is my own version of TODO application. This is my Python project.

---

## How to use this application
First we need **Python** to run this application obviously!!!!.

To add todos we need to click **+ Add New Todo** button and give a name and press enter. It will create a checkbox that we can check or uncheck.

To delete a todo we need to click **Delete Todo** button and give the name of the todo that we want to delete and press enter.

---

## Requirements
To create this application we will need these modules

* tkinter
* csv

We can install these modules using "pip install module name"

---

## Classes Explained
There is only one **class** used in this application and that is **MyApp**. This **class** will contain everything.

---

## Functions used in MyApp class
### __init():

This function will create two buttons, **add_button** and **delete_button**. It will also create a frame, **checkbutton_frame**. It will call **stored_todo()** function.

---

### stored_todo():
This function will open **Stored_Todo.csv** file and read every row in that file and append every row to **todo_dict**.
It will loop through **todo_dict** and create **Checkbuttons**.

This function will be called from **__init()** function.

---

### entry_box():
This function will take two arguments **self** and **from_where**. It will create an **Entry** widget. But before packing and binding it will check what string **from_where** variable contains.

It will be called from **add_button** or **delete_button**.

---

### checkbox():
This function will create **Checkbuttons**.   It will also create a **lambda** function.

When we check or uncheck **Checkbuttons** it will call **write()** function. The **write()** function will only be called when we check or uncheck **Checkbuttons**. But we don't want that, we want, **write()** function to always be called.

Here we used **lambda** function to call **write()** function. The reason we've used **lambda** function, so, that we can capture value using **local** variables.

This function will be called from **entry_box() function.

---

### write():
This function will take two arguments **value** and **text**. **value** will contain **Checkbutton** value and **text** will contain **Checkbutton** text. It will write **value** and **text** to **Stored_Todo.csv** file.

First it will append **value** and **text** to **Stored_Todo.csv** file. It will write using **csv.DictWriter.writerow({"todo_text": text, "checkbox_value": value})**

Second it will read every row in **Stored_Todo.csv** file and add rows to **todo_dict**. It will add rows like this: **todo_dict.update({todo_text: checkbox_value})**. The reason we've used dictionary to add rows, it's because dictionaries does not contain duplicate values. So, if there's any todo inputted twice then it will not be added in **todo_dict**.

Third it will write **todo_dict** items to **Stored_Todo.csv** file again.

At the end it will call **MyApp()** class to refresh the app.

This function will be called from **checkbox()** function

---

### delete_todo():
This function will take two arguments **self** and **todo_text**. **todo_text** will contain **Checkbutton** name.

First it will read every row in **Stored_Todo.csv** file and add rows to **todo_dict**. It will add rows like this: **todo_dict.update({todo_text: checkbox_value})**. Header will not be included in **todo_dict**.

Second it will loop through every item in **todo_dict**, and it will add everything to **new_todo_dict** if **todo_text** != any todo text in **new_todo_dict**. If **todo_text** == any todo text in **new_todo_dict** then it will not be included.

Third it will write every item in **new_todo_dict** to **Stored_Todo.csv** file again.

At the end it will call **MyApp()** class to refresh the app.

This function will be called by from **entry_box()**.

