from tkinter import *
from tkinter import messagebox
from csv import *
import random

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x300+0+0")
        self.root.maxsize(width = 1280,height = 650)
        self.root.minsize(width = 1280,height = 650)
        self.root.title("Le Cafe")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))

        self.burger = IntVar()
        self.tacos = IntVar()
        self.pizza = IntVar()
        self.hotdog = IntVar()
        self.sandwich = IntVar()
        self.shakes = IntVar()
        self.beverages = IntVar()
        self.juice = IntVar()
        self.mojito = IntVar()
        self.coffee = IntVar()
        self.nachos = IntVar()
        self.fries = IntVar()
        self.nuggets = IntVar()
        self.pasta = IntVar()
        self.biscuits = IntVar()
        self.total_mains = StringVar()
        self.total_drinks = StringVar()
        self.total_sides = StringVar()
        self.tax_mains = StringVar()
        self.tax_drinks = StringVar()
        self.tax_sides = StringVar()


        #=================================== dodger blue
        bg_color = "dodger blue"
        fg_color = "black"
        lbl_color = 'black'
        #Title of App
        title = Label(self.root,text = "LE CAFE",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("Algerian",28,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "black",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 10,y = 80,relwidth = 1)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        def cname():
            global cname_en
            cname_en= Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname()
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 20)
        def cphn():
            global cphon_en
            cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphn()
        cphon_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 4,padx = 20)
        def billno():
            global cbill_en
            cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        billno()
        
        cbill_en.grid(row = 0,column = 5,ipadx = 30,ipady = 4,pady = 5)
        
        #==================Mains Frame=====================#
        F2 = LabelFrame(self.root,text = 'Mains',bd = 10,relief = GROOVE,bg = bg_color,fg = "black",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 180,width = 325,height = 300)

        #===========Frame Content
        burg_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Burger")
        burg_lbl.grid(row = 0,column = 0,padx = 2,pady = 10)
        burg_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.burger)
        burg_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======tacos
        tac_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Tacos")
        tac_lbl.grid(row = 1,column = 0,padx = 12,pady = 10)
        tac_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.tacos)
        tac_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Hamburger
        piz_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pizza")
        piz_lbl.grid(row = 2,column = 0,padx = 2,pady = 10)
        piz_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.pizza)
        piz_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hotdog
        hd_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hotdog")
        hd_lbl.grid(row = 3,column = 0,padx = 2,pady = 10)
        hd_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hotdog)
        hd_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Sandwich
        sw_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
        sw_lbl.grid(row = 4,column = 0,padx = 2,pady = 10)
        sw_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sandwich)
        sw_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Drinks Frame=====================#
        F2 = LabelFrame(self.root,text = 'Drinks',bd = 10,relief = GROOVE,bg = bg_color,fg = "black",font = ("times new roman",13,"bold"))
        F2.place(x = 330,y = 180,width = 325,height = 300)

        #===========Frame Content
        sha_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Shakes")
        sha_lbl.grid(row = 0,column = 0,padx = 2,pady = 10)
        sha_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.shakes)
        sha_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        bev_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Beverages")
        bev_lbl.grid(row = 1,column = 0,padx = 2,pady = 10)
        bev_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.beverages)
        bev_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        jui_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Juice")
        jui_lbl.grid(row = 2,column = 0,padx = 2,pady = 10)
        jui_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.juice)
        jui_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        moj_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Mojito")
        moj_lbl.grid(row = 3,column = 0,padx = 2,pady = 10)
        moj_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.mojito)
        moj_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        coff_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coffee")
        coff_lbl.grid(row = 4,column = 0,padx = 2,pady = 10)
        coff_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coffee)
        coff_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Sides Frame=====================#

        F2 = LabelFrame(self.root,text = 'Sides',bd = 10,relief = GROOVE,bg = bg_color,fg = "black",font = ("times new roman",13,"bold"))
        F2.place(x = 655,y = 180,width = 325,height = 300)

        #===========Frame Content
        nach_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nachos")
        nach_lbl.grid(row = 0,column = 0,padx = 2,pady = 10)
        nach_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.nachos)
        nach_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        fries_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Fries")
        fries_lbl.grid(row = 1,column = 0,padx = 2,pady = 10)
        fries_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.fries)
        fries_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        nugg_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Nuggets")
        nugg_lbl.grid(row = 2,column = 0,padx = 2,pady = 10)
        nugg_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.nuggets)
        nugg_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        pasta_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Pasta")
        pasta_lbl.grid(row = 3,column = 0,padx = 2,pady = 10)
        pasta_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.pasta)
        pasta_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 2,pady = 10)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #===================Bill Area================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 180,width = 325,height =300)
        #===========
        bill_title = Label(F3,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "black",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 495,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Mains")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        def mains():
            global cosm_en
            cosm_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_mains)
        mains()
        cosm_en.grid(row = 0,column = 1,ipady = 2,ipadx = 5)

        #===================
        totd_lbl  = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Drinks")
        totd_lbl .grid(row = 1,column = 0,padx = 10,pady = 5)
        def drinks():
            global totd_en
            totd_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_drinks)
        drinks()
        totd_en.grid(row = 1,column = 1,ipady = 2,ipadx = 5)

        #================
        tots_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Sides")
        tots_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        def sides():
            global tots_en
            tots_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.total_sides)
        sides()
        tots_en.grid(row = 2,column = 1,ipady = 2,ipadx = 5)

        #================
        mtax_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Mains Tax")
        mtax_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        mtax_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_mains)
        mtax_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        dtax_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Drinks Tax")
        dtax_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        dtax_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_drinks)
        dtax_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        dtax_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sides Tax")
        dtax_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        dtax_en = Entry(F4,bd = 8,relief = GROOVE,textvariable = self.tax_sides)
        dtax_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 10,padx = 20)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 10)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 10,padx = 20)

        #======================
        exit_btn = Button(F4,text = "Exit",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 11,ipadx =10,padx = 10)

        #======================
        save_btn = Button(F4,text = "Save data",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.Add)
        save_btn.grid(row = 1,column = 7,ipadx = 10,padx = 10)

