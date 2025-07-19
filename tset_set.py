import tkinter as tk
from tkinter import messagebox

friends = set()

# 함수 정의
def add_friend():
    name = entry_friend.get().strip()
    if not name:
        messagebox.showwarning("입력 오류", "친구 이름을 입력하세요.")
        return
    if name in friends:
        messagebox.showinfo("이미 존재", f"{name}은 이미 친구입니다.")
    else:
        friends.add(name)
        messagebox.showinfo("추가 완료", f"{name}을 친구로 추가했습니다.")
    entry_friend.delete(0, tk.END)

def check_friend():
    name = entry_friend.get().strip()
    if not name:
        messagebox.showwarning("입력 오류", "확인할 이름을 입력하세요.")
        return
    if name in friends:
        messagebox.showinfo("친구 확인", f"{name}은 친구 목록에 있습니다.")
    else:
        messagebox.showinfo("친구 확인", f"{name}은 친구가 아닙니다.")
    entry_friend.delete(0, tk.END)

def show_friends():
    if not friends:
        messagebox.showinfo("친구 목록", "등록된 친구가 없습니다.")
    else:
        friend_list = "\n".join(friends)
        messagebox.showinfo("친구 목록", friend_list)

def exit_program():
    root.destroy()

# UI 설정
root = tk.Tk()
root.title("👥 친구 관리 프로그램")
root.geometry("400x250")

tk.Label(root, text="친구 이름:").pack(pady=5)
entry_friend = tk.Entry(root)
entry_friend.pack()

tk.Button(root, text="친구 추가", command=add_friend).pack(pady=5)
tk.Button(root, text="친구 확인", command=check_friend).pack(pady=5)
tk.Button(root, text="친구 목록 보기", command=show_friends).pack(pady=5)
tk.Button(root, text="종료", command=exit_program).pack(pady=10)

root.mainloop()