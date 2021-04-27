import rsync

if __name__ == '__main__':
   output = rsync.file('HUGE_FILE_new.txt', 'HUGE_FILE_old.txt')
with open('HUGE_FILE_old.txt', 'a') as ft:
   ft.write(output)
