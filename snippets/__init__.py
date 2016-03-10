from pony.orm import select, Entity, PrimaryKey, Required


class Person(Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)

persons = select(p for p in Person if p.age > 20)[:]


root_dir = "./music"
file_mask = ".*\\.mp3"
rules = ...


Artist = "Metallica"
Genre = "Rock"


WITH       'WITH
VALUE       '".*\\.mp3"
IN       'IN'
VALUE       '"./music"'
SET       'SET'
ATTRIBUTE       'Artist'
EQUALS       '='
VALUE       '"Metallica"'
SET       'SET'
ATTRIBUTE       'Genre'
EQUALS       '='
VALUE       '"Rock"'