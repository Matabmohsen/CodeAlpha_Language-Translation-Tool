from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry('1100x420')
root.resizable(0, 0)
root['bg'] = 'lightblue'
root.title('Translator')

Label(root, text="Language Translator", font="Arial 20 bold", bg='white smoke').pack()

Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=30, y=90)
Input_text = Entry(root, width=50, font='arial 10', bd=2)
Input_text.place(x=30, y=130, height=80)

Label(root, text="Translated Text", font='arial 13 bold', bg='white smoke').place(x=600, y=90)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

language_list = list(LANGUAGES.values())
    
# Style configuration for Combobox dropdown
style = ttk.Style()
style.configure('Custom.TCombobox', padding=5, font=('Arial', 10), background='white')

src_lang = ttk.Combobox(root, values=language_list, width=23, style='Custom.TCombobox')
src_lang.place(x=30, y=240)
src_lang.set('Choose Input Language')

dest_lang = ttk.Combobox(root, values=language_list, width=23, style='Custom.TCombobox')
dest_lang.place(x=600, y=240)
dest_lang.set('Choose Output Language')

def Translate():
    text = Input_text.get()
    inp_lang = src_lang.get()
    out_lang = dest_lang.get()
    
    if inp_lang == 'Choose Source Language' or out_lang == 'Choose Destination Language':
        Output_text.delete(1.0, END)
        Output_text.insert(END, "Please select both source and destination languages.")
        return
    
    try:
        translator = Translator()
        translation = translator.translate(text, src=inp_lang, dest=out_lang)
        Output_text.delete(1.0, END)
        Output_text.insert(END, translation.text)
    except Exception as e:
        Output_text.delete(1.0, END)
        Output_text.insert(END, f"Translation error: {e}")

trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='black', fg='white', activebackground='green')
trans_btn.place(x=445, y=180)

root.mainloop()
