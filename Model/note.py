class Note:

    def __init__(self, data_note: dict) -> None:
        self.id = data_note['id']
        self.title = data_note['title']
        self.text = data_note['text']
        self.data = data_note['data']

    def __repr__(self) -> str:
        return f'id {self.id}\nНазвание: {self.title}\n{self.text}\nДата: {self.data}\n'
