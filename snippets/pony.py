from pony.orm import select, Entity, PrimaryKey, Required


class Person(Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)

persons = select(p for p in Person if p.age > 20)[:]

