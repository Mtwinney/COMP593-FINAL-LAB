from tkinter import *
from PIL import Image, ImageTk  
import requests
import re
import apod_desktop
import datetime


apod_desktop.init_apod_cache()

def download_apod():
    selected_date = entry_date.get()
    
    apod_date = datetime.datetime.strptime(selected_date, "%Y-%m-%d").date()
    apod_id = apod_desktop.add_apod_to_cache(apod_date)
    if apod_id != 0:
        print("APOD downloaded successfully for date:", selected_date)
    else:
        print("Failed to download APOD for date:", selected_date)

def set_desktop_background():
    pass

def search_apod_archive():
    selected_date = entry_date.get()
    
    image_url = get_image_from_archive(selected_date)
    
    if image_url:
        display_image(image_url)

def get_image_from_archive(date):
    archive_url = 'https://apod.nasa.gov/apod/archivepixFull.html'
    
    response = requests.get(archive_url)

    if response.status_code == 200:
        pattern = r'<a href="(?P<url>ap{}\.html)">[^<]*?</a>'.format(date.replace("-", ""))
        match = re.search(pattern, response.text)
        
        if match:
            image_relative_url = match.group('url')
            image_url = f'https://apod.nasa.gov/apod/{image_relative_url}'
            print("Image URL:", image_url) 
            return image_url
        else:
            print("Error: APOD not found for the selected date.")
    else:
        print("Failed to fetch APOD archive page.")



def display_image(image_url):
    response = requests.get(image_url)
    
    if response.status_code == 200:

            nasa_logo_image = Image.open("C:/Users/micha/OneDrive/Documents/COMP593-LAB/FINAL/images/NASA_logo.png")
            nasa_logo_image = nasa_logo_image.resize((200, 200))  # Resize the image
            nasa_logo_photo = ImageTk.PhotoImage(nasa_logo_image)

            image_label.configure(image=nasa_logo_photo)
            image_label.image = nasa_logo_photo
    else:
        print("Failed to fetch image from URL:", image_url)
#GUI
root = Tk()
root.geometry('1000x800')
root.title("Astronomy Picture of the Day Viewer")


label_date = Label(root, text="Select Date:")
label_date.grid(row=0, column=0, padx=50, pady=50)

entry_date = Entry(root, width=20)
entry_date.grid(row=0, column=1, padx=50, pady=50)

button_search_apod = Button(root, text="Type A Date then Click Me", command=search_apod_archive)
button_search_apod.grid(row=0, column=2, padx=10, pady=10, sticky="w")

button_download_apod = Button(root, text="Download", command=download_apod)
button_download_apod.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

button_set_background = Button(root, text="Set as Background", command=set_desktop_background)
button_set_background.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

image_label = Label(root)
image_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

nasa_logo_image = Image.open("C:/Users/micha/OneDrive/Documents/Comp593-FinalProject-main/images/NASA_logo.png")
nasa_logo_image = nasa_logo_image.resize((600, 600))
nasa_logo_photo = ImageTk.PhotoImage(nasa_logo_image)
nasa_logo_label = Label(root, image=nasa_logo_photo)
nasa_logo_label.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

root.grid_rowconfigure(4, weight=1)

root.mainloop()