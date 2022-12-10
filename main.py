from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk,ImageFilter


class Face_Recognition_System:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1400x800+20+0")
        self.root.title("Face Recognition System")
        
        
        # first image(background)
        img = Image.open("/Users/gaurav/Desktop/Face_recognition/college Images/Main page.jpeg")
        img = img.resize((1400,790),Image.ANTIALIAS)
        img= img.filter(ImageFilter.GaussianBlur(3))
        img= img.filter(ImageFilter.BoxBlur(4))
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img= Label(self.root, image=self.photoimg)
        bg_img.place(x=0,y=0, width=1400,height=790)
        

        # Title of the page
        title_lbl=Label(bg_img,text="FACE  RECOGNITION  ATTENDANCE  SYSTEM", font=("Quartz",60,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0, width=1400, height=200)


        # #second image
        # img1 = Image.open("/Users/gaurav/Desktop/Face_recognition/college Images/istockphoto-1124560262-612x612.jpeg")
        # img1 = img1.resize((500,200),Image.ANTIALIAS)
        # self.photoimg1 = ImageTk.PhotoImage(img1)

        # f_lbl= Label(self.root, image=self.photoimg)
        # f_lbl.place(x=500,y=0, width=500,height=130)

        # #third image
        # img2 = Image.open("/Users/gaurav/Desktop/Face_recognition/college Images/istockphoto-1124560262-612x612.jpeg")
        # img2 = img2.resize((500,200),Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # f_lbl= Label(self.root, image=self.photoimg)
        # f_lbl.place(x=1000,y=0, width=400,height=130)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()