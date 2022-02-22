# student id : M00734701
# importing libraries
from tkinter import *
import pickle
import socket
import tkinter.messagebox
from tkinter import ttk
import pandas as pd
import csv
import numpy as np
# to put pie charts in tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# initialising the HOST and PORT
HOST = '127.0.0.1'
PORT = 3333

# step 1 Create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# step 2 Listen for a connection from a server and accepted
client_socket.connect((HOST, PORT))

# initialising variables and assigning it to 0
totalPrice = 0
amount_paid = 0

# class initializing the main frame of window and function to switch frames
class Application(Tk):
    # initialzing the main frame
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.title("Vending Machine")
        self.config(bg='Black', highlightthickness=10)
        # preventing to resize the window
        self.resizable(0, 0)
        self.switch_frame(Welcome)

    # function that will be used to switch from one frame to another one
    def switch_frame(self, Frame_class):
        new_Frame = Frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_Frame
        self._frame.pack(pady=25)

    # cancel function
    def cancel(self):
        exit = tkinter.messagebox.askyesno("Vending Machine", "Are you sure you want to exit?", icon='warning')
        if exit > 0:
            self.switch_frame(Welcome)


# class to display a welcome message and buttons for client or admin
class Welcome(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        welcome_message = Label(self, text='Welcome to our \n Vending Machine', font=('Time New Romans', 40, 'bold'),
                                fg='white', bg='Black')
        welcome_message.pack(pady=155)

        client_button = Button(self, text='Client', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                               width=10, height=2, command=lambda: master.switch_frame(Client_Page1))
        client_button.pack(pady=50)

        admin_button = Button(self, text='Admin', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                              width=10, height=2, command=lambda: master.switch_frame(Admin_Page1))
        admin_button.pack(pady=10)


# class to choose which type of product the client wants to order
class Client_Page1(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        question_1 = Label(self, text='What would you like?', font=('Time New Romans', 40, 'bold'), fg='white',
                           bg='Black')
        question_1.pack(pady=70)

        drinks_button = Button(self, text='Drinks', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                               width=20, height=2, command=lambda: master.switch_frame(Drinks))
        drinks_button.pack(pady=30)

        Snacks_button = Button(self, text='Snacks', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                               width=20, height=2, command=lambda: master.switch_frame(Snacks))
        Snacks_button.pack(pady=30)

        Chocolates_button = Button(self, text='Chocolates', font=('Time New Romans', 15, 'bold'), bg='white',
                                   width=20, height=2, command=lambda: master.switch_frame(Chocolates))
        Chocolates_button.pack(pady=30)

        Cancel_button = Button(self, text='Cancel', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                               width=30, height=2, command=lambda: master.cancel())
        Cancel_button.pack(pady=70)


# class to display the drinks, their price and code
class Drinks(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        # label to display the title, and instructions
        drinks_label = Label(self, text='Drinks', font=('Time New Romans', 35, 'bold'), fg='white', bg='black')
        drinks_label.pack(pady=10)
        message = Label(self, text='List of Drinks. \nIf you want to order, press on the button CONTINUE. '
                                   '\nPlease do not forget the code, Thank you!', fg='white', bg='black',
                        font=('Time New Romans', 10, 'bold'))
        message.pack()

        row = Label(self, width=70, height=30, bg='black')
        row.pack()
        # displaying a picture for the item redbull
        redbull = PhotoImage(file=r'Redbull_Drink.png')
        redbull_label = Label(row, image=redbull, bg='Black')
        redbull_label.pack(side=LEFT, pady=10, padx=30)
        redbull_label.image = redbull

        # displaying a picture for the item fanta
        fanta = PhotoImage(file=r'Fanta_Drink.png')
        fanta_label = Label(row, image=fanta, bg='black')
        fanta_label.pack(side=RIGHT, pady=10, padx=30)
        fanta.image = fanta

        # displaying a picture for the item sprite
        sprite = PhotoImage(file=r'Sprite_Drink.png')
        sprite_label = Label(row, image=sprite, bg='black')
        sprite_label.pack(pady=10)
        sprite.image = sprite

        row2 = Label(self, width=70, height=30, bg='black')
        row2.pack()
        # details of the items
        redbull_name = Label(row2, text='Redbull \nCode: D42 \nPrice: Rs 15', fg='white', bg='black', font=('arial', 12,
                                                                                                            'bold'))
        redbull_name.pack(side=LEFT, pady=10, padx=30)

        fanta_name = Label(row2, text='Fanta \nCode: D10 \nPrice: Rs 25', fg='white', bg='black', font=('arial', 12,
                                                                                                        'bold'))
        fanta_name.pack(side=RIGHT, pady=10, padx=30)

        sprite_name = Label(row2, text='Sprite \nCode: D15 \nPrice: Rs 25', fg='white', bg='black', font=('arial', 12,
                                                                                                          'bold'))
        sprite_name.pack(pady=10, padx=50)

        row3 = Label(self, width=70, height=30, bg='black')
        row3.pack()
        # displaying a picture for the item coke
        coke = PhotoImage(file=r'Coke_Drink.png')
        coke_label = Label(row3, image=coke, bg='black')
        coke_label.pack(side=LEFT, pady=10, padx=30)
        coke_label.image = coke

        # displaying a picture for the item monster
        monster = PhotoImage(file=r'Monster_Drink.png')
        monster_label = Label(row3, image=monster, bg='black')
        monster_label.pack(side=RIGHT, pady=10, padx=30)
        monster_label.image = monster

        row4 = Label(self, width=70, height=30, bg='black')
        row4.pack()
        # details of the items
        coke_name = Label(row4, text='Coke \nCode: D23 \nPrice: Rs 30', fg='white', bg='black', font=('arial', 12,
                                                                                                      'bold'))
        coke_name.pack(side=LEFT, pady=10, padx=60)

        monster_name = Label(row4, text='Monster \nCode: D39 \nPrice: Rs 20', fg='white', bg='black', font=('arial', 12,
                                                                                                            'bold'))
        monster_name.pack(side=RIGHT, pady=30, padx=60)

        row5 = Label(self, width=70, height=30, bg='white')
        row5.pack()
        # Buttons
        continue_button = Button(row5, text='Continue', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                                 width=10, height=2, command=lambda: master.switch_frame(Order))
        continue_button.pack(side=LEFT, pady=10, padx=5)

        cancel_button = Button(row5, text='Cancel', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                               width=10, height=2, command=lambda: master.cancel())
        cancel_button.pack(side=RIGHT, pady=10, padx=5)

        goback_button = Button(row5, text='Go back', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                               width=10, height=2, command=lambda: master.switch_frame(Client_Page1))
        goback_button.pack(pady=10, padx=5)


# class to display the snacks, their price and code
class Snacks(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        # label to display the title, and instructions
        snacks_label = Label(self, text='Snacks', font=('Time New Romans', 35, 'bold'), fg='white', bg='black')
        snacks_label.pack(pady=10)

        message = Label(self, text='List of Snacks. \nIf you want to order, press on the button CONTINUE. '
                                   '\nPlease do not forget the code, Thank you!', fg='white', bg='black',
                        font=('Time New Romans', 10, 'bold'))
        message.pack()

        row1_4 = Label(self, width=70, height=30, bg='black')
        row1_4.pack()
        row1 = Label(row1_4, width=70, height=30, bg='black')
        row1.pack()

        # displaying the picture for item light_blue_doritos
        light_blue_doritos = PhotoImage(file=r'Doritos_blue_snack.png')
        light_blue_doritos_label = Label(row1, image=light_blue_doritos, bg='Black')
        light_blue_doritos_label.pack(side=LEFT, pady=10, padx=30)
        light_blue_doritos.image = light_blue_doritos

        # displaying the picture for the item orange_doritos
        orange_doritos = PhotoImage(file=r'Doritos_orange_snack.png')
        orange_doritos_label = Label(row1, image=orange_doritos, bg='black')
        orange_doritos_label.pack(side=RIGHT, pady=10, padx=30)
        orange_doritos.image = orange_doritos

        # displaying the picture for the item red_doritos
        red_doritos = PhotoImage(file=r'Doritos_red_snack.png')
        red_doritos_label = Label(row1, image=red_doritos, bg='black')
        red_doritos_label.pack(pady=10)
        red_doritos.image = red_doritos

        row2 = Label(row1_4, width=70, height=30, bg='black')
        row2.pack()
        # details of the items
        light_blue_doritos_name = Label(row2, text='Doritos Paprika \nCode: S03 \nPrice: Rs 45', fg='white', bg='black',
                                        font=('arial', 12, 'bold'))
        light_blue_doritos_name.pack(side=LEFT, pady=10, padx=30)

        orange_doritos_name = Label(row2, text='Doritos Cheese \nCode: S50 \nPrice: Rs 40', fg='white', bg='black',
                                    font=('arial', 12, 'bold'))
        orange_doritos_name.pack(side=RIGHT, pady=10, padx=30)

        red_doritos_name = Label(row2, text='Doritos BBQ \nCode: S30 \nPrice: Rs 45', fg='white', bg='black',
                                 font=('arial', 12, 'bold'))
        red_doritos_name.pack(pady=10, padx=50)

        row3 = Label(row1_4, width=70, height=30, bg='black')
        row3.pack()
        # displaying the picture for the item blue_doritos
        blue_doritos = PhotoImage(file=r'Doritos_blue2_snack.png')
        blue_doritos_label = Label(row3, image=blue_doritos, bg='black')
        blue_doritos_label.pack(side=LEFT, pady=10, padx=30)
        blue_doritos_label.image = blue_doritos

        # displaying the picture for the item black_doritos
        black_doritos = PhotoImage(file=r'Doritos_black_snack.png')
        black_doritos_label = Label(row3, image=black_doritos, bg='black')
        black_doritos_label.pack(side=RIGHT, pady=10, padx=30)
        black_doritos_label.image = black_doritos

        row4 = Label(row1_4, width=70, height=30, bg='black')
        row4.pack()
        # details of the items
        blue_doritos_name = Label(row4, text='Doritos Sweet\nChilli Pepper \nCode: S21 \nPrice: Rs 50', fg='white',
                                  bg='black', font=('arial', 12, 'bold'))
        blue_doritos_name.pack(side=LEFT, pady=10, padx=60)

        black_doritos_name = Label(row4, text='Doritos Sweet\nChilli \nCode: S39 \nPrice: Rs 50', fg='white',
                                   bg='black', font=('arial', 12, 'bold'))
        black_doritos_name.pack(side=RIGHT, pady=30, padx=60)

        row5 = Label(self, width=70, height=30, bg='white')
        row5.pack()
        # Bittons
        continue_button = Button(row5, text='Continue', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                                 width=10, height=2, command=lambda: master.switch_frame(Order))
        continue_button.pack(side=LEFT, pady=10, padx=5)
        cancel_button = Button(row5, text='Cancel', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                               width=10, height=2, command=lambda: master.cancel())
        cancel_button.pack(side=RIGHT, pady=10, padx=5)

        goback_button = Button(row5, text='Go back', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                               width=10, height=2, command=lambda: master.switch_frame(Client_Page1))
        goback_button.pack(pady=10, padx=5)


# class to display the chocolates, their price and code
class Chocolates(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        # label to display the title, and instructions
        chocolates_label = Label(self, text='Chocolates', font=('Time New Romans', 35, 'bold'), fg='white', bg='black')
        chocolates_label.pack(pady=10)

        message = Label(self, text='List of Chocolates. \nIf you want to order, press on the button CONTINUE. '
                                   '\nPlease do not forget the code, Thank you!', fg='white', bg='black',
                        font=('Time New Romans', 10, 'bold'))
        message.pack()

        row1_4 = Label(self, width=70, height=30, bg='black')
        row1_4.pack()
        row1 = Label(row1_4, width=70, height=30, bg='black')
        row1.pack()

        # displaying the picture for item mars
        mars = PhotoImage(file=r'Mars_Chocolate.png')
        mars_label = Label(row1, image=mars, bg='Black')
        mars_label.pack(side=LEFT, pady=10, padx=30)
        mars.image = mars

        # displaying the picture for item twix
        twix = PhotoImage(file=r'Twix_Chocolate.png')
        twix_label = Label(row1, image=twix, bg='black')
        twix_label.pack(side=RIGHT, pady=10, padx=30)
        twix.image = twix

        # displaying the picture for item kitkat
        kitkat = PhotoImage(file=r'KitKat_Chocolate.png')
        kitkat_label = Label(row1, image=kitkat, bg='black')
        kitkat_label.pack(pady=10)
        kitkat.image = kitkat

        row2 = Label(row1_4, width=70, height=30, bg='black')
        row2.pack()
        # details of the items
        mars_name = Label(row2, text='Mars \nCode: C05 \nPrice: Rs 70', fg='white', bg='black', font=('arial', 12,
                                                                                                      'bold'))
        mars_name.pack(side=LEFT, pady=10, padx=30)

        twix_name = Label(row2, text='Twix \nCode: C40 \nPrice: Rs 55', fg='white', bg='black', font=('arial', 12,
                                                                                                      'bold'))
        twix_name.pack(side=RIGHT, pady=10, padx=30)

        kitkat_name = Label(row2, text='KitKat \nCode: C45 \nPrice: Rs 60', fg='white', bg='black', font=('arial', 12,
                                                                                                          'bold'))
        kitkat_name.pack(pady=10, padx=50)

        row3 = Label(row1_4, width=70, height=30, bg='black')
        row3.pack()
        # displaying the picture for item crunch
        crunch = PhotoImage(file=r'Crunch_Chocolate.png')
        crunch_label = Label(row3, image=crunch, bg='black')
        crunch_label.pack(side=LEFT, pady=0, padx=30)
        crunch_label.image = crunch

        # displaying the picture for item dairyMilk
        dairyMilk = PhotoImage(file=r'DairyMilk_Chocolate.png')
        dairyMilk_label = Label(row3, image=dairyMilk, bg='black')
        dairyMilk_label.pack(side=RIGHT, pady=0, padx=30)
        dairyMilk_label.image = dairyMilk

        row4 = Label(row1_4, width=70, height=30, bg='black')
        row4.pack()
        # details of the items
        crunch_name = Label(row4, text='Crunch \nCode: C32 \nPrice: Rs 60', fg='white', bg='black', font=('arial', 12,
                                                                                                          'bold'))
        crunch_name.pack(side=LEFT, pady=10, padx=60)

        dairyMilk_name = Label(row4, text='Dairy Milk \nCode: C46 \nPrice: Rs 80', fg='white', bg='black',
                               font=('arial', 12, 'bold'))
        dairyMilk_name.pack(side=RIGHT, pady=30, padx=60)

        row5 = Label(self, width=70, height=30, bg='white')
        row5.pack()
        # Buttons
        continue_button = Button(row5, text='Continue', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                                 width=10, height=2, command=lambda: master.switch_frame(Order))
        continue_button.pack(side=LEFT, pady=10, padx=5)

        cancel_button = Button(row5, text='Cancel', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                               width=10, height=2, command=lambda: master.cancel())
        cancel_button.pack(side=RIGHT, pady=10, padx=5)

        goback_button = Button(row5, text='Go back', font=('Time New Romans', 15, 'bold'), fg='white', bg='black',
                               width=10, height=2, command=lambda: master.switch_frame(Client_Page1))
        goback_button.pack(pady=10, padx=5)


# class to give the order
class Order(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        # variables
        global totalPrice
        code_entered = StringVar()
        quantity_entered = IntVar()
        totalPrice = IntVar()

        title = Label(self, text="Order", bd=5, relief=GROOVE, fg='Black', bg='White',
                      font=("times new roman", 30, "bold"), pady=3)
        title.pack(fill=X)

        frame1_3 = Label(self, width=100, height=100, bg='black')
        frame1_3.pack()
        frame1 = LabelFrame(frame1_3, text='Enter Details', font=("time new roman", 12, "bold"), fg="Red", bg='White',
                            relief=GROOVE, bd=10)
        frame1.place(x=0, y=30, relwidth=1)

        product_code = Label(frame1, text='Product Code: ', bg='White', fg='Black',
                             font=('times new roman', 12, 'bold'))
        product_code.grid(row=0, column=0, padx=10, pady=5)

        code_entry = Entry(frame1, bd=7, relief=GROOVE, textvariable=code_entered)
        code_entry.grid(row=0, column=1, ipady=4, ipadx=7, pady=5)

        # in case the user press the '?' button
        def option():
            # creating a toplevel window
            toplevel = Toplevel(self)
            toplevel.title("Products Details")

            # creating a table
            table = ttk.Treeview(toplevel, height=15, columns=('p_id', 'p_name', 'p_price', 'p_quantity'))
            table.pack()

            # assigning headers to each column
            table.heading('p_id', text="Product ID")
            table.heading('p_name', text="Product Name")
            table.heading('p_price', text="Product Price")
            table.heading('p_quantity', text="Product Quantity")
            # dislaying the headers into the table
            table['show'] = 'headings'
            # size of each column
            table.column('p_id', width=80)
            table.column('p_name', width=120)
            table.column('p_price', width=80)
            table.column('p_quantity', width=120)
            # displaying the whole table
            table.pack(fill=BOTH, expand=1)

            # filling the table with the use of 'Product.csv' file
            with open('Product.csv') as product_file:
                read = csv.DictReader(product_file, delimiter=',')
                for row in read:
                    product_id = row['Product_ID']
                    product_name = row['Product_Name']
                    product_price = row['Product_Price']
                    productquantity = row['Product_Quantity']
                    # inserting values into the table
                    table.insert("", 0, values=(product_id, product_name, product_price, productquantity))

        show_details = Button(frame1, text='?', bg='White', fg='Black', width=2, bd=2, command=option)
        show_details.grid(row=0, column=2)

        product_quantity = Label(frame1, text='Quantity: ', bg='White', fg='Black',
                                 font=('times new roman', 12, 'bold'))
        product_quantity.grid(row=0, column=3, padx=10, pady=5)
        quantity_entry = Entry(frame1, bd=8, relief=GROOVE, textvariable=quantity_entered)
        quantity_entry.grid(row=0, column=4, ipady=4, ipadx=7, pady=5)

        frame2 = LabelFrame(frame1_3, text='Bill', fg="Red", font=("time new roman", 12, "bold"), bg='White', bd=10,
                            relief=GROOVE)
        frame2.place(x=0, y=140,  relwidth=1)

        # creating table for the order
        order = ttk.Treeview(frame2, height=18, columns=('p_name', 'p_quty', 'p_price_unit', 'p_price'))
        # assigning headers to each column
        order.heading('p_name', text='Product Name')
        order.heading('p_quty', text='Quantity')
        order.heading('p_price_unit', text='Product Unit Price')
        order.heading('p_price', text='Product Total Price')
        # dislaying the headers into the table
        order['show'] = 'headings'
        # size of each column
        order.column('p_name', width=80)
        order.column('p_quty', width=120)
        order.column('p_price_unit', width=80)
        order.column('p_price', width=120)
        #displaying the table
        order.pack(fill=BOTH, expand=1)

        total_label = Label(frame2, text='Total Price: Rs.', font=("time new roman", 12, "bold"), bg='white',
                            fg='black')
        total_label.pack(side=LEFT, padx=20, pady=10)

        total_price_entry = Entry(frame2, font=("time new roman", 12, "bold"), textvariable=totalPrice, state=DISABLED,
                                  width=10)
        total_price_entry.pack(side=LEFT, padx=0, pady=10)

        order_dict = {'Name': 'Quantity'}
        # function add_another in case the button 'add another' is pressed
        def add_another():
            # read the file 'product.csv' as a dictionary
            with open('Product.csv') as product_file:
                read = csv.DictReader(product_file, delimiter=',')
                found = False
                for row in read:
                    if row['Product_ID'] == code_entered.get():
                        found = True
                        product_name = row['Product_Name']
                        productquantity = float(row['Product_Quantity'])
                        product_price = row['Product_Price']
                        product_price_total = float(product_price)*quantity_entered.get()

                        if quantity_entered.get() == 0:
                            tkinter.messagebox.showerror('Error', "Quantity required ")
                        elif quantity_entered.get() <= productquantity:
                            if product_name in order_dict:
                                tkinter.messagebox.showerror('Error', "Product already exist in your order."
                                                                      "\nYou can update the quantity if needed."
                                                                      "\nThank you!")
                            else:
                                order.insert('', 0, values=(product_name, quantity_entered.get(),
                                                            product_price, product_price_total))
                                price = totalPrice.get() + product_price_total
                                totalPrice.set(price)
                                order_dict[product_name] = quantity_entered.get()
                        else:
                            tkinter.messagebox.showerror('Error', f"Only {productquantity} available.")

                if found == False:
                    tkinter.messagebox.showerror('Error', "Code doesn't exist. "
                                                          "\nKindly press '?' to check the code for each item."
                                                          "\nThank you!")

        # function delete in case button 'delete' is pressed
        def delete():
            selected_row = order.focus()
            value = order.item(selected_row, 'value')
            price = totalPrice.get() - float(value[3])
            totalPrice.set(price)
            row = order.selection()[0]
            if value[0] in order_dict:
                del order_dict[value[0]]
            order.delete(row)

        # function reset in case button 'reset' is pressed
        def reset():
            for record in order.get_children():
                order.delete(record)
                totalPrice.set(0)
                order_dict.clear()
                order_dict['Name'] = 'Quantity'

        # function finish_pay in case button 'finish and pay' is pressed
        def finish_pay():
            question_confirmation = tkinter.messagebox.askyesno('Confirmation', 'Are you sure you want to confirm your order?')
            if question_confirmation > 0:
                # if yes, it will write into the order file
                with open('order.csv', 'w', newline='') as file:
                    writer = csv.writer(file, delimiter=',')
                    file.write('Product_Name,Product_Quantity, Product_Unit_Price, Product_Total_Price\n')
                    for row in order.get_children():
                        value = order.item(row)['values']
                        writer.writerow(value)
                master.switch_frame(Finish)

        # function cancel in case button 'cancel' is pressed
        def cancel():
            icancel = tkinter.messagebox.askyesno('Cancel', 'Are you sure you want to exit?')
            if icancel > 0:

                window = Toplevel(bg='white', width=50, height=200)
                window.geometry('600x900')
                window.config(bg='black')
                apology = Label(window, text='Sorry, we could not provide \nyou with your choice today.'
                                             '\nWe hope to see you soon again.\n Thank you! \nHave a good day!',
                                font=('time mew roman', 20, 'bold'))
                apology.pack(pady=250)

                def home():
                    master.switch_frame(Welcome)
                    window.destroy()

                home = Button(window, text='Home', bg='White', fg='Black', font=("time new roman", 12, "bold"),
                              bd=7, relief=GROOVE, command=home)
                home.pack(ipadx=10)

        # function select in case button 'select' is pressed
        def select():
            code_entry.delete(0, END)
            quantity_entry.delete(0, END)

            selected = order.focus()
            values = order.item(selected, 'values')

            with open('Product.csv') as product_file:
                read = csv.DictReader(product_file, delimiter=',')
                for row in read:
                    if row['Product_Name'] == values[0]:
                        product_id = row['Product_ID']
                        code_entry.insert(0, product_id)
                        quantity_entry.insert(0, values[1])

        # function update in case button 'update' is pressed
        def update():
            selected = order.focus()
            value = order.item(selected, 'value')
            with open('Product.csv') as product_file:
                read = csv.DictReader(product_file, delimiter=',')
                for row in read:
                    if row['Product_Name'] == value[0]:
                        product_name = row['Product_Name']
                        productquantity = float(row['Product_Quantity'])
                        product_price = row['Product_Price']
                        product_price_total = float(product_price)*quantity_entered.get()

                        if quantity_entered.get() <= productquantity:

                            order.insert('', 0, values=(product_name, quantity_entered.get(),
                                                        product_price, product_price_total))
                            price = totalPrice.get() + product_price_total
                            totalPrice.set(price)
                            order_dict[product_name] = quantity_entered.get()
                            price = totalPrice.get() - float(value[3])
                            totalPrice.set(price)
                            row2 = order.selection()[0]
                            order.delete(row2)
                        else:
                            tkinter.messagebox.showerror('Error', f"Only {productquantity} available.")

                if code_entered.get() == '' or quantity_entered.get() == '':
                    tkinter.messagebox.showerror('Error', "Code and quantity required ")

            code_entry.delete(0, END)
            quantity_entry.delete(0, END)

        frame3 = LabelFrame(frame1_3, text='More..', fg="Red", font=("time new roman", 12, "bold"), bg='White', bd=10,
                            relief=GROOVE)
        frame3.place(x=0, y=620,  relwidth=1)
        # buttons
        add_another_button = Button(frame3, text="Add\nAnother", bg='White', fg='Black',
                                    font=("time new roman", 12, "bold"), bd=7, relief=GROOVE, command=add_another)
        add_another_button.grid(row=0, column=0, ipadx=10)

        remove_button = Button(frame3, text="Delete", bg='White', fg='Black', font=("time new roman", 12, "bold"),
                               bd=7, height=2, width=7, relief=GROOVE, command=delete)
        remove_button.grid(row=0, column=1, ipadx=10)

        reset_button = Button(frame3, text="Reset", bg='White', fg='Black', font=("time new roman", 12, "bold"),
                              bd=7, relief=GROOVE, height=2, width=7, command=reset)
        reset_button.grid(row=0, column=2, ipadx=10)

        finish_pay_button = Button(frame3, text='Finish \nand Pay', font=('Time New Romans', 12, 'bold'),
                                   fg='black', bg='white', bd=7, width=16, height=4, relief=GROOVE, command=finish_pay)
        finish_pay_button.place(x=350, y=15)

        cancel_button = Button(frame3, text="Cancel", bg='White', fg='Black', height=2,
                               font=("time new roman", 12, "bold"), bd=7, width=7, relief=GROOVE, command=cancel)
        cancel_button.grid(row=1, column=0,  ipadx=10)
        update_button = Button(frame3, text="Update", bg='White', fg='Black', height=2,
                               font=("time new roman", 12, "bold"), bd=7, width=7, relief=GROOVE, command=update)
        update_button.grid(row=1, column=1, ipadx=10)
        select_button = Button(frame3, text="Select", bg='White', fg='Black', height=2,
                               font=("time new roman", 12, "bold"), bd=7, width=7, relief=GROOVE, command=select)
        select_button.grid(row=1, column=2, ipadx=10)


# class to proceed payment
class Finish(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.title("Finish and Pay")
        self.master.geometry("600x900")

        global totalPrice
        global amount_paid

        bill = Frame(self, bd=10, relief=GROOVE, bg='white', height=50)
        bill.pack(pady=30)

        title = Label(bill, text='Bill', font=('Arial Black', 17, 'bold'), bd=5, relief=GROOVE, bg='white', fg='black')
        title.pack(fill=X)

        scroll = Scrollbar(bill, orient=VERTICAL)
        self.text = Text(bill, yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        scroll.config(command=self.text.yview)
        self.text.pack(fill=BOTH, expand=1)

        self.text.insert(END, " \t\t\tWelcome to Our Vending Machine\n")
        self.text.insert(END, "=" * 67)
        self.text.insert(END, "\nProduct Name\t\tQty\t\tIndividual Price\t\t\tTotal Price")
        self.text.insert(END, "\n" + ("=" * 67))

        with open('order.csv') as order_file:
            read = csv.DictReader(order_file, delimiter=',')
            total_amount = 0
            for row in read:
                product = row['Product_Name']
                quantity = row['Product_Quantity']
                price_unit = row[' Product_Unit_Price']
                total_price = row[' Product_Total_Price']
                total_amount += float(total_price)

                self.text.insert(END, f"\n{product}\t\t{quantity}\t\t   {price_unit}\t\t\t   {total_price}")

            self.text.insert(END, "\n" + ("=" * 67))
            self.text.insert(END, f"Total Bill Amount :Rs. {total_amount}")

        def cash():
            window = Toplevel(bg='white', width=50, height=200)
            window.geometry('440x500')
            window.config(bg='black')
            window.resizable(0, 0)

            def confirm():
                iconfirm = tkinter.messagebox.askyesno('Confirmation', 'Are you sure you want to confirm the payment?')
                if iconfirm == 1:
                    if amount_paid.get() == '':
                        tkinter.messagebox.showerror('Error', 'Kindly first check the amount entered.')
                        cash()
                    elif float(amount_paid.get()) < float(price.get()):
                        tkinter.messagebox.showerror('Error', 'Amount entered is not enough. ' 
                                                              '\nKindly check again the total amount')
                        cash()
                    elif float(amount_paid.get()) > float(price.get()):
                        change = float(amount_paid.get()) - float(price.get())
                        tkinter.messagebox.showinfo('Payment Done', f'Payment and Order confirmed.\nChanges = {change}'
                                                                    f'\nThank You, Have a good Day!')

                        with open('order.csv', 'r') as order_file:
                            content = csv.reader(order_file)
                            list_order = list(content)

                        client_message = pickle.dumps(list_order)
                        client_socket.send(client_message)

                        from_server = client_socket.recv(1024)
                        print(from_server.decode())
                        window.destroy()
                        master.switch_frame(Welcome)

            def cancel_cash():
                window.destroy()

            payment_type = Label(window, text='Payment by Cash: ', font=('Arial Black', 15, 'bold'), fg='white',
                                 bg='black')
            payment_type.grid(row=0, column=1, pady=20)

            display_amount = Label(window, text='Total Price: ', font=('Arial Black', 11, 'bold'), fg='white', bg='black')
            display_amount.grid(row=2, column=0)

            price = IntVar()
            price.set(total_amount)

            total_price_display = Entry(window, font=("time new roman", 12, "bold"), textvariable=price, state=DISABLED,
                                        width=10)
            total_price_display.grid(row=2, column=2)

            amount = LabelFrame(window, font=('Arial Black', 15, 'bold'), bg='white', relief = GROOVE, fg='black')
            amount.grid(row=3, columnspan=3, pady=20)

            value1000 = IntVar()
            value500 = IntVar()
            value200 = IntVar()
            value100 = IntVar()
            value50 = IntVar()
            value25 = IntVar()

            entry1000 = StringVar()
            entry500 = StringVar()
            entry200 = StringVar()
            entry100 = StringVar()
            entry50 = StringVar()
            entry25 = StringVar()
            amount_paid = StringVar()

            entry1000.set(0)
            entry500.set(0)
            entry200.set(0)
            entry100.set(0)
            entry50.set(0)
            entry25.set(0)


            def total():
                value1 = float(entry1000.get())
                value2 = float(entry500.get())
                value3 = float(entry200.get())
                value4 = float(entry100.get())
                value5 = float(entry50.get())
                value6 = float(entry25.get())

                calculate =(value1*1000)+(value2*500)+(value3*200)+(value4*100)+(value5*50)+(value6*25)
                amount_paid.set(calculate)


            def check_rs1000():
                if value1000.get() == 1:
                    txtrs1000.configure(state=NORMAL)
                    txtrs1000.delete(0, END)
                    entry1000.set('')
                elif value1000.get() ==0:
                    txtrs1000.configure(state=DISABLED)
                    entry1000.set('0')


            def check_rs500():
                if value500.get() == 1:
                    txtrs500.configure(state=NORMAL)
                    txtrs500.focus()
                    txtrs500.delete('0', END)
                    entry500.set('')

                elif value500.get() ==0:
                    txtrs500.configure(state=DISABLED)
                    entry500.set('0')

            def check_rs200():
                if value200.get() == 1:
                    txtrs200.configure(state=NORMAL)
                    txtrs200.focus()
                    txtrs200.delete('0', END)
                    entry200.set('')

                elif value200.get() ==0:
                    txtrs200.configure(state=DISABLED)
                    entry200.set('0')

            def check_rs100():
                if value100.get() == 1:
                    txtrs100.configure(state=NORMAL)
                    txtrs100.focus()
                    txtrs100.delete('0', END)
                    entry100.set('')
                elif value100.get() ==0:
                    txtrs100.configure(state=DISABLED)
                    entry100.set('0')

            def check_rs50():
                if value50.get() == 1:
                    txtrs50.configure(state=NORMAL)
                    txtrs50.focus()
                    txtrs50.delete('0', END)
                    entry50.set('')
                elif value50.get() ==0:
                    txtrs50.configure(state=DISABLED)
                    entry50.set('0')

            def check_rs25():
                if value25.get() == 1:
                    txtrs25.configure(state=NORMAL)
                    txtrs25.focus()
                    txtrs25.delete('0', END)
                    entry25.set('')
                elif value25.get() ==0:
                    txtrs25.configure(state=DISABLED)
                    entry25.set('0')


            txtrs1000 = Entry(amount,font=('Time New Roman', 11), bd=8, width=6, justify=LEFT, state=DISABLED,
                               textvariable=entry1000)
            txtrs1000.grid(row=0, column=2, padx=10)

            txtrs500 = Entry(amount, font=('Time New Roman', 11), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=entry500)
            txtrs500.grid(row=1, column=2, padx=10)
            txtrs200 = Entry(amount, font=('Time New Roman', 11), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=entry200)
            txtrs200.grid(row=2, column=2, padx=10)
            txtrs100 = Entry(amount, font=('Time New Roman', 11), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=entry100)
            txtrs100.grid(row=3, column=2, padx=10)
            txtrs50 = Entry(amount, font=('Time New Roman', 11), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=entry50)
            txtrs50.grid(row=4, column=2, padx=10)
            txtrs25 = Entry(amount, font=('Time New Roman', 11), bd=8, width=6, justify=LEFT, state=DISABLED,
                              textvariable=entry25)
            txtrs25.grid(row=5, column=2, padx=10)

            text_amount = Entry(amount, font=('Time New Roman', 11), bd=8, width=10, justify=LEFT, state=DISABLED,
                              textvariable=amount_paid)
            text_amount.grid(row=6, column=2, padx=10)


            rs1000 = Checkbutton(amount, text='Rs.1000', variable = value1000, onvalue=1, offvalue=0,
                                 font=('Time New Roman', 11), bg='white', fg='black', command=check_rs1000)
            rs1000.grid(row=0, column=1,sticky=W)
            rs500 = Checkbutton(amount, text='Rs.500', variable=value500, onvalue=1, offvalue=0,
                                 font=('Time New Roman', 11), bg='white', fg='black', command=check_rs500)
            rs500.grid(row=1, column=1,sticky=W)
            rs200 = Checkbutton(amount, text='Rs.200', variable=value200, onvalue=1, offvalue=0,
                                 font=('Time New Roman', 11), bg='white', fg='black', command=check_rs200)
            rs200.grid(row=2, column=1,sticky=W)
            rs100 = Checkbutton(amount, text='Rs.100', variable=value100, onvalue=1, offvalue=0,
                                 font=('Time New Roman', 11), bg='white', fg='black', command=check_rs100)
            rs100.grid(row=3, column=1,sticky=W)
            rs50 = Checkbutton(amount, text='Rs.50', variable=value50, onvalue=1, offvalue=0,
                                 font=('Time New Roman', 11), bg='white', fg='black',command=check_rs50)
            rs50.grid(row=4, column=1,sticky=W)
            rs25 = Checkbutton(amount, text='Rs.25', variable=value25, onvalue=1, offvalue=0,
                                 font=('Time New Roman', 11), bg='white', fg='black', command=check_rs25)
            rs25.grid(row=5, column=1,sticky=W)

            amount_entered = Label(amount, text='Amount entered: Rs.',font=('Time New Roman', 11,'bold'), bg='white',
                                   fg='black')
            amount_entered.grid(row=6, column=1, pady=20)
            check_amount_btn = Button(amount, text="Check Amount", fg='White', bg='Black', height=2,
                                font=("time new roman", 11, "bold"), bd=7, width=12, relief=GROOVE, command=total)
            check_amount_btn.grid(row=7, column=1, columnspan=2)

            cancel_btn = Button(amount, text="Cancel", fg='White', bg='Black', height=2,
                               font=("time new roman", 11, "bold"), bd=7, width=7, relief=GROOVE, command=cancel_cash)
            cancel_btn.grid(row=7, column=0, columnspan=1, sticky=W)

            confirm_btn = Button(amount, text="Confirm", fg='White', bg='Black', height=2,
                               font=("time new roman", 11, "bold"), bd=7, width=7, relief=GROOVE, command=confirm)
            confirm_btn.grid(row=7, column=3, sticky=W)



        def card():
            window = Toplevel(bg='white', width=50, height=200)
            window.geometry('400x460')
            window.config(bg='black')
            window.resizable(0,0)

            def confirm_card():
                confirmation = tkinter.messagebox.askyesno('Confirmation', 'Are you sure you want to confirm the payment?')
                if confirmation == 1:
                    if pin.get() == '0000':
                        tkinter.messagebox.showinfo('Payment Done', f'Payment and Order confirmed.'
                                                                    f'\nThank You, Have a good Day!')

                        with open('order.csv', 'r') as order_file:
                            content = csv.reader(order_file)
                            list_order = list(content)

                        client_message = pickle.dumps(list_order)
                        client_socket.send(client_message)
                        from_server = client_socket.recv(1024)
                        print(from_server.decode())
                        window.destroy()


                        master.switch_frame(Welcome)
                    else:
                        tkinter.messagebox.showerror('Error', 'Pin invalid. Try again')
                        card()

            def cancel_card():
                window.destroy()

            payment_type = Label(window, text='Payment by Card: ', font=('Arial Black', 15, 'bold'), fg='white',
                                 bg='black')
            payment_type.grid(row=0, column=1, pady=20)

            display_amount = Label(window, text='Total Price: ', font=('Arial Black', 11, 'bold'), fg='white',
                                   bg='black')
            display_amount.grid(row=2, column=0)

            price = IntVar()
            price.set(total_amount)

            total_price_display = Entry(window, font=("time new roman", 12, "bold"), textvariable=price, state=DISABLED,
                                        width=10)
            total_price_display.grid(row=2, column=2)

            display = LabelFrame(window, font=('Arial Black', 15, 'bold'), bg='white', relief=GROOVE, fg='black')
            display.grid(row=3, columnspan=3, pady=20)

            message_pin = Label(display, text='Kindly enter your pin. \n(4 digits)', font=('Time New Roman', 11, 'bold'),
                                bg='white', fg='black')
            message_pin.grid(row=0, column=1, pady=20)

            pin = StringVar()
            pin_entry = Entry(display, font=('Time New Roman', 11), bd=8, width=10, justify=LEFT,textvariable=pin)
            pin_entry.grid(row=1, column=1, padx=10, pady=10)

            button_frame = LabelFrame(window, font=('Arial Black', 15, 'bold'), bg='white', relief=GROOVE, fg='black')
            button_frame.grid(row=4, columnspan=3, pady=20)

            cancel_btn = Button(button_frame, text="Cancel", fg='White', bg='Black', height=2,
                                font=("time new roman", 11, "bold"), bd=7, width=12, relief=GROOVE, command=cancel_card)
            cancel_btn.grid(row=0, column=0, columnspan=1, sticky=W, pady=20, padx=30)

            confirm_btn = Button(button_frame, text="Confirm", fg='White', bg='Black', height=2,
                                 font=("time new roman", 11, "bold"), bd=7, width=12, relief=GROOVE, command=confirm_card)
            confirm_btn.grid(row=0, column=3, sticky=W,pady=20, padx=30)



        payment_type_selection = LabelFrame(self, text='Payment type selection', font=('Arial Black',12,'bold'), bd=5,
                                            relief=GROOVE, bg='white', fg='black')
        payment_type_selection.pack(pady=30, fill=X)
        label = Label(payment_type_selection, bg='white')
        label.pack(pady=10)
        message = Label(label, text='Select the payment type:', font=('Arial Black', 12, 'bold'),
                      bd=5, bg='white', fg='black')
        message.pack(pady=10)
        cash_button = Button(label, text="CASH", bg='White', fg='Black', height=2,
                               font=("time new roman", 12, "bold"), bd=7, width=10, relief=GROOVE, command=cash)
        cash_button.pack(side=LEFT)
        card_button = Button(label, text="CARD", bg='White', fg='Black', height=2,
                             font=("time new roman", 12, "bold"), bd=7, width=10, relief=GROOVE, command=card)
        card_button.pack(side=RIGHT)

        def cancel():
            icancel = tkinter.messagebox.askyesno('Cancel', 'Are you sure you want to exit?')
            if icancel > 0:
                window = Toplevel(bg='white', width=50, height=200)
                window.geometry('600x900')
                window.config(bg='black')
                apology = Label(window, text='Sorry, we could not provide \nyou with your choice today.'
                                             '\nWe hope to see you soon again.\n Thank you! \nHave a good day!',
                                font=('time mew roman', 20, 'bold'))
                apology.pack(pady=250)

                def home():
                    master.switch_frame(Welcome)
                    window.destroy()

                home = Button(window, text='Home', bg='White', fg='Black', font=("time new roman", 12, "bold"),
                              bd=7, relief=GROOVE, command=home)
                home.pack(ipadx=10)

        btn_frame = Label(payment_type_selection, bg='white')
        btn_frame.pack()

        cancel_button = Button(btn_frame, text="Cancel", bg='White', fg='Black', height=2,
                               font=("time new roman", 12, "bold"), bd=7, width=20, relief=GROOVE, command=cancel)
        cancel_button.pack(side =LEFT)


# class to login (Admin)
class Admin_Page1(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.title("Login System")
        self.master.geometry("600x900")

        # icons
        self.username_icon = PhotoImage(file='user-icon.png')
        self.password_icon = PhotoImage(file='password-icon.png')
        # variables
        self.username = StringVar()
        self.password = StringVar()

        title = Label(self, text="Login System", font=('Time New Romans', 30, 'bold'))
        title.grid(pady=120)

        login_frame = Frame(self, bg='white')
        login_frame.grid()

        user_label = Label(login_frame, text="Username : ", image=self.username_icon, compound=LEFT, bg="white",
                           font=('Time New Romans', 15, 'bold'))
        user_label.grid(row=0, column=0, pady=20)
        username_entry = Entry(login_frame, bd=5, relief=GROOVE, font=('Time New Romans', 15), textvariable=self.username)
        username_entry.grid(row=0, column=1, pady=20)

        password_label = Label(login_frame, text="Password : ", image=self.password_icon, compound=LEFT, bg="white",
                               font=('Time New Romans', 15, 'bold'))
        password_label.grid(row=1, column=0, pady=20)
        password_entry = Entry(login_frame, bd=5, relief=GROOVE, font=('Time New Romans', 15), textvariable=self.password)
        password_entry.grid(row=1, column=1, pady=20)

        login_button = Button(login_frame, text="Login", width=15, font=('Time New Romans', 15, 'bold'), bg="Black",
                              fg="white", command=self.login)
        login_button.grid(row=3, column=1, pady=20)
    # login function
    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            tkinter.messagebox.showerror("Error", "Login details are required")
        elif self.username.get() == "Admin" and self.password.get() == "1234":
            self.master.switch_frame(Admin_Page2)
        else:
            tkinter.messagebox.showerror("Error", "Invalid username or password")


# class to display the options either the admin wants to check the stock or have a look at the reports (pie charts)
class Admin_Page2(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")
        message = Label(self, text='What would you like to do?', font=('Time New Romans', 30, 'bold'), fg='white',
                        bg='black')
        message.pack(pady=80)

        stock_button = Button(self, text='Stock', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                              width=20, height=2, command=lambda: master.switch_frame(Stock))
        stock_button.pack(pady=50)

        report_button = Button(self, text='Report', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                               width=20, height=2, command=lambda: master.switch_frame(Report))
        report_button.pack(pady=50)

        Cancel_button = Button(self, text='Cancel', font=('Time New Romans', 15, 'bold'), fg='black', bg='white',
                               width=30, height=2, command=lambda: master.cancel())
        Cancel_button.pack(pady=70)


# class to display the stock
class Stock(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("776x700")
        self.master.title('Stock')

        main_frame = Frame(self, bd=10, width=770, height=700, relief=RIDGE, bg='black')
        main_frame.grid()

        title = Frame(main_frame, bd=7, width=770, height=100, relief=RIDGE, bg='white')
        title.grid(row=0, column=0)
        top = Frame(main_frame, bd=5, width=770, height=500, relief=RIDGE, bg='white')
        top.grid(row=1, column=0)

        left = Frame(top, bd=5, width=770, height=400, relief=RIDGE, bg='black', padx=2)
        left.pack(side=LEFT)
        left1 = Frame(left, bd=5, width=600, height=180, relief=RIDGE, bg='white', padx=2, pady=4)
        left1.pack(side=TOP, padx=0, pady=0)

        right = Frame(top, bd=5, width=100, height=400, relief=RIDGE, bg='black', padx=2)
        right.pack(side=RIGHT)
        right1 = Frame(right, bd=5, width=90, height=380, relief=RIDGE, bg='white', padx=2, pady=2)
        right1.pack(side=TOP, padx=0, pady=0)

        # Variables
        product_id = StringVar()
        product_name = StringVar()
        product_price = StringVar()
        product_quantity = StringVar()

        self.title = Label(title, font=('Time New Romans', 40, 'bold'), text='STOCK', bd=7, bg='white')
        self.title.grid(row=0, column=0, padx=130)

        self.productID = Label(left1, font=('Time New Romans', 12, 'bold'), text='Product ID', bd=7, bg='white')
        self.productID.grid(row=1, column=0, sticky=W, padx=5)
        self.productID_entry = Entry(left1, textvariable=product_id, font=('Time New Romans', 12, 'bold'), bd=5,
                                     width=44, justify='left')
        self.productID_entry.grid(row=1, column=1, sticky=W, padx=5)

        self.productName = Label(left1, font=('Time New Romans', 12, 'bold'), text='Product Name', bd=7, bg='white')
        self.productName.grid(row=2, column=0, sticky=W, padx=5)
        self.productName_entry = Entry(left1, textvariable=product_name, font=('Time New Romans', 12, 'bold'), bd=5,
                                       width=44, justify='left')
        self.productName_entry.grid(row=2, column=1, sticky=W, padx=5)

        self.productPrice = Label(left1, font=('Time New Romans', 12, 'bold'), text='Product Price', bd=7, bg='white')
        self.productPrice.grid(row=3, column=0, sticky=W, padx=5)
        self.productPrice_entry = Entry(left1, textvariable=product_price, font=('Time New Romans', 12, 'bold'), bd=5,
                                        width=44, justify='left')
        self.productPrice_entry.grid(row=3, column=1, sticky=W, padx=5)

        self.quantity = Label(left1, font=('Time New Romans', 12, 'bold'), text='Quantity', bd=7, bg='white')
        self.quantity.grid(row=4, column=0, sticky=W, padx=5)
        self.quantity_entry = Entry(left1, textvariable=product_quantity, font=('Time New Romans', 12, 'bold'), bd=5,
                                    width=44, justify='left')
        self.quantity_entry.grid(row=4, column=1, sticky=W, padx=5)
        # Table Treeview
        scroll = Scrollbar(left, orient=VERTICAL)
        # creating a Treeview table
        self.product_record = ttk.Treeview(left, height=12, columns=('p_id', 'p_name', 'p_price', 'p_quantity'),
                                           yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT, fill=Y)
        # assigning headers to each column
        self.product_record.heading('p_id', text="Product ID")
        self.product_record.heading('p_name', text="Product Name")
        self.product_record.heading('p_price', text="Product Price")
        self.product_record.heading('p_quantity', text="Product Quantity")
        # displaying the headers
        self.product_record['show'] = 'headings'
        # size of each column
        self.product_record.column('p_id', width=80)
        self.product_record.column('p_name', width=120)
        self.product_record.column('p_price', width=80)
        self.product_record.column('p_quantity', width=80)
        # displaying the table
        self.product_record.pack(fill=BOTH, expand=1)

        # filling the table by using the file 'product.csv
        with open('Product.csv') as product_file:
            read = csv.DictReader(product_file, delimiter=',')
            for row in read:
                product_id = row['Product_ID']
                product_name = row['Product_Name']
                product_price = row['Product_Price']
                product_quantity = row['Product_Quantity']
                self.product_record.insert("", 0, values=(product_id, product_name, product_price, product_quantity))

        # Button behaviours
        def exit():
            iexit = tkinter.messagebox.askyesno("Exit", "Confirm if you want to exit")
            if iexit > 0:
                self.destroy()
                self.master.switch_frame(Admin_Page2)

        def reset():
            self.productID_entry.delete(0, END)
            self.productName_entry.delete(0, END)
            self.productPrice_entry.delete(0, END)
            self.quantity_entry.delete(0, END)

        def remove_all():
            for record in self.product_record.get_children():
                self.product_record.delete(record)

        def selected_record():
            self.productID_entry.delete(0, END)
            self.productName_entry.delete(0, END)
            self.productPrice_entry.delete(0, END)
            self.quantity_entry.delete(0, END)

            selected = self.product_record.focus()
            values = self.product_record.item(selected, 'values')

            self.productID_entry.insert(0, values[0])
            self.productName_entry.insert(0, values[1])
            self.productPrice_entry.insert(0, values[2])
            self.quantity_entry.insert(0, values[3])

        def update():
            selected = self.product_record.focus()
            self.product_record.item(selected, text="",
                                     values=(self.productID_entry.get(), self.productName_entry.get(),
                                             self.productPrice_entry.get(), self.quantity_entry.get()))
            self.productID_entry.delete(0, END)
            self.productName_entry.delete(0, END)
            self.productPrice_entry.delete(0, END)
            self.quantity_entry.delete(0, END)

        def delete():
            value = self.product_record.selection()[0]
            self.product_record.delete(value)

        def save():
            with open('Product.csv', 'w', newline='') as file:
                writer = csv.writer(file, delimiter=',')
                file.write('Product_ID,Product_Name,Product_Price,Product_Quantity\n')
                for row_id in self.product_record.get_children():
                    row2 = self.product_record.item(row_id)['values']
                    writer.writerow(row2)
                tkinter.messagebox.showinfo("Save to CSV file", "File was saved")
        # Buttons
        self.delete = Button(right1, font=('Time New Romans', 12, 'bold'), text='Delete', bd=5, pady=1, padx=25,
                             width=6, height=2, command=delete)
        self.delete.grid(row=1, column=0, padx=1)

        self.remove_all = Button(right1, font=('Time New Romans', 12, 'bold'), text='Remove All', bd=5, pady=1, padx=25,
                                 width=6, height=2, command=remove_all)
        self.remove_all.grid(row=2, column=0, padx=1)
        self.update = Button(right1, font=('Time New Romans', 12, 'bold'), text='Update', bd=5, pady=1, padx=25,
                             width=6, height=2, command=update)
        self.update.grid(row=3, column=0, padx=1)

        self.select = Button(right1, font=('Time New Romans', 12, 'bold'), text='Select', bd=5, pady=1, padx=25,
                             width=6, height=2, command=selected_record)
        self.select.grid(row=4, column=0, padx=1)

        self.reset = Button(right1, font=('Time New Romans', 12, 'bold'), text='Reset', bd=5, pady=1, padx=25,
                            width=6, height=2, command=reset)
        self.reset.grid(row=5, column=0, padx=1)

        self.save = Button(right1, font=('Time New Romans', 12, 'bold'), text='Save / Export', bd=5, pady=1, padx=25,
                           width=6, height=2, command=save)
        self.save.grid(row=6, column=0, padx=1)

        self.exit = Button(right1, font=('Time New Romans', 12, 'bold'), text='Exit', bd=5, pady=1, padx=25,
                           width=6, height=2, command=exit)
        self.exit.grid(row=7, column=0, padx=1)


# class to display different options for the report
class Report(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        question_1 = Label(self, text='What would you like\n to check?', font=('Time New Romans', 30, 'bold'), fg='white',
                           bg='Black')
        question_1.pack(pady=70)

        drinks_button = Button(self, text='Pie Chart of Drinks', font=('Time New Romans', 14, 'bold'), fg='black',
                               bg='white', width=20, height=2, command=lambda: master.switch_frame(Pie_Chart_Drinks))
        drinks_button.pack(pady=20)

        Snacks_button = Button(self, text='Pie Chart of Snacks', font=('Time New Romans', 14, 'bold'), fg='black',
                               bg='white', width=20, height=2, command=lambda: master.switch_frame(Pie_Chart_Snacks))
        Snacks_button.pack(pady=20)

        Chocolates_button = Button(self, text='Pie Chart of Chocolates', font=('Time New Romans', 14, 'bold'),
                                   bg='white', width=20, height=2, command=lambda: master.switch_frame(Pie_Chart_Chocolates))
        Chocolates_button.pack(pady=20)

        Cancel_button = Button(self, text='Cancel', font=('Time New Romans', 12, 'bold'), fg='black', bg='white',
                               width=30, height=2, command=lambda: master.cancel())
        Cancel_button.pack(pady=50)
        go_back_button = Button(self, text='Go Back', font=('Time New Romans', 12, 'bold'), fg='black', bg='white',
                               width=30, height=2, command=lambda: master.switch_frame(Admin_Page2))
        go_back_button.pack()


# class to display the report for Drinks, using Matplotlib library
class Pie_Chart_Drinks(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        frame1 = LabelFrame(self,text='Available Drinks', font=('Time New Roman', 15, 'bold'), fg='gold', bg='black',
                            height=50)
        frame1.pack(pady=40)
        # from file 'product.csv' creating another file 'Drinks.csv' that will contain only drinks
        with open('Product.csv', 'r') as file_in, open('Drink.csv', 'w') as file_out:
            reader = csv.reader(file_in)
            writer = csv.writer(file_out)
            file_out.write('Product_ID,Product_Name,Product_Price,Product_Quantity')
            file_out.write('\r\n')
            for counter, row in enumerate(reader):
                if counter < 11: continue
                if counter > 15: break
                writer.writerow(row)


        def autospt(percentage, quantity):
            absolute_value = int(percentage / 100. * np.sum(quantity))
            return "{:.1f}%\n({:d} items)".format(percentage, absolute_value)
        #analizing datas
        data = pd.read_csv('Drink.csv')
        drinks = data['Product_Name']
        quantity = data['Product_Quantity']

        figure = Figure()
        figure.patch.set_facecolor('white')

        ax = figure.add_subplot(111)

        colors = ['blue', 'green', 'orange', 'red', 'grey']
        ax.pie(quantity, labels=drinks, colors=colors, autopct=lambda percentage: autospt(percentage, quantity),
               startangle=140)
        canvas = FigureCanvasTkAgg(figure, master = frame1)
        # drawing the pie chart
        canvas.draw()
        # displaying the pie chart
        canvas.get_tk_widget().pack()

        frame2 = LabelFrame(self,text='Buttons', font=('Time New Roman', 10, 'bold'), fg='Black', bg='white', height=50)
        frame2.pack(pady=40, fill=BOTH, expand=1)
        # buttons
        snacks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Pie Chart Snacks', bd=5, pady=1, padx=25,
                           width=12, height=2, bg='Black', fg='White',
                        command=lambda: master.switch_frame(Pie_Chart_Snacks))
        snacks.grid(row=0, column=0, padx=3)

        chocolates = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Pie Chart Chocolates', bd=5, pady=1,
                            padx=25,
                        width=12, height=2, bg='Black', fg='White',
                            command=lambda: master.switch_frame(Pie_Chart_Chocolates))
        chocolates.grid(row=0, column=1, padx=5)

        stocks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Check Stock', bd=5, pady=1, padx=25,
                        width=12, height=2, bg='Black', fg='White',
                        command=lambda: master.switch_frame(Stock))
        stocks.grid(row=0, column=2, padx=2)

        go_back = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Go back', bd=5, pady=1, padx=25,
                        width=10, height=2, bg='Black', fg='White',
                         command=lambda: master.switch_frame(Report))
        go_back.grid(row=1, column=0, columnspan=2, padx=1, pady=10)

        exit = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Exit', bd=5, pady=1, padx=25,
                         width=10, height=2, bg='Black', fg='White', command=lambda: master.cancel())
        exit.grid(row=1, column=1, columnspan=2, padx=1, pady=10)


# class to display the report for Snacks, using Matplotlib library
class Pie_Chart_Snacks(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        frame1 = LabelFrame(self,text='Available Snacks', font=('Time New Roman', 15, 'bold'), fg='gold', bg='black', height=50)
        frame1.pack(pady=40)
        # from file 'product.csv' creating another file 'Snacks.csv' that will contain only snacks
        with open('Product.csv', 'r') as file_in, open('Snacks.csv', 'w', newline='') as file_out:
            reader = csv.reader(file_in)
            writer = csv.writer(file_out)
            file_out.write('Product_ID,Product_Name,Product_Price,Product_Quantity')
            file_out.write('\r\n')
            for counter, row in enumerate(reader):
                if counter < 6: continue
                if counter > 10: break

                writer.writerow(row)


        def autospt(percentage, quantity):
            absolute_value = int(percentage / 100. * np.sum(quantity))
            return "{:.1f}%\n({:d} items)".format(percentage, absolute_value)
        # analizing datas
        data = pd.read_csv('Snacks.csv')
        snacks = data['Product_Name']
        quantity = data['Product_Quantity']

        figure = Figure()
        figure.patch.set_facecolor('white')

        ax = figure.add_subplot(111)

        colors = ['blue', 'green', 'orange', 'red', 'grey']
        ax.pie(quantity, labels=snacks, colors=colors,autopct=lambda percentage:autospt(percentage,quantity), startangle=140)
        canvas = FigureCanvasTkAgg(figure, master = frame1)
        # drawing the pie chart
        canvas.draw()
        # displaying the pie chart
        canvas.get_tk_widget().pack()

        frame2 = LabelFrame(self,text='Buttons', font=('Time New Roman', 10, 'bold'), fg='Black', bg='white', height=50)
        frame2.pack(pady=40, fill=BOTH, expand=1)
        #buttons
        drinks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Pie Chart Drinks', bd=5, pady=1, padx=25,
                           width=12, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Pie_Chart_Drinks))
        drinks.grid(row=0, column=0, padx=3)

        chocolates = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Pie Chart Chocolate', bd=5, pady=1, padx=25,
                        width=12, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Pie_Chart_Chocolates))
        chocolates.grid(row=0, column=1, padx=5)

        stocks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Check Stock', bd=5, pady=1, padx=25,
                        width=12, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Stock))
        stocks.grid(row=0, column=2, padx=2)

        go_back = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Go back', bd=5, pady=1, padx=25,
                        width=10, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Report))
        go_back.grid(row=1, column=0, columnspan=2, padx=1, pady=10)

        exit = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Exit', bd=5, pady=1, padx=25,
                         width=10, height=2, bg='Black', fg='White', command=lambda: master.cancel())
        exit.grid(row=1, column=1, columnspan=2, padx=1, pady=10)


