import rsync

if __name__ == '__main__':
   output = rsync.file('HUGE_FILE_new.txt', 'HUGE_FILE_old.txt')
with open('HUGE_FILE_old.txt', 'w') as ft:
   ft.write(output)


#with open('HUGE_FILE_old.txt', 'rw') as ft:
#   num_of_block = int(output[0])
#   print('num_of_block is {}'.format(num_of_block))
#   print('original output:')
#   print(output)
#   output = output[1:]
#   print('output after change')
#   print(output)
   #think of what happens if it's a perfect cut 
   #=> we would delete the last block we need
#   if num_of_block is 0:
      #ft.seek(1024)
#      old_data = 1024
#   else:
      #ft.seek(num_of_block * 1024)
#      old_data = num_of_block * 1024 
#   ft.write(f.read(old_data))
#   ft.write(output[:1025])
