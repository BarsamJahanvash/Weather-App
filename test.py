# # from tkinter import *
from tkinter import *
import customtkinter
# # from time import strftime
# # root = Tk()
# # root.geometry("500x500")
# # root.resizable(0,0)
# # root.title('Python Clock')
# # def time():
# #     global mark
# #     string = strftime('%H:%M:%S %p')
# #     mark.config(text = string)
# #     mark.after(1000, time)
# # mark = Label(root, 
# #             font = ('calibri', 40, 'bold'),
# #             pady=150,
# #             foreground = 'black')
# # mark.pack(anchor = 'center')
# # time()
 
# # mainloop()
# import tkinter as tk
# running = False
# hours, minutes, seconds = 0, 0, 0
# def start():
#     global running
#     if not running:
#         update()
#         running = True
# def pause():
#     global running
#     if running:
#         stopwatch_label.after_cancel(update_time)
#         running = False
# def reset():
#     global running
#     if running:
#         stopwatch_label.after_cancel(update_time)
#         running = False
#     global hours, minutes, seconds
#     hours, minutes, seconds = 0, 0, 0
#     stopwatch_label.config(text='00:00:00')
# def update():
#     global hours, minutes, seconds
#     seconds += 1
#     if seconds == 60:
#         minutes += 1
#         seconds = 0
#     if minutes == 60:
#         hours += 1
#         minutes = 0
#     hours_string = f'{hours}' if hours > 9 else f'0{hours}'
#     minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
#     seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
#     stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
#     global update_time
#     update_time = stopwatch_label.after(1000, update)
# root = tk.Tk()
# root.geometry('485x220')
# root.title('Stopwatch')
# stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 80))
# stopwatch_label.pack()
# start_button = tk.Button(text='start', height=5, width=7, font=('Arial', 20), command=start)
# start_button.pack(side=tk.LEFT)
# pause_button = tk.Button(text='pause', height=5, width=7, font=('Arial', 20), command=pause)
# pause_button.pack(side=tk.LEFT)
# reset_button = tk.Button(text='reset', height=5, width=7, font=('Arial', 20), command=reset)
# reset_button.pack(side=tk.LEFT)
# quit_button = tk.Button(text='quit', height=5, width=7, font=('Arial', 20), command=root.quit)
# quit_button.pack(side=tk.LEFT)
# root.mainloop()
# app = Tk()
# app.geometry("700x700")
# Entry(app).place(relx=0.5,rely=0.4,anchor=CENTER)
# Button(app,text="Hello").place(relx=0.5,rely=0.5,anchor=CENTER)
# app.mainloop()
app = customtkinter.CTk()
customtkinter.CTkEntry(app).place(relx=0.5,rely=0.4,anchor=CENTER)
customtkinter.CTkButton(app,text="Hello",corner_radius=7,width=10).place(relx=0.5,rely=0.5,anchor=CENTER)
app.mainloop()