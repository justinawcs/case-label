import datetime
import string
import tkinter

import weeks_list
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

def week_letter(iso_date_string=None, letter_only=None):
    d = datetime.datetime.now().strftime("%V")
    if iso_date_string is not None:
        d = datetime.date.fromisoformat(iso_date_string).strftime("%V")
    alpha = list(string.ascii_uppercase)
    index = int(d) % 26
    result = alpha[index-1]
    if int(d) == 53:
        result = "ZA"
    if letter_only:
        return result
    else:
        return "Week #{}: {}".format(d, result)

def example_case_names(iso_date_string=None):
    week_count = datetime.datetime.now().strftime("%V")
    if iso_date_string is not None:
        week_count = datetime.date.fromisoformat(iso_date_string).strftime("%V")
    letter = week_letter(iso_date_string, letter_only=True)
    result = ["E+_##X","Z+_##X"] # where
    if int(week_count) <= 26:
        result[0] = result[0].replace("+", "B")
        result[1] = result[1].replace("+", "B")
    else:
        result[0] = result[0].replace("+", "E") #repeat letter
        result[1] = result[1].replace("+", "Z") #repeat letter
    result[0] = result[0].replace("_", letter)
    result[1] = result[1].replace("_", letter)
    return result

def main():
    examples = "Case Labels:\n{}\n{}".format(example_case_names()[0], example_case_names()[1] )
    title = "This is week\n"+week_letter().lstrip("Week ")
    #print(week_letter())
    root = Tk()
    root.title("Case Label")
    root.resizable(0,0)
    #root.attributes('-toolwindow', True)
    frm = ttk.Frame(root, padding=30)
    frm.grid()
    ttk.Label(frm, text=title,font=("Arial", 20, "bold"), padding=15, justify="center" ).grid(column=0, row=0, rowspan=2)
    ttk.Label(frm, text= examples, font=("Arial", 14,), padding=5, justify="left").grid(column=0, row=2, )
    #ttk.Label(frm, text=example_case_names()[1], font=("Arial", 12, "bold"), padding=5, ).grid(column=0, row=3)
    ttk.Button(frm, text="Close", padding=10, command=root.destroy).grid(column=0, columnspan=2, row=3)
    #ref = ttk.Button(frm, text="Weeks Reference...", padding=10, command=open_reference() ).grid(column=0, row=1)
    ref = ScrolledText(frm, width=45, height=12, relief="sunken", yscrollcommand="True", font=(12), bd=5, padx=4, pady=4)
    #ref.pack(side=LEFT, fill=BOTH, expand=True)
    # scrollbar = Scrollbar(root)
    # scrollbar.grid(column=2, row=0,)
    # scrollbar.config(command=ref.yview)
    # ref.config(yscrollcommand=scrollbar.set)

    ref.grid(column=1, row=0, rowspan=3)
    ref.insert(tkinter.END, weeks_list.make_list().rstrip())
    root.mainloop()

if __name__ == '__main__':
    main()