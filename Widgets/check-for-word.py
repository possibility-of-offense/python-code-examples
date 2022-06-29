import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image

def open_file_handle(cb):
    filepath = askopenfilename()
    word_to_check = search_for_word_ent.get()

    if not word_to_check or not filepath:
        return
    
    words_to_write = list()
    with open(filepath, mode="r", encoding="utf-8") as file_handle:
        search_for_word_ent.delete(0, tk.END)

        for line in file_handle:
            if not line.startswith(word_to_check):
                continue
            else:
                words_to_write.append(line.rstrip())

        if len(words_to_write) > 0:
            cb(words_to_write)
        else:
            search_for_word_ent.insert(0, 'Търсенета дума не беше намерена; опитайте с малка буква!')
    
    window.title(f'Документ за проверка - {filepath}')
    
def save_file(words):
    filepath = asksaveasfilename()

    if not filepath:
        return

    with open(filepath, mode="w", encoding="utf-8") as file_handle:
        main_text = f'Намерени думи: \n'
        file_handle.write(main_text)
        file_handle.write(', '.join(words))
        window.destroy()

window = tk.Tk()
window.title('Потърси за дума')
window.columnconfigure(0, minsize=60, weight=1)
window.rowconfigure([0, 1], weight=1)

frame = tk.Frame(window, relief=tk.RAISED)
frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
open_btn = tk.Button(
    master=frame,
    text="Отвори файл",
    command=lambda: open_file_handle(save_file),
    padx=5,
    pady=5
)

path = 'me.jpg'
image = Image.open('me.jpg')
MAX_SIZE = (200, 200)
image.thumbnail(MAX_SIZE)

img = ImageTk.PhotoImage(image)

show_image = tk.Label(master=frame, image=img)
search_for_word_lbl = tk.Label(master=frame, text="Потърси за дума; след това натисни бутона! Когато избереш файл, ще се появи втори прозорец, \nчрез който можеш да избереш къде да се запази новия файл!")
search_for_word_ent = tk.Entry(master=frame, width=100, text="Търсена дума...")

open_btn.grid(row=1, column=0, padx=10)
show_image.grid(row=3, column=1, pady=10)
search_for_word_lbl.grid(row=1, column=1, pady=5)
search_for_word_lbl.configure(font=("sans-serif", 10, 'italic'))
search_for_word_ent.grid(row=2, column=1, sticky="snwe", padx=10)

window.mainloop()