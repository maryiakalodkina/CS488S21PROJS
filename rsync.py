import collections
import hashlib
import zlib


BLOCK_SIZE = 4096


# Helper functions
# ----------------
def md5_chunk(chunk):
    """
    Returns md5 checksum for chunk
    """
    m = hashlib.md5()
    m.update(chunk)
    return m.hexdigest()


def adler32_chunk(chunk):
    """
    Returns adler32 checksum for chunk
    """
    return zlib.adler32(chunk)

# Checksum objects
# ----------------
Signature = collections.namedtuple('Signature', 'md5 adler32')


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
    chunks = Chunks()
    with open(fn) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break

            chunks.append(
                Signature(
                    adler32=adler32_chunk(chunk),
                    md5=md5_chunk(chunk)
                )
            )

        return chunks

def _get_block_list(file_one, file_two):
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
    checksums = checksums_file(file_two)
    blocks = []
    offset = 0
    with open(file_one) as f:
        while True:
            chunk = f.read(BLOCK_SIZE)
            if not chunk:
                break

            chunk_number = checksums.get_chunk(chunk)

            if chunk_number is not None:
                offset += BLOCK_SIZE
                blocks.append(chunk_number)
                continue
            else:
                offset += 1
                blocks.append(chunk[0])
                f.seek(offset)
                continue

    return blocks

def file(file_one, file_two):
    """
    Essentially this returns file one, but in a fancy way :)

    The output from get_block_list is a list of either chunk indexes or data as
    strings.

    If it's a chunk index, then read that chunk from the file and append it to
    output. If it's not a chunk index, then it's actual data and should just be
    appended to output directly.
    """
    output = ''
    with open(file_two) as ft:
        for block in _get_block_list(file_one, file_two):
            if isinstance(block, int):
                ft.seek(block * BLOCK_SIZE)
                output += ft.read(BLOCK_SIZE)
            else:
                output += block

    return output


#if __name__ == '__main__':
file('foo.txt', 'bar.txt')
