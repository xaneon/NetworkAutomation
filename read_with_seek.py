with open("testdatei.txt") as fid:
    fid.seek(0, 0)
    idcs = list()
    chunk_size = 10
    char = " "
    curr_chunk = True

    while curr_chunk:
        curr_chunk = fid.read(chunk_size)
        n_chars = curr_chunk.count(char)
        lidx = 0
        chlist = list()
        for i in range(n_chars):
            lidx = curr_chunk.find(char, lidx+1)
            chlist.append(lidx)
        idcs.append(chlist)
print(idcs)

