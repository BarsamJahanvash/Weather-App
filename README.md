# Weather-App
#### Video Demo: https://youtu.be/iIMwM-jNyI0
#### Description:
Hello
<br>
<br>
Welcome To Barsam Jahanvash's CS50 Final Project - "Weather App"
<br>
<br>
"Weather App" Is An Application That You Can Search For Your Desired City And after Searching You Can See The Weather Profile Of That City.For This Part I Used OpenWeatherMap Api Because Its Free And Famous.
<br>
<br>
When You Lunch The Program You Arrive To The Weather app Page But If You Open The Menu And Select Another Option You Arrive To That Option Page.Apart From The Weather App This Program Also Has Clock And Timer App.For The Weather App Part I Wrote 4 Funcs That They Are:
Defult_Home, getweather, makeanswer and finalshow.
In Defult_Home Func I Defined The Relevant Variables Such As:
Search box
Buttons
Labels
In The getweather Func I Send A Request To OPenWeatherMap And I Store The Desired Answers In The Relevant Variables Which They Are:
temp:In This Variable I Save Desired City Tempreture.
condition: In This Variable I Save Desired City Condition Such As:Clear,Clouds And Rain
final_data:In This Variable I Save Things Like Wind Speed, Minimum Temperature And Maximum Temperature etc. In finalshow Func It Process Datas And Use makeanswer Func.
But It Has 1 Exception:
If The Status Code Equals To "404" It Returns "Negetive" And Change Page To "Not Found :(".In Make Answer Func It Uses The Final Datas And Show Them On Screen.
<br>
<br>
For The Second Part That Is Clock App, I Used Strftime From Time Library and Date From DateTime Library.
<br>
<br>
For The Last Part That Is Timer, I Made The Functions Manually.This Part Has 4 Functions That They Are:Start,Pause,Reset and Update.In The Update Func The Program Will Check The Seconds,Minutes And Hours Variable And If They Need To Update, It Will Update Them.
<br>
<br>
The Programming Language I Used Was Python .In Python, Tkinter Library Use For Creating Graphical Environment, Which Is Both Simple And Easy To Use, But The Problem Was That The Widgets Of This Library Were Not Soft And Modern And Brought To Life The Memory Of Windows XP. So I Found The Rewritten Tkinter That Has had Modern Widgets So I Used It.
<br>
<br>
This Is All About My App, Hope You Enjoy Using It.
<br>
<br>
-Barsam Jahanvash-
