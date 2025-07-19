word_dict = {}

while True:
    print("\n[1] 단어 등록 [2] 단어 찾기 [3] 단어 목록 보기 [4] 종료")
    choice = input("메뉴를 선택하세요: ")

    if choice == '1':
        word = input("등록할 단어: ")
        meaning = input(f"{word}의 뜻: ")
        word_dict[word] = meaning
        print(f"'{word}' 단어가 등록되었습니다.")
    
    elif choice == '2':
        word = input("찾을 단어: ")
        if word in word_dict:
            print(f"{word}: {word_dict[word]}")
        else:
            print("등록되지 않은 단어입니다.")
    
    elif choice == '3':
        if not word_dict:
            print("등록된 단어가 없습니다.")
        else:
            print("등록된 단어 목록:")
            for word, meaning in word_dict.items():
                print(f"{word}: {meaning}")
    
    elif choice == '4':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("⚠️ 잘못된 입력입니다. 1~4 사이 숫자를 입력하세요.")


friends = set()

while True:
    action = input("\n[1] 친구 추가 [2] 친구 확인 [3] 친구 목록 보기 [4] 종료: ")

    if action == '1':
        name = input("추가할 친구 이름: ")
        if name in friends:
            print(f"{name}은 이미 친구입니다.")
        else:
            friends.add(name)
            print(f"{name}을 친구로 추가했습니다.")

    elif action == '2':
        name = input("확인할 친구 이름: ")
        if name in friends:
            print(f"{name}은 친구 목록에 있습니다.")
        else:
            print(f"{name}은 친구가 아닙니다.")

    elif action == '3':
        print("📜 친구 목록:")
        for f in friends:
            print(f)

    elif action == '4':
        break