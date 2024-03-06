import re
from Exceptions.exception import IndexListException
from Model.listNotes import ListNotes


def validation_note_number(notes: ListNotes, number: int) -> bool:
    for obj in notes.get_notes():
        if getattr(obj, 'id') == number:
            return True
    raise IndexListException()


def validation_data(data: str) -> bool:
    patterns = [r'^(29.02.(2000|2400|2800|(19|2[0-9])(0[48]|[2468][048]|[13579][26])))$',
                r'^((0[1-9]|1[0-9]|2[0-8]).02.((19|2[0-9])[0-9]{2}))$',
                r'^((0[1-9]|[12][0-9]|3[01]).(0[13578]|10|12).((19|2[0-9])[0-9]{2}))$',
                r'^((0[1-9]|[12][0-9]|30).(0[469]|11).((19|2[0-9])[0-9]{2}))$']
    for pattern in patterns:
        matches = re.fullmatch(pattern, data, re.IGNORECASE)
        if matches:
            return True
    return False
