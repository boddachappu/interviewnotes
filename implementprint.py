import sys


def vinod(*args, sep=' ', end='\n', file=None, flush=False):
    r"""print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    """
    fp = file
    if fp is None:
        fp = sys.stdout
        if fp is None:
            return
    if sep is None:
        sep = ' '
    if not isinstance(sep, str):
        raise TypeError("sep must be None or a string")
    if end is None:
        end = '\n'
    if not isinstance(end, str):
        raise TypeError("end must be None or a string")
    if len(args) == 1:
        fp.write(str(args[0]))
    else:
        for i, arg in enumerate(args):
            if i:
                fp.write(sep)
            fp.write(str(arg))
    fp.write(end)
    if flush:
        fp.flush()


vinod(1, 2)
