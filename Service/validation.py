from Exceptions.exception import IndexListException
from Model.listNotes import ListNotes


def validation_note_number(notes: ListNotes, number: int) -> bool:
    if number > len(notes.get_notes()):
        raise IndexListException()
    return True