#Function to get total prices
    def total(self):
        #=================Total Mains Prices
        self.total_mains_prices = (
            (self.burger.get() * 150)+
            (self.tacos.get() * 100)+
            (self.pizza.get() * 200)+
            (self.hotdog.get() * 130)+
            (self.sandwich.get() * 100)
        )
        self.total_mains.set("₹"+str(self.total_mains_prices))
        self.tax_mains.set("₹"+str(round(self.total_mains_prices*0.05)))
        #====================Total Drinks Prices
        self.total_drinks_prices = (
            (self.shakes.get()*80)+
            (self.beverages.get() * 50)+
            (self.juice.get() * 40)+
            (self.mojito.get() *90)+
            (self.coffee.get() * 70)

        )
        self.total_drinks.set("₹"+str(self.total_drinks_prices))
        self.tax_drinks.set("₹"+str(round(self.total_drinks_prices*0.05)))
        #======================Total Sides Prices
        self.total_sides_prices = (
            (self.nachos.get() * 100)+
            (self.fries.get() * 70)+
            (self.nuggets.get() * 80)+
            (self.pasta.get() * 120)+
            (self.biscuits.get() * 50)
        )
        self.total_sides.set("₹"+str(self.total_sides_prices))
        self.tax_sides.set("₹"+str(round(self.total_sides_prices*0.05)))


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Our Cafe\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================")

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.welcome_soft()
        if self.burger.get() != 0:
            self.txt.insert(END,f"\nBurger             {self.burger.get()}           {self.burger.get() * 150}")
        if self.tacos.get() != 0:
            self.txt.insert(END,f"\nTacos              {self.tacos.get()}           {self.tacos.get() * 100}")
        if self.pizza.get() != 0:
            self.txt.insert(END,f"\nPizza              {self.pizza.get()}           {self.pizza.get() * 200}")
        if self.hotdog.get() != 0:
            self.txt.insert(END,f"\nHotdog             {self.hotdog.get()}           {self.hotdog.get() * 130}")
        if self.sandwich.get() != 0 :
            self.txt.insert(END,f"\nSandwich           {self.sandwich.get()}           {self.sandwich.get() * 100}")
        if self.shakes.get() != 0:
            self.txt.insert(END,f"\nShakes             {self.shakes.get()}           {self.shakes.get() * 80}")
        if self.beverages.get() != 0:
            self.txt.insert(END,f"\nBeverages          {self.beverages.get()}           {self.beverages.get() * 50}")
        if self.juice.get() != 0:
            self.txt.insert(END,f"\nJuice              {self.juice.get()}           {self.juice.get() * 40}")
        if self.mojito.get() != 0:
            self.txt.insert(END,f"\nMojito             {self.mojito.get()}           {self.mojito.get() * 90}")
        if self.coffee.get() != 0:
            self.txt.insert(END,f"\nCoffee             {self.coffee.get()}           {self.coffee.get() * 70}")
        if self.nachos.get() != 0:
            self.txt.insert(END,f"\nNachos             {self.nachos.get()}           {self.nachos.get() * 100}")
        if self.fries.get() != 0:
            self.txt.insert(END,f"\nFries              {self.fries.get()}           {self.fries.get() * 70}")
        if self.nuggets.get() != 0:
            self.txt.insert(END,f"\nNuggets            {self.nuggets.get()}          {self.nuggets.get() * 80}")
        if self.pasta.get() != 0:
            self.txt.insert(END,f"\nPasta              {self.pasta.get()}           {self.pasta.get() * 120}")
        if self.biscuits.get() != 0:
            self.txt.insert(END,f"\nBiscuits           {self.biscuits.get()}           {self.biscuits.get() * 50}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,f"\n                   Total : ₹{self.total_mains_prices+self.total_drinks_prices+self.total_sides_prices+self.total_mains_prices * 0.05+self.total_drinks_prices * 0.05+self.total_sides_prices * 0.05}")

    

    def Add(self):
        main_lst=[]
        lst=[cname_en.get(),cphon_en.get(),cbill_en.get(),cosm_en.get(),totd_en.get(),tots_en.get(),self.total_mains_prices+self.total_drinks_prices+self.total_sides_prices]
        main_lst.append(lst)
        
        with open("cafe.csv","w", encoding="utf-8") as file:
            Writer=writer(file)
            Writer.writerow(["Customer name" ,"Customer Phoneno.","Bill no.","Mains amount","Drinks amount","Sides amount","Total amount"])
            Writer.writerows(main_lst)
            messagebox.showinfo("Information","Saved succesfully")
        

    def exit(self):
        self.root.destroy()




root = Tk()
object = Bill_App(root)
root.mainloop()