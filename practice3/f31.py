import struct

def f31(binary: bytes) -> dict:
    def struct_a(offset: int) -> dict:
        a1 = struct_b(offset)
        offset += 8 + 1
        
        a2 = struct_c(offset)
        offset += 6 * 1 + 2
        
        a3 = struct_d(offset)
        offset += 8 + 2 + 2 + 3 * (2 + 8 + 8 * 1) + 2 + 8 + 1 + 4
        
        [a4] = struct.unpack('> q', binary[offset: offset + 8])
        offset += 8
        
        [a5] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        
        [k] = struct.unpack('> I', binary[offset: offset + 4])
        offset += 4
        [offset1] = struct.unpack('> I', binary[offset: offset + 4])
        s = '>' + str(k) + 'b'
        a6 = list(struct.unpack(s, binary[offset1: offset1 + 1 * k]))
        offset += 4
        
        return {
            'A1': a1,
            'A2': a2,
            'A3': a3,
            'A4': a4,
            'A5': a5,
            'A6': a6,
            }

    def struct_b(offset: int) -> dict:
        [b1] = struct.unpack('> d', binary[offset: offset + 8 ])
        offset += 8

        [b2] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1
        
        return {
            'B1': b1,
            'B2': b2,
            }

    def struct_c(offset: int) -> dict:
        c1 = list(struct.unpack('> 6b', binary[offset: offset + 6]))
        for i in range(len(c1)):
            c1[i] = chr(c1[i])
        c1 = ''.join(c1)
        offset += 6

        [c2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        
        return {
            'C1': c1,
            'C2': c2,
            }
    
    def struct_d(offset: int) -> dict:
        [d1] = struct.unpack('> q', binary[offset: offset + 8])
        offset += 8

        [d2] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2

        [d3] = struct.unpack('> h', binary[offset: offset + 2])
        offset += 2
        
        d4 = [struct_e(offset + i * 18) for i in range(3)]
        offset += 18 * 3

        [k] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        d5 = struct_f(k)

        [d6] = struct.unpack('> q', binary[offset: offset + 8])
        offset += 8

        [d7] = struct.unpack('> b', binary[offset: offset + 1])
        offset += 1

        [d8] = struct.unpack('> f', binary[offset: offset + 4])
        offset += 4
        
        return {
            'D1': d1,
            'D2': d2,
            'D3': d3,
            'D4': d4,
            'D5': d5,
            'D6': d6,
            'D7': d7,
            'D8': d8,
            }

    def struct_e(offset: int) -> dict:
        [e1] = list(struct.unpack('> H', binary[offset: offset + 2]))
        offset += 2
        
        [e2] = list(struct.unpack('> d', binary[offset: offset + 8]))
        offset += 8
        
        e3 = list(struct.unpack('> 8b', binary[offset: offset + 8]))
        offset += 8
        
        return {
            'E1': e1,
            'E2': e2,
            'E3': e3,
            }

    def struct_f(offset: int) -> dict:
        [f1] = list(struct.unpack('> f', binary[offset: offset + 4]))
        offset += 4

        [f2] = list(struct.unpack('> i', binary[offset: offset + 4]))
        offset += 4

        [k] = struct.unpack('> H', binary[offset: offset + 2])
        offset += 2
        [offset1] = struct.unpack('> H', binary[offset: offset + 2])
        s = '>' + str(k) + 'f'
        f3 = list(struct.unpack(s, binary[offset1: offset1 + 4 * k]))
        offset += 2

        [f4] = list(struct.unpack('> I', binary[offset: offset + 4]))
        offset += 4

        [f5] = list(struct.unpack('> H', binary[offset: offset + 2]))
        offset += 2
        
        return {
            'F1': f1,
            'F2': f2,
            'F3': f3,
            'F4': f4,
            'F5': f5,
            }

    
    return struct_a(4)



print(f31(b'\x96JSR?\xba\x9e\xc6R\x1bZ\x80+yiluqy4\xa2`\xa1b\xd4OW\x1a\xd3"\xe7\x99'
b'J\xb7\xb6?\xe8\x99\xf9\xb5\t}b\x08\xbfJY!z:[/\xff?\xedL\xf5\xafAe'
b'\xfe\x0c\x8f"\x7f%o>\xe9\x19q\xbf\xe6\x0c\xf1\xe6z\xc10\t\x06\xbbg\x86'
b'\xf5H\x94\x00\x86\xd8\x9e\xees\xcd\xbb\xf8\xe1}\xbfd?\x06\xc9\xea'
b'\xfd\xf8\xff\xd4\xcf\xa2\xb7\xcf\r\x0b\x00\x00\x00\x02\x00\x00\x00\x98?,'
b'ia\xbe\xa9?g\xbfM\x96\xa7>pg\x9d\xb4\xee&;\x00\x03\x00z\xff\xc1^\xf0\x1fL'
b'\xd2\xbc'))
