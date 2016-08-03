import tkinter

window = tkinter.Tk()
window.geometry("1000x600")
              
window.title("Colour Matching!")


frameButtons = tkinter.Frame(window)


colours = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
count = 0
for i in colours:
    count = count + 1
    exec("button_" + i +" = tkinter.Button(frameButtons, text='" + i +"').grid(row = "+str(count)+",column = " + str(count) + ")")


frameButtons.pack()

window.mainloop()
