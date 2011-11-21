#!/usr/bin/env python

#from .. import utils

def simple(readers, indices, ffunc, pre, post):
    #find_extreme = utils.find_extreme(direction)
    waves = []
    main = readers[0]
    for index in indices:
        wave = []
        start = index - pre
        length = pre + post
        main.seek(start)
        data = ffunc(main.read_frames(length))
        if len(data) != pre+post:
            del data
            continue # check length
        wave.append(data)
        del data
        for reader in readers[1:]:
            reader.seek(start)
            wave.append(ffunc(reader.read_frames(length)))
        waves.append(wave)
        del wave
    return waves
