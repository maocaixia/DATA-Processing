binfile = open(fd_data[i], 'rb')
d_str = binfile.read()
binfile.close()
d_len = len(d_str)

data = struct.unpack(str(d_len//4)+'f', d_str) #float32: 4 Bytes
j = 0
while j < int(d_len/4):
    tmp_out.append((float(data[j]), float(data[j+1]), float(data[j+2])))
    j = j+3
