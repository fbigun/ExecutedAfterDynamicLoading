import os
import glob


BASEDIR = os.path.dirname(os.path.abspath(__file__))

pythonfiles = glob.glob(BASEDIR + os.sep + '*.py')

mods = []

for filefullpath in pythonfiles:
    basedir, file = os.path.split(filefullpath)
    fn, suffix = os.path.splitext(file)
    if fn == '__init__':
        continue
    mods.append(fn)
    __import__('task', globals(), locals(), [fn])


__all__ = mods