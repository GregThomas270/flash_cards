from tkinter import*
import pandas as pd
import random


def new_word():
    new_word_choice = (word_dict[random.randint(0, 101)]["French"])
    return new_word_choice


def did_not_know(text):
    new_word()


def did_know():
    new_word()


BACKGROUND_COLOR = "#B1DDC6"
list_words = pd.read_csv("data/french_words.csv")
df = pd.DataFrame(list_words)
word_dict = pd.DataFrame.to_dict(df, orient="records")
print(word_dict)

window = Tk()
window.title = "Flashy"
window.config(pady=20, padx=20, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="French", font=("ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text=new_word(), font=("ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

x_image = PhotoImage(file="images/wrong.png")
do_not_know_button = Button(image=x_image, command=did_not_know)
do_not_know_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
know_button = Button(image=check_image, command=did_know)
know_button.grid(row=1, column=1)





window.mainloop()


