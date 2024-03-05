class Note:

    def __init__(self, data_note: dict) -> None:
        self.title = data_note['title']
        self.author = data_note['author']
        self.text = data_note['text']
        self.data = data_note['data']

    def __repr__(self) -> str:
        return f'Название: {self.title} \nАвтор: {self.author}\n{self.text}\nДата: {self.data}\n'
