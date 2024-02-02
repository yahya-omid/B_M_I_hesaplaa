from tkinter import *


window = Tk()
window.title("BMI calculator")
window.minsize(width=500, height=400)
#label
label1 = Label(text="BMI Calculator")
label1.config(bg="grey")
label1.config(fg="light blue")
label1.place(x=250-45,y=80)


label2 = Label(text="boyunuzu giriniz (cm)")
label2.config(fg="black")
label2.place(x=250-60,y=100)
label2.update()



label3= Label(text="kilonuzu giriniz (kg)")
label3.config(fg="black")
label3.place(x=250-60,y=160)

result_label = Label(text="BMI: ")
result_label.place(x=250-61,y=270)

def button_clicked():
    try:
     boy = float(entery1.get())
     kilo = float(entery2.get())
     bmı = BMI_hesapla(boy,kilo)

    except ValueError:
     result_label.config(text="Lütfen geçerli bir sayı girin!")


    if bmı<18.5:
         result_label.config(text=f"BMI:{bmı:.2f} çok zayfsın")

    elif 18.5<= bmı <=24.9:
         result_label.config(text=f"BMI:{bmı:.2f} normal sınız")

    elif 25<= bmı <29.9:
         result_label.config(text=f"BMI:{bmı:.2f} fazla kilolusunuz")
    else:
        if bmı >= 30:
         result_label.config(text=f"BMI:{bmı:.2f} obezsiniz ")




#entry
entery1=Entry()
entery1.place(x=250-61,y=130)

entery2=Entry()
entery2.place(x=250-61,y=190)
def BMI_hesapla(boy,kilo):
    bmı=kilo/ ((boy/100)**2)
    return bmı



#button
button=Button(text="button clicked",command=button_clicked)
button.config()
button.place(x=250-45,y=220)



window.mainloop()