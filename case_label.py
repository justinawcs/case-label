import datetime
import string
import tkinter

import weeks_list
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def week_letter(iso_date_string=None):
    d = datetime.datetime.now().strftime("%V")
    if iso_date_string is not None:
        d = datetime.date.fromisoformat(iso_date_string).strftime("%V")
    alpha = list(string.ascii_uppercase)
    index = int(d) % 26
    result = alpha[index-1]
    if int(d) == 53:
        result = "ZA"
    return "Week #{}: {}".format(d, result)


def main():
    #print(week_letter())
    root = Tk()
    root.title("Case Label")
    root.resizable(0,0)
    #root.attributes('-toolwindow', True)
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text=week_letter(),font=("Arial", 18, "bold"), padding=15, ).grid(column=0, row=0)
    ttk.Button(frm, text="Close", padding=10, command=root.destroy).grid(column=1, row=1)
    #ref = ttk.Button(frm, text="Weeks Reference...", padding=10, command=open_reference() ).grid(column=0, row=1)
    ref = ScrolledText(frm, width=45, height=12, relief="sunken", yscrollcommand="True", font=(12), bd=5, padx=4, pady=4)
    #ref.pack(side=LEFT, fill=BOTH, expand=True)
    # scrollbar = Scrollbar(root)
    # scrollbar.grid(column=2, row=0,)
    # scrollbar.config(command=ref.yview)
    # ref.config(yscrollcommand=scrollbar.set)

    ref.grid(column=1, row=0)
    ref.insert(tkinter.END, weeks_list.make_list().rstrip())
    root.mainloop()

if __name__ == '__main__':
    main()