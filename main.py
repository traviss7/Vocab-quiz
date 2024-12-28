import requests
import random
import tkinter as tk
from tkinter import messagebox

# 예시 단어 리스트
words = ["study", "learn", "read", "write", "speak"]

def translate_to_korean(word):
    url = "https://libretranslate.de/translate"
    payload = {
        'q': word,
        'source': 'en',
        'target': 'ko',
        'format': 'text'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return result.get('translatedText', "번역 실패")
    else:
        print("API 요청 실패:", response.status_code)
        return None

def quiz():
    global current_word, correct_meaning
    current_word = random.choice(words)
    correct_meaning = translate_to_korean(current_word)
    if correct_meaning:
        word_label.config(text=f"단어: {current_word}")
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("오류", "번역을 가져올 수 없습니다. 다시 시도하세요.")

def check_answer():
    user_input = entry.get().strip()
    if correct_meaning and user_input == correct_meaning:
        messagebox.showinfo("결과", "정답입니다!")
    else:
        messagebox.showinfo("결과", f"틀렸습니다. 정답은 {correct_meaning}입니다.")

import requests

import requests

import requests

def test_libretranslate():
    url = "https://libretranslate.de/translate"
    payload = {
        'q': 'hello',
        'source': 'en',
        'target': 'ko',
        'format': 'text'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, json=payload, headers=headers, verify=False)  # SSL 검증 비활성화
    if response.status_code == 200:
        result = response.json()
        print("번역 결과:", result.get('translatedText', '번역 실패'))
    else:
        print(f"서버 응답 오류: {response.status_code}")

test_libretranslate()

# 메인 윈도우 설정
root = tk.Tk()
root.title("영어 단어 암기 앱")

# 단어 표시 레이블
word_label = tk.Label(root, text="단어: ", font=("Arial", 16))
word_label.pack(pady=10)

# 사용자 입력 필드
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# 확인 버튼
check_button = tk.Button(root, text="확인", font=("Arial", 14), command=check_answer)
check_button.pack(pady=10)

# 다음 단어 버튼
next_button = tk.Button(root, text="다음 단어", font=("Arial", 14), command=quiz)
next_button.pack(pady=10)

# 첫 퀴즈 시작
quiz()

# GUI 루프 시작
root.mainloop()


# 시나리오 
# 1. 영어 단어를 입력하면 우리말로 해설을 보여준다.
# 2. 해설을 입력하면 뜻이 맞으면, 정답입니다. 하고 메세지를 보여주고, 
# 정답이 아니면, 올바른 뜻을 보여주며, 틀렸고, 더 분발하라고 메세지를 보여줌
