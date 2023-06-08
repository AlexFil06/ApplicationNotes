import view
import data


def start():
    while True:
        choice = view.menu()
        if choice == '1':
            data.add_note()
        elif choice == '2':
            data.read_all_notes()
        elif choice == '3':
            data.read_note()
        elif choice == '4':
            data.edit_note()
        elif choice == '5':
            data.delete_note()
        elif choice == '0':
            break
        else:
            print('Некорректный выбор.')
