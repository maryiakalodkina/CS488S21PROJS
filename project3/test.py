import rsync

if __name__ == '__main__':
    rsync.file('foo.txt', 'bar.txt')
