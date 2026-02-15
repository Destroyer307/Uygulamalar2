import tkinter as tk
import instaloader
from tkinter import ttk , messagebox

def get_user_info(username):
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context,username)

    user_info ={
        "Username" : profile.username,
        "Followers" : profile.followers,
        "Followees" : profile.followees,
        "Post Count" : profile.mediacount,
        "Last Post Date" : get_last_post_date(profile)
    }
    return user_info


# kullanıcının son gönderi tarihini çekme
def get_last_post_date(profile):
    last_post = None
    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            last_post = post
    return last_post.date_utc.strftime("%Y-%m-%d %H:%M:%S")


def show_user():
    username = entry_username.get()
    user_info = get_user_info(username)
    if isinstance(user_info,dict):
        for widget in tree.get_children():
            tree.delete(widget)

        tree.insert("","end",values = (
            user_info["Username"],
            user_info["Followers"],
            user_info["Followees"],
            user_info["Post Count"],
            user_info["Last Post Date"]
        ))
    else:
        messagebox.showerror("Hata",user_info)

# tkinter arayüzü
root = tk.Tk()
root.title("Kullanıcı Bilgi Görüntüleyicisi")

frame = tk.Frame(root)
frame.pack(padx=25,pady=25)

# kullanıcı adı 
Label = tk.Label(frame,text="kullanıcı adı :")
Label.grid(row=0 , column=0 , padx=10 , pady=10)

#kullanıcı adı giriş kutusu
entry_username = tk.Entry(frame)
entry_username.grid(row=0 , column=1 , padx=10 , pady=10)


search_button = tk.Button(frame , text="Bilgileri görüntüle" , command=show_user)
search_button.grid(row=2,column=2,padx=10,pady=10)


# bilgi tablosu 
tree = ttk.Treeview(root , columns=("Username","Followers","Followees","Post Count","Last Post Date"))
tree.heading("Username",text="kullanıcı adı :")
tree.heading("Followers",text="takipçiler :")
tree.heading("Followees",text="takip edilenler :")
tree.heading("Post Count",text="gönderi sayısı :")
tree.heading("Last Post Date",text="Son gönderi tarihi :")
tree.pack(padx=20,pady=20)


root.mainloop()