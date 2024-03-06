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
        for note in self.list_notes:
            print(f'id: {getattr(note, "id")} - {getattr(note, "title")}')

    def __repr__(self) -> str:
        list_to_str = ''
        for note in self.list_notes:
            list_to_str += f'{note}\n'
        return list_to_str
