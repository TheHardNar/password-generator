from tkinter import *
import random

window = Tk()
window.title('password generator')
window.resizable(False,False)
window.geometry('320x340')
lowercase = BooleanVar()
numbers = BooleanVar()
highercase = BooleanVar()
symbols = BooleanVar()
frame = LabelFrame(text='Symbols')
check_lowercase = Checkbutton(frame,text = 'abcdefghijklmnopqrstuvwxyz',variable=lowercase,
                              offvalue=False, onvalue=True)
check_numbers = Checkbutton(frame,text = '0123456789',variable=numbers,
                            offvalue=False, onvalue=True)
check_highercase = Checkbutton(frame,text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',variable=highercase,
                              offvalue=False, onvalue=True)
check_symbols = Checkbutton(frame,text = '!@#$%^&*(){}[]?><',variable=symbols,
                            offvalue=False, onvalue=True)
spin_lowercase = Spinbox(frame,width=4,from_=1,to_=8)
spin_highercase = Spinbox(frame,width=4,from_=1,to_=8)
spin_numbers = Spinbox(frame,width=4,from_=1,to_=8)
spin_symbols = Spinbox(frame,width=4,from_=1,to_=8)
entry = Listbox(frame,width=45,justify =CENTER,height=5)
bAutton = Button(frame,text='Generate')
frame.pack(expand=True)
check_lowercase.grid(column=0,row=0,sticky=W,pady=5,padx=10)
check_highercase.grid(column=0,row=1,sticky=W,pady=5,padx=10)
check_symbols.grid(column=0,row=2,sticky=W,pady=5,padx=10)
check_numbers.grid(column=0,row=3,sticky=W,pady=5,padx=10)
spin_lowercase.grid(column=1,row=0,sticky=E,pady=5,padx=10)
spin_highercase.grid(column=1,row=1,sticky=E,pady=5,padx=10)
spin_numbers.grid(column=1,row=3,sticky=E,pady=5,padx=10)
spin_symbols.grid(column=1,row=2,sticky=E,pady=5,padx=10)
entry.grid(column=0,columnspan=2,row=4,pady=5,padx=10)
bAutton.grid(column=0,columnspan=2,row=5,pady=5,padx=10)


def generate_password(lowercase,numbers,symbols,highercase,low,numb,symb,high):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabeta = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbolsss = '!@#$%^&*(){}[]?><'
    password = []
    ende = ''
    if lowercase == True:
        for i in range(int(low)):
            a = random.randint(0,25)
            password.append(alphabet[a])
    if numbers == True:
        for i in range(int(numb)):
            a = random.randint(0,9)
            password.append(str(a))
    if symbols == True:
        for i in range(int(symb)):
            a = random.randint(0,16)
            password.append(symbolsss[a])
    if highercase == True:
        for i in range(int(high)):
            a = random.randint(0,25)
            password.append(alphabeta[a])
    random.shuffle(password)
    for i in password:
        ende = ende + i
    password = ende
    return password
    


def generate():
    entry.delete(0,'end')
    for i in range(5):
        numberss = numbers.get()
        lowercasee = lowercase.get()
        symbolss = symbols.get()
        highercasee = highercase.get()
        low = spin_lowercase.get()
        numb = spin_numbers.get()
        symb = spin_symbols.get()
        high = spin_highercase.get()
        aa = generate_password(lowercasee, numberss,symbolss,highercasee,low,numb,symb,high)
        entry.insert('end', aa)
bAutton['command'] = generate

if __name__ == '__main__':
    window.mainloop()  