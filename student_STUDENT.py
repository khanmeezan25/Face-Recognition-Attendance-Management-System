from tkinter import*
from tkinter import ttk
from customtkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student1:
    def __init__(self, root, main_root):
        self.root = root
        self.main_root = main_root
        self.root.geometry("1550x900+0+0")
        self.root.title("Face Recoginiton System")
        self.root.state('zoomed')

        #____VARIABLES_____
        self.name_var=StringVar()
        self.dep_var=StringVar()
        self.year_var=StringVar()
        self.course_var=StringVar()
        self.sem_var=StringVar()
        self.std_id_var=StringVar()
        self.roll_no_var=StringVar()
        self.gendre_var=StringVar()
        self.email_var=StringVar()

        self.div_var=StringVar()
        self.dob_var=StringVar()
        self.phone_var=StringVar()
        self.address_var=StringVar()
        self.teacher_var=StringVar()

        #1st image
        img13=Image.open(r"Used Pictures\studenttop1.webp")
        img13=img13.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg13=ImageTk.PhotoImage(img13)
        
        label13=Label(self.root,image=self.photoimg13)
        label13.place(x=0,y=0,width=500,height=130)


        #2nd image
        img14=Image.open(r"Used Pictures\studenttop2.jpg")
        img14=img14.resize((400,130),Image.Resampling.LANCZOS)
        self.photoimg14=ImageTk.PhotoImage(img14)
        
        label14=Label(self.root,image=self.photoimg14)
        label14.place(x=500,y=0,width=400,height=130)

        #3rd image
        img15=Image.open(r"Used Pictures\student2.jpg")
        img15=img15.resize((630,130),Image.Resampling.LANCZOS)
        self.photoimg15=ImageTk.PhotoImage(img15)
        
        label15=Label(self.root,image=self.photoimg15)
        label15.place(x=900,y=0,width=630,height=130)

        #background image
        img16=Image.open(r"Used Pictures\faceR.webp")
        img16=img16.resize((1530,750),Image.Resampling.LANCZOS)
        self.photoimg16=ImageTk.PhotoImage(img16)
        
        label16=Label(self.root,image=self.photoimg16)
        label16.place(x=0,y=130,width=1530,height=750)

        #creating title for the bg image
        title=Label(label16,text="STUDENT MANAGEMENT SYSTEM",font=('times new roman',25,'bold'),fg='white',bg='black')
        title.place(x=-2,y=-2,width=1530,height=42)

        #creating back button
        back_button=CTkButton(title,command=self.back_button,width=83,height=42,text='Back',font=('times new roman',15,'bold'),fg_color='white',corner_radius=8,bg_color='black',text_color='black',hover_color='gray')
        back_button.place(x=-2,y=-2)

        # main frame
        std_frame=Frame(label16,bd=2,bg='white')
        std_frame.place(x=380,y=40,width=600,height=450)

        # left frame(inside main frame)
        left_frame1=LabelFrame(std_frame,bd=2,relief=RIDGE,text='Student Registration',font=('times new roman',10),bg='white')
        left_frame1.place(x=8,y=5,width=580,height=430)

        #providing image for the left frame(line 58-63)
        img_left=Image.open(r"Used Pictures\top3.jpg")
        img_left=img_left.resize((580,100),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        label_left=Label(left_frame1,image=self.photoimg_left)
        label_left.place(x=0,y=0,width=580,height=100)

        #creating a frame for course details
        current_frame=LabelFrame(left_frame1,bd=2,relief=RIDGE,text='Course Info',font=('times new roman',10),bg='white')
        current_frame.place(x=0,y=105,width=575,height=305)

        #Student Name
        studentname_label=Label(current_frame,text='Student Name',font=('times new roman',10,'bold'),bg='white')
        studentname_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentname_entry=ttk.Entry(current_frame,textvariable=self.name_var,width=25,font=('times new roman',10))
        studentname_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #department
        dep_label=Label(current_frame,text='Department',font=('times new roman',10,'bold'),bg='white')
        dep_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        dep_combo=ttk.Combobox(current_frame,textvariable=self.dep_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        # dep_combo['values']=('Select Department','Computer','IT','Civil','Mechanical')
        dep_combo['values']=('Select Department','BSc. CSDA','BBA')
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #course
        course_label=Label(current_frame,text='Course',font=('times new roman',10,'bold'),bg='white')
        course_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        course_combo=ttk.Combobox(current_frame,textvariable=self.course_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        course_combo['values']=('Select Course','UG','PG')
        course_combo.current(0)
        course_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #year
        year_label=Label(current_frame,text='Year',font=('times new roman',10,'bold'),bg='white')
        year_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_frame,textvariable=self.year_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        # year_combo['values']=('Select Year','22-23','23-24','24-25','25-26')
        year_combo['values']=('Select Year','23-26','24-27','25-28')
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #semester
        semester_label=Label(current_frame,text='Semester',font=('times new roman',10,'bold'),bg='white')
        semester_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        semester_combo=ttk.Combobox(current_frame,textvariable=self.sem_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        semester_combo['values']=('Select Semester','Semester-1','Semester-2')
        semester_combo.current(0)
        semester_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # studentID
        studentID_label=Label(current_frame,text='StudentID/ID No.',font=('times new roman',10,'bold'),bg='white')
        studentID_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        
        studentID_entry=ttk.Entry(current_frame,textvariable=self.std_id_var,width=25,font=('times new roman',10))
        studentID_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        #Roll no
        rollno_label=Label(current_frame,text='Roll No.',font=('times new roman',10,'bold'),bg='white')
        rollno_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        rollno_entry=ttk.Entry(current_frame,textvariable=self.roll_no_var,width=25,font=('times new roman',10))
        rollno_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #gender
        gender_label=Label(current_frame,text='Gender',font=('times new roman',10,'bold'),bg='white')
        gender_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)

        gender_combo=ttk.Combobox(current_frame,textvariable=self.gendre_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        gender_combo['values']=('Select Gender','Male','Female','Other')
        gender_combo.current(0)
        gender_combo.grid(row=3,column=3,padx=5,pady=5,sticky=W)

        #Email
        email_label=Label(current_frame,text='Email',font=('times new roman',10,'bold'),bg='white')
        email_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)

        email_entry=ttk.Entry(current_frame,textvariable=self.email_var,width=25,font=('times new roman',10))
        email_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)

        #Class division
        classdiv_label=Label(current_frame,text='Batch',font=('times new roman',10,'bold'),bg='white')
        classdiv_label.grid(row=4,column=2,padx=5,pady=5,sticky=W)

        classdiv_entry=ttk.Combobox(current_frame,textvariable=self.div_var,font=('times new roman',10,'bold'),width=19,state='readonly')
        classdiv_entry['values']=('Select Batch','A','B','C')
        classdiv_entry.current(0)
        classdiv_entry.grid(row=4,column=3,padx=5,pady=5,sticky=W)

        #DOB
        dob_label=Label(current_frame,text='DOB',font=('times new roman',10,'bold'),bg='white')
        dob_label.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        dob_entry=ttk.Entry(current_frame,textvariable=self.dob_var,width=25,font=('times new roman',10))
        dob_entry.grid(row=5,column=1,padx=5,pady=5,sticky=W)

        #Phone no
        phoneno_label=Label(current_frame,text='Phone No.',font=('times new roman',10,'bold'),bg='white')
        phoneno_label.grid(row=5,column=2,padx=5,pady=5,sticky=W)

        phoneno_entry=ttk.Entry(current_frame,textvariable=self.phone_var,width=25,font=('times new roman',10))
        phoneno_entry.grid(row=5,column=3,padx=5,pady=5,sticky=W)

        #Address
        address_label=Label(current_frame,text='Address',font=('times new roman',10,'bold'),bg='white')
        address_label.grid(row=6,column=0,padx=5,pady=5,sticky=W)

        address_entry=ttk.Entry(current_frame,textvariable=self.address_var,width=25,font=('times new roman',10))
        address_entry.grid(row=6,column=1,padx=5,pady=5,sticky=W)

        #Teacher name
        teachername_label=Label(current_frame,text='Teacher Name',font=('times new roman',10,'bold'),bg='white')
        teachername_label.grid(row=6,column=2,padx=5,pady=5,sticky=W)

        teachername_entry=ttk.Entry(current_frame,textvariable=self.teacher_var,width=25,font=('times new roman',10))
        teachername_entry.grid(row=6,column=3,padx=5,pady=5,sticky=W)

        #Creating radio button(s) [modified in student_modified]
        self.radio1_var=StringVar()
        Take_or_Not_label=Label(current_frame,text='Take Photo Sample?',font=('times new roman',10,'bold'),bg='white')
        Take_or_Not_label.grid(row=7,column=0,padx=5,pady=5,sticky=W)

        radio_btn1=CTkRadioButton(current_frame,width=50,border_width_unchecked=1,radiobutton_height=10,radiobutton_width=10
                                  ,fg_color='green',border_color='black',text_color='black'
                                  ,variable=self.radio1_var,text='Yes',font=('times new roman',12,'bold'),value='Yes')
        radio_btn1.grid(row=7,column=1,padx=5,pady=5,sticky=W)

        radio_btn2=CTkRadioButton(current_frame,width=50,border_width_unchecked=1,radiobutton_height=10,radiobutton_width=10
                                  ,fg_color='red',border_color='black',text_color='black'
                                  ,variable=self.radio1_var,text='No',font=('times new roman',12,'bold'),value='No')
        radio_btn2.grid(row=7,column=2,padx=5,pady=5,sticky=W)

        #Creating a frame1 for buttions
        button_frame1=Frame(current_frame,relief=RIDGE,bg='white')
        button_frame1.place(x=0,y=250,width=570,height=35)

        #save button
        save_button=CTkButton(button_frame1,command=self.add_data,text='Save without photos',width=283,height=31,font=('times new roman',15),fg_color='green',corner_radius=8,bg_color='white',text_color='white',hover_color='#5bb450')
        save_button.grid(row=0,column=0,padx=0,pady=0)

        #button to take photo
        take_button=CTkButton(button_frame1,command=self.generate_dataset,text='Take photo and Save',width=284,height=31,font=('times new roman',15),fg_color='green',corner_radius=8,bg_color='white',text_color='white',hover_color='#5bb450')
        take_button.grid(row=0,column=1,padx=0,pady=0)
        
    
    #_____FUNCTIONS DECLARATION______
    #_____________for back button_________
    def back_button(self):
        self.root.destroy()
        self.main_root.deiconify()

    #______to save data without taking photo samples______
    def add_data(self):
        if self.dep_var.get()=='Select Department' or self.name_var.get()=='' or self.std_id_var.get()=='':
            messagebox.showerror('Error','All fields are required',parent=self.root)
        else:
            try:
                connection=mysql.connector.connect(host="localhost", username="root",password="khanskmk",database="face_recognition_sys")
                cursor_my=connection.cursor()
                cursor_my.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.name_var.get(),
                                self.dep_var.get(),
                                self.year_var.get(),
                                self.course_var.get(),
                                self.sem_var.get(),
                                self.std_id_var.get(),
                                self.roll_no_var.get(),
                                self.gendre_var.get(),
                                self.email_var.get(),
                                self.div_var.get(),
                                self.dob_var.get(),
                                self.phone_var.get(),
                                self.address_var.get(),
                                self.teacher_var.get(),
                                self.radio1_var.get()
                                ))
                connection.commit()
                connection.close()
                messagebox.showinfo("Succeed","Your data has been saved",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)

    #_____to save data with taking photo samples
    def generate_dataset(self):
        if self.dep_var.get() == 'Select Department' or self.name_var.get() == '' or self.std_id_var.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=self.root)
        else:
            try:
                connection = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="khanskmk",
                    database="face_recognition_sys"
                )
                cursor_my = connection.cursor()
                cursor_my.execute("INSERT INTO student (Student_Id, Name, Department, Course, Year, Semester, Roll_No, Gender, Email, Division, DoB, Phone, Address, Teacher, Photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (self.std_id_var.get(), self.name_var.get(), self.dep_var.get(), self.course_var.get(),
                                self.year_var.get(), self.sem_var.get(), self.roll_no_var.get(), self.gendre_var.get(),
                                self.email_var.get(), self.div_var.get(), self.dob_var.get(), self.phone_var.get(),
                                self.address_var.get(), self.teacher_var.get(), self.radio1_var.get()))

                connection.commit()
                connection.close()

                if self.radio1_var.get() == 'Yes':
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            cropped_img = img[y:y + h, x:x + w]
                            return cropped_img
                        
                    
                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    

                    while True:
                        ret, my_frame = cap.read()
                        if face_cropped(my_frame) is not None:
                            img_id += 1
                            face = cv2.resize(face_cropped(my_frame), (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_path = "stored_pictures/user_" + str(self.std_id_var.get()) + "_" + str(img_id) + ".jpg"
                            cv2.imwrite(file_path, face)

                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255), 2)
                            cv2.imshow("Cropped Face", face)


                        if cv2.waitKey(1) == 13 or int(img_id) == 50:
                            break

                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Dataset has been generated", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj2 = Student1(root,root)
    root.mainloop()