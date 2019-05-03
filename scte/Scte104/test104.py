#!/usr/bin/env
from SpliceEvent import SpliceEvent
import bitstring

test_string = "/DBIAAAAAsrbAP/wBQb/sbn3DQAyAjBDVUVJ/////3//AAAba98JHHVybjpuYmN1bmkuY29tOmJyYzozNTA3NTU4OTMxBQCk1C6w"

# hex_string="ffff004c00014d0000000003010400020000010b0030ffffffff0000db011e30303030324d4130303030303030333838343954303432343139313630300105011d010101000b010f0002000c"
hex_string="FFFF00280001F600000000020101000E01000000F600001F4802580000000109000650043132312A"
# hex_printable="FFFF004A0001 5100 0000 0003 0104 0002 \n0684 010B 002E FFFF FFFF 0000 1D09 1C75 \n726E 3A6E 6263 756E 692E 636F 6D3A 6272 \n633A 3337 3232 3235 3135 3231 0204 1D01 \n0101 000B 010F 0002 000B"
bitarray_data = bitstring.BitString(bytes=bytes.fromhex(hex_string))

# print("ff ff 00 4c 00 01 4d 00 00 00 00 03 01 04 00 02\n00 00 01 0b 00 30 ff ff ff ff 00 00 db 01 1e 30\n30 30 30 32 4d 41 30 30 30 30 30 30 30 33 38 38\n34 39 54 30 34 32 34 31 39 31 36 30 30 01 05 01\n1d 01 01 01 00 0b 01 0f 00 02 00 0c")
my_event = SpliceEvent(bitarray_data)



my_event.print()
print(hex_string)
my_event.to_binary()