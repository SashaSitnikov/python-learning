class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)

    def __len__(self):                    # len(p)
        return len(self._songs)

    def __getitem__(self, index):         # p[0], p[1:3]
        return self._songs[index]

    def __contains__(self, song):         # "x" in p
        return song in self._songs

    def __iter__(self):                   # for song in p
        return iter(self._songs)
    
    def __repr__(self):
        return f"Songs=({self._songs})"
    
p = Playlist(["a", "b", "c"])
print(len(p))
print(p[2])
print(p[0:2])
print("c" in p)
for el in p:
    print(el, end=" ")
if not p:
    print("Плейлист пуст!")
else:
    print("Плейлист заполнен")