#_____Libraries_____ 
from tkinter import CENTER, Entry, PhotoImage,Frame,Button,Label
import customtkinter
from PIL import ImageTk, Image
import requests
from time import *
from time import strftime
from datetime import datetime,date
import calendar
import webbrowser
app = customtkinter.CTk()
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid=9eb97d66352d8cf98e6ca6332aa31c25
CloseMenuBtn = PhotoImage(file=r"assest\img\Menu Btn Close.png")
def toggle_win():
    def site():
        webbrowser.open("https://barsamjahanvash.github.io/Web/English-Home.html")
    global f1,CloseBtn
    f1 = customtkinter.CTkFrame(app,fg_color="#2F2D2D",width=326,height=605,corner_radius=0)
    f1.place(x=0,y=0)
    def bttn(x,y,text,bcolor,fcolor,cmd):
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= 'white'  #000d33
        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= 'white'
        myButton1 = Button(f1,text=text,
                       width=46,
                       height=2,
                       fg='white',
                       border=0,
                       bg=fcolor,
                       activeforeground='#0B3E53',
                       activebackground="#0B3E53",        
                       command=cmd)
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)
        myButton1.place(x=x,y=y)
    bttn(0,80,'W E A T H E R','#0f9d9a','#2F2D2D',defult_home)
    bttn(0,117,'C L O C K','#0f9d9a','#2F2D2D',clock)
    bttn(0,154,'S T O P W A T C H','#0f9d9a','#2F2D2D',stopwatch)
    bttn(0,191,'A B O U T  M E','#0f9d9a','#2F2D2D',site)
    def closewin():
        f1.destroy()
        CloseBtn.place_forget()
    CloseBtn = Button(app,image=CloseMenuBtn,borderwidth=0,background="#2F2D2D",command=closewin,activebackground="#2F2D2D")
    CloseBtn.place(x=22,y=20)
app.geometry("800x600")
app.title("App")
# icon = PhotoImage(file=r"assest\img\icon.png")
app.iconbitmap(r"assest\img\icon.ico")
app.resizable(0,0)
app.config(background = "#0f9d9a")
background = PhotoImage(file=r"assest\img\Backgroun2.png")
MenuBtn = PhotoImage(file=r"assest\img\Menu Btn Open.png")
def defult_home():
    app.config(background = "#0f9d9a")
    for widgets in app.winfo_children():
        widgets.destroy()
    global Entry1,Back_Frame,homelable,SearchBtn,citynamelbl,templbl,conditionlbl,infolbl
    Back_Frame = Frame(master = app,background="#2F2D2D",width=800,height=53).place(x=0,y=0)
    Entry1 = customtkinter.CTkEntry(app,placeholder_text="Search City...",width=349,height=25,bg_color="#2F2D2D",fg_color="#D9D9D9",corner_radius=13,placeholder_text_color="black",state="normal",text_color="black")
    Entry1.place(x=225,y=14)
    SearchBtn = customtkinter.CTkButton(app,text="Search",bg_color="#2F2D2D",fg_color="#C8C5C5",corner_radius=10,width=60,height=25,text_color="black",hover_color="#C8C5C5",command=finalshow)
    SearchBtn.place(x=583,y=14)
    homelable = Label(app,image=background,borderwidth=0, highlightthickness=0)
    homelable.place(x=50,y=100)
    citynamelbl = Label(app,background="#0f9d9a",foreground="#0f9d9a")
    citynamelbl.place(x=0,y=60)
    templbl = Label(app,background="#0f9d9a",foreground="#0f9d9a")
    templbl.place(x=0,y=60)
    conditionlbl = Label(app,background="#0f9d9a",foreground="#0f9d9a")
    conditionlbl.place(x=0,y=60)
    infolbl = Label(app,background="#0f9d9a",foreground="#0f9d9a")
    infolbl.place(x=0,y=60)
    Menubtn = Button(app,image=MenuBtn,borderwidth=0,background="#2F2D2D",activebackground="#2F2D2D",command=toggle_win).place(x=22,y=20)
