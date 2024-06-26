from pathlib import Path

from tkinter import *

from orasidata import *
from frameuri import frameuri
from taskuri import taskuri


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\User\Desktop\zona de lucru\myapp\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def schimba_in_float():
    a = int(detaliidatatimp()[2]) / 23
    a = a * 100
    b = int(detaliidatatimp()[3]) / 7
    b = b * 100
    c = int(get_day_of_year()[0]) / float(get_day_of_year()[1])
    c = c * 100
    tuplu = (a, b, c)
    return tuplu


def update_custom_progress_bar(progress_bar, x1, y1, x2, y2, progress):
    # Calculează lățimea barei de progres bazată pe progresul curent
    new_width = x1 + (x2 - x1) * progress / 100
    # Actualizează bara de progres
    canvas.coords(progress_bar, x1, y1, new_width, y2)


def update_ceas():
    x = detaliidatatimp()[4]
    canvas.itemconfig(ceas, text=x)
    canvas.after(1000, update_ceas)


def update_temperatura():
    temperatura = returneaza_temperatura()
    canvas.itemconfig(grade, text=temperatura)


def tip_vreme():
    timp = detaliidatatimp()[2]
    vreme = returneaza_descriere_vremea()
    tip = {"Clear": 1, "Clouds": 2, "Rain": 3, "Thunderstorm": 3}

    # De la 6 dimineata pana la ora 22
    if timp in range(6, 23) and tip[vreme] == 1:
        canvas.itemconfig(image_6, image=iconvreme1)
    # De la ora 23 pana la 6 dimineata
    if (timp == 23 or timp in range(0, 6)) and tip[vreme] == 1:
        canvas.itemconfig(image_6, image=iconvreme2)
    if tip[vreme] == 2:
        canvas.itemconfig(image_6, image=iconvreme4)
    if tip[vreme] == 3:
        canvas.itemconfig(image_6, image=iconvreme3)


def afisaj(root):
    data_initiala = root.canvas.itemcget(root.text_canvas, "text")
    day = delimitare_data(data_initiala)
    for fr in frameuri.obiecte:
        if str(fr[1]) == day[0]:
            root.id = fr[0]
            for tsk in taskuri.obiecte:
                if tsk[1] == root.id:
                    root.tasks.append(tsk)
    taskuri.ia_din_db(root, button_5)
    print(root.id, data_initiala)


def la_dreapta():
    parametrii = frameuri.switch_frame(frame, "+")
    fr_update = frameuri(window, sursa_imagine=image_calendar, text=parametrii[0])
    afisaj(fr_update)


def la_stanga():
    parametrii = frameuri.switch_frame(frame, "-")
    fr_update = frameuri(window, sursa_imagine=image_calendar, text=parametrii[0])
    afisaj(fr_update)


def addTaskTab():
    add_window.deiconify()


def comanda_addButton():
    taskuri.creaza_task(frame, entry=add_entry.get(), button=button_5)
    add_entry.delete(0, END)
    add_window.withdraw()


window = Tk()
add_window = Toplevel(window)
# edit_window = Toplevel(window)

label1 = Label(add_window, text="Introdu task ul:", bg="#4169E1")
add_entry = Entry(add_window)
add_button = Button(add_window, text="ADAUGA", command=comanda_addButton)


window.geometry("900x700")
window.configure(bg="#9D9D9D")
add_window.geometry("300x150")
add_window.configure(bg="#4169E1")
add_window.title("Add task")


canvas = Canvas(
    window,
    bg="#4169E1",
    height=700,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)


image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    33.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    44.01031494140625,
    34.23529052734375,
    image=image_image_2
)

canvas.create_text(
    84.85714721679688,
    14.0,
    anchor="nw",
    text="GYM ",
    fill="#000000",
    font=("Rowdies Regular", 36 * -1)
)

# Progress bar
canvas.create_rectangle(
    35.73651123046875,
    158.78286743164062,
    193.95391845703125,
    185.20130729675293,
    fill="",
    outline="#D9D9D9")

progress1 = canvas.create_rectangle(
    35.73651123046875,
    158.78286743164062,
    193.95391845703125,
    185.20130729675293,
    fill="#00BFFF",
    outline="")
update_custom_progress_bar(progress1, 35.73651123046875, 158.78286743164062, 193.95391845703125, 185.20130729675293,
                           schimba_in_float()[1])
canvas.create_rectangle(
    35.555572509765625,
    124.0,
    193.77297973632812,
    150.4184398651123,
    fill="",
    outline="#D9D9D9")
progress2 = canvas.create_rectangle(
    35.555572509765625,
    124.0,
    193.77297973632812,
    150.4184398651123,
    fill="#00BFFF",
    outline="")
update_custom_progress_bar(progress2, 35.555572509765625, 124.0, 193.77297973632812, 150.4184398651123,
                           schimba_in_float()[2])

