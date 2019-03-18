from tkinter import Canvas, Tk
from PIL import Image, ImageTk
from threading import Thread
from sys import argv
import time
import requests
import numpy as np
import cv2

from input_manager import InputManager
from vnc import VNC

def gui(client, input_manager):

    window = Tk()
    window.geometry("1280x720")
    window.title("VNC Madafaka")
    
    window.update()
    input_manager.set_resolution(window.winfo_width(), window.winfo_height())
    #input_manager.transmit()
    #input_transmitter_thread = Thread(target=input_manager.transmit, args=[])
    #input_transmitter_thread.start()
    
    canvas = Canvas()

    # window.bind("<KeyPress>", input_manager.key_pressed)
    # window.bind("<KeyRelease>", input_manager.key_released)

    # canvas.bind("<Motion>", input_manager.motion)
    # canvas.bind("<ButtonPress-1>", input_manager.left_click_pressed)
    # canvas.bind("<ButtonRelease-1>", input_manager.left_click_released)
    # canvas.bind("<ButtonPress-2>", input_manager.right_click_pressed)
    # canvas.bind("<ButtonRelease-2>", input_manager.right_click_released)
    canvas.pack(side='top', fill='both', expand='yes')

    url = "http://" + str(client.ip) + ":" + str(client.port)
    print(url)
    exception = ""
    while True:
        try:
            image = client.image.resize((window.winfo_width(), window.winfo_height()), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image=image)
            canvas.create_image(0, 0, image=photo, anchor='nw')
            exception = ""
        except Exception as e:
            if exception != str(e):
                exception = str(e)
                print(e)
        
        window.update_idletasks()
        window.update()
        input_manager.set_resolution(window.winfo_width(), window.winfo_height())

if __name__ == "__main__":
    
    try:
        ip = argv[1]
    except:
        ip = "127.0.0.1"
    print(ip)
    client = VNC(ip, 5000)
    input_manager = InputManager(ip, 6969)

    client.start_receive()
    #Thread(target=client.receive, args=[]).start()

    gui(client, input_manager)




