from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageFilter
from tkmacosx import Button
from tkinter import messagebox
import mysql.connector


class Students:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x800+20+0")
        self.root.title("Face Recognition System")



# =================variables======================

        self.var_class= StringVar()
        self.var_ID=StringVar()
        self.var_name=StringVar()
        self.var_fatherName=StringVar()
        self.var_class=StringVar()
        self.var_section=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()
        self.var_subjects=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_email_ID=StringVar()
        self.var_photo=StringVar()
        self.var_year=StringVar()

        


     # first image(background)
        img = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/Button background/bg1.jpeg")
        img = img.resize((1400,790),Image.ANTIALIAS)
        img= img.filter(ImageFilter.GaussianBlur(2))
        img= img.filter(ImageFilter.BoxBlur(3))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1400,height=790)

    # Title of the page
        title_lbl=Label(bg_img,text=" STUDENT     MANAGEMENT     SYSTEM", font=("Quartz",55,"bold"))
        title_lbl.place(x=-30,y=0, width=1440, height=120)

    # Frame
        main_frame=Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10,y=130, width=1380, height=620)

    # Left Frame
        left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman", 18, "bold" ))
        left_frame.place(x=10, y=10, width=630, height=605)

    # Left Frame pic
        img_left=Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/students.jpg")
        img_left=img_left.resize((520,150),Image.ANTIALIAS)
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl= Label(left_frame, image= self.photoimg_left)
        f_lbl.place(x=80,y=-5, width=480, height=128)

    # Info Frame(inside left frame)
        currentCourse_frame=LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Course Details", font=("Times New Roman", 15, "bold" ))
        currentCourse_frame.place(x=3, y=122, width=620, height=110)
    # Class
        dep_label= Label(currentCourse_frame,text="Class", font=("Quratz",13,"bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=3)

        dep_combo=ttk.Combobox(currentCourse_frame, textvariable=self.var_class, font=("Quratz",12), width=18, state="readonly")
        dep_combo["values"]=("Select Class", "Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8", "Class 9", "Class 10")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5, sticky=W)

    # Section 
        Section_label= Label(currentCourse_frame,text="Section", font=("Quratz",13,"bold"), bg="white")
        Section_label.grid(row=0, column=2, padx=5, sticky=W)

        Section_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_section, font=("Quratz",12), width=18, state="readonly")
        Section_combo["values"]=("Select Section", "A", "B", "C")
        Section_combo.current(0)
        Section_combo.grid(row=0,column=3,padx=2,pady=5, sticky=W) 

    # Subjects 
        Subjects_label= Label(currentCourse_frame,text="Subjects", font=("Quratz",13,"bold"), bg="white")
        Subjects_label.grid(row=1, column=0, padx=5, pady=15, sticky=W)

        Subjects_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_subjects, font=("Quratz",12), width=18, state="readonly")
        Subjects_combo["values"]=("Select Subject", "All", "PCM", "PCB", "Home Science", "Art")
        Subjects_combo.current(0)
        Subjects_combo.grid(row=1,column=1,padx=2,pady=5, sticky=W) 
            
    # Year 
        Year_label= Label(currentCourse_frame,text="Year", font=("Quratz",13,"bold"), bg="white")
        Year_label.grid(row=1, column=2, padx=3, pady=15)

        Year_combo=ttk.Combobox(currentCourse_frame,textvariable=self.var_year, font=("Quratz",12), width=18, state="readonly")
        Year_combo["values"]=("Select Year", "2020-2021", "2021-2022","2022-2023","2023-2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=3 ,padx=2 ,pady=5, sticky=W) 

# Creating Entry Fields

    # Entry Frame(inside left frame)
        entry_frame=LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("Times New Roman", 15, "bold"))
        entry_frame.place(x=3, y=235, width=620, height=340)

    # Student ID
        StudentId_label= Label(entry_frame,text="Student ID", font=("Quratz",13,"bold"), bg="white")
        StudentId_label.grid(row=0, column=0, padx=0, pady=7)

        StudentId_entry= ttk.Entry(entry_frame,textvariable=self.var_ID, width=25, font=("Times New Roman",12,"bold"))
        StudentId_entry.grid(row=0, column=1, padx=0, pady=7, sticky=W)

    # Student Name
        studentName_label= Label(entry_frame,text= " Name ", font=("Quratz",13,"bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=0, pady=7)

        studentName_entry= ttk.Entry(entry_frame,textvariable=self.var_name, width=30, font=("Times New Roman",12))
        studentName_entry.grid(row=0, column=3, padx=0, pady=7, sticky=W)

    # Gender    
        gender_label= Label(entry_frame,text= "Gender", font=("Quratz",13,"bold"), bg="white")
        gender_label.grid(row=1, column=0, pady=7)

        gender_combo=ttk.Combobox(entry_frame,textvariable=self.var_gender, font=("Quratz",12), width=14, state="readonly")
        gender_combo["values"]=("Select Gender", "Male", "Female", "Ohter")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=1, pady=7, sticky=W) 

    # Father's Name
        fatherName_label= Label(entry_frame,text= "Father's Name", font=("Quratz",13,"bold"), bg="white")
        fatherName_label.grid(row=1, column=2, padx=0, pady=7)

        fatherName_entry= ttk.Entry(entry_frame,textvariable=self.var_fatherName, width=30, font=("Times New Roman",12))
        fatherName_entry.grid(row=1, column=3, padx=3, pady=7, sticky=W)

    # Date of Birth
        dob_label= Label(entry_frame,text= "Date of Birth", font=("Quratz",13,"bold"), bg="white")
        dob_label.grid(row=2, column=0, padx=0, pady=7)

        dob_entry= ttk.Entry(entry_frame,textvariable=self.var_dob, width=25, font=("Times New Roman",12))
        dob_entry.grid(row=2, column=1, padx=0, pady=7, sticky=W)

    # Email Id
        email_label= Label(entry_frame,text= "Email ID", font=("Quratz",13,"bold"), bg="white")
        email_label.grid(row=2, column=2, padx=20, pady=7)

        email_entry= ttk.Entry(entry_frame,textvariable=self.var_email_ID, width=30, font=("Times New Roman",12))
        email_entry.grid(row=2, column=3, padx=3, pady=7, sticky=W) 

    # Phone No
        phone_label= Label(entry_frame,text= "Phone No", font=("Quratz",13,"bold"), bg="white")
        phone_label.grid(row=3, column=0, padx=0, pady=7)

        phone_entry= ttk.Entry(entry_frame,textvariable=self.var_phone, width=25, font=("Times New Roman",12))
        phone_entry.grid(row=3, column=1, padx=0, pady=7, sticky=W) 

    # Address
        address_label= Label(entry_frame,text= "Address", font=("Quratz",13,"bold"), bg="white")
        address_label.grid(row=3, column=2, padx=10, pady=7)

        address_entry= ttk.Entry(entry_frame,textvariable=self.var_address, width=30, font=("Times New Roman",12))
        address_entry.grid(row=3, column=3, padx=3, pady=7, sticky=W)

    # radio buttons
        self.var_radio1=StringVar()
        radiob1=ttk.Radiobutton(entry_frame,text="Take Photo Sample",variable=self.var_radio1, value="Yes")
        radiob1.grid(row=6, column=0, padx=5)

        radiob2=ttk.Radiobutton(entry_frame,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiob2.grid(row=6, column=3, pady=10)

    # Lower button frame
        btn_frame=Frame(entry_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=2, y=195, width=610, height=60)  

        save_btn=Button(btn_frame, text="Save", command=self.add_data, width='6c',height='2c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0, padx=4)  

        update_btn=Button(btn_frame, text="Update", command= self.update_data, width='5c',height='2c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        delete_btn=Button(btn_frame, text="Delete", command= self.delete_data, width='5c',height='2c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        reset_btn=Button(btn_frame, text="Reset", command = self.reset_data, width='5c',height='2c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn1_frame=Frame(entry_frame, bd=2, bg="white", relief=RIDGE)
        btn1_frame.place(x=2, y=255, width=610, height=65)  

        takephoto_btn=Button(btn1_frame, text="Take Photo",width='11c',height='2c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        takephoto_btn.grid(row=0, column=0, padx=4)

        updatephoto_btn=Button(btn1_frame, text="Update Photo",width='10c',height='2c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        updatephoto_btn.grid(row=0, column=1)


    # Right Frame
        right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Times New Roman", 18, "bold" ))
        right_frame.place(x=650, y=10, width=720, height=605)

    # Right Frame pic
        img_right=Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/students right.jpg")
        img_right=img_right.resize((670,150),Image.ANTIALIAS)
        self.photoimg_right= ImageTk.PhotoImage(img_right)

        f_lbl= Label(right_frame, image= self.photoimg_right)
        f_lbl.place(x=50,y=-3, width=620, height=128)    
        
    # ========== Search System==========

    # Search Frame
        search_frame=LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 15, "bold"))
        search_frame.place(x=3, y=123, width=710, height=65) 

        search_label= Label(search_frame,text= "Search By", font=("Quratz",13,"bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=5, pady=7, sticky=W) 

        search_combo=ttk.Combobox(search_frame, font=("Quratz",12), width=13, height=10, state="readonly")
        search_combo["values"]=("Select", "Student ID", "Roll No", "Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1 ,padx=2 ,pady=7, sticky=W)

        search_entry= ttk.Entry(search_frame, width=20, font=("Times New Roman",12,"bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        
        search_btn=Button(search_frame, text="Search",width='6c', height='1c',font=("Quartz", 13, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=3)

        showAll_btn=Button(search_frame, text="Show All",width='6c', height='1c', font=("Quartz", 13, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=2)  

    # Table Frame
        table_frame=Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=3, y=190, width=710, height=390) 

        scroll_x=ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)


        self.student_table=ttk.Treeview(table_frame, column=("ID","name","fatherName", "class", "section","address","phone", "subjects", "dob", "gender", "email_ID", "photo","year"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="Student ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("fatherName", text="Father's Name")
        self.student_table.heading("class", text="Class")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("subjects", text="Subjects")
        self.student_table.heading("dob", text="Date of Birth")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("email_ID", text="Email ID")
        self.student_table.heading("photo", text="Photo")
        self.student_table.heading("year", text="Year")

        self.student_table["show"]= "headings"

        self.student_table.column("ID",width=100)
        self.student_table.column("name",width=230)
        self.student_table.column("fatherName",width=230 )
        self.student_table.column("class",width=100 )
        self.student_table.column("section",width=100 )
        self.student_table.column("address",width=400 )
        self.student_table.column("phone",width=180 )
        self.student_table.column("subjects",width=200 )
        self.student_table.column("dob",width=100)
        self.student_table.column("gender",width=100 )
        self.student_table.column("email_ID",width=230)
        self.student_table.column("photo",width=100 )
        self.student_table.column("year",width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        
        self.student_table.bind("<ButtonRelease>", self.get_cursor)       # /// binding the student table with get cursor for updating entries in table.////
        
        self.fetch_Data()     #fetching MySql data to the right frame table

# ===================Function for adding data======================
    def add_data(self):
        if self.var_class.get()=="Select Class" or self.var_name.get()==" " or self.var_ID.get()==" ":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        else:
            try:
                conn=mysql.connector.connect(host="localhost",user='root', password="gaurav", database="face_recognition")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_ID.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_fatherName.get(),
                                                                                                            self.var_class.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_subjects.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_email_ID.get(),
                                                                                                        
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_year.get()

                                                                                                        ))

                conn.commit()
                self.fetch_Data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully!", parent=self.root)                                                                                        

            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}",parent=self.root)   
            
    # ================== Fetching MySql Data to student page==================
    
    def fetch_Data(self):
        conn=mysql.connector.connect(host="localhost",user='root', password="gaurav", database="face_recognition")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            
            conn.commit()
        conn.close()



# =========== Get cursor for updating entries============

    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_ID.set(data[0]),
        self.var_name.set(data[1]),
        self.var_fatherName.set(data[2]),
        self.var_class.set(data[3]),
        self.var_section.set(data[4]),
        self.var_address.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_subjects.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_email_ID.set(data[10]),
                                                                                                        
        self.var_radio1.set(data[11]),
        self.var_year.set(data[12])


# =========== Updating the data==========   
    def update_data(self):
        if self.var_class.get()=="Select Class" or self.var_name.get()==" " or self.var_ID.get()==" ":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        else:
            try:
                Upadate= messagebox.askyesno("Update", "Do you want to update these changes", parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",user="root", password="gaurav", database="face_recognition")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set `Name`=%s,`Father's Name`=%s,`Class`=%s,`Section`=%s,`Address`=%s,`Phone No`=%s,`Subjects`=%s,`Date of Birth`=%s,`Gender`=%s,`Email ID`=%s,`Photo`=%s,`Year`=%s where `Student ID` =%s" ,(

                                                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                                                            self.var_fatherName.get(),
                                                                                                                                                                                                                            self.var_class.get(),
                                                                                                                                                                                                                            self.var_section.get(),
                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                            self.var_subjects.get(),
                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                            self.var_email_ID.get(),
                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                            self.var_ID.get()      
                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                    ))

                else: 
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Details are updated successfully!", parent= self.root)
                conn.commit()
                self.fetch_Data()
                conn.close() 
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


# ============ Deleting the data============
    def delete_data(self):
        if self.var_ID.get() =="":
            messagebox.showerror("Error", "Student ID is required", parent= self.root)
        else:
            try:
                delete= messagebox.askyesno("Delete Info", "Do you want to delete this student info", parent= self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",user="root", password="gaurav", database="face_recognition")
                    my_cursor=conn.cursor()
                    sql= "delete from student where `Student ID`=%s"
                    val= (self.var_ID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_Data()
                conn.close() 
                messagebox.showinfo("Delete Info", "Stduent info deleted successfully.", parent= self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


# ========== Reset function========
    def reset_data(self):
        self.var_ID.set(""),
        self.var_name.set(""),
        self.var_fatherName.set(""),
        self.var_class.set("Select Class"),
        self.var_section.set("Select Section"),
        self.var_address.set(""),
        self.var_phone.set(""),
        self.var_subjects.set("Select Subject"),
        self.var_dob.set(""),
        self.var_gender.set("Select Gender"),
        self.var_email_ID.set(""),
                                                                                                        
        self.var_radio1.set(""),
        self.var_year.set("Select Year")
        
        


             





          





if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()