def getweather():       
    city = Entry1.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    if requests.get(api).status_code == 200:
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp'] - 273.15)
        min_temp = int(json_data['main']['temp_min'] - 273.15)
        max_temp = int(json_data['main']['temp_max'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        sunrise = strftime('%I:%M:%S',gmtime(json_data['sys']['sunrise'] - 21600))
        sunset = strftime('%I:%M:%S',gmtime(json_data['sys']['sunset'] - 21600))
        final_info = condition + "\n" + str(temp) + "°C" 
        final_data = "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    elif requests.get(api).status_code == 404:
        return "Negetive"
    return temp,condition,final_data
def makeanswer(condi,city,backgcolor,infos,temps):
    global SearchBtn,Entry1,citynamelbl,templbl,conditionlbl,infolbl,homelable,eroor,homebtn
    homelable.destroy()
    app.config(background = backgcolor)
    conditions = ""
    for i in condi.upper():
        conditions += str(i)+" "
    try:
        homebtn.destroy()
        eroor.destroy()
    except:
        pass
    SearchBtn.destroy()
    Entry1.destroy()
    SearchBtn = customtkinter.CTkButton(app,text="Search",bg_color="#2F2D2D",fg_color="#C8C5C5",corner_radius=10,width=60,height=25,text_color="black",hover_color="#C8C5C5",command=finalshow)
    SearchBtn.place(x=583,y=14)
    Entry1 = customtkinter.CTkEntry(app,placeholder_text="Search City...",width=349,height=25,bg_color="#2F2D2D",fg_color="#D9D9D9",corner_radius=13,placeholder_text_color="black",state="normal",text_color="black")
    Entry1.place(x=225,y=14)
    citynamelbl.config(text=city.upper(),background=backgcolor,foreground="white",anchor=CENTER,font=("inter",96))
    citynamelbl.place(relx=0.5,rely=0.122, anchor=CENTER)
    templbl.config(text=(str(temps) + "°C" ),background=backgcolor,foreground="white",anchor=CENTER,font=("inter",40))
    templbl.place(relx=0.5,rely=0.26,anchor=CENTER)
    conditionlbl.config(text=conditions,background=backgcolor,foreground="white",anchor=CENTER,font=("inter",24))
    conditionlbl.place(relx=0.5,rely=0.33,anchor=CENTER)
    infolbl.config(text=infos,background=backgcolor,foreground="white",anchor=CENTER,font=("inter",20))
    infolbl.place(relx=0.5,rely=0.58,anchor=CENTER)
def finalshow():
    global homelable,app,Entry1,SearchBtn,eroor,homebtn
    value = getweather()
    try:
        if "Negetive" in value:
            app.config(background = "#0f9d9a")
            for widgets in app.winfo_children():
                widgets.destroy()
            
            eroor = Label(app,text="Not Found :(",font = ("Inter",26),background="#0f9d9a",foreground="white")
            eroor.place(relx=0.5,rely=0.3,anchor=CENTER)
            homebtn = Button(app,text="Home",background="#2F2D2D",foreground="white",activebackground="#0f9d9a",command=defult_home,borderwidth=0,font=("Inter",25))
            homebtn.place(relx=0.5,rely=0.4,anchor=CENTER)
        else:
            if value[1] == "Clear":
                background = "#f78954"
                makeanswer(value[1],Entry1.get(),background,value[2],value[0])
            elif value[1] == "Clouds":
                background = "#7492b3"
                makeanswer(value[1],Entry1.get(),background,value[2],value[0])
            elif value[1] == "Rain":
                background = "#60789e"
                makeanswer(value[1],Entry1.get(),background,value[2],value[0])
    except:
        pass
def clock():
    global timelbl
    for widgets in app.winfo_children():
      widgets.destroy()
    app.config(background = "#132030")
    def time():
        a = strftime("%H:%M:%S")
        timelbl.config(text=a)
        timelbl.after(1000,time)
    Back_Frame = Frame(master = app,background="#3B2E62",width=800,height=53).place(x=0,y=0)
    titlelbl = Label(app,text="C L O C K",background="#3B2E62",foreground="white",font=("Inter",30)).place(relx=0.5,rely=0.04,anchor=CENTER)
    Menubtn = Button(app,image=MenuBtn,borderwidth=0,background="#2F2D2D",activebackground="#2F2D2D",command=toggle_win).place(x=22,y=20)
    timelbl = Label(app,font=("Inter",96),background="#132030",foreground="#FFFFFF")
    timelbl.place(relx=0.5,rely=0.4,anchor=CENTER)
    curr_date = date.today()
    day = calendar.day_name[curr_date.weekday()]
    now = datetime.now()
    datecheck = now.strftime("%D")
    strday = ""
    for i in day.upper():
        strday += str(i)+" "
    daylbl = Label(app,text=strday,font=("Inter",26),background="#132030",foreground="#FFFFFF")
    daylbl.place(relx=0.5,rely=0.55,anchor=CENTER)
    finaldate = ""
    for u in datecheck.upper():
        finaldate += str(u)+" " 
    datelbl = Label(app,text=finaldate,font=("Inter",20),background="#132030",foreground="#FFFFFF")
    datelbl.place(relx=0.5,rely=0.62,anchor=CENTER)
    time()
running = False
hours, minutes, seconds = 0, 0, 0
def stopwatch():
    running = False
    for widgets in app.winfo_children():
      widgets.destroy()
    app.config(background = "#301813")
    def start():
        global running
        if not running:
            update()
            running = True
    def pause():
        global running
        if running:
            stopwatch_label.after_cancel(update_time)
            running = False
    def reset():
        global running
        if running:
            stopwatch_label.after_cancel(update_time)
            running = False
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        stopwatch_label.config(text='00:00:00')
    def update():
        global hours, minutes, seconds
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0
        hours_string = f'{hours}' if hours > 9 else f'0{hours}'
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        global update_time
        update_time = stopwatch_label.after(1000, update)
    Back_Frame = Frame(master = app,background="#C12E2E",width=800,height=53).place(x=0,y=0)
    Menubtn = Button(app,image=MenuBtn,borderwidth=0,background="#C12E2E",activebackground="#C12E2E",command=toggle_win).place(x=22,y=20)
    titlelbl = Label(app,text="S T O P  W A T C H",background="#C12E2E",foreground="white",font=("Inter",30)).place(relx=0.5,rely=0.04,anchor=CENTER)
    stopwatch_label = Label(text='00:00:00', font=('Inter', 80),background="#301813",foreground="white")
    stopwatch_label.place(relx=0.5,rely=0.4,anchor=CENTER)
    startbtn = customtkinter.CTkButton(app,text="Start",corner_radius=13,bg_color="#301813",fg_color="#05485E",width=100,height=36,text_color="White",hover_color="#078DB8",text_font=("Inter",20),command=start)
    startbtn.place(relx=0.25,rely=0.55,anchor=CENTER)
    pausebtn = customtkinter.CTkButton(app,text="Pause",corner_radius=13,bg_color="#301813",fg_color="#05485E",width=100,height=36,text_color="White",hover_color="#078DB8",text_font=("Inter",20),command=pause)
    pausebtn.place(relx=0.5,rely=0.55,anchor=CENTER)
    resetbtn = customtkinter.CTkButton(app,text="Reset",corner_radius=13,bg_color="#301813",fg_color="#05485E",width=100,height=36,text_color="White",hover_color="#078DB8",text_font=("Inter",20),command=reset)
    resetbtn.place(relx=0.75,rely=0.55,anchor=CENTER)
defult_home()
app.mainloop()