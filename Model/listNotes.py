from Exceptions.exception import ObjectExistsException
from Model.note import Note


class ListNotes:

    def __init__(self) -> None:
        self.list_notes = []

    def add_note(self, note: Note) -> None:
        if note == None:
            raise ObjectExistsException()
        self.list_notes.append(note)

    def get_notes(self) -> list:
        return self.list_notes

    def print_titles(self) -> None:
        id = 0
        for note in self.list_notes:
            print(f'id: {id} - {getattr(note, "title")}')
            id += 1

    def __repr__(self) -> str:
        list_to_str = ''
        id = 0
        for note in self.list_notes:
            list_to_str += f'id: {id}\n{note}\n'
            id += 1
        return list_to_str