canvas.create_rectangle(
    35.73651123046875,
    194.3063201904297,
    193.95391845703125,
    220.724760055542,
    fill="",
    outline="#D9D9D9")
progress3 = canvas.create_rectangle(
    35.73651123046875,
    194.3063201904297,
    193.95391845703125,
    220.724760055542,
    fill="#00BFFF",
    outline="")
update_custom_progress_bar(progress3, 35.73651123046875, 194.3063201904297, 193.95391845703125, 220.724760055542,
                           schimba_in_float()[0])

canvas.create_text(
    213.29824829101562,
    199.0,
    anchor="nw",
    text=f"Day: {detaliidatatimp()[2]}/23",
    fill="#FFFFFF",
    font=("Rowdies Regular", 13 * -1)
)

canvas.create_text(
    213.29824829101562,
    163.0,
    anchor="nw",
    text=f"Week: {detaliidatatimp()[3]}/7",
    fill="#FFFFFF",
    font=("Rowdies Regular", 13 * -1)
)

canvas.create_text(
    213.29824829101562,
    128.0,
    anchor="nw",
    text=f"Year: {get_day_of_year()[0]}/{get_day_of_year()[1]}",
    fill="#FFFFFF",
    font=("Rowdies Regular", 13 * -1)
)

ceas = canvas.create_text(
    351.0,
    128.0,
    anchor="nw",
    text="12:25:11",
    fill="#FFFFFF",
    font=("RUSerius Regular", 64 * -1)
)
update_ceas()

canvas.create_text(
    430.0,
    191.1376190185547,
    anchor="nw",
    text=detaliidatatimp()[1],
    fill="#FFFFFF",
    font=("RozhaOne Regular", 20 * -1)
)

grade = canvas.create_text(
    739.0,
    150.0,
    anchor="nw",
    text="25",
    fill="#FFFFFF",
    font=("Rowdies Regular", 36 * -1)
)

update_temperatura()

iconvreme1 = PhotoImage(
    file=relative_to_assets("sun.png"))
iconvreme2 = PhotoImage(
    file=relative_to_assets("moon.png"))
iconvreme3 = PhotoImage(
    file=relative_to_assets("rain.png"))
iconvreme4 = PhotoImage(
    file=relative_to_assets("fewclouds.png"))
image_6 = canvas.create_image(
    699.0,
    168.0,
    image=iconvreme1
)
tip_vreme()
image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    793.0,
    161.0,
    image=image_image_7
)

canvas.create_text(
    810.0,
    150.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Rowdies Regular", 36 * -1)
)

grafic = canvas.create_rectangle(
    15.0,
    521.0,
    885.0,
    684.0,
    fill="#00BFFF",
    outline="")


# Frame ul principal - afisaj
coordFrame = {"x1": 15.0, "y1": 294.0, "x2": 885.0, "y2": 509.0}
frame_width = coordFrame["x2"] - coordFrame["x1"]
frame_height = coordFrame["y2"] - coordFrame["y1"]

mainframe = Frame(window, width=frame_width, height=frame_height, bg="#00BFFF")
mainframe.place(x=coordFrame["x1"], y=coordFrame["y1"])
cv = Canvas(mainframe, width=frame_width, height=frame_height, bg="#00BFFF", bd=0, highlightthickness=0, relief="ridge")
cv.place(x=0, y=0)

image_calendar = PhotoImage(
    file=relative_to_assets("icon_calendar.png"))
main_photo = PhotoImage(
    file=relative_to_assets("mainphoto2.png"))
mf = cv.create_image(
    190.0,
    110.0,
    image=main_photo
)
z = zi_curenta()
frame = frameuri(window, sursa_imagine=image_calendar, text=z[4])


# Butoane
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=la_dreapta,
    relief="flat"
)
button_1.place(
    x=841.0,
    y=363.0,
    width=36.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=la_stanga,
    relief="flat"
)
button_2.place(
    x=25.0,
    y=363.0,
    width=36.0,
    height=80.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=669.0,
    y=245.0,
    width=97.0,
    height=35.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=772.0,
    y=310.0,
    width=102.0,
    height=39.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=addTaskTab,
    relief="flat"
)
button_5.place(
    x=783.0,
    y=244.56097412109375,
    width=97.0,
    height=35.58536911010742
)

# Aplerari de functii

afisaj(frame)

# print(frame.id, frame.canvas.itemcget(frame.text_canvas, "text"))
# frameuri.switch_frame(frame, "+")

label1.place(x=100, y=20)
add_entry.place(x=78, y=50)
add_button.place(x=110, y=80)

window.resizable(False, False)
add_window.resizable(width=False, height=False)
add_window.withdraw()
window.mainloop()
add_window.mainloop()
