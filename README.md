import tkinter as tk

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Секундомер")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.running = False
        self.seconds = 0

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 32))
        self.label.pack(pady=20)

        self.start_stop_btn = tk.Button(root, text="Старт", font=("Helvetica", 14), command=self.toggle)
        self.start_stop_btn.pack()

        self.reset_btn = tk.Button(root, text="Сброс", font=("Helvetica", 14), command=self.reset)
        self.reset_btn.pack(pady=10)
        self.reset_btn.pack_forget()  # скрываем по умолчанию

        self.update_timer()

    def format_time(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    def update_timer(self):
        if self.running:
            self.seconds += 1
            self.label.config(text=self.format_time())
        else:
            self.label.config(text=self.format_time())
        
        # Показываем/скрываем кнопку Сброс
        if self.seconds > 0:
            self.reset_btn.pack()
        else:
            self.reset_btn.pack_forget()

        self.root.after(1000, self.update_timer)

    def toggle(self):
        self.running = not self.running
        self.start_stop_btn.config(text="Стоп" if self.running else "Старт")

    def reset(self):
        self.running = False
        self.seconds = 0
        self.label.config(text="00:00:00")
        self.start_stop_btn.config(text="Старт")
        self.reset_btn.pack_forget()

if __name__ == "__main__":
