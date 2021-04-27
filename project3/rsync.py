import collections
import hashlib
import zlib

#Credits to: https://tylercipriani.com/blog/2017/07/09/the-rsync-algorithm-in-python/

BLOCK_SIZE = 1024


# Helper functions
# ----------------
def md5_chunk(chunk):
    """
    Returns md5 checksum for chunk
    """
    print('------Inside md5_chunk()------')

    m = hashlib.md5()
#    m.update(chunk.encode('utf-8'))
    enc_chunk = bytes(chunk, 'utf-8')
    m.update(enc_chunk)
   # print('printing chuck:')
   # print(chunk)
       
 #   print(m.hexdigest())
    return m.hexdigest()


def adler32_chunk(chunk):
    """
    Returns adler32 checksum for chunk
    """
    print('------Inside adler32_chunk()------')
#    res = zlib.adler32(bytes(chunk, encoding='utf8')) #bytes() returns a bytes object, an object that cannot be modified & zlib.adler32 returns the unsigned 32-bit checksum integer
#    print('printing chunk:')
#    print(chunk)
    enc_chunk = bytes(chunk, 'utf-8')
#    print('printing encoded chunk')
#    print(enc_chunk)
    res = zlib.adler32(enc_chunk)
#    print(type(chunk))
#    print(type(enc_chunk))
   # print(res)
    return res
  # Checksum objects
# ----------------
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
        adler32 = self.chunk_sigs.get(adler32_chunk(chunk))

        if adler32:
            return adler32.get(md5_chunk(chunk))

        return None

    def __getitem__(self, idx):
        return self.chunks[idx]

    def __len__(self):
        return len(self.chunks)


# Build Chunks from a file
# ------------------------
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
  #          print(chunk)
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

def _get_block_list(file_one, file_two):
    print('------Inside _get_block_list()------')
    """
    The good stuff.

    1. create rolling checksums file_two
    2. for each chunk in file one, determine if chunk is already in file_two
        a. If so:
            i. return the index of that chunk
            ii. move the read head by the size of a chunk
        b. If not:
            i. return the next byte
            ii. move the read head by 1 byte
    3. start over at 2 until you're out of file to read
    """
    print('------Entering checksums_file() call inside _get_block_list()------')
    checksums = checksums_file(file_two)
    print('------Exiting checksums_file() call inside _get_block_list()------')
    print(checksums)
    blocks = []
    offset = 0
    temp_offset = 0
    count = 0
   
    with open(file_one) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            print('In file_one (new) reading 1024 bytes chunk')
            print(chunk)
            if not chunk:
                print('End of file_one')                 
                break
            print('Using NEW file, entering get_chunk()')
            chunk_number = checksums.get_chunk(chunk)
            print('Using NEW file, exiting get_chunk()')

            if chunk_number is not None: #checksum of chunk in NEW file matches
                #checksum of OLD file
                offset += BLOCK_SIZE
                blocks.append(chunk_number)
                continue
            else:
                offset += 1
                blocks.append(chunk[0])
                f.seek(offset)
                continue
    print('printing blocks')
    print(blocks)
    return blocks

def file(file_one, file_two):
    """
    !!! File-two is OLD; File-one  is NEW

    Essentially this returns file one, but in a fancy way :)

    The output from get_block_list is a list of either chunk indexes or data as
    strings.

    If it's a chunk index, then read that chunk from the file and append it to
    output. If it's not a chunk index, then it's actual data and should just be
    appended to output directly.
    """
    print('----------Beginning of output----------')
    output = ''
    with open(file_two) as ft:
        for block in _get_block_list(file_one, file_two):
#            print('------Inside for loop in file()------')
 #           print(block)
            if isinstance(block, int): 
                ft.seek(block * BLOCK_SIZE)
                
#                output += ft.read(BLOCK_SIZE)
               # output += ft.read(BLOCK_SIZE).decode('UTF-8')

            else:
                output += block
   # with open(file_two) as ft_output:
   #    ft_output.write(output)
    return output 
   # return output


