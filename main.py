from tkinter import *
from tkinter import messagebox
import base64
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


window = Tk()
window.title("Secret Notes")

def save_and_encryt():
    title = title_entry.get()
    secret = secret_text.get(1.0,END)
    key = key_entry.get()

    if len(title) == 0 or len(secret) == 0 or len(key) ==0:
        messagebox.showinfo(title="Error",message="Please enter all info")
    else:
        message_encrypted = encode(key,secret)
        try:
            with open("mysecret.txt","a") as file:
                file.write(f"\n{title}\n{message_encrypted}")
        except FileNotFoundError:
            with open("mysecret.txt","w") as file:
                file.write(f"\n{title}\n{message_encrypted}")
        finally:
            title_entry.delete(0,END)
            secret_text.delete("1.0",END)
            key_entry.delete(0,END)

def decrypt_notes():
    message_encrypted = secret_text.get("1,0",END)
    master_secret = key_entry.get()

    if len(message_encrypted) == 0 or len(master_secret) ==0:
        messagebox.showinfo(title="Error!",message="Please enter all info.")
    else:
        try:
            decrypt_message = decode(master_secret,message_encrypted)
            secret_text.delete("1.0",END)
            secret_text.insert("1.0",decrypt_message)
        except:
            messagebox.showinfo(title="Error!",message="Please enter encrypted text!")













photo = PhotoImage(file="top-secret.png")
photo_label = Label(image=photo)
photo_label.pack()

title_label = Label(text="Enter your title")
title_label.config(pady=10,padx=10)
title_label.pack()

title_entry = Entry()
title_entry.pack()

secret_label = Label(text="Enter your secret")
secret_label.pack()

secret_text = Text()
secret_text.pack()

key_label = Label(text="Enter master key")
key_label.pack()

key_entry = Entry()
key_entry.pack()

save_button = Button(text="Save & Encrypt",command=save_and_encryt)
save_button.pack()

decrypt_button = Button(text="Decrypt",command=decrypt_notes)
decrypt_button.pack()




window.mainloop()
