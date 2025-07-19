import tkinter as tk
from tkinter import messagebox

word_dict = {}

# 함수 정의
def add_word():
    word = entry_word.get().strip()
    meaning = entry_meaning.get().strip()
    if word and meaning:
        word_dict[word] = meaning
        messagebox.showinfo("등록 성공", f"'{word}'가 등록되었습니다.")
        entry_word.delete(0, tk.END)
        entry_meaning.delete(0, tk.END)
    else:
        messagebox.showwarning("입력 오류", "단어와 뜻을 모두 입력하세요.")

def search_word():
    word = entry_search.get().strip()
    meaning = word_dict.get(word)
    if meaning:
        messagebox.showinfo("단어 검색", f"{word}: {meaning}")
    else:
        messagebox.showerror("검색 실패", f"'{word}'는 등록되지 않았습니다.")

def show_all_words():
    if not word_dict:
        messagebox.showinfo("단어 목록", "등록된 단어가 없습니다.")
    else:
        all_words = "\n".join([f"{word}: {meaning}" for word, meaning in word_dict.items()])
        messagebox.showinfo("단어 목록", all_words)

def exit_program():
    root.destroy()

# 윈도우 설정
root = tk.Tk()
root.title("📘 단어장 프로그램")
root.geometry("400x300")

# 단어 등록 영역
tk.Label(root, text="단어:").pack()
entry_word = tk.Entry(root)
entry_word.pack()

tk.Label(root, text="뜻:").pack()
entry_meaning = tk.Entry(root)
entry_meaning.pack()

tk.Button(root, text="단어 등록", command=add_word).pack(pady=5)

# 단어 검색 영역
tk.Label(root, text="검색할 단어:").pack()
entry_search = tk.Entry(root)
entry_search.pack()

tk.Button(root, text="단어 찾기", command=search_word).pack(pady=5)

# 기타 기능
tk.Button(root, text="단어 목록 보기", command=show_all_words).pack(pady=5)
tk.Button(root, text="프로그램 종료", command=exit_program).pack(pady=10)

# 메인 루프 실행
root.mainloop()