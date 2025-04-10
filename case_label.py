import datetime
import string
import tkinter
import tkinter.font
import webbrowser
from functools import partial

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
        result = "-"
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
    def callback(url):
        webbrowser.open_new(url)
    def adjust_year(i):
        global curr_year
        curr_year += i
        #print(curr_year)
        #update ref
        ref.delete("1.0", tkinter.END)
        ref.insert(tkinter.END, weeks_list.make_list(year=curr_year, header=False).rstrip())
    examples = "Case Labels:\n{}\n{}".format(example_case_names()[0], example_case_names()[1] )
    title = "This is week\n"+week_letter().lstrip("Week ")
    explanation = weeks_list.HEADER_TEXT.split("\n")
    global curr_year
    curr_year = datetime.datetime.now().year
    #print(week_letter())
    root = Tk()
    root.title("Case Label")
    root.resizable(0,0)
    #root.attributes('-toolwindow', True)
    frm = ttk.Frame(root, padding=20)
    frm.grid()
    ttk.Label(frm, text=title,font=("Arial", 20, "bold"), padding=15, justify="center" ).grid(column=0, row=2, rowspan=2)
    ttk.Label(frm, text=examples, font=("Arial", 14,), padding=5, justify="left").grid(column=0, row=4, )
    ttk.Label(frm, text=explanation[0], font=("Arial", 12,), padding=None, justify="left").grid(column=1, row=0, columnspan=6, rowspan=1)
    underline_font = tkinter.font.Font(family="Arial", size=12, underline=True)
    link = Label(frm, text=explanation[1], font=underline_font, foreground="blue", cursor="hand2")
    link.bind("<Button-1>", lambda e: callback(explanation[1]))
    link.grid(column=1, row=1, columnspan=6, rowspan=1)

    #ttk.Label(frm, text=example_case_names()[1], font=("Arial", 12, "bold"), padding=5, ).grid(column=0, row=3)
    prev_b = ttk.Button(frm, text="Previous Year", padding=10, command=partial(adjust_year, -1) )
    prev_b.grid(column=1, columnspan=2, row=6)
    ttk.Button(frm, text="Close", padding=10, command=root.destroy).grid(column=3, columnspan=2, row=6)
    next_b = ttk.Button(frm, text="Next Year", padding=10, command=partial(adjust_year, 1) )
    next_b.grid(column=5, columnspan=2, row=6)

    #ref = ttk.Button(frm, text="Weeks Reference...", padding=10, command=open_reference() ).grid(column=0, row=1)
    global ref
    ref = ScrolledText(frm, width=45, height=12, relief="sunken", yscrollcommand="True", font=(12), bd=5, padx=4, pady=4)
    #ref.pack(side=LEFT, fill=BOTH, expand=True)
    # scrollbar = Scrollbar(root)
    # scrollbar.grid(column=2, row=0,)
    # scrollbar.config(command=ref.yview)
    # ref.config(yscrollcommand=scrollbar.set)

    ref.grid(column=1, row=2, columnspan=6, rowspan=4)
    ref.insert(tkinter.END, weeks_list.make_list(year=curr_year, header=False).rstrip())
    root.mainloop()

if __name__ == '__main__':
    main()