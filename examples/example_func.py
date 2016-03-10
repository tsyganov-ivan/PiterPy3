from internal.func import set, update, settings, path, mask

update(
    settings(
        path('../tests/music'),
        mask('.*\.mp3')
    ),
    set(Artist='Metallica'),
    set(Genre='Rock')
)

update(
    settings(
        path='../tests/music',
        mask='.*\.mp3'
    ),
    set(Artist='Metallica'),
    set(Genre='Rock')
)



