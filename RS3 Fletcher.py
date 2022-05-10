# pip install tkinter
# pip install pyautogui


from time import sleep
from random import randint
import pyautogui
import tkinter as tk
from tkinter import RAISED, Canvas, Frame, PhotoImage, filedialog, Text
import os
#
#

mousedelay=randint(1,2)
clickdelay=randint(1,3)

path = "goblin.jpg"

root = tk.Tk()
root.title('RS3 Fletcher')
root.configure(bg='gray')

bankerlocation = 0
grabLogs = 0
fletchLogs = 0
loopAmt = 0

def selectBanker():
    global bankerlocation
    sleep(2.5)
    bankerlocation=(pyautogui.position())
    print("Selected Banker", bankerlocation)

def grabLogs():
    global grabLogs
    sleep(2.5)
    grabLogs=(pyautogui.position())
    print("Grabed Logs", grabLogs)

def fletchLogs():
    global fletchLogs
    sleep(2.5)
    fletchLogs=(pyautogui.position())
    print("Selected Log", fletchLogs)
    print()


def startScript():
    for i in range(5):

    #Moves mouse and clicks the banker
     pyautogui.moveTo((bankerlocation), duration=(mousedelay))
     sleep(0.5)
     pyautogui.leftClick()


    #deposits the fletched items into the bank

     sleep(2)
     pyautogui.typewrite("3")



     #Moves mouse and clicks logs
     sleep(2)
     pyautogui.moveTo((grabLogs), duration=(mousedelay))
     sleep(0.5)
     pyautogui.leftClick()
     sleep(2)
     pyautogui.keyDown('esc')
     sleep(0.5)
     pyautogui.keyUp('esc')

     #moves mouse to start to fletch the logs
     sleep(0.5)
     pyautogui.moveRel((fletchLogs), duration=(mousedelay))
     sleep(0.5)
     pyautogui.leftClick()
     sleep(1.5)
     pyautogui.keyDown('space')
     sleep(0.5)
     pyautogui.keyUp('space')

     sleep(50)
     print("done")


Canvas = tk.Canvas(root, height=200, width=250, bg="gray")
Canvas.pack()

frame = tk.Frame(root, bg="gray")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)


SelectLocation = tk.Button(frame, text="Select Banker", padx=10, pady=5, fg="white", bg="#263D42", command=selectBanker)
SelectLocation.pack()

SelectLogs = tk.Button(frame, text="Withdraw Logs", padx=10, pady=5, fg="white", bg="#263D42", command=grabLogs)
SelectLogs.pack()

SelectInv = tk.Button(frame, text="Select Log", padx=10, pady=5, fg="white", bg="#263D42", command=fletchLogs)
SelectInv.pack()

startScript = tk.Button(frame, text="Start Script", padx=10, pady=5, fg="white", bg="#263D42", command=startScript)
startScript.pack()


root.mainloop()

