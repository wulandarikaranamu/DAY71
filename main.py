remote = 5
#belajar menggunakan while do
while(remote > 0):
    print("masih ingin menonton Tv,gunakan remote")
    remote = remote - 1

while(True):
    print("nyalakan Tv")
    remote = remote - 1
    if(remote < 0):
        break