from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkFont
from main import main_algo
from main import read_old_data
from main import add_data_to_file
from Classes import IP_address

background_color="#DFDFDF"

def add_header(root):
    header_frame = Frame(root, width=500, height=50, bg=background_color)
    header_frame.grid(row=0, column=0, padx=10, pady=5, sticky='w' + 'e' + 'n' + 's')

    Label(header_frame, font=('Helvetica', 12, 'bold'), text="      ", justify=LEFT, bg=background_color) \
        .grid(row=0, column=0, padx=0, pady=5)
    Label(header_frame, font=('Helvetica', 12, 'bold'), text="שם רשת", justify=LEFT, bd=5, bg=background_color) \
        .grid(row=0, column=1, padx=40, pady=5)
    Label(header_frame, font=('Helvetica', 12, 'bold'), text="IP כתובת", bg=background_color) \
        .grid(row=0, column=2, padx=40, pady=5)
    Label(header_frame, font=('Helvetica', 12, 'bold'), text="סטאטוס פעילות", bg=background_color) \
        .grid(row=0, column=3, padx=30, pady=5)
    Label(header_frame, font=('Helvetica', 12, 'bold'), text="עדכון אחרון", justify=RIGHT, bg=background_color) \
        .grid(row=0, column=4, padx=15, pady=5)

def add_body(root, list_of_all_addresses):
    middle_frame = Frame(root, width=700, height=300, bg=background_color)
    middle_frame.grid(row=1, column=0, padx=10, pady=5)

    canvas = Canvas(middle_frame, width=620, height=300, borderwidth=0, bg=background_color, highlightthickness=0)
    frame = Frame(canvas, bg=background_color)
    vsb = Scrollbar(middle_frame, orient="vertical", command=canvas.yview, bg=background_color)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=False)
    canvas.create_window((4, 4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    insert_to_middle(frame, list_of_all_addresses)

def add_footer(root):

    footer_frame = Frame(root, width=700, height=150, bg=background_color)
    footer_frame.grid(row=2, column=0, padx=10, pady=5, sticky='w' + 'e' + 'n' + 's')

    Button(footer_frame, activeforeground="green", text=" חדשה IP הוסף כתובת ",
           bd=4, command=lambda: new_ip_window(root,footer_frame), font=('Helvetica', 12, 'bold')) \
        .grid(row=0, column=0, padx=100, pady=5, sticky='w' + 'e' + 'n' + 's')

    Button(footer_frame, text="התחל סריקה", command= lambda: new_scanning(root), bd=4,
           font=('Helvetica', 12, 'bold')) \
        .grid(row=1, column=1, padx=80, pady=5, sticky='w' + 'e' + 'n' + 's')

def ok_clicked(main_ui_footer, new_ip_window,ip_number, ip_name):
    ip = ip_number.get()
    name = ip_name.get()
    print(ip, name)

    path = "first_data.xlsx"

    add_data_to_file(path, name, ip)

    Label(main_ui_footer, text="יש לסרוק בשנית על מנת לראות את הכתובת שהתווספה", bg=background_color,
          font=('Helvetica', 12, 'bold')).grid(row=1, column=0, padx=10, pady=0)

    new_ip_window.destroy()

def cancel_clicked(root):
    print("cancel window")
    root.destroy()

def new_ip_window(root, main_footer):
    new_ip_window = Toplevel(root)
    new_ip_window.title("New Window")
    new_ip_window.config(bg=background_color)

    # Create three frames -> header -- middle -- footer
    header_frame = Frame(new_ip_window, width=300, height=50, bg=background_color)
    header_frame.grid(row=0, column=0, padx=10, pady=5)

    body_frame = Frame(new_ip_window, width=300, height=200, bg=background_color)
    body_frame.grid(row=1, column=0, padx=10, pady=5)

    footer_frame = Frame(new_ip_window, width=300, height=100, bg=background_color)
    footer_frame.grid(row=2, column=0, padx=10, pady=5, sticky='w' + 'e' + 'n' + 's')
    # ---------------------------------------------------------------------------
    ip_name = StringVar()
    ip_number = StringVar()

    Label(header_frame, text="חדשה IP הוספת כתובת", bg=background_color,  font=('Helvetica', 12, 'bold')).grid(row=0, column=0, padx=10, pady=5)

    Label(body_frame, text=":שם", bg=background_color).grid(row=0, column=1, padx=10, pady=5)
    name_entry = Entry(body_frame, textvariable = ip_name).grid(row=0, column=0, padx=10, pady=5)

    Label(body_frame, text=":IP כתובת", bg=background_color).grid(row=1, column=1, padx=10, pady=5)
    ip_entry = Entry(body_frame, textvariable = ip_number).grid(row=1, column=0, padx=10, pady=5)

    Button(footer_frame, activeforeground="green", text=" אישור ",
            command=lambda: ok_clicked(main_footer, new_ip_window, ip_number, ip_name), font=('Helvetica', 10, 'bold')) \
        .grid(row=0, column=0, padx=5, pady=5)

    Button(footer_frame, text="  ביטול  ", command=lambda: cancel_clicked(new_ip_window),
           font=('Helvetica', 10, 'bold'))\
        .grid(row=0, column=1, padx=5, pady=5)

def new_scanning(old_window):
    list_of_all_addresses = main_algo()
    print("new window opened")
    old_window.destroy()
    abc = Tk()
    creating_window(abc, list_of_all_addresses)

def onFrameConfigure(canvas):
    #Reset the scroll region to encompass the inner frame
    canvas.configure(scrollregion=canvas.bbox("all"))

def insert_to_middle(frame, list_of_all_addresses):

    i = 1
    font_style = tkFont.Font(family="Lucida Grande", size=14)
    font_time_style = tkFont.Font(family="Lucida Grande", size=10)

    for key in list_of_all_addresses:
        Label(frame, text="%s" % i, width=3, borderwidth="1", bg=background_color,
                 relief="solid").grid(row=i, column=0, padx=5, pady=5)

        name = list_of_all_addresses[key].name
        ip = list_of_all_addresses[key].ip
        status = list_of_all_addresses[key].status
        last_modify = list_of_all_addresses[key].modify

        Label(frame, text=name, font = font_style, anchor= "w", bg=background_color).grid(row=i, column=1, padx=5, pady=5)
        Label(frame, text=ip, font = font_style, bg=background_color).grid(row=i, column=2, padx=5, pady=5)

        # xyz = tk.Frame(frame, background="red").grid(row=i, column=3, padx=10, pady=1)
        if status == "work":
           color = '#489640'
        else:
            color = '#c62121'
        Label(frame, text="                          ",
                 font=font_style, bg=color).grid(row=i, column=3, padx=5, pady=5)
        Label(frame, text=last_modify, font = font_time_style, bg=background_color).grid(row=i, column=4, padx=5, pady=5)
        i += 1

def creating_window(window_name, list_of_all_addresses):

    window_name.title("Ping Sender")
    # root.maxsize(900, 600) # width x height
    window_name.config(bg=background_color)

    # Create three frames -> header -- middle -- footer
    add_header(window_name)
    add_body(window_name, list_of_all_addresses)
    add_footer(window_name)

    window_name.mainloop()

if __name__ == '__main__':

    # run the algo and show the object
    list_of_all_addresses = read_old_data()
    # list_of_all_addresses = main_algo()
    root = Tk()  # create root window

    root.iconbitmap("icon_image.ico")

    creating_window(root, list_of_all_addresses)


