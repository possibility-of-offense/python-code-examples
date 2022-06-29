# Import dependencies
import tkinter as tk
import random

# Event handlers
def show_random_wisdom():
    val = random.choice(list(wisdoms.values()))
    show_output_lbl['text'] = val


# Init window
window = tk.Tk()

# Create a frames
flag_frm = tk.Frame(master=window)

bulgarian_flag_frm_1 = tk.Frame(master=flag_frm, height=100, width=150, bg="white")
bulgarian_flag_frm_2 = tk.Frame(master=flag_frm, height=100, width=150, bg="red")
bulgarian_flag_frm_3 = tk.Frame(master=flag_frm, height=100, width=150, bg="green")

bulgarian_flag_frm_1.pack(fill=tk.Y, side=tk.LEFT)
bulgarian_flag_frm_2.pack(fill=tk.Y, side=tk.LEFT)
bulgarian_flag_frm_3.pack(fill=tk.Y, side=tk.LEFT)
flag_frm.pack()

main_frm = tk.Frame()
main_frm.pack()

created_by_lbl = tk.Label(master=main_frm, text="Създадено от някой си!", padx=10, pady=10)
created_by_lbl.configure(font=("sans-serif", 15, "italic"))
created_by_lbl.pack()

show_wisdom_btn = tk.Button(
    text="Покажи мъдрост", 
    padx=10, 
    pady=10, 
    master=main_frm, 
    borderwidth=2, 
    relief=tk.RAISED,
    command=show_random_wisdom
)
show_wisdom_btn.configure(font=("sans-serif", 10))
show_wisdom_btn.pack()

label_text = 'Нищо не е генерирано засега'
show_output_lbl = tk.Label(text=label_text, master=main_frm)
show_output_lbl.pack()

# Main Logic

wisdoms = {
    "first": "Игра има ли?",
    "second": "Това да не е със разузнавателна цел?",
    "third": "Яко маратонки за 200 лева!"
}

window.mainloop()
