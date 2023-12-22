import tkinter as tk

class Commands:
    @staticmethod
    def help():
        help_text.delete(1.0, tk.END)  # Очистка текстового поля
        help_text.insert(tk.END, "Available Commands:\n")
        help_text.insert(tk.END, "1. add-contact <name> <address> <phone> <email> <birthday>\n")
        help_text.insert(tk.END, "2. add-phone <name> <phone>\n")
        help_text.insert(tk.END, "3. add-email <name> <email>\n")
        help_text.insert(tk.END, "4. add-address <name> <address>\n")
        help_text.insert(tk.END, "5. add-birthday <name> <birthday>\n")
        help_text.insert(tk.END, "6. edit-phone <name> <old_phone> <new_phone>\n")
        help_text.insert(tk.END, "7. edit-email <name> <old_email> <new_email>\n")
        help_text.insert(tk.END, "8. edit-address <name> <new_address>\n")
        help_text.insert(tk.END, "9. edit-birthday <name> <new_birthday>\n")
        help_text.insert(tk.END, "10. show-all\n")
        help_text.insert(tk.END, "11. show-phone <name>\n")
        help_text.insert(tk.END, "12. show-email <name>\n")
        help_text.insert(tk.END, "13. show-address <name>\n")
        help_text.insert(tk.END, "14. show-birthday <name>\n")
        help_text.insert(tk.END, "15. delete-contact <name>\n")
        help_text.insert(tk.END, "16. delete-phone <name> <phone>\n")
        help_text.insert(tk.END, "17. delete-email <name> <email>\n")
        help_text.insert(tk.END, "18. delete-address <name>\n")
        help_text.insert(tk.END, "19. delete-birthday <name>\n")
        help_text.insert(tk.END, "20. birthday\n")
        help_text.insert(tk.END, "21. exit\n")
        help_text.insert(tk.END, "22. help\n")

root = tk.Tk()
root.title("Help")

# Створення тексового поля для відображення допомоги
help_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
help_text.pack()

# Додавання кнопкі для виклику допомоги
help_button = tk.Button(root, text="Help", command=Commands.help)
help_button.pack()

# Налаштування зеленого кольору для тексту
help_text.config(fg="green")

root.mainloop()
