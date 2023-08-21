# Tkinter Flash Card
#### Video Demo:  <https://youtu.be/Pe6exm934HA>
#### Description:
Assalamualaikum World!

My name is Tanjilul Hasan. For my final project of CS50P I've created a simple Flash Card application. To create this application I've used tkinter which is a GUI library built into Python. In this application we can:

* Store Words
* Review Words
* See or Change

# Requirements
To make this app we will need a these modules:

* tkinter
* tkinter.messagebox
* csv
* random
* tksheet

You can install these modules using "pip install module name"

---

# Functions
There are a lot of functions in this app so let me walk you through each of them.

## main():
This function will create our "root" window. Our app will only run if this function is called. The main() function will not be called if we import this file in another file.

---

## start_page():
This function will create a page like this

![](readme_images/0.Start_Page.PNG)

---

## store_words_page():
When we click "Store Words" button this function will be called. It will create a page like this

![](readme_images/1.Store_Words.PNG)

#### writing_words():
When we click "Store" button or press "Enter" button from keyboard this function will be called. It will write inputted words and meaning to "Stored Words.csv" file. It will write every language from left to right.

---

## review_words_page():
When we click "Review Words" button this function will be called. It will create a page like this

![](readme_images/2.Review_Words.PNG)

It will generate random words.

#### enter_and_next_word():
When we click "Enter" or press "Enter" from keyboard or click "Next Word" button this function will be called.

**Enter**: If we click "Enter" button it will check if the meaning is correct or not. If the meaning is correct then it will append the word in "list_of_correct_words" and increase the value of "count_got_right" variable and generate another random word. But if the meaning is not correct then it will give an error message "Meaning is not correct".

**Next Word**: If we click "Next Word" button it will just generate a new random word.

#### back_of_the_card():
When we click "Flip Card" button this function will be called. It will create a page like this.

![](readme_images/3.Flip_Card.PNG)

It will give a sheet of all the correct meanings. It will store the word in "list_of_wrong_words" and increase the value of "count_got_wrong" variable.

#### got_right_button_command():
When we click "You Got Right" button this function will be called. It will create a page like this

![](readme_images/4.You_Got_Right.PNG)

It will show us how many times we got the same word correct.

#### got_wrong_button_command():
When we click "You Got Wrong" button this function will be called. It will create a page like this

![](readme_images/5.You_Got_Wrong.PNG)

It will show us how many times we got the same word wrong.

---

## see_or_change_page():
When we click "See or Change" button this function will be called. It will create a page like this

![](readme_images/6.See_or_Change.PNG)

It will give a sheet of our stored words and meaning. We can change words and meaning if we want.

#### save_changes():
When we click "Save Change" button this function will be called. It will rewrite our changes to "Stored Words.csv" file.

To delete a word we just have to erase both of the columns and click "Save Changes" button, the word will be deleted.

---

## exit_program():
When we click "Exit" button this function will be called. It will close our application.

---


**I never wrote a "README.md" file before, so I hope it's not that bad!!!!**
