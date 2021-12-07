from tkinter import *
import otp
import tkinter.messagebox
fh = open('userdata.txt','w')
window=Tk()
window.title("USER LOGIN")
window.geometry('350x250+100+120')
l1=Label(window,text=' USER LOGIN ',fg='white',bg='dark orange',font=('comic sans ms',15)).grid(row=0,column=1)
l2=Label(window,text='  USERID  ',fg='white',bg='red',font=('comic sans ms',11,'bold')).grid(row=3,column=0)
e1=Entry(window,bd=5,font=('comic sans ms',10,'bold'),fg='green')
e1.grid(row=3,column=1,padx=0,pady=5)
#v1.set("8421296860")
e1.bind('<return>') or e1.bind('<Tab>') or e1.bind('<Leave>')
l3=Label(window,text='PASSWORD',fg='white',bg='red',font=('comic sans ms',11,'bold')).grid(row=4,column=0)
e2=Entry(window,bd=5,show='*',fg='green',font=('comic sans ms',10,'bold'))
e2.grid(row=4,column=1,padx=0,pady=5)
e2.bind('<Return>') or e2.bind('<Tab>') or e2.bind('<Leave>')
l10=Label(window,text='OTP',fg='white',bg='red',font=('comic sans ms',11,'bold')).grid(row=5,column=0)
otp1=Entry(window,bd=5,show='*',fg='green',font=('comic sans ms',10,'bold'))
otp1.grid(row=5,column=1,padx=0,pady=5)
otp1.bind('<Return>') or otp1.bind('<Tab>') or otp1.bind('<Leave>')
#v2.set("pass@123")
#print(e1,e2)
name='Bhushan'
client_otp=otp.otpfunc(name)


def login():
    userid = e1.get()
    password = e2.get()
    chk_otp=otp1.get()
    print(chk_otp,client_otp)
    if (userid == "8421296860" or userid == "981410142432") and (password == "pass@123" or password == "bhushan") :
        if (chk_otp==client_otp):
            tkinter.messagebox.showinfo('Login alert','Login successful')
            ans = tkinter.messagebox.askyesno('LOGIN','Do you want to exit')
            if ans == 1: window.destroy()
        else:
            tkinter.messagebox.showerror('Login alert', 'login failed')
            ans = tkinter.messagebox.askyesno('LOGIN', 'Do you want to exit')
            if ans == 1:
                window.destroy()


       

       
        






      
        

    else:
        tkinter.messagebox.showerror('Login alert', 'login failed')
        ans = tkinter.messagebox.askyesno('LOGIN', 'Do you want to exit')
        if ans == 1:
            window.destroy()
        #l4=Label(window,text='Invalid userid or password',fg='red').grid(row=6,column=1)
b1=Button(window,text='LOGIN',bg='gold',fg='black',font=('comic',12,'bold'),command=login).grid(row=7,column=1)
window.mainloop()

