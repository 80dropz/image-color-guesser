import tkinter
import customtkinter
import random
hexlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
num1 = random.choice(hexlist)
num2 = random.choice(hexlist)
num3 = random.choice(hexlist)
num4 = random.choice(hexlist)
num5 = random.choice(hexlist)
num6 = random.choice(hexlist)
hexcoderan = f"#{num1}{num2}{num3}{num4}{num5}{num6}"
main=customtkinter.CTk()
main.title("Backgrounder")
main.geometry("250x250")
main.configure(fg_color=hexcoderan)
main.mainloop()
#window genereated
#window genereated
print(hexcoderan)

def guessed():
    if "#" in gussedhex.get():
        if gussedhex.get() == hexcoderan:
            rightorwrong.configure(text="Correct", text_color="green")
        else:
            rightorwrong.configure(text="Wrong", text_color="red")
    else:
        rightorwrong.configure(text="No hex entered", text_color="red")

entry=customtkinter.CTk()
entry.title("Guesser")
entry.geometry("250x250")

header=customtkinter.CTkLabel(entry, text="Enter your guess")
header.place(relx=.5, rely=.1, anchor="center")

gussedhex = customtkinter.CTkEntry(entry, placeholder_text="hex code guess")
gussedhex.place(relx=.5, rely=.3, anchor="center")

guessbtn = customtkinter.CTkButton(entry, text="guess!", fg_color="green", command=guessed)
guessbtn.place(relx=.5, rely=.5, anchor="center")


rightorwrong = customtkinter.CTkLabel(entry, text=" ", font=("Arial", 20))
rightorwrong.place(relx=.5, rely=.7, anchor="center")
entry.mainloop()
