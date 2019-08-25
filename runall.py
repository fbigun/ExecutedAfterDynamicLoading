mod = __import__('task')
for attr in mod.__all__:
    fn = getattr(mod, attr)
    fn.run()