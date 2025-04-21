import tkinter as tk
import random
import string

# Генерация одного пароля
def create_password(name_parts, birth_parts):
    symbols = "!@#$%^&*_-+="
    name = random.choice(name_parts)
    birth = ''.join(random.sample(birth_parts, k=4))  # случайные 4 цифры из даты
    sym = ''.join(random.choices(symbols, k=2))
    rand_letters = ''.join(random.choices(string.ascii_letters, k=2))
    return f"{name}{birth}{sym}{rand_letters}"

# Генерация 10 уникальных паролей
def generate_passwords():
    full_name = name_entry.get().strip()
    birth_date = dob_entry.get().strip().replace('-', '')

    output.delete("1.0", tk.END)

    if not full_name or not birth_date:
        output.insert(tk.END, "⚠️ Пожалуйста, введите ФИО и дату рождения.\n")
        return

    name_parts = full_name.split()
    passwords = []

    while len(passwords) < 10:
        pwd = create_password(name_parts, birth_date)
        if pwd not in passwords:
            passwords.append(pwd)

    for p in passwords:
        output.insert(tk.END, p + "\n")

# Интерфейс
root = tk.Tk()
root.title("Генератор паролей")
root.geometry("420x400")
root.resizable(False, False)

tk.Label(root, text="Введите ФИО:").pack(pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.pack()

tk.Label(root, text="Введите дату рождения (гггг-мм-дд):").pack(pady=5)
dob_entry = tk.Entry(root, width=40)
dob_entry.pack()

tk.Button(root, text="Сгенерировать 10 паролей", command=generate_passwords).pack(pady=10)

output = tk.Text(root, height=12, width=50, font=("Courier", 10))
output.pack(pady=5)

root.mainloop()
