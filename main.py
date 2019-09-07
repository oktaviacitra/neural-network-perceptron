def find_index(inputs):
    index = []
    for i in range(len(inputs)):
        if inputs[i] == 1:
            index.append(i)
    return index

def implements_true(inputs, w2):
    index = find_index(inputs)
    result = []
    j = 0
    for i in range(len(w2)):
        if(j >= len(index)):
            break
        else:
            if i == index[j]:
                result.append(w2[i])
                j += 1
    return sum(result)

def operan_true(inputs, w1, w2):
    index = find_index(inputs)
    result = []
    j = 0
    for i in range(len(w2)):
        if j >= len(index):
            result.append(w1[i])
        else:
            if i == index[j]:
                result.append(w2[i])
                j += 1
            else:
                result.append(w1[i])
    return result

x1 = list(map(int,input("Masukkan nilai x1\t: ").split()))
x2 = []
while True:
    x2 = list(map(int,input("Masukkan nilai x2\t: ").split()))
    if len(x2) == len(x1):
        break
threshold = float(input("Masukkan threshold\t: "))
epoch = None
while True:
    epoch = int(input("Masukkan epoch\t\t: "))
    if epoch >= 1:
        break
miu = float(input("Masukkan miu\t\t: "))
w = []
while True:
    w = list(map(float,input("Masukkan nilai w\t: ").split()))
    if len(w) == 3:
        break
x0 = [1] * len(x1)
x = []
for i in range(len(x1)):
    temp = []
    temp.append(x0[i])
    temp.append(x1[i])
    temp.append(x2[i])
    x.append(temp)
bias_awal = sum([(w[i] * x[0][i]) for i in range(3)])
# print(bias_awal)
temp_x1 = [True if x1[i] == 1 else False for i in range(len(x1))]
temp_x2 = [True if x2[i] == 1 else False for i in range(len(x2))]
temp_target = [(temp_x1[i] ^ temp_x2[i]) for i in range(len(x1))]
target = [1 if temp_target[i] == True else 0 for i in range(len(temp_target))]
# print(target)
print("-->DATA\nx0\tx1\tx2\ttarget")
for i in range(len(x)):
    print("%d\t%d\t%d\t%d" %(x0[i], x1[i], x2[i], target[i]))
bobot_akhir = []
w2 = [None] * len(x[i])
print("-->PROSES\nepoch\ti\tj\tbias\tstatus\teror\tbobot")
for k in range(epoch):
    number = 0
    for i in range(len(x)):
        index = None
        if k == 0:
            index = i
        else:
            index = number
            number += 1 
        bias = bias_awal if i == 0 and k == 0 else implements_true(x[index], w2)
        status = 1 if bias > threshold else 0
        eror = target[i] - status
        bobot_akhir = []
        result_w = [None] * len(x[i])
        if i != 0:
            result_w = operan_true(x[i], w, w2)
        for j in range(len(x[i])):
            bobot = [None] * len(x[i])
            bobot[j] = (w[j] if i == 0 else result_w[j]) + float(miu * x[i][j] * eror)
            w2[j] = bobot[j]
            print("%d\t%d\t%d\t%.2f\t%d\t%d\t%.2f" %(k+1, i, j, bias, status, eror, bobot[j]))
            bobot_akhir.append(bobot[j])
bias_akhir = []
for i in range(len(x)):
    temp_bias = []
    for j in range(len(x[i])):
        operasi = x[i][j] * bobot_akhir[j]
        temp_bias.append(operasi)
    bias_akhir.append(sum(temp_bias))
status_akhir = [1 if bias_akhir[i] > threshold else 0 for i in range(len(bias_akhir))]
keterangan = [ "match" if status_akhir[i] == target[i] else "eror" for i in range(len(status_akhir))]
print("-->HASIL\nbias\tstatus\ttarget\tketerangan")
for i in range(len(bias_akhir)):
    print("%.2f\t%d\t%d\t%s" %(bias_akhir[i], status_akhir[i], target[i], keterangan[i]))
if "eror" in keterangan:
    print("tambah epoch untuk tidak eror lagi")
else:
    print("berhasil")