import os
class ColorfulPrint(object):# {{{

    """Docstring for ColorfulPrint. """

    def __init__(self):
        """nothing needs to be define """
        self.colors = {
            'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
            'blue': 34, 'magenta': 35, 'cyan': 36, 'white': 37,
        }

        self.done = '(#g)done(#)'

    def trans(self, *args, auto_end=True):
        s = ' '.join(map('{}'.format, args))
        s = s.replace('(##)', '\033[0m')
        s = s.replace('(#)', '\033[0m')
        for color, value in self.colors.items():
            color_tag = '(#%s)'%color
            s_color_tag = '(#%s)'%color[0]
            s = s.replace(color_tag, '\033[%dm'%value).\
                    replace(s_color_tag, '\033[%dm'%value)
        if auto_end:
            s = s + '\033[0m'
        return s

    def err(self, *args):
        return self('(#r)[ERR](#)', *args)

    def log(self, *args):
        return self('(#blue)[LOG](#)', *args)

    def wrn(self, *args):
        return self('(#y)[WRN](#)', *args)

    def suc(self, *args):
        return self('(#g)[SUC](#)', *args)

    def __call__(self, *args):
        print(self.trans(*args))

cp = ColorfulPrint()
# }}}


def file_stat(path):
    if os.path.isdir(path):
        return 'dir'
    if os.path.isfile(path):
        return 'file'
    if os.path.islink(path):
        return 'link'
    return None

def touchdir(path):
    dirname = os.path.dirname(path)
    file_type = file_stat(dirname)
    assert file_type in {'dir', None},\
            cp.trans('(#r)[ERR](#) father directory \'(#y){}(#)\' is neither a directory nor empty'.format(dirname))
    if file_type == None:
        os.makedirs(dirname)

    if file_stat(path):
        for i in range(1000):
            p = '{}({})'.format(path, i)
            if os.path.isdir(p) or os.path.isfile(p):
                continue
            return p
    return path


class AverageMeter(object):
    """Computes and stores the average and current value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


if __name__ == '__main__':
    cp('(#r)hi')
