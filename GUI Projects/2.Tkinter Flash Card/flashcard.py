import tkinter
import tkinter.messagebox
import csv
import random
import tksheet


def main():
    # Creating a root window
    root = tkinter.Tk()                 # Creating a Tk() object
    root.geometry("350x500")            # Giving (width x height) to our app
    root.resizable(False, False)        # Stopping window from resizing
    root.title("Tkinter Flash Card")    # Giving a title to our app

    # Filling our Frame to the whole root window
    root.grid_rowconfigure(index=0, weight=1)
    root.grid_columnconfigure(index=0, weight=1)

    # When our app opens Start Page should appear
    start_page(root)  # Passing root as an argument

    # Our app will be in an infinite loop until we exit
    root.mainloop()


# This function is for Start Page
def start_page(root):
    # The main Start Page Frame
    start_page_frame = tkinter.Frame(root)
    start_page_frame.grid(row=0, column=0, sticky="nsew")

    # "Tkinter" and "Flash Card" title
    tkinter_label = tkinter.Label(start_page_frame, text="      Tkinter", font="helvetica 20 bold", fg="grey")
    tkinter_label.grid(row=0, column=0, sticky="nsew", pady=40)
    flash_card_label = tkinter.Label(start_page_frame, text="Flash Card", font="helvetica 20 bold", fg="red")
    flash_card_label.grid(row=0, column=1, sticky="nsew", pady=40)

    # Store Words Button
    store_words_button = tkinter.Button(start_page_frame, text="Store Words", font="arial 20 bold", fg="green",
                                        command=lambda: store_words_page(root))
    store_words_button.grid(row=1, column=0, sticky="nsew", columnspan=20, padx=64, pady=10)

    # Review Words Button
    review_words_button = tkinter.Button(start_page_frame, text="Review Words", font="arial 20 bold", fg="blue",
                                         command=lambda: review_words_page(root, "From start_page"))
    review_words_button.grid(row=2, column=0, sticky="nsew", columnspan=20, padx=64, pady=10)

    # See or Change button
    see_or_change_button = tkinter.Button(start_page_frame, text="See or Change", font="arial 20 bold", fg="orange",
                                          command=lambda: see_or_change_page(root))
    see_or_change_button.grid(row=3, column=0, sticky="nsew", columnspan=20, padx=64, pady=10)

    # Exit Button
    exit_button = tkinter.Button(start_page_frame, text="Exit", font="arial 20 bold", fg="red",
                                 command=lambda: exit_program(root))
    exit_button.grid(row=4, column=0, sticky="nsew", columnspan=20, padx=64, pady=10)


# To count how many words currently stored
count_stored_words = 0