# class to display the report for Chocolates, using Matplotlib library
class Pie_Chart_Chocolates(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(bg='Black')
        self.master.geometry("600x900")

        frame1 = LabelFrame(self,text='Available Chocolates', font=('Time New Roman', 15, 'bold'), fg='gold', bg='black', height=50)
        frame1.pack(pady=40)
        # from file 'product.csv' creating another file 'Chocolates.csv' that will contain only chocolates
        with open('Product.csv', 'r') as file_in, open('Chocolates.csv', 'w') as file_out:
            reader = csv.reader(file_in)
            writer = csv.writer(file_out)

            for counter, row in enumerate(reader):
                if counter < 0: continue
                if counter > 5: break
                writer.writerow(row)

        def autospt(percentage, quantity):
            absolute_value = int(percentage / 100. * np.sum(quantity))
            return "{:.1f}%\n({:d} items)".format(percentage, absolute_value)
        # analizing datas
        data = pd.read_csv('Chocolates.csv')
        chocolates = data['Product_Name']
        quantity = data['Product_Quantity']

        figure = Figure()
        figure.patch.set_facecolor('white')

        ax = figure.add_subplot(111)

        colors = ['blue', 'green', 'orange', 'red', 'grey']
        ax.pie(quantity, labels=chocolates, colors=colors, autopct=lambda percentage:autospt(percentage,quantity), startangle=140)
        canvas = FigureCanvasTkAgg(figure, master = frame1)
        # drawing the pie chart
        canvas.draw()
        # diplaying the pie chart
        canvas.get_tk_widget().pack()

        frame2 = LabelFrame(self,text='Buttons', font=('Time New Roman', 10, 'bold'), fg='Black', bg='white', height=50)
        frame2.pack(pady=40, fill=BOTH, expand=1)
        # buttons
        drinks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Pie Chart Drinks', bd=5, pady=1, padx=25,
                           width=12, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Pie_Chart_Drinks))
        drinks.grid(row=0, column=0, padx=3)

        snacks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Pie Chart Snacks', bd=5, pady=1, padx=25,
                        width=12, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Pie_Chart_Snacks))
        snacks.grid(row=0, column=1, padx=5)

        stocks = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Check Stock', bd=5, pady=1, padx=25,
                        width=12, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Stock))
        stocks.grid(row=0, column=2, padx=2)

        go_back = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Go back', bd=5, pady=1, padx=25,
                        width=10, height=2, bg='Black', fg='White', command=lambda: master.switch_frame(Report))
        go_back.grid(row=1, column=0, columnspan=2, padx=1, pady=10)

        exit = Button(frame2, font=('Time New Romans', 12, 'bold'), text='Exit', bd=5, pady=1, padx=25,
                         width=10, height=2, bg='Black', fg='White', command=lambda: master.cancel())
        exit.grid(row=1, column=1, columnspan=2, padx=1, pady=10)


# executing the code when we run the program
if __name__ == "__main__":
    app = Application()
    app.mainloop()
