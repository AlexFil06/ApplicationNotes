import json
import datetime



def read_notes():
    try:
        with open('notes.json', 'r', encoding='UTF-8') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = {}
    return notes

def save_notes(notes):
    with open('notes.json', 'w', encoding='UTF-8') as file:
        json.dump(notes, file)
    print('Изменения сохранены\nВозврат в главное меню')


def add_note():
    notes = read_notes()
    id = input('Введите идентификатор заметки: ')
    title = input('Введите заголовок заметки: ')
    body = input('Введите текст заметки: ')
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    notes[id] = {'title': title, 'body': body, 'date': date}
    save_notes(notes)

def read_all_notes():
    notes = read_notes()
    for id in notes:
        note = notes[id]
        print(f'ID: {id}\nЗаголовок: {note["title"]}\nТекст: {note["body"]}\nДата: {note["date"]}\n')


def read_note():
    notes = read_notes()
    id = input('Введите идентификатор заметки: ')
    if id in notes:
        note = notes[id]
        print(f'ID: {id}\nЗаголовок: {note["title"]}\nТекст: {note["body"]}\nДата: {note["date"]}\n')
    else:
        print('Заметка с таким ID не найдена\nВозврат в главное меню')

def edit_note():
    notes = read_notes()
    id = input('Введите идентификатор заметки: ')
    if id in notes:
        note = notes[id]
        print(f'Заголовок: {note["title"]}\nТекст: {note["body"]}\n')
        title = input('Введите новый заголовок заметки (оставьте пустым, чтобы не изменять): ')
        if title:
            note['title'] = title
        body = input('Введите новый текст заметки (оставьте пустым, чтобы не изменять): ')
        if body:
            note['body'] = body
        note['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes(notes)
    else:
        print('Заметка с таким ID не найдена\nВозврат в главное меню')


# функция для удаления заметки по ID
def delete_note():
    notes = read_notes()
    id = input('Введите идентификатор заметки: ')
    if id in notes:
        del notes[id]
        save_notes(notes)
    else:
        print('Заметка с таким ID не найдена.')