# Store Words Page
def store_words_page(root):
    global count_stored_words

    # Clearing count_stored_words every time we enter store_words_page
    count_stored_words = 0

    # The main Store Words Frame
    store_words_frame = tkinter.Frame(root)
    store_words_frame.grid(row=0, column=0, sticky="nsew")

    # To go back to Start Page
    go_back = tkinter.Button(store_words_frame, text="Back", font="arial 10 bold", command=lambda: start_page(root))
    go_back.pack(anchor="nw", pady=5, padx=5)

    # FIRST FLASH CARD FRAME
    first_card_frame = tkinter.Frame(store_words_frame, border=3, relief="ridge", width=175, height=190)
    first_card_frame.pack()
    first_card_frame.pack_propagate(False)  # Stopping Frame from resizing
    # Putting a Label inside first_card_frame to indicate that this is the Front of the card
    front_label = tkinter.Label(first_card_frame, text="Front", font="helvetica 20 bold", fg="green")
    front_label.pack()
    # Letting user input a word using entry widget and getting users word
    word_value = tkinter.StringVar()  # To get users value
    entered_word = tkinter.Entry(first_card_frame, justify="center", font="helvetica 20 bold", textvariable=word_value)
    entered_word.pack(fill="x", pady=40)

    # If this button is pressed then write words to a file
    # I believe we have to use lambda function in order to access nested functions
    write_button = tkinter.Button(store_words_frame, text="Store", font="arial 10 bold", fg="green",
                                  command=lambda: writing_words())
    write_button.pack(pady=5)

    # SECOND FLASH CARD FRAME
    second_card_frame = tkinter.Frame(store_words_frame, border=3, relief="ridge", width=175, height=190)
    second_card_frame.pack()
    second_card_frame.pack_propagate(False)  # Stopping Frame from resizing
    # Putting a Label inside second_card_frame to indicate that this is the Back of the card
    back_label = tkinter.Label(second_card_frame, text="Back", font="helvetica 20 bold", fg="red")
    back_label.pack()
    # Letting user input the meaning of the word using entry widget and getting the users meaning
    meaning_value = tkinter.StringVar()  # To get users value
    entered_meaning = tkinter.Entry(second_card_frame, justify="center", font="helvetica 20 bold",
                                    textvariable=meaning_value)
    entered_meaning.pack(fill="x", pady=40)

    # Status Bar
    status_bar = tkinter.Label(store_words_frame, text="Currently Stored: 0", border=3, relief="raised")
    status_bar.pack(side="bottom", fill="x")

    # If "Enter" button is pressed from keyboard then also store words
    entered_word.bind("<Return>", lambda event: writing_words())  # Binding "Enter" button to Entry widget
    entered_meaning.bind("<Return>", lambda event: writing_words())  # Binding "Enter" button to Entry widget

    # If "Store" and "Enter" button is pressed then call this function, "Enter" button can also be pressed from the
    #   keyboard
    def writing_words():
        # Accessing global variables
        global count_stored_words

        # Getting word_value and meaning_value
        word = word_value.get()
        meaning = meaning_value.get()
        # Reading the "Stored Words.csv" file only to check if the random_word exists in the file or not
        list_of_word_meaning = []
        with open("Stored Words.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, fieldnames=["front", "back"])
            # csv.DictReader() will read every row as a dictionary,
            #   {"front": word, "back": meaning}
            # So we are looping through every row in "Stored Words.csv" file and appending word, meaning to a list
            #   as a dictionary {word: meaning}
            for row in csv_reader:
                list_of_word_meaning.append({row["front"]: row["back"]})

        # If something exists in entered_word Entry widget and entered_meaning Entry widget, then store words,
        #   otherwise give an error message
        if (word != "") and (meaning != ""):
            # :list_of_word_meaning: contains word and meaning from "Stored Words.csv" file
            # Making a dictionary of currently inputted {word: meaning} and checking if the current dictionary exists
            #   in the list_of_word_meaning list
            # If the current {word: meaning} dictionary doesn't exist in list_of_word_meaning list
            #   then write the dictionary to "Stored Words.csv" file
            # Otherwise give an error message
            word, meaning = word_value.get().lower(), meaning_value.get().lower()  # Getting and lowering word, meaning
            if {word: meaning} not in list_of_word_meaning[1:]:  # Not checking first dictionary which is the header
                with open("Stored Words.csv", "a", newline="", encoding="utf-8") as f:
                    csv_writer = csv.DictWriter(f, fieldnames=["front", "back"])
                    # Writing header only once
                    if f.tell() == 0:  # .tell() method would give the cursors position
                        csv_writer.writeheader()
                    csv_writer.writerow({"front": word, "back": meaning})

                # Increasing count_stored_words value
                count_stored_words += 1
                # Changing status_bar_text variable
                status_bar_text = f"Currently Stored: {count_stored_words}"
                # Updating the status_bar
                status_bar.config(text=status_bar_text)
                # Clearing entry widgets
                entered_word.delete(0, "end")     # From zeroth character to end
                entered_meaning.delete(0, "end")  # From zeroth character to end
            else:
                tkinter.messagebox.showerror("Exists", "Word and Meaning exists in the File")
                # Clearing entry widgets
                entered_word.delete(0, "end")  # From zeroth character to end
                entered_meaning.delete(0, "end")  # From zeroth character to end
        else:
            tkinter.messagebox.showerror("Empty", "There should be something in the front and back of the card")

    # We are returning something in order to test our store_words_page function using pytest
    return "Store Words Page Opened"


# To access and change these variables anywhere
random_word = ""     # To store randomly generated word
count_got_right = 0  # Is to count how many words the user got right
count_got_wrong = 0  # Is to count how many words the user got wrong

# This list is to contain all the words that user got right
list_of_right_words = []
# This list is to contain all the words that user got wrong
list_of_wrong_words = []


# Review Words Page
def review_words_page(root, from_which_page):
    # Accessing global variables
    global random_word
    global count_got_right
    global count_got_wrong
    global list_of_right_words
    global list_of_wrong_words

    # We are clearing every data in review_words_page every time we enter review_words_page from start_page
    if from_which_page == "From start_page":
        count_got_right = 0
        count_got_wrong = 0
        list_of_right_words = []
        list_of_wrong_words = []

    # The main Review Words Page Frame
    review_words_frame = tkinter.Frame(root)
    review_words_frame.grid(row=0, column=0, sticky="nsew")

    # To go back to Start Page
    go_back = tkinter.Button(review_words_frame, text="Back", font="arial 10 bold", command=lambda: start_page(root))
    go_back.pack(anchor="nw", pady=5, padx=5)

    # FRONT OF THE FLASH CARD
    front_frame = tkinter.Frame(review_words_frame, border=3, relief="ridge", width=260, height=250)
    front_frame.pack()
    front_frame.pack_propagate(False)
    # Scrollbar in front_frame
    front_frame_scrollbar = tkinter.Scrollbar(front_frame, orient="horizontal")
    front_frame_scrollbar.pack(side="bottom", fill="x")

    # This Frame is to contain flip_card and next_word_button buttons
    flip_and_next_frame = tkinter.Frame(review_words_frame)
    flip_and_next_frame.pack(fill="x", pady=20)
    # Button to see the words meaning
    flip_card = tkinter.Button(flip_and_next_frame, text="Flip Card", font="arial 12 bold", fg="red",
                               command=lambda: back_of_the_card())
    flip_card.pack(side="left", padx=10)
    # Button to go to the next word
    next_word_button = tkinter.Button(flip_and_next_frame, text="Next Word", font="arial 12 bold", fg="green",
                                      command=lambda: enter_and_next_word("Next Word"))
    next_word_button.pack(side="right", padx=10)

    # This Frame is to contain got_right and got_wrong buttons
    right_wrong_frame = tkinter.Frame(review_words_frame)
    right_wrong_frame.pack(side="bottom", pady=20)
    # This button text will show how many words the user got right
    # When the user presses got_right_button, it will display a Sheet that will contain how many times the user
    #   got the same word correct
    got_right_button = tkinter.Button(right_wrong_frame, text=f"You Got Right: {count_got_right}",
                                      font="helvetica 15 bold", fg="green",
                                      command=lambda: got_right_button_command(list_of_right_words))
    got_right_button.grid(row=0, column=0, sticky="nsew")
    # This button text will show how many words the user got wrong
    # When the user presses got_wrong_button, it will display a Sheet that will contain how many times the user
    #   got the same word wrong
    got_wrong_button = tkinter.Button(right_wrong_frame, text=f"You Got Wrong: {count_got_wrong}",
                                      font="helvetica 14 bold", fg="red",
                                      command=lambda: got_wrong_button_command(list_of_wrong_words))
    got_wrong_button.grid(row=1, column=0, sticky="nsew")

    # Opening "Stored Words.csv" file and reading all the "words" and storing it in a list
    words_list = []
    with open("Stored Words.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, fieldnames=["front", "back"])
        for row in csv_reader:
            words_list.append(row["front"])

    # If words_list is empty then give an error message and get the user to the store_words_page
    if len(words_list) <= 1:
        tkinter.messagebox.showerror("Empty", "No words stored")
        store_words_page(root)
    else:
        # Generating a random word
        random_word = random.choice(words_list[1:])

    # Displaying the random_word
    # The reason we've used Entry widget to display random_word, it's because, so that we can Scroll horizontally,
    #   if we have a big word
    random_word_text = tkinter.StringVar(value=random_word.title())
    displaying_random_word = tkinter.Entry(front_frame, justify="center", textvariable=random_word_text, border=0,
                                           state="readonly", font="helvetica 20 bold", fg="green")
    displaying_random_word.pack(pady=20)
    # Telling front_frame_scrollbar to control displaying_random_word Entry widgets x-axis
    front_frame_scrollbar.config(command=displaying_random_word.xview)
    # Telling displaying_random_word Entry widget that front_frame_scrollbar is going to control your x-axis, so do as
    #   front_frame_scrollbar says
    displaying_random_word.config(xscrollcommand=front_frame_scrollbar.set)

    # Letting user enter a meaning
    answer_value = tkinter.StringVar()  # To get users value
    what_meaning = tkinter.Entry(front_frame, justify="center", textvariable=answer_value, font="helvetica 20 bold")
    what_meaning.pack(fill="x", pady=30)
    # If "Enter" button is pressed from keyboard then call enter_and_next_word() function
    what_meaning.bind("<Return>", lambda event: enter_and_next_word("Enter"))

    # When the user presses enter_button then also call enter_and_next_word() function
    enter_button = tkinter.Button(front_frame, text="Enter", font="arial 10 bold",
                                  command=lambda: enter_and_next_word("Enter"))
    enter_button.pack(pady=10)

    # This function will only be called if enter or next_word button is pressed
    def enter_and_next_word(button_text):
        # Accessing global variables
        global random_word
        global count_got_right

        # Opening "Stored Words.csv" file and reading all the rows and storing it in a list as a dictionary
        #   {word: meaning}
        list_of_word_meaning = []
        with open("Stored Words.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, fieldnames=["front", "back"])
            for r in reader:
                list_of_word_meaning.append({r["front"]: r["back"]})

        if button_text == "Enter":
            # Getting users answer and lowering it and removing spaces from either side of the meaning value
            meaning = answer_value.get().lower().strip()
            # If the users answer is correct then generate another random word, otherwise give an error message that
            #   the user is wrong
            if {random_word: meaning} in list_of_word_meaning[1:]:  # First dictionary is the header
                # If the random_word is correct then append it to list_of_correct_words list
                list_of_right_words.append(random_word)
                # Generating another random Word
                random_word = random.choice(words_list[1:])
                # Displaying the new random word
                random_word_text.set(value=random_word.title())
                # Clearing the what_meaning Entry widget
                what_meaning.delete(0, "end")
                # Updating got_right Label
                count_got_right += 1
                got_right_button.config(text=f"You Got Right: {count_got_right}")
            else:
                tkinter.messagebox.showerror("Wrong", "Meaning is not correct")

        elif button_text == "Next Word":
            random_word = random.choice(words_list[1:])  # Not accessing the first item which is the header
            # Displaying the new random word
            random_word_text.set(value=random_word.title())
            # Clearing the enter_word
            what_meaning.delete(0, "end")

    # This function will only be called when user wants to see the meaning of the word
    # BACK OF THE FLASH CARD
    def back_of_the_card():
        # Accessing global variable
        global count_got_wrong

        # Asking the user if the user is sure that the user wants to see the meaning
        # If "Yes" then show the meaning, otherwise do nothing
        yes_no = tkinter.messagebox.askyesno("Meaning", "Are you sure you want to see the meaning? ")
        if yes_no is True:

            # Hiding front_frame and flip_and_next_frame and go_back button
            front_frame.pack_forget()
            flip_and_next_frame.pack_forget()
            go_back.pack_forget()

            # "Correct Meanings:" header
            meaning_heading = tkinter.Label(review_words_frame, text="Correct Meanings: ", font="helvetica 15 bold",
                                            fg="red")
            meaning_heading.pack(pady=20)

            # This is the main back_frame
            back_frame = tkinter.Frame(review_words_frame, border=3, relief="ridge", width=290, height=250)
            back_frame.pack()
            back_frame.pack_propagate(False)

            # Button to go to the Next Word
            next_button = tkinter.Button(review_words_frame, text="Next Word", font="arial 12 bold", fg="green",
                                         command=lambda: review_words_page(root, "From back_of_the_card"))
            next_button.pack(pady=10)

            # Opening "Stored Words.csv" file and reading all the rows and
            #   checking if random_word equals to the word in "Stored Words.csv" file
            #   if matches then storing that word and meaning in a list as a [word, meaning] list
            list_of_meanings = []
            with open("Stored Words.csv", "r", encoding="utf-8") as f:
                reader = csv.DictReader(f, fieldnames=["front", "back"])
                for dictionary in reader:
                    if random_word == dictionary["front"]:
                        list_of_meanings.append([random_word, dictionary["back"]])

            # Creating a Sheet inside back_frame
            meanings_sheet = tksheet.Sheet(back_frame, headers=["Word", "Meaning"], font="helvetica 15",
                                           header_font="helvetica 12 bold")
            meanings_sheet.pack()
            # Putting list_of_meanings inside meanings_sheet
            meanings_sheet.set_sheet_data(list_of_meanings)
            # Making our meanings_sheet editable
            meanings_sheet.enable_bindings("all")

            # If the random_word is not correct then append it to list_of_wrong_words list
            list_of_wrong_words.append(random_word)
            # Updating got_wrong label
            count_got_wrong += 1
            got_wrong_button.config(text=f"You Got Wrong: {count_got_wrong}")

    # This function is for got_right_button
    def got_right_button_command(correct_words_list):
        # This the main Frame
        got_right_frame = tkinter.Frame(root)
        got_right_frame.grid(row=0, column=0, sticky="nsew")

        # To go back to review_words_page
        to_go_back = tkinter.Button(got_right_frame, text="Back", font="arial 10 bold",
                                    command=lambda: review_words_page(root, "From got_right_button_command"))
        to_go_back.pack(anchor="nw", pady=5, padx=5)

        # Header inside got_right_frame
        header_label = tkinter.Label(got_right_frame, text="Got The Same Word Right", font="helvetica 15 bold",
                                     fg="green")
        header_label.pack(pady=20)

        # This Frame will contain correct_sheet
        correct_frame = tkinter.Frame(got_right_frame, border=3, relief="sunken", width=290, height=300)
        correct_frame.pack(pady=20)
        correct_frame.pack_propagate(False)

        # Counting how many times the user got the same word correct
        correct_dict = {}
        for correct_word in correct_words_list:
            count_correct_word = correct_words_list.count(correct_word)
            correct_dict[correct_word] = count_correct_word
        # Creating a list of [key, value] lists only to set_sheet_data
        correct_lists = []
        for key, value in correct_dict.items():
            correct_lists.append([key, value])

        # Creating a Sheet inside correct_frame
        correct_sheet = tksheet.Sheet(correct_frame, headers=(["Word", "Times"]), font="helvetica 15",
                                      header_font="helvetica 12 bold")
        correct_sheet.pack()
        # Putting correct_lists inside correct_sheet
        correct_sheet.set_sheet_data(correct_lists)
        # Making our correct_sheet editable
        correct_sheet.enable_bindings("all")

    # This function is for got_wrong_button
    def got_wrong_button_command(wrong_words_list):
        # This the main Frame
        got_wrong_frame = tkinter.Frame(root)
        got_wrong_frame.grid(row=0, column=0, sticky="nsew")

        # To go back to review_words_page
        go_back_button = tkinter.Button(got_wrong_frame, text="Back", font="arial 10 bold",
                                        command=lambda: review_words_page(root, "From got_wrong_button_command"))
        go_back_button.pack(anchor="nw", pady=5, padx=5)

        # Header inside got_wrong_frame
        header_label = tkinter.Label(got_wrong_frame, text="Got The Same Word Wrong", font="helvetica 15 bold",
                                     fg="red")
        header_label.pack(pady=20)

        # This Frame will contain wrong_sheet
        wrong_frame = tkinter.Frame(got_wrong_frame, border=3, relief="sunken", width=290, height=300)
        wrong_frame.pack(pady=20)
        wrong_frame.pack_propagate(False)

        # Counting how many times the user got the same word wrong
        wrong_dict = {}
        for wrong_word in wrong_words_list:
            count_wrong_word = wrong_words_list.count(wrong_word)
            wrong_dict[wrong_word] = count_wrong_word
        # Creating a list of [key, value] lists only to set_sheet_data
        wrong_lists = []
        for key, value in wrong_dict.items():
            wrong_lists.append([key, value])

        # Creating a Sheet inside wrong_frame
        wrong_sheet = tksheet.Sheet(wrong_frame, headers=(["Word", "Times"]), font="helvetica 15",
                                    header_font="helvetica 12 bold")
        wrong_sheet.pack()
        # Putting wrong_lists inside wrong_sheet
        wrong_sheet.set_sheet_data(wrong_lists)
        # Making our wrong_sheet editable
        wrong_sheet.enable_bindings("all")

    # We are returning something in order to test our review_words_page function using pytest
    return "Review Words Page Opened"


# See or Change Page
def see_or_change_page(root):
    # This the main Frame of See or Change Page
    see_words_list_frame = tkinter.Frame(root)
    see_words_list_frame.grid(row=0, column=0, sticky="nsew")

    # To go back to Start Page
    go_back = tkinter.Button(see_words_list_frame, text="Back", font="arial 10 bold", command=lambda: start_page(root))
    go_back.pack(anchor="nw", pady=5, padx=5)

    # Opening "Stored Words.csv" file and reading all the rows and storing it in a list as a dictionary
    #   {word: meaning}
    list_of_word_meaning = []
    with open("Stored Words.csv", "r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file, fieldnames=["front", "back"])
        for row in csv_reader:
            list_of_word_meaning.append([row["front"], row["back"]])

    # This frame will contain word_meaning_sheet
    table_frame = tkinter.Frame(see_words_list_frame, border=3, relief="sunken", width=300, height=300)
    table_frame.pack(pady=30)
    table_frame.pack_propagate(False)

    # Creating a Sheet
    word_meaning_sheet = tksheet.Sheet(table_frame, headers=(["Front", "Back"]), font="helvetica 15",
                                       header_font="helvetica 12 bold")
    word_meaning_sheet.pack()
    # Putting list_of_word_meaning in word_meaning_sheet
    word_meaning_sheet.set_sheet_data(list_of_word_meaning[1:])  # First dictionary is the header
    # Making our word_meaning_sheet editable
    word_meaning_sheet.enable_bindings("all")

    # This button is to save changes made to word_meaning_sheet
    save_button = tkinter.Button(see_words_list_frame, text="Save Changes", font="arial 15",
                                 command=lambda: save_changes())
    save_button.pack()

    # This function will only be called if save_button is pressed
    def save_changes():
        # There should be something in both of the columns or nothing to save changes
        # If one column is empty and the other column is not empty then don't save changes
        empty_column = ""
        # Looping through each row in word_meaning_sheet
        for lst in word_meaning_sheet.get_sheet_data():
            # If column 1 is empty and column 2 is not empty then put something in empty_column variable
            if (lst[0] == "") and (lst[1] != ""):
                empty_column = "One of the column is empty"
            # If column 2 is empty and column 1 is not empty then put something in empty_column variable
            elif (lst[1] == "") and (lst[0] != ""):
                empty_column = "One of the column is empty"

        # If there's something in empty_column then that means "One of the column is empty"
        #   so, give an error message
        if empty_column:  # If something in this variable then python will return True, otherwise False
            tkinter.messagebox.showerror("Empty", "There should be something in both of the columns or nothing")
        else:
            # Opening "Stored Words.csv" file in write mode
            with open("Stored Words.csv", "w", newline="", encoding="utf-8") as f:
                csv_writer = csv.DictWriter(f, fieldnames=["front", "back"])
                # Writing header only once
                if f.tell() == 0:  # .tell() will give cursor position
                    csv_writer.writeheader()
                # Getting each row from word_meaning_sheet
                for r in word_meaning_sheet.get_sheet_data():
                    # There should be something in both of the columns to write
                    # If column 1 and column 2 is not empty then write, otherwise don't write
                    if (r[0] != "") and (r[1] != ""):
                        # Writing each row as a dictionary
                        csv_writer.writerow({"front": r[0].lower(), "back": r[1].lower()})

            # Refreshing see_or_change page
            see_or_change_page(root)

    # We are returning something in order to test our see_or_change_page function using pytest
    return "See or Change Page Opened"


# To quit the program
def exit_program(root):
    # Destroying the main window
    root.destroy()


# If main function is called than our app will run
# We are telling Python to only call main function if we run this program from this file
# If we import this file in another file the main function will not be called, unless we call it ourselves
if __name__ == "__main__":
    main()
