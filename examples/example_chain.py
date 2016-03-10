from internal import FileUpdater

FileUpdater().path(
    '../tests/music'
).set(Genre='Rock').set(Artist='Metallica').do()

FileUpdater().path(
    '../tests/music'
).mask('.*\.mp3').set(Genre='Rock').set(Artist='Metallica').do()
