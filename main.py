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

    powerball_label = Label(window,text="POWERBALL", fg='blue')
    powerball_label.place(relx=0.7, rely=0.35)
    button_submit.place(relx=0.40,rely=0.60)

def get_sumitted_numbers():
    '''Function to get the numbers submitted
    and convert to a list that will be evaluated
    '''
    global user_numbers, user_powerball
    
    list_of_text_entry_block = [num_1,num_2,num_3,num_4,num_5,powerball]
    user_numbers = [item.get() for item in list_of_text_entry_block]
    user_powerball = [powerball.get()]

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

window.mainloop()
system("clear")
