import tkinter as tk
import os, shutil
from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label, StringVar
from tkinter.messagebox import askquestion, showerror, showwarning
from tkinter.font import BOLD
from PIL import Image, ImageTk
from plyer import notification


def winNotify(title, desc):
    notification.notify(
        title = title,
        message = desc,
        app_name= "Junk Cleaner",
        app_icon= "Assets\\junk.ico"
        )

def delete():
    ifDelete = askquestion("Delete Selected Items?", "Do You want to Delete all the selected items?")
    if ifDelete == "yes":
        for path, var in zip(dirList, varList):
            if var.get() == 1:
                delFileFolder(path)
        winNotify("Deleted Items Successfully!", "Your selected items were deleted successfully!")
    

def delete_all():
    ifDelete = askquestion("Delete Items?", "Do You want to Delete all the items?")
    if ifDelete == "yes":
        for path in dirList:
            delFileFolder(path)
        winNotify("Success", "Successfully deleted all the junk.")

def selectAll():
    for var in varList:
        var.set(1)

def deselectAll():
    for var in varList:
        var.set(0)


def delFileFolder(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
        except Exception as e:
            showerror(f"Error: {e}", f"An error occured while deleting the file ({path}).\nDescription: {e}.")

    elif os.path.isdir((path)):
        ItemList = os.listdir(path)
        for item in ItemList:
            if os.path.isfile(item):
                try:
                    os.remove(item)
                except Exception as e:
                    showerror(f"Error: {e}", f"An error occured while deleting the file ({path}).\nDescription: {e}.")
            elif os.path.isdir(item):
                try:
                    shutil.rmtree(item)
                except Exception as e:
                    showerror(f"Error: {e}", "An error occured while deleting the folder ({path}).\nDescription: {e}.")
    else:
        showwarning("File/Folder doesn't exists!", f"The file or folder path ({path}) you entered does not exists.")
        

def changeUser(event):
    usr_temp_check.config(text=f"C:\\Users\\{USERNAME.get()}\\AppData\\Local\\Temp")
    global dirList
    dirList[2] = f"C:\\Users\\{USERNAME.get()}\\AppData\\Local\\Temp"




window = tk.Tk()

# Window Settings
window.title("Junk Cleaner by Logic2apply")
window.wm_iconbitmap("Assets\\junk.ico")

window_width = 500
window_height = 700
window.geometry(f"{window_width}x{window_height}")
window.resizable(False, True)


# Global Variables
fontPrimary = "Helvetica"

# Heading Image and Label
# Heading Frame
headFrame = Frame(window)
headFrame.grid(column=1, row=1, columnspan=3)

# Heading Image
headImgSize = 32
head_image = Image.open("Assets\\junk.ico").resize((headImgSize,headImgSize), Image.ANTIALIAS)
head_photo = ImageTk.PhotoImage(head_image)
headingImage = Label(headFrame, image=head_photo, height=headImgSize, width=headImgSize)
headingImage.grid(column=1, row=1, pady=7, padx=7)

heading = Label(headFrame, text="Junk Cleaner", font=(fontPrimary, 30, BOLD))
heading.grid(column=2, row=1, columnspan=2)
subHead = Label(headFrame, text="by Logic2apply", font=(fontPrimary, 10))
subHead.grid(column=3, row=2, sticky="e")

# Main Body
folders = Label(window, text="Which File(s)/Folder(s) do you want to delete?", font=(fontPrimary, 15, BOLD))
folders.grid(column=1, row=2, columnspan=3, ipady=15, ipadx=5, sticky="w")

# folderlist
folderlist = Frame(window, pady=7, padx=7)
folderlist.grid(column=1, columnspan=3, row=3)


USERNAME = StringVar()
WIN_TEMP_VAR = IntVar()
PREFETCH_VAR = IntVar()
USR_TEMP_VAR = IntVar()
TEMPOR_VAR = IntVar()
WIN_TMP_VAR = IntVar()
WIN_FF_VAR = IntVar()
HIST_VAR = IntVar()
COOKIES_VAR = IntVar()
RECENT_VAR = IntVar()
SPOOL_VAR = IntVar()
SWP_VAR = IntVar()

varList = [
    WIN_TEMP_VAR,
    PREFETCH_VAR,
    USR_TEMP_VAR,
    TEMPOR_VAR,
    WIN_TMP_VAR,
    WIN_FF_VAR,
    HIST_VAR,
    COOKIES_VAR,
    RECENT_VAR,
    SPOOL_VAR,
    SWP_VAR
]

win_temp = "C:\\windows\\temp"
prefetch = "C:\\windows\\prefetch"
usr_temp = f"C:\\Users\\{USERNAME.get()}\\AppData\\Local\\Temp"
tempor = "C:\\windows\\tempor~1"
win_tmp = "C:\\windows\\tmp"
win_ff = "C:\\windows\\ff*.tmp"
hist = "C:\\windows\\history"
cookies = "C:\\windows\\cookies"
recent = "C:\\windows\\recent"
spool = "C:\\windows\\spool\\printers"
swp = "C:\\WIN386.SWP"

dirList = [
    win_temp,
    prefetch,
    usr_temp,
    tempor,
    win_tmp,
    win_ff,
    hist,
    cookies,
    recent,
    spool,
    swp
]

username_label = Label(folderlist, text="Username", font=("Calibri",12,BOLD)).grid(column=1, row=1)
username_entry = Entry(folderlist, textvariable=USERNAME)
username_entry.grid(column=2, row=1)



win_temp_check = Checkbutton(folderlist, text=win_temp, variable=WIN_TEMP_VAR)
win_temp_check.grid(column=1, row=2, sticky="w", padx=5)

prefetch_check = Checkbutton(folderlist, text=prefetch, variable=PREFETCH_VAR)
prefetch_check.grid(column=1, row=3, sticky="w", padx=5)

usr_temp_check = Checkbutton(folderlist, text=usr_temp, variable=USR_TEMP_VAR)
usr_temp_check.grid(column=1, row=4, sticky="w", padx=5)

tempor_check = Checkbutton(folderlist, text=tempor, variable=TEMPOR_VAR)
usr_temp_check.grid(column=1, row=5, sticky="w", padx=5)

win_tmp_check = Checkbutton(folderlist, text=win_tmp, variable=WIN_TMP_VAR)
win_tmp_check.grid(column=1, row=6, sticky="w", padx=5)

win_ff_check = Checkbutton(folderlist, text=win_ff, variable=WIN_FF_VAR)
win_ff_check.grid(column=1, row=7, sticky="w", padx=5)

hist_check = Checkbutton(folderlist, text=hist, variable=HIST_VAR)
hist_check.grid(column=1, row=8, sticky="w", padx=5)

cookies_check = Checkbutton(folderlist, text=cookies, variable=COOKIES_VAR)
cookies_check.grid(column=1, row=9, sticky="w", padx=5)

recent_check = Checkbutton(folderlist, text=recent, variable=RECENT_VAR)
recent_check.grid(column=1, row=10, sticky="w", padx=5)

spool_check = Checkbutton(folderlist, text=spool, variable=SPOOL_VAR)
spool_check.grid(column=1, row=11, sticky="w", padx=5)

swp_check = Checkbutton(folderlist, text=swp, variable=SWP_VAR)
swp_check.grid(column=1, row=12, sticky="w", padx=5)

# Select Deselect
select_all = Button(folderlist, text="Select All", command=selectAll, width=15)
select_all.grid(column=3, row=5, sticky="w", padx=5)

deselect_all = Button(folderlist, text="Deselect All", command=deselectAll, width=15)
deselect_all.grid(column=3, row=6, sticky="w", padx=5)
# Buttons

delete_all_btn = Button(window, text="Delete All", command=delete_all, padx=8, pady=3, width=14).grid(column=1, row=4)
delete_btn = Button(window, text="Delete", command=delete, padx=8, pady=3, width=14).grid(column=2, row=4)
exit_btn = Button(window, text="Exit", command=window.destroy, padx=8, pady=3, width=14).grid(column=3,row=4)


username_entry.bind("<KeyRelease>", changeUser)


window.mainloop()