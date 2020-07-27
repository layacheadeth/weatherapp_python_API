import tkinter as tk
import requests
from PIL import Image, ImageTk
root=tk.Tk()
root.geometry('600x600+600+200')
root.title("Weather_app")
#a5933736cf63897b4b0abd7c8eb51337

#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}
#https://pro.openweathermap.org/data/2.5/forecast/climate?q={city name},{country code}

def format_response(weather):
    try:
        name=weather['name']
        description=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City: %s \ndescription: %s \nTemperature(0c): %s '%(name,description,temp)
    except:
        final_str='There was a problem retrieving the info'

    return final_str

def get_weather(city):
    weather_key='a5933736cf63897b4b0abd7c8eb51337'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={
        'APPID':weather_key,
        'q':city,
        'units':'Metric'
    }
    response=requests.get(url,params=params)
    weather=(response.json())

    label['text']=format_response(weather)

    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])

background_image = tk.PhotoImage(file='/Users/deth/Desktop/weather2.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame=tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Search",font=40,command=lambda :get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame=tk.Frame(root,bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5,rely=0.3,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,font=('courier',18),anchor='nw')
label.place(relheight=1,relwidth=1)



root.mainloop()
