import customtkinter as ctk
import tkinter as tk
from tkcalendar import DateEntry

date = DateEntry(
    master=None,
    width=12,
    background="darkblue",
    foreground="white",
    borderwidth=2,
    date_pattern="dd/mm/yyyy",
)
for data in date.keys():
    print(data)
