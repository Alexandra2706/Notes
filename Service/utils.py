import json

from jsonschema import validate

from Exceptions.exception import DictKeyException

from Model.listNotes import ListNotes
from Model.note import Note


schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "text": {"type": "string"},
        "data": {"type": "string"},
    },
}


def parse_json(templates: dict) -> ListNotes:
    notes = ListNotes()
    try:
        if 'notes' not in templates:
            raise DictKeyException()
        validate(templates, schema)
        for obj in templates['notes']:
            note = Note(obj)
            notes.add_note(note)
        return notes
    except (DictKeyException, Exception) as e:
        print(f'Ошибка при чтении json: {type(e).__name__} {e}')


def file_read(filename: str) -> ListNotes:
    ''' Чтение из json файла в ListNotes '''
    try:
        with open(filename) as f:
            data = f.read()
    except (FileNotFoundError, PermissionError, ValueError, Exception) as e:
        print(f'Ошибка при чтении файла {filename}: {type(e).__name__} {e}')
    try:
        return json.loads(data)
    except Exception as e:
        print(f'Ошибка разборе json: {type(e).__name__} {e}')


def file_write(filename: str, list_notes: ListNotes) -> None:
    ''' Запись в json файл '''
    list_dict = []
    for obj in list_notes.get_notes():
        list_dict.append({'title': getattr(obj, 'title'), 'author': getattr(obj, 'author'),
                          'text': getattr(obj, 'text'), 'data': getattr(obj, 'data')})
    to_json = {'notes': list_dict}
    try:
        with open(filename, 'w') as f:
            f.write(json.dumps(to_json))
    except Exception as e:
        print(f'Ошибка записи в файл: {type(e).__name__} {e}')
