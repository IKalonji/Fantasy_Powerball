import number_check
import number_generator
from tkinter import *
from os import system

def start_game():
    '''Function to allow user to strart the game'''
    button_enter.destroy()
    window.geometry('480x300')
    welcome_label.configure(text="Insert Your Winning Numbers below")
    
    num_1.place(relx=0.0,rely=0.3,width=50,height=50)    
    num_2.place(relx=0.15,rely=0.3,width=50,height=50)
    num_3.place(relx=0.30,rely=0.3,width=50,height=50)
    num_4.place(relx=0.45,rely=0.3,width=50,height=50)
    num_5.place(relx=0.60,rely=0.3,width=50,height=50)
    powerball.place(relx=0.88,rely=0.3,width=50,height=50)
    powerball_label.place(relx=0.7, rely=0.35)
    button_submit.place(relx=0.40,rely=0.60)
    instructions.place(rely=0.7, relx=0.19)

def get_sumitted_numbers():
    '''Function to get the numbers submitted
    and convert to a list that will be evaluated
    '''
    global user_numbers, user_powerball

    list_of_text_entry_block = [num_1,num_2,num_3,num_4,num_5,powerball]
    user_numbers = [item.get() for item in list_of_text_entry_block]
    user_numbers.sort()
    user_powerball = [powerball.get()]

    for item in list_of_text_entry_block:
        item.destroy()

    button_submit.destroy()
    powerball_label.destroy()
    instructions.destroy()
    welcome_label.configure(text="Checking your numbers...", anchor=CENTER, fg='green')
    window.after(3000, set_click_to_check_button)
    
def check_numbers():
    """Function to generate CPU numbers
    and check against user numbers
    and display results"""
    global user_numbers, user_powerball
    global correct_number, correct_powerball

    click_to_check.destroy()


    cpu_numbers, cpu_powerball = number_generator.number_generator()
    cpu_numbers.sort()
    correct_number, correct_powerball = number_check.number_check(cpu_numbers,cpu_powerball,user_numbers,user_powerball)
    window.geometry('440x300')

    if correct_number > 0 or correct_number == True:
        welcome_label.configure(text="CONGRATULATIONS!!!")
        numbers = str(cpu_numbers[0]) + " " + str(cpu_numbers[1]) + " " + str(cpu_numbers[2]) + " " + str(cpu_numbers[3]) +" " + str(cpu_numbers[4])
        powerball_ = str(cpu_powerball[0])
        sys_numbers = Label(window, text=f"These are system Powerball numbers\n{numbers} Powerball: {powerball_}", anchor=CENTER, font=("Comic Sans",12)).grid(column=0,row=3)
        if correct_powerball == True:
            statement = f"You got {correct_number} correct number as well as the Powerball"
            new_text = Label(window, text=statement,font=("Comic Sans",12)).grid(column=0,row=4)
        else:
            statement = f"You got {correct_number} correct numbers but not the Powerball"
            new_text = Label(window, text=statement,font=("Comic Sans",12)).grid(column=0,row=4)
    else:
        window.geometry('500x300')
        welcome_label.configure(text="UNLUCKY!!! NO CORRECT NUMBERS")
        numbers = str(cpu_numbers[0]) + " " + str(cpu_numbers[1]) + " " + str(cpu_numbers[2]) + " " + str(cpu_numbers[3]) +" " + str(cpu_numbers[4])
        powerball_ = str(cpu_powerball[0])
        sys_numbers = Label(window, text=f"These are the system Powerball numbers:\n{numbers} Powerball: {powerball_}", anchor=CENTER, font=("Comic Sans",12)).grid(column=0,row=3)
        statement = f"\nYour numbers:\n{user_numbers[0]} {user_numbers[1]} {user_numbers[2]} {user_numbers[3]} {user_numbers[4]}\nPowerBall: {user_powerball[0]}"
        new_text = Label(window, text=statement,font=("Comic Sans",12), anchor=CENTER).grid(column=0,row=4)


def set_click_to_check_button():
    '''Function to set the click to check result button'''

    click_to_check.place(relx=0.3, rely=0.4)



#set globals to hold the return values of the function get_submitted
user_numbers, user_powerball = None,None
#setup the display window
window = Tk()
window.geometry('420x300')
window.title("Fantasy Powerball")
#Setup the main screen label
welcome_label = Label(window, text='Welcome to Fantasy PowerBall',font=('Comic Sans', 20))
welcome_label.grid(column=0, row=2)
#Setup the main screen button
button_enter = Button(window, text="Click to begin", bg="yellow", fg="blue", command=start_game)
button_enter.grid(row=3)
button_submit = Button(window, text="SUBMIT", bg="blue", fg='black', command=get_sumitted_numbers)
#Setup the text entries that will be used by start game function
num_1 = Entry(window)
num_2 = Entry(window)
num_3 = Entry(window)
num_4 = Entry(window)
num_5 = Entry(window)
powerball = Entry(window)

powerball_label = Label(window,text="POWERBALL", fg='blue', relief=RAISED)
instructions = Label(window, text="Instruction:\nChoose five (5)\nunique numbers between 1-50\nand the PowerBall should be between 1-20", anchor=CENTER, fg='blue')
click_to_check = Button(window, text="Click to See Results", command=check_numbers)

window.mainloop()
system("clear")