
from aes import (
    bytes2matrix, 
    matrix2bytes,
    sub_bytes,
    inv_sub_bytes,
    shift_rows,
    inv_shift_rows,
    mix_columns,
    inv_mix_columns,
    add_round_key,
    pad,
    unpad,
    xor_bytes
    )

class TestBytes2Matrix:
    def test_bytes_to_matrix(self):
        text = bytes.fromhex("000102030405060708090A0B0C0D0E0F")

        matrix = bytes2matrix(text)

        assert matrix==[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    def test_matrix_to_bytes(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

        text = matrix2bytes(matrix)

        assert text==bytes.fromhex("000102030405060708090A0B0C0D0E0F")

class TestSubBytes:
    def test_sub_bytes(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

        sub_bytes(matrix)

        assert matrix==[[99, 124, 119, 123], [242, 107, 111, 197], [48, 1, 103, 43], [254, 215, 171, 118]] 

    def test_matrix_to_bytes(self):
        matrix = [[99, 124, 119, 123], [242, 107, 111, 197], [48, 1, 103, 43], [254, 215, 171, 118]] 

        inv_sub_bytes(matrix)

        assert matrix== [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

class TestShiftRow():
    def test_shift_row(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

        shift_rows(matrix)

        assert matrix==[[0, 5, 10, 15], [4, 9, 14, 3], [8, 13, 2, 7], [12, 1, 6, 11]]

    def test_inv_shift_row(self):
        matrix = [[0, 5, 10, 15], [4, 9, 14, 3], [8, 13, 2, 7], [12, 1, 6, 11]]

        inv_shift_rows(matrix)

        assert matrix== [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

class TestShiftRow():
    def test_shift_row(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

        shift_rows(matrix)

        assert matrix==[[0, 5, 10, 15], [4, 9, 14, 3], [8, 13, 2, 7], [12, 1, 6, 11]]

    def test_inv_shift_row(self):
        matrix = [[0, 5, 10, 15], [4, 9, 14, 3], [8, 13, 2, 7], [12, 1, 6, 11]]

        inv_shift_rows(matrix)

        assert matrix== [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]


class TestAddRoundKey():
    def test_visuel(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        key_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

        add_round_key(matrix, key_matrix)

        assert matrix==[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

    def test_xor_nul(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
        key_matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

        add_round_key(matrix, key_matrix)

        assert matrix==[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


class TestMixColumns():
    def test_mix_columns(self):
        matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

        mix_columns(matrix)

        assert matrix== [[2, 7, 0, 5], [6, 3, 4, 1], [10, 15, 8, 13], [14, 11, 12, 9]] 

    def test_inv_mix_columns(self):
        matrix =  [[2, 7, 0, 5], [6, 3, 4, 1], [10, 15, 8, 13], [14, 11, 12, 9]] 

        inv_mix_columns(matrix)

        assert matrix ==[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]


class TestPad():
    def test_0(self):
        bytes_text = bytes(0)

        padded = pad(bytes_text)

        assert padded == b""

    def test_4(self):
        bytes_text = b"abcd"

        padded = pad(bytes_text)

        assert padded == b'abcd\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'

    def test_16(self):
        bytes_text = bytes.fromhex("000102030405060708090A0B0C0D0E0F")

        padded = pad(bytes_text)

        assert padded == b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

class TestUnpadPad():
    def test_0(self):
        bytes_text = b'\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'

        unpadded = unpad(bytes_text)

        assert unpadded == b''

    def test_4(self):
        bytes_text = b'abcd\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c\x0c'

        unpadded = unpad(bytes_text)

        assert unpadded == b'abcd'

    def test_16(self):
        bytes_text = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'

        unpadded = unpad(bytes_text)

        assert unpadded == bytes.fromhex("000102030405060708090A0B0C0D0E0F")


class TestXorBytes():
    def test_random(self):
        a = [8, 9, 10, 11]
        b = [12, 13, 14, 15]

        xored = xor_bytes(a,b)

        assert xored == b'\x04\x04\x04\x04'

    def test_random(self):
        a = [8, 9, 10, 11]
        b = [0, 0, 0, 0]

        xored = xor_bytes(a,b)

        assert xored == b'\x08\t\n\x0b'
