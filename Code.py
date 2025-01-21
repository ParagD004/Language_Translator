from tkinter import *
from tkinter import ttk
from deep_translator import GoogleTranslator
import threading

root = Tk()
root.geometry('900x500')
root['bg'] = '#ffafcc'
root.resizable(0,0)
root.title('Language Translator by Parag Dharmik')

Label(root, text="Languages Translator", font="Arial 25 bold").pack()
Label(root, text="Enter text", font='arial 13 bold', bg='white smoke').place(x=250, y=150)
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=180)

Label(root, text="Output", font='arial 15 bold', bg='white smoke').place(x=650, y=150)
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, width=60)
Output_text.place(x=450, y=200)

# Get available languages
languages = GoogleTranslator().get_supported_languages()
dest_lang = ttk.Combobox(root, values=languages, width=22)
dest_lang.place(x=250, y=300)
dest_lang.set('choose languages')

def translate_text():
    try:
        text = Input_text.get()
        dest = dest_lang.get()
        
        if not text:
            Output_text.delete(1.0, END)
            Output_text.insert(END, "Please enter text to translate")
            return
            
        if dest == 'choose languages':
            Output_text.delete(1.0, END)
            Output_text.insert(END, "Please select a target language")
            return
            
        # Run translation in a separate thread
        def do_translation():
            try:
                translator = GoogleTranslator(target=dest)
                translated_text = translator.translate(text)
                # Update UI in the main thread
                root.after(0, lambda: update_output(translated_text))
            except Exception as e:
                root.after(0, lambda: update_output(f"Translation error: {str(e)}"))
                
        threading.Thread(target=do_translation).start()
        
    except Exception as e:
        Output_text.delete(1.0, END)
        Output_text.insert(END, f"Error: {str(e)}")

def update_output(text):
    Output_text.delete(1.0, END)
    Output_text.insert(END, text)

trans_btn = Button(root, text='Translate', font='arial 15 bold', pady=5, command=translate_text, bg='orange', activebackground='green')
trans_btn.place(x=300, y=400)

root.mainloop()
