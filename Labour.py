from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector


class Labour:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Labour Management System")


      # Variables
        self.variable_organisation = StringVar()
        self.variable_name = StringVar()
        self.variable_designation = StringVar()
        self.variable_email = StringVar()
        self.variable_address = StringVar()
        self.variable_marital_status = StringVar()
        self.variable_dob = StringVar()
        self.variable_doj = StringVar()
        self.variable_IDproofcombobox = StringVar()
        self.variable_IDproof = StringVar()
        self.variable_gender = StringVar()
        self.variable_phoneno = StringVar()
        self.variable_fathername = StringVar()
        self.variable_pay = StringVar()
        self.variable_paytype = StringVar()



        label_title = Label(self.root,text = 'LABOUR MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        label_title.place(x=0,y=0,width = 1550,height = 50)


        #  logo
        img_logo=Image.open('pics/logo.webp')
        img_logo = img_logo.resize((50,50),Image.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=320,y=0,width = 50,height = 50)

        img_logo1=Image.open('pics/logo.webp')
        img_logo1 = img_logo1.resize((50,50),Image.LANCZOS)
        self.photo_logo1=ImageTk.PhotoImage(img_logo1)

        self.logo1 = Label(self.root,image=self.photo_logo1)
        self.logo1.place(x=1180,y=0,width = 50,height = 50)

        
        # Image Frame
        image_frame = Frame(self.root,bd=2,relief=RIDGE,bg = 'white')
        image_frame.place(x=0,y=50,width=1920,height =160 )


        # 1st
        img1=Image.open('pics/pic4.png')
        img1 = img1.resize((510,160),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        
        self.img_1 = Label(image_frame,image=self.photo1)   
        self.img_1.place(x=0,y=0,width = 510,height = 160)

        #2nd
        img2=Image.open('pics/pic5.jpg')
        img2 = img2.resize((520,160),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        self.img_2 = Label(image_frame,image=self.photo2)
        self.img_2.place(x=510,y=0,width = 520,height = 160)


        #3rd
        img3=Image.open('pics/pic7.webp')
        img3 = img3.resize((520,160),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        self.img3 = Label(image_frame,image=self.photo3)
        self.img3.place(x=1020,y=-1,width = 520,height = 160)

        # main Frame
        main_frame = Frame(self.root,bd=4,relief=RIDGE,bg = 'white')
        main_frame.place(x=11,y=220,width=1510.5,height =560 )

        # Upper Frame
        upper_frame = LabelFrame(main_frame,bd=3,bg='white',relief=RIDGE,text='LABOUR INFORMATION',font=('times new roman',13,'bold'),fg='crimson')
        upper_frame.place(x=10,y=10,width=1480.5,height =270 )

          # Labels and Entry fields(inside upper frame)
        label_organisation = Label(upper_frame,text = 'Organization:',font=('arial',12,'bold'),bg='white')
        label_organisation.grid(row=0,column=0,padx=2,sticky=W)
        combobox_organisation=ttk.Combobox(upper_frame,textvariable=self.variable_organisation,font=('Comic Sans Ms',11,'bold'),width =18,state ='readonly')
        combobox_organisation['value']=('-----Select--------','INFORMATION TECHNOLOGY','TELECOM','HEALTH CARE','INFRASTRUCTURE','RETAIL','AGRICULTURE','FOOD INDUSTRY','CONSTRUCTION','TOURISM','MINING','AVIATION','ELECTRONICS','E-COMMERCE','BIOTECHNOLOGY','FINANCIAL SERVICES','HOSPITALITY INDUSTRY')
        combobox_organisation.current(0)
        combobox_organisation.grid(row=0,column=1,padx =2,pady=10,sticky = W)

            # Name
        label_name =Label(upper_frame,font=('arial',12,'bold'),text='Name:',bg='white')
        label_name.grid(row =0,column =2,sticky=W,padx =2,pady=7)

        txt_name=ttk.Entry(upper_frame,textvariable=self.variable_name,width=19,font=('Comic Sans Ms',11,'bold'))
        txt_name.grid(row=0,column =3,padx =2,pady=7)

            #Designation
        label_designation=Label(upper_frame,font=('arial',12,'bold'),text='Designation:',bg='white')
        label_designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designation=ttk.Entry(upper_frame,textvariable=self.variable_designation,width=20,font=('Comic Sans Ms',11,'bold'))
        txt_Designation.grid(row=1,column =1,sticky=W,padx =2,pady=7)

             #Email
        label_email=Label(upper_frame,font=('arial',12,'bold'),text='Email:',bg='white')
        label_email.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(upper_frame,textvariable=self.variable_email,width=18,font=('Comic Sans Ms',11,'bold'))
        txt_email.grid(row=1,column =5,sticky=W,padx =2,pady=7)


            #Father/Husband name
        label_Father_Husband_name=Label(upper_frame,font=('arial',12,'bold'),text='Father/Husband Name:',bg='white')
        label_Father_Husband_name.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        txt_Father_Husband_name=ttk.Entry(upper_frame,textvariable=self.variable_fathername,width=19,font=('Comic Sans Ms',11,'bold'))
        txt_Father_Husband_name.grid(row=4,column =3,sticky=W,padx =2,pady=7)

          #address
        label_address=Label(upper_frame,font=('arial',12,'bold'),text='Address:',bg='white')
        label_address.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_address=ttk.Entry(upper_frame,textvariable=self.variable_address,width=18,font=('Comic Sans Ms',11,'bold'))
        txt_address.grid(row=2,column =5,sticky=W,padx =2,pady=7)
        


          #Married
        label_Married=Label(upper_frame,font=('arial',12,'bold'),text='Marital Status:',bg='white')
        label_Married.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        combobox_married=ttk.Combobox(upper_frame,textvariable=self.variable_marital_status,state ='readonly',font = ('Comic Sans Ms',11,'bold'),width =17)
        combobox_married['value']=('-----Select--------','Single',"Married","Widowed",'Divorced')
        combobox_married.current(0)
        combobox_married.grid(row = 3,column =3,sticky =W,padx=2,pady =7)

              #DOB
        label_DOB=Label(upper_frame,font=('arial',12,'bold'),text='Date Of Birth:',bg='white')
        label_DOB.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_DOB=ttk.Entry(upper_frame,textvariable=self.variable_dob,width=19,font=('Comic Sans Ms',11,'bold'))
        txt_DOB.grid(row=1,column =3,sticky=W,padx =2,pady=7)


            
              #DOJ
        label_DOJ=Label(upper_frame,font=('arial',12,'bold'),text='Joining Date:',bg='white')
        label_DOJ.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_DOJ=ttk.Entry(upper_frame,textvariable=self.variable_doj,width=20,font=('Comic Sans Ms',11,'bold'))
        txt_DOJ.grid(row=2,column =1,sticky=W,padx =2,pady=7)


        
            
              #Gender
        label_gender=Label(upper_frame,font=('arial',12,'bold'),text='Gender:',bg='white')
        label_gender.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        combobox_gender=ttk.Combobox(upper_frame,textvariable=self.variable_gender,state ='readonly',font = ('Comic Sans Ms',11,'bold'),width =17)
        combobox_gender['value']=('-----Select--------','Male',"Female",'Non-binary','Other:')
        combobox_gender.current(0)
        combobox_gender.grid(row = 2,column =3,sticky =W,padx=2,pady =7)


        
              #phone_no
        label_phone_no=Label(upper_frame,font=('arial',12,'bold'),text='Phone No:',bg='white')
        label_phone_no.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone_no=ttk.Entry(upper_frame,textvariable=self.variable_phoneno,width=18,font=('Comic Sans Ms',11,'bold'))
        txt_phone_no.grid(row=0,column =5,sticky=W,padx =2,pady=7)


               #Id_proof
        combobox_gender=ttk.Combobox(upper_frame,textvariable=self.variable_IDproofcombobox,state ='readonly',font = ('Comic Sans Ms',11,'bold'),width =17)
        combobox_gender['value']=('-Select ID Proof-','PAN CARD',"AADHAR CARD",'DRIVING LICENSE','PASSPORT','VOTER ID CARD')
        combobox_gender.current(0)
        combobox_gender.grid(row = 3,column =4,sticky =W,padx=2,pady =7)

        txt_Id_proof=ttk.Entry(upper_frame,textvariable=self.variable_IDproof,width=18,font=('Comic Sans Ms',11,'bold'))
        txt_Id_proof.grid(row=3,column =5,sticky=W,padx =2,pady=7)


        #Salary_type
        label_Salary_type=Label(upper_frame,font=('arial',12,'bold'),text='Pay Type:',bg='white')
        label_Salary_type.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        combobox_Salary_type=ttk.Combobox(upper_frame,textvariable=self.variable_paytype,state ='readonly',font = ('Comic Sans Ms',11,'bold'),width =18)
        combobox_Salary_type['value']=('-----Select--------','Hourly','Daily',"Weekly",'Monthly','Quaterly','Half Yearly','Annually')
        combobox_Salary_type.current(0)
        combobox_Salary_type.grid(row = 3,column =1,sticky =W,padx=2,pady =7)


            #salary
        label_salary=Label(upper_frame,font=('arial',12,'bold'),text='Pay(₹):',bg='white')
        label_salary.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_salary=ttk.Entry(upper_frame,textvariable=self.variable_pay,width=20,font=('Comic Sans Ms',11,'bold'))
        txt_salary.grid(row=4,column =1,sticky=W,padx =2,pady=7)
            


         # side image
        side_img=Image.open('pics/pic1.webp')
        side_img = side_img.resize((250,250),Image.LANCZOS)
        self.side_photo=ImageTk.PhotoImage(side_img)

        # Side Image Frame
        self.side_img = Label(upper_frame,image=self.side_photo)
        self.side_img.place(x=1025,y=-5,width = 250,height =250)


         # Button Frame
       # button_frame = Frame(upper_frame,bd=2,relief=RIDGE)
        button_frame = LabelFrame(upper_frame,bd=1,bg='white',relief=RIDGE,text='ACTIONS',font=('times new roman',12,'bold'),fg='crimson')

        button_frame.place(x=1280,y=0,width=183,height =240)


        btn_add=Button(button_frame,text='SAVE',command=self.enter_information,font=('arial',15,'bold'),width=14,bg='lime green',fg='white')
        btn_add.grid(row=0,column=0,padx=0,pady=8)

        
        btn_update=Button(button_frame,text='UPDATE',command=self.update_information,font=('arial',15,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=0,pady=8)

        
        btn_delete=Button(button_frame,text='DELETE',command=self.delete_information,font=('arial',15,'bold'),width=14,bg='red',fg='white')
        btn_delete.grid(row=2,column=0,padx=0,pady=8)

        
        btn_clear=Button(button_frame,text='CLEAR',command=self.clear_information,font=('arial',15,'bold'),width=14,bg='midnightblue',fg='white')
        btn_clear.grid(row=3,column=0,padx=0,pady=8)







         # Lower Frame
        lower_frame = LabelFrame(main_frame,bd=3,relief=RIDGE,bg = 'white',text='LABOUR INFORMATION TABLE',font=('times new roman',13,'bold'),fg='crimson')
        lower_frame.place(x=10,y=280,width=1480.5,height =270 ) 

         # Search Frame
        search_frame = LabelFrame(lower_frame,relief=RIDGE,bg = 'white',text='SEARCH LABOUR INFORMATION',font=('times new roman',11,'bold'),fg='GREEN')
        search_frame.place(x=3,y=3,width=1470.5,height =60 )

         #search label
        search_by = Label(search_frame,font=('arial',15,'bold'),text='SEARCH BY:',bg='red',fg='white')
        search_by.grid(row=0,column=0,sticky=W,padx=5,pady=5) 

         #search
        self.var_combo_search=StringVar()
        combobox_text_search = ttk.Combobox(search_frame,textvariable=self.var_combo_search,state='readonly',font = ("Comic Sans Ms",12,"bold"),width=28)

        combobox_text_search['value']=("------------Select-------------","Phone_no ",'ID_proof','Name','Email','Designation','Organisation','Address','Marital_Status','Pay_Type','Gender','DOB','DOJ') 
        combobox_text_search.current(0)
        combobox_text_search.grid(row=0,column=1,sticky=W,padx=5,pady=5)


        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=30,font=('Comic Sans Ms',12,'bold'))
        txt_search.grid(row=0,column =2,sticky=W,padx =2,pady=2)
        
        button_search=Button(search_frame,command=self.search_information,text='SEARCH',font=('arial',12,'bold'),width=33,bg='lime green',fg='white')
        button_search.grid(row=0,column=3,padx=2,pady=3)

        button_showall=Button(search_frame,command=self.get_datafrom_database,text='SHOW ALL',font=('arial',12,'bold'),width=33,bg='BLUE',fg='white')
        button_showall.grid(row=0,column=4,padx=5,pady=3)

        #==================LABOUR TABLE============================
        # Table Frame
        table_frame = Frame(lower_frame,bd=4,relief=RIDGE)
        table_frame.place(x=1,y=60,width=1473.5,height =185 )

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.labour_table=ttk.Treeview(table_frame,columns=('org','name','degi','doj','pay','paytype','idproofcombo','idproof','email','address','married','dob','gender','phone','fathername'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.labour_table.xview)
        scroll_y.config(command=self.labour_table.yview)
        
        self.labour_table.heading('org',text='ORGANIZATION')
        self.labour_table.heading("name", text="NAME")
        self.labour_table.heading("degi",text="DESIGNATION")
        self.labour_table.heading("doj",text="DATE OF JOINING")
        self.labour_table.heading("pay",text="PAY")
        self.labour_table.heading("paytype",text="PAY TYPE")
        self.labour_table.heading("idproofcombo",text="ID TYPE")
        self.labour_table.heading("idproof",text="ID NO.")
        self.labour_table.heading("email",text="EMAIL")
        self.labour_table.heading("address",text="ADDRESS")
        self.labour_table.heading("married",text="MARITAL STATUS")
        self.labour_table.heading("dob", text="DATE OF BIRTH" )
        self.labour_table.heading("gender", text="GENDER")
        self.labour_table.heading("phone",text="PHONE NO.")
        self.labour_table.heading("fathername",text="FATHER/HUSBAND NAME")
       


        self.labour_table['show']='headings'
        self.labour_table.column('org',width=100)
        self.labour_table.column('name',width=100)
        self.labour_table.column('degi',width=100)
        self.labour_table.column('doj',width=120)
        self.labour_table.column('pay',width=100)
        self.labour_table.column('paytype',width=100)
        self.labour_table.column('idproofcombo',width=100)
        self.labour_table.column('idproof',width=100)
        self.labour_table.column('email',width=100)
        self.labour_table.column('address',width=100)
        self.labour_table.column('married',width=100)
        self.labour_table.column('dob',width=100)
        self.labour_table.column('gender',width=100)
        self.labour_table.column('phone',width=100)
        self.labour_table.column('fathername',width=150)
       


        
        self.labour_table.pack(fill=BOTH,expand=1)
        # clicking on info and filling that data in entry fields
        self.labour_table.bind("<ButtonRelease>",self.get_cursor)

        self.get_datafrom_database()


    # +=====================Function Declarations===============+

    def enter_information(self):
      if self.variable_IDproof.get()==""or self.variable_organisation.get()==""or self.variable_name.get()==""or self.variable_designation.get()==""or self.variable_address.get()==""or self.variable_dob.get()==""or self.variable_doj.get()==""or self.variable_email.get()==""or self.variable_fathername.get()==""or self.variable_gender.get()==""or self.variable_IDproofcombobox.get()==""or self.variable_marital_status.get()==""or self.variable_pay.get()==""or self.variable_paytype.get()==""or self.variable_phoneno.get()=="":
        messagebox.showerror('INVALID ACTION !!! ',"All Fields Are Mandatory ")
      else:
        try:
            connection=mysql.connector.connect(host='localhost',username='root',password='01Isincorrect',database='ghanidb')
            data_cursor =connection.cursor()
            data_cursor.execute('insert into labour_management values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(

                                                                                            self.variable_organisation.get(),
                                                                                            self.variable_name.get(),
                                                                                            self.variable_designation.get(),
                                                                                            self.variable_doj.get(),
                                                                                            self.variable_pay.get(),
                                                                                            self.variable_paytype.get(),
                                                                                            self.variable_IDproofcombobox.get(),
                                                                                            self.variable_IDproof.get(),
                                                                                            self.variable_email.get(),
                                                                                            self.variable_address.get(),
                                                                                            self.variable_marital_status.get(),
                                                                                            self.variable_dob.get(),
                                                                                            self.variable_gender.get(),
                                                                                            self.variable_phoneno.get(),
                                                                                            self.variable_fathername.get(),



                                                                                                                     ))
            connection.commit()
            self.get_datafrom_database()
            connection.close()
            messagebox.showinfo('SUCCESS','Information Successfully Saved ✔',parent=self.root)
        
        except Exception as ES:
          messagebox.showerror('ERROR',f'Due To:{str(ES)}',parent=self.root)

    # GET DATA FROM DATABASE
    def get_datafrom_database(self):
      connection=mysql.connector.connect(host='localhost',username='root',password='01Isincorrect',database='ghanidb')
      data_cursor =connection.cursor()
      data_cursor.execute("Select * from labour_management")
      information = data_cursor.fetchall()
      
      self.labour_table.delete(*self.labour_table.get_children())
      if len(information)>=0:
        for i in information:
         self.labour_table.insert("",END,value =i)
        connection.commit()                           #commit means update
        connection.close()

    # Get Cursor
    def get_cursor(self,event= ''):
      cursor_row =  self.labour_table.focus()
      content=self.labour_table.item(cursor_row)
      data = content['values']

      self.variable_organisation.set(data[0])
      self.variable_name.set(data[1])
      self.variable_designation.set(data[2])
      self.variable_doj.set(data[3])
      self.variable_pay.set(data[4])
      self.variable_paytype.set(data[5])
      self.variable_IDproofcombobox.set(data[6])
      self.variable_IDproof.set(data[7])
      self.variable_email.set(data[8])
      self.variable_address.set(data[9])
      self.variable_marital_status.set(data[10])
      self.variable_dob.set(data[11])
      self.variable_gender.set(data[12])
      self.variable_phoneno.set(data[13])
      self.variable_fathername.set(data[14])

  # Update Information

    def update_information(self):
      if self.variable_IDproof.get()==""or self.variable_organisation==""or self.variable_name.get()==""or self.variable_designation.get()==""or self.variable_address.get()==""or self.variable_dob.get()==""or self.variable_doj.get()==""or self.variable_email.get()==""or self.variable_fathername.get()==""or self.variable_gender.get()==""or self.variable_IDproofcombobox.get()==""or self.variable_marital_status.get()==""or self.variable_pay.get()==""or self.variable_paytype.get()==""or self.variable_phoneno.get()=="":   
        messagebox.showerror('INVALID ACTION !!!' ,"All Fields Are Mandatory  ")
      else:
          try:
            update=messagebox.askyesno('ACTION REQUIRED','Are You Sure To Update This Information')
            if update>0:            
             connection=mysql.connector.connect(host='localhost',username='root',password='01Isincorrect',database='ghanidb')
             data_cursor =connection.cursor()
             data_cursor.execute('update labour_management set Organisation=%s,Name = %s,Designation = %s,DOJ = %s,Pay=%s,Pay_Type=%s,ID_proof_type=%s,Email=%s,Address=%s,Marital_Status = %s,DOB=%s,Gender=%s,Phone_no=%s,Father_husband_name=%s where ID_proof=%s',(

             self.variable_organisation.get(),
             self.variable_name.get(),
             self.variable_designation.get(),
             self.variable_doj.get(),
             self.variable_pay.get(),
             self.variable_paytype.get(),
             self.variable_IDproofcombobox.get(),           
             self.variable_email.get(),
             self.variable_address.get(),
             self.variable_marital_status.get(),
             self.variable_dob.get(),
             self.variable_gender.get(),
             self.variable_phoneno.get(),
             self.variable_fathername.get(),
             self.variable_IDproof.get()
             ))
  
            else:
              if not update:
                  return      
            connection.commit()
            self.get_datafrom_database()
            connection.close()
            messagebox.showinfo('SUCCESS','Information Successfully Updated ✔',parent=self.root)

          except Exception as ES:   
            messagebox.showerror('ERROR',f'Due To:{str(ES)}',parent=self.root)


  #   Delete Information Function
    def delete_information(self):
      if self.variable_IDproof.get()==""or self.variable_organisation.get()==""or self.variable_name.get()=="":
        messagebox.showerror('INVALID ACTION !!!',"Information Required To Delete ")
      else:
        try:
          Delete = messagebox.askyesno("ACTION REQUIRED",'Are You Sure To Delete This Information',parent = self.root) #parent = self.root se usi window pr show ho msg jisme data h
          if Delete>0:
            connection=mysql.connector.connect(host='localhost',username='root',password='01Isincorrect',database='ghanidb')
            data_cursor =connection.cursor()
            sql='delete from labour_management where ID_proof=%s'
            value =(self.variable_IDproof.get(),)
            data_cursor.execute(sql,value)
          else:
            if not Delete:
              return
          
          connection.commit()
          self.get_datafrom_database()
          connection.close()
          messagebox.showinfo('DELETE','Information Successfully Deleted ✔',parent=self.root)

        except Exception as ES:   
          messagebox.showerror('ERROR',f'Due To:{str(ES)}',parent=self.root)


  #   Reset button

    def clear_information(self):
      self.variable_organisation.set('-----Select--------')
      self.variable_name.set('')
      self.variable_designation.set('')
      self.variable_doj.set('')
      self.variable_pay.set('')
      self.variable_paytype.set('-----Select--------')
      self.variable_IDproofcombobox.set('-Select ID Proof-')
      self.variable_IDproof.set('')
      self.variable_email.set('')
      self.variable_address.set('')
      self.variable_marital_status.set('-----Select--------')
      self.variable_dob.set('')
      self.variable_gender.set('-----Select--------')
      self.variable_phoneno.set('')
      self.variable_fathername.set('')
      self.var_combo_search.set('------------Select-------------')
      self.var_search.set('')

    #search information

    def search_information(self):
      if self.var_combo_search.get()==''or self.var_search.get()=='':
        messagebox.showerror('INVALID ACTION !!!',"Please Select Option")
      else:
        try:
         connection=mysql.connector.connect(host='localhost',username='root',password='01Isincorrect',database='ghanidb')
         data_cursor =connection.cursor()
         data_cursor.execute('select * from labour_management where ' +str(self.var_combo_search.get())+" LIKE'%"+str(self.var_search.get()+"%'"))  #mysql query to search
         rows = data_cursor.fetchall()
         if len(rows)!=0:
           self.labour_table.delete(*self.labour_table.get_children())  
           for i in rows:
            self.labour_table.insert("",END,values=i)
         elif len(rows)==0:
          messagebox.showerror('No Record Found !!!',"Please Enter Correct Information")

         connection.commit()
         connection.close()
         
        except Exception as ES:   
          messagebox.showerror('ERROR',f'Due To:{str(ES)}',parent=self.root)
if __name__=="__main__":
    root=Tk()
    obj= Labour(root)
    root.mainloop()