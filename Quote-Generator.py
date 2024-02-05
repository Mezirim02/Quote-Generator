import tkinter as tk
import requests
from threading import Thread

api = "https://api.quotable.io/random"
quotes = []
quotes_num = 0


UI = tk.Tk()
UI.geometry("900x260")
UI.title("Quote Generator")
UI.grid_columnconfigure(0, weight=1)
UI.resizable(False, False)
UI.configure(bg="grey")


def preload_quotes():
    global quotes

    print("Loading quotes...")
    for x in range(10):
        random_quote = requests.get(api).json()
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "By " + author
        print(content)

        quotes.append(quote)

    print("Finished loading quotes!")


preload_quotes()


def g_random_quote():
    global quote_label
    global quotes
    global quotes_num
    
    quote_label.configure(text=quotes[quotes_num])
    quotes_num = quotes_num + 1
    print(quotes_num)
    
    if quotes[quotes_num] == quotes[-3]:
        thread = Thread(target=preload_quotes)
        thread.start()


quote_label = tk.Label(UI, text="Click on the button to generate a random quote", height=6, pady=15, wraplength=800, font=("Helvetica", 14))
quote_label.grid(row=0, column=0, stick="WE", padx=20, pady=10)

button = tk.Button(text="Generate", command=g_random_quote, bg="black", fg="white", activebackground="grey", font=("Helvetica", 14))
button.grid(row=1, column=0, stick="WE", padx=20, pady=10)


if __name__ == "__main__":
    UI.mainloop()
