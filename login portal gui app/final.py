from tkinter import *
import tkinter.messagebox
fh = open('userdata.txt','w')
window=Tk()
window.title("USER LOGIN")
window.geometry('350x200+100+120')
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
#v2.set("pass@123")
def logedin():
    e1.setvar(e1.get())
    e2.setvar(e1.get())
def login():
    userid = e1.get()
    password = e2.get()
    if (userid == "8421296860" or userid == "981410142432") and (password == "pass@123" or password == "bhushan" or password == "vaishnavi") :
        tkinter.messagebox.showinfo('Login alert','Login successful')
        ans = tkinter.messagebox.askyesno('LOGIN','Do you want to exit')
        if ans == 1: window.destroy()
        #l4=Label(window,text="LOGIN SUCCESSFUL....",fg='green').grid(row=7,column=1)

        email = Tk()
        email.title('Email')
        email.geometry('500x200+500+200')
        l5 = Label(email,text='+Compose',fg='red',font=('comic sans ms',30,'bold'))
        l5.grid(row=0,column=1)
        l6 = Label(email,text=' Email ID ',fg='red',font=('comic sans ms',10,'bold'))
        l6.grid(row=1,column=0)
        e6 = Entry(email,bg='white',fg='green',width=50,bd=3)
        e6.grid(row=1,column=1)
        e6.bind('<Return>') or e6.bind('<Tab>') or e6.bind('<Leave>')
        l7 = Label(email,text=' Message ',fg='red',font=('comic sans ms',10,'bold'))
        l7.grid(row=2,column=0)
        e7 = Entry(email,bg='white',fg='blue',bd=3,width=50)
        e7.grid(row=2,column=1,padx=0,pady=10)
        e7.bind('<Return>') or e7.bind('<Tab>') or e7.bind('<Leave>')
        def send():
            import smtplib, ssl
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "bhushansdeshmukh@coep.sveri.ac.in"
            receiver_email = e6.get()
            pwd = "BD@981410142432"
            message =  e7.get()
            fh.write(receiver_email+'  message- '+ message + '\n')

            
            e7.delete(0,END)

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                 server.ehlo()  # Can be omitted
                 server.starttls(context=context)
                 server.ehlo()  # Can be omitted
                 server.login(sender_email,pwd)
                 server.sendmail(sender_email, receiver_email, message)
                 ans = tkinter.messagebox.askyesno('SENT','Do you want to exit')
                 
                 if ans == 1: email.destroy()   
        b2=Button(email,text='SEND',fg='white',bg='red',font=('comic sans ms',10,'bold'),command=send)
        b2.grid(row=3,column=1)

        
        

    else:
        tkinter.messagebox.showerror('Login alert', 'login failed')
        ans = tkinter.messagebox.askyesno('LOGIN', 'Do you want to exit')
        if ans == 1:
            window.destroy()
        #l4=Label(window,text='Invalid userid or password',fg='red').grid(row=6,column=1)
b1=Button(window,text='LOGIN',bg='gold',fg='black',font=('comic',12,'bold'),command=login).grid(row=5,column=1)
cb1=Checkbutton(window,text='Keep me Loged in',fg='black',command=logedin,bg='green')
cb1.grid(row=6,column=1)

window.mainloop()

