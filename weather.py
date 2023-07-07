from tkinter import *
import requests
k=273.15
def Weather(root):
    city=text1.get()
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7d2e1edf1823c5be5cbae5b864968f2b"
    # calling api and access the required data
    jdat=requests.get(api).json()
    condition=jdat['weather'][0]['main']
    temp=int(jdat['main']['temp']-k)
    min_temp=int(jdat['main']['temp_min']-k)
    max_temp=int(jdat['main']['temp_max']-k)
    pressure=jdat['main']['pressure']
    humidity=jdat['main']['humidity']
    wind=jdat['wind']['speed']
    # storing the data in a variable
    label1.config(text=condition+"\n"+str(temp)+"°C")
    label2.config(text="\n"+"Min Temp : "+str(min_temp)+"°C"+"\n"+"Max Temp :"+str(max_temp)+"°C"+"\n"+"Pressure : "+str(pressure)+" hPa"+"\n"+"Humidity : "+str(humidity)+"%"+"\n"+"Wind Speed : "+str(wind)+" meter/sec"+"\n")
root=Tk()
root.geometry("650x550")
root.title("Weather information")
text1=Entry(root,justify='center',width=15,font=("poppins", 15, "bold"))
text1.pack(pady = 20)
text1.focus()
text1.bind('<Return>', Weather)
# printing the value
label1=Label(root, font=("poppins", 35, "bold"))
label1.pack()
label2=Label(root, font=("poppins", 15, "bold"))
label2.pack()
root.mainloop()