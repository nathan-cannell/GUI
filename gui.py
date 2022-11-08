from  tkinter import Tk, Text
root = Tk()
UW_ACC_ACTIVE = 0
SET_SPEED = 69
MPG = 0



# message = tk.Label(root, text="MPG")
# message.pack()
# message = tk.Label(root, text=MPG)
# message.pack()


# root.resizable(False, False)
root.title('GUI')

text = Text(root, height=16)
text.pack()


text.insert('1.0',"UW_ACC_ACTIVE: ")
text.insert('1.15',UW_ACC_ACTIVE)

text.insert('2.0',"   SET_SPEED: ")
text.insert('2.11',SET_SPEED)

text.insert('3.0',"   MPG: ")
text.insert('3.6',MPG)

root.mainloop() 