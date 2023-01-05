from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageFilter
from tkmacosx import Button
from students import Students

class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1400x800+20+0")
        self.root.title("Face Recognition System")
        
        
        # first image(background)
        img = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/Main page.jpeg")
        img = img.resize((1400,790),Image.ANTIALIAS)
        img= img.filter(ImageFilter.GaussianBlur(2))
        img= img.filter(ImageFilter.BoxBlur(3))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1400,height=790)
        

        # Title of the page
        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM", font=("Quartz",60,"bold"),bg="navyblue", fg="white")
        title_lbl.place(x=0,y=0, width=1400, height=170)


        #student image(button)
        img1 = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/students.jpg")
        img1 = img1.resize((250,200),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
                                                # here command function is used to link student page
        b1=Button(bg_img,image=self.photoimg1, command=self.student_details, cursor="hand")
        b1.place(x=160, y=220, width=230, height=200)

        #creating text as button on img1                # here command function is used to link student page
        b1_1= Button(bg_img, text="Students Details", command=self.student_details, cursor="hand", font=("Times New Roman",25,"bold"),fg="black")
        b1_1.place(x=160,y=415, width=230, height=35)

        #Face Detection Button
        img2 = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/face detect.jpeg")
        img2 = img2.resize((250,200),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1=Button(bg_img,image=self.photoimg2, cursor="hand")
        b1.place(x=550, y=220, width=230, height=200)

        #creating text as button on img2
        b1_1= Button(bg_img, text="Face Detect", cursor="hand", font=("Times New Roman",25,"bold"),fg="black")
        b1_1.place(x=550 ,y=415, width=230, height=35)

       # Attendance 
        img3 = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/attendance1.jpg")
        img3 = img3.resize((250,200),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1=Button(bg_img,image=self.photoimg3, cursor="hand")
        b1.place(x=950, y=220, width=230, height=200)

        #creating text as button on img3
        b1_1= Button(bg_img, text="Attendance", cursor="hand", font=("Times New Roman",25,"bold"),fg="black")
        b1_1.place(x=950,y=415, width=230, height=35)

         # Photos
        img4 = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/photos.jpg")
        img4= img4.resize((250,200),Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4, cursor="hand")
        b1.place(x=160, y=500, width=230, height=200)

        #creating text as button on img3
        b1_1= Button(bg_img, text="Photos", cursor="hand", font=("Times New Roman",25,"bold"),fg="black")
        b1_1.place(x=160,y=692, width=230, height=35)

         # Train Data
        img5 = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/train2.jpeg")
        img5= img5.resize((250,200),Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5, cursor="hand")
        b1.place(x=550, y=500, width=230, height=200)

        #creating text as button on img3
        b1_1= Button(bg_img, text="Train Data", cursor="hand", font=("Times New Roman",25,"bold"),fg="black")
        b1_1.place(x=550,y=692, width=230, height=35)

        
        # Developer
        img6 = Image.open("/Users/gaurav/Desktop/Face_Recognition_Attendance_System/college Images/developer.png")
        img6= img6.resize((220,200),Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6, cursor="hand")
        b1.place(x=950, y=500, width=230, height=200)

        #creating text as button on img3
        b1_1= Button(bg_img, text="Developer", cursor="hand", font=("Times New Roman",25,"bold"),fg="black")
        b1_1.place(x=950,y=692, width=230, height=35)

# ============creating function for linking student page===========
    def student_details(self):
        self.new_window= Toplevel(self.root)
        self.app=Students(self.new_window)






      


       





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()