import socket
import sys
import collections
import hashlib
import zlib
import os
import fnmatch

ServerName = sys.argv[1]
ServerPort = int(sys.argv[2])
ServerAddress = (ServerName, ServerPort)

#old_file = sys.argv[3]
#dir2 = sys.arg[4]


BLOCK_SIZE = 1024
output = ''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    clientSocket.connect(ServerAddress)
       
    # Helper functions
# ----------------
    def md5_chunk(chunk):
    """
        Returns md5 checksum for chunk
    """
        print('------Inside md5_chunk()------')

        m = hashlib.md5()
        enc_chunk = bytes(chunk, 'utf-8')
        m.update(enc_chunk)
   # print('printing chuck:')
   # print(chunk)

        return m.hexdigest()

    def adler32_chunk(chunk):
    """
    Returns adler32 checksum for chunk
    """
        print('------Inside adler32_chunk()------')
#    print('printing chunk:')
#    print(chunk)
        enc_chunk = bytes(chunk, 'utf-8')
        res = zlib.adler32(enc_chunk)
        return res

Signature = collections.namedtuple('Signature', 'md5 adler32') #Declaring named tuple

    class Chunks(object):
    """
    Data stucture that holds rolling checksums for file B
    """
        def __init__(self):
            self.chunks = []
            self.chunk_sigs = {}

        def append(self, sig):
            self.chunks.append(sig)
            self.chunk_sigs.setdefault(sig.adler32, {})
            self.chunk_sigs[sig.adler32][sig.md5] = len(self.chunks) - 1

        def get_chunk(self, chunk):
            adler32 = self.chunk_sigs.get(adler21_chunk(chunk))

            if adler32:
                return adler32.get(md5_chunk(chunk))

            return None

        def __getitem__(self, idx):
            return self.chunks[idx]

        def __len__(self):
            return len(self.chunks)


    def checksums_file(fn):
        """
    Returns object with checksums of file
    """
        print('------Inside checksums_file()C------')
        chunks = Chunks()
        print(chunks)
        with open(fn) as f:
            while True:
                chunk = f.read(BLOCK_SIZE)
  #            print(chunk)
                if not chunk:
                    break

                print('------Entering chunks.append() call inside checksums_file()------')    
                chunks.append(
                Signature(
                    adler32=adler32_chunk(chunk),
                    md5=md5_chunk(chunk)
                )
            )
        print('------Exiting chunks.append() call inside checksums_file()------')
        return chunks

serv_list = []
#credit to https://realpython.com/working-with-files-in-python/
for file_name in os.listdir('dir1/'):
    if fnmatch.fnmatch(HUGE_FILE_old, '*.txt'):
        with open('HUGE_FILE_old.txt') as old_file:
            checksums = checksums_file(old_file)
            blocks = []
            offset = 0
            data,addr = clientSocket.recvfrom(2048) 
            while data:
                #receive from server checksums of its new_file
                list_of_blocks = clientSocket.recvfrom(2048)
                serv_list += list_of_blocks
            for element in serv_list:
                    
    else:
        


    
    
