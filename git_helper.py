import os
import sys

def run_command(command):
    print(f"\n>>> {command}")
    os.system(command)

def print_menu():
    print("\n" + "="*50)
    print("🔥 ГИТ-МЕНЮ (выбирай цифру и не ссы):")
    print("1. Отменить последний коммит (локально)")
    print("2. Удалить последний коммит и пуш (полный откат)")
    print("3. Проверить статус (что изменилось?)")
    print("4. Закоммитить всё и запушить")
    print("5. Принудительно перезаписать удалёнку (--force)")
    print("6. Посмотреть историю коммитов (коротко)")
    print("7. Откатить конкретный файл")
    print("8. Создать новую ветку")
    print("9. Выйти (или CTRL+C)")
    print("="*50 + "\n")

def main():
    try:
        while True:
            print_menu()
            choice = input("Твой выбор: ").strip()

            if choice == "1":
                run_command("git reset --soft HEAD~1")
                print("✅ Коммит отменён (изменения остались в staging).")
            
            elif choice == "2":
                run_command("git reset --hard HEAD~1")
                branch = input("Введи имя ветки (main/master): ").strip()
                run_command(f"git push origin {branch} --force")
                print("💀 Коммит и пуш УНИЧТОЖЕНЫ.")
            
            elif choice == "3":
                run_command("git status")
            
            elif choice == "4":
                message = input("Введи сообщение коммита: ").strip()
                run_command("git add .")
                run_command(f'git commit -m "{message}"')
                run_command("git push origin main")
                print("🚀 Залил в удалёнку.")
            
            elif choice == "5":
                branch = input("Введи ветку для --force (main/master): ").strip()
                run_command(f"git push origin {branch} --force")
                print("☠️ Всё перезаписано. Надеюсь, ты уверен.")
            
            elif choice == "6":
                run_command("git log --oneline")
            
            elif choice == "7":
                file = input("Введи имя файла для отката: ").strip()
                run_command(f"git checkout -- {file}")
                print(f"♻️ Файл {file} откачен.")
            
            elif choice == "8":
                branch = input("Введи имя новой ветки: ").strip()
                run_command(f"git checkout -b {branch}")
                print(f"🌿 Ветка {branch} создана.")
            
            elif choice == "9":
                print("Выходим... (или жми CTRL+C, если застрял)")
                break
            
            else:
                print("🚫 Нет такого варианта, читай внимательно.")
    
    except KeyboardInterrupt:
        print("\n💩 Вылетел по CRTL+C. Так даже быстрее.")

if __name__ == "__main__":
    main()