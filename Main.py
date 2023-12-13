from add_date import add_date
from add_note import add_note
from delete_note import delete_note
from edit_note import edit_note
from load_notes import load_notes
from save_notes import save_notes
from sort_data import sort_data


def main():
    file_path = 'notes.json'
    notes = load_notes(file_path)

    while True:
        print('1. Вывести все заметки.')
        print('2. Добавить заметку.')
        print('3. Редактировать заметку.')
        print('4. Удалить заметку.')
        print('5. Отсортировать по дате. ')
        print('6. Выйти.')

        choice = input('Выберите действие: ')

        if choice =='1':
            if not notes:
                print('Заметок нет!')
            else:
                print('Заметки: ')
                for note in notes:
                    print(f"ID: {note['id']}")
                    print(f"Заголовок: {note['title']}")
                    print(f"Текст: {note['body']}")
                    print(f"Дата: {note['date']}")
                    print()

        elif choice == '2':
            id = int
            title = input('Введите заголовок заметки: ')
            body = input('Введите текст заметки: ')

            year = int(input('Ввод даты и времени заметки. Введите год: '))
            month = int(input('Ввод даты и времени заметки. Введите месяц (цифрами): '))
            day = int(input('Ввод даты и времени заметки. Введите день: '))
            hour = int(input('Ввод даты и времени заметки. Введите часы: '))
            minute = int(input('Ввод даты и времени заметки. Введите минуты: '))
            second = int(input('Ввод даты и времени заметки. Введите секунды: '))

            datetime_object = add_date(year, month, day, hour, minute, second)

            new_note = {
                'id': id,
                'title': title,
                'body': body,
                'date': str(datetime_object)
            }

            add_note(notes, new_note)
            save_notes(notes, file_path)

        elif choice == '3':
            note_id = int(input('Введите ID заметки для редактирования: '))
            new_title = input('Введите новый заголовок заметки: ')
            new_body = input('Введите новый текст заметки: ')

            year = int(input('Ввод новой даты и нового времени заметки. Введите год: '))
            month = int(input('Ввод новой даты и нового времени заметки. Введите месяц (цифрами): '))
            day = int(input('Ввод новой даты и нового времени заметки. Введите день: '))
            hour = int(input('Ввод новой даты и нового времени заметки. Введите часы: '))
            minute = int(input('Ввод новой даты и нового времени заметки. Введите минуты: '))
            second = int(input('Ввод новой даты и нового времени заметки. Введите секунды: '))

            new_date = str(add_date(year, month, day, hour, minute, second))

            edit_note(notes, note_id, new_title, new_body, new_date)
            save_notes(notes, file_path)

        elif choice == '4':
            note_id = int(input('Введите ID заметки для удаления: '))

            delete_note(notes, note_id)
            save_notes(notes, file_path)

        elif choice == '5':
            sort_data(notes)

            save_notes(notes, file_path)

        elif choice == '6':
            print('До свидания!')
            break

        else:
            print('Неверный выбор. Попробуйте еще раз.')

if __name__ == '__main__':
    main()



