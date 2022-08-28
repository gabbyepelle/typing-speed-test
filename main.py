from tkinter import *
import time
import random

timer = None
# --------------------------------TEXT TO TYPE-------------------------------------#
# source: https://www.usingenglish.com/comprehension/

text_1 = "Some scientists have predicted that healthy adults and children may one day take drugs to improve their " \
         "intelligence and intellectual performance.  A research group has suggested that such drugs might become as " \
         "common as coffee or tea within the next couple of decades. To counter this, students taking exams might have " \
         "to take drugs tests like athletes.  There are already drugs that are known to improve mental performance, " \
         "like Ritalin, which is given to children with problems concentrating.  A drug given to people with trouble " \
         "sleeping also helps people remember numbers.These drugs raise serious legal and moral questions, but people " \
         "already take vitamins to help them remember things better, so it will not be a simple problem to solve.  It " \
         "will probably be very difficult to decide at what point a food supplement becomes an unfair drug in an " \
         "examination. "
text_2 = "The makers of a controversial computer game about bullying have decided to go ahead and launch it despite " \
         "calls for it to be banned. In the game, players take on the role of a new students at a school and have to " \
         "fight the bullies, by punching them or hitting them with a baseball bat.Critics have said that the game " \
         "encourages violence, but the makers deny this and say that, while there is violence in the game, it is just " \
         "an amusing look at school life, besides which, the violence in the game is directed against the bullies to " \
         "protect pupils who are being bullied. The makers also say that players will learn to stand up to bullies.A " \
         "British politician, a former minister, has called for it to be banned as it might affect the way young " \
         "people perceive violence.Anti-bullying charities have said that the game might make people respond violently " \
         "to bullies, which might make things more complicated and result in injuries. "


# --------------------Test Logic-----------------------#
# put text on canvas
def load_test():
    test_list = [text_1, text_2]
    test = random.choice(test_list)
    test_pssg.insert(END, test)
    test_pssg.config(state=DISABLED)
    text_box.config(state=DISABLED)


def start_test(count):
    text_box.config(state=NORMAL)
    if count > 0:
        global timer
        # call countdown again after 1000ms (1s)
        timer_label.config(text=f"{count}")
        timer = window.after(1000, start_test, count - 1)
    else:
        timer_label.config(text="0")
        grade_test()


def grade_test():
    text_box.config(state=DISABLED)
    # calculate the number of characters in the passage
    user_input = text_box.get("1.0", 'end-1c')
    no_spaces = user_input.replace(" ", "")
    chars = len(no_spaces)
    words = chars / 5
    # calculate errors
    test_text = test_pssg.get("1.0", 'end-1c')
    passage_words = test_text.split()
    typed_words = user_input.split()

    errors = 0
    test_text = test_pssg.get("1.0", 'end-1c')
    rubric = test_text.replace(" ", "")

    for i in range(len(no_spaces)):
        if no_spaces[i] != rubric[i]:
            errors += 1

    net_words = words - errors
    if net_words < 0:
        net_words = 0
    test_pssg.config(state=NORMAL)
    test_pssg.delete('1.0', END)
    results = f"Gross Typing Speed: {words}\n Errors: {errors}\n Words Per Minute {net_words}"
    test_pssg.insert(END, results)


def reset_test():
    window.after_cancel(timer)
    test_pssg.delete('1.0', END)
    text_box.delete('1.0', END)
    load_test()
    timer_label.config(text="60")


# --------------------------------UI SETUP-----------------------------#

window = Tk()
window.title("Typing Speed Test")
window.configure(bg="#FFFCC9")
title = Label(text="1 Minute Typing Speed Test")
title.config(font=("Courier", 40, "bold"), bg="#FFFCC9", pady=15, fg="blue")
title.pack()
timer_label = Label(text="60")
timer_label.config(font=("Courier", 60, "bold"), bg="#FFFCC9", pady=10, fg="red")
timer_label.pack()

start_button = Button(text="Start", fg="green", highlightbackground="#FFFCC9", command=lambda: start_test(60))
start_button.pack()
reset_button = Button(text="Reset", fg="red", highlightbackground="#FFFCC9", command=reset_test)
reset_button.pack()
test_pssg = Text(window, height=18)
test_pssg.pack(pady=20)
test_pssg.configure(font=("Courier", 40, "bold"), spacing2=20)

text_box = Text(window, height=5)
text_box.configure(font=("Courier", 40, "bold"))
text_box.pack()

load_test()

window.mainloop()
