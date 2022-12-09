# Weather-App
#### Video Demo: https://youtu.be/iIMwM-jNyI0
## Tech Used:
1.Python
## Description:
Hello.
Welcome To Barsam Jahanvash's CS50 Final Project - "Weather App"
<br>
<br>
"Weather App" Is An Application That You Can Search For Your Desired City And after Searching You Can See The Weather Profile Of That City.For This Part I Used OpenWeatherMap Api Because Its Free And Famous.
### About First Part
When You Lunch The Program You Arrive To The Weather app Page But If You Open The Menu And Select Another Option You Arrive To That Option Page.Apart From The Weather App This Program Also Has Clock And Timer App.For The Weather App Part I Wrote 4 Funcs That They Are:
Defult_Home, getweather, makeanswer and finalshow.
In Defult_Home Func I Defined The Relevant Variables Such As:
* Search box
* Buttons
* Labels

In The getweather Func I Send A Request To OPenWeatherMap And I Store The Desired Answers In The Relevant Variables Which They Are:
* temp:In This Variable I Save Desired City Tempreture.
* condition: In This Variable I Save Desired City Condition Such As:Clear,Clouds And Rain
* final_data:In This Variable I Save Things Like Wind Speed, Minimum Temperature And Maximum Temperature etc.

In finalshow Func It Process Datas And Use makeanswer Func.
But It Has 1 Exception:
If The Status Code Equals To "404" It Returns "Negetive" And Change Page To "Not Found :(".In Make Answer Func It Uses The Final Datas And Show Them On Screen.
<br>
<br>
In the second part, there is a clock that works with the time zone specified by you, and in addition to the time, it also shows the date and day of the week. For this part, I used the Time and DateTime libraries. In the main function of this There is a function named Time that updates the time every 1 second. The libraries I use receive the time and date from your system, and this means if you manually change the time zone in your system settings The time and date that the application shows you will change.
<br>
<br>
In the last section, there is a stopwatch. I wrote the functions of this section manually and did not use any special libraries. This section has 4 functions, the working process of which is as follows:
* Update: This function controls the second, minute and time variables and if these variables need to be changed, they will make the change.
* Start: This function checks that if the running variable is false, it calls the update function and then sets running to positive.
* Stop: This function stops all items and variables and sets running to false.
* Reset: This function resets all the variables and false the running.
<br>
<br>
The Programming Language I Used Was Python .In Python, Tkinter Library Use For Creating Graphical Environment, Which Is Both Simple And Easy To Use, But The Problem Was That The Widgets Of This Library Were Not Soft And Modern And Brought To Life The Memory Of Windows XP. So I Found The Rewritten Tkinter That Has had Modern Widgets So I Used It.
<br>
<br>
This Is All About My App, Hope You Enjoy Using It.
<br>
<br>
-Barsam Jahanvash-