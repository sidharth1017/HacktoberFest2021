# Following is the implementation of Simplified Data Encryption Algorithm in Python
# Input given by the user is 8 bit plain text and 10 bit key
# Output of both rounds are displayed along with the final cipher text

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]

sBOX0 = [
    ["01", "00", "11", "10"],
    ["11", "10", "01", "00"],
    ["00", "10", "01", "11"],
    ["11", "01", "11", "10"],
]
sBOX1 = [
    ["00", "01", "10", "11"],
    ["10", "00", "01", "11"],
    ["11", "00", "01", "00"],
    ["10", "01", "0", "11"],
]

# Initial permutation
def ip(pt):
    temp = list(pt)
    for i in range(0, len(pt)):
        temp[i] = pt[IP[i] - 1]
    return "".join(temp)


# inverse initial permutation fuction. IP^(-1)
def ipInverse(pt):
    temp = list(pt)
    for i in range(0, len(pt)):
        temp[i] = pt[IP_inv[i] - 1]
    return "".join(temp)


# P10 permutation function
def pTEN(key):
    tmp = list(key)
    for i in range(0, len(key)):
        tmp[i] = key[P10[i] - 1]
    return "".join(tmp)


# P8 permutation function
def pEIGHT(key):
    tmp = list(key)
    for i in range(0, len(key) - 2):
        tmp[i] = key[P8[i] - 1]
    return "".join(tmp[:8])


# P4 permutation function
def pFOUR(key):
    tmp = "{}{}{}{}".format(key[1], key[3], key[2], key[0])
    return tmp


# shift left by one bit function. LS-1
def lsONE(key):
    ls1 = "{}{}{}{}{}".format(key[1], key[2], key[3], key[4], key[0])
    ls2 = "{}{}{}{}{}".format(key[6], key[7], key[8], key[9], key[5])
    return ls1 + ls2


# shift left by 2 bits function. LS-2
def lsTWO(key):
    ls1 = "{}{}{}{}{}".format(key[2], key[3], key[4], key[0], key[1])
    ls2 = "{}{}{}{}{}".format(key[7], key[8], key[9], key[5], key[6])
    return ls1 + ls2


# expansion permutation function
def eXp(fBits):
    ep = [
        fBits[3],
        fBits[0],
        fBits[1],
        fBits[2],
        fBits[1],
        fBits[2],
        fBits[3],
        fBits[0],
    ]
    return "".join(ep)


# bit-by-bit XOR function.
def bitXOR(bitsA, bitsB):
    r = ""
    for i in range(len(bitsA)):
        if bitsA[i] != bitsB[i]:
            r += "1"
        else:
            r += "0"
    return r


# swap function
def sw(iput):
    switched = "{}{}{}{}{}{}{}{}".format(
        iput[4], iput[5], iput[6], iput[7], iput[0], iput[1], iput[2], iput[3]
    )
    return switched


def keyGeneration(key):
    k1 = pEIGHT(lsONE(pTEN(key)))  # First Key (K1)
    k2 = pEIGHT(lsTWO(lsONE(pTEN(key))))  # Second Key(K2)
    return k1, k2


def f(half, key):
    ep = eXp(half)  # Expansion permutation of R
    xr = bitXOR(ep, key)  # Bit-by-bit XOR between the half nibble (R) and the key
    xr_s0 = xr[:4]  # Left half of XOR result
    xr_s1 = xr[4:]  # Right half of XOR result
    s0_r = int(xr_s0[0] + xr_s0[3], 2)  # CHOOSE ROW FOR SBOX0
    s0_c = int(xr_s0[1] + xr_s0[2], 2)  # CHOOSE COLUMN FOR SBOX0
    sbz = sBOX0[s0_r][s0_c]  # TAKE RESULT FROM SBOX0
    s1_r = int(xr_s1[0] + xr_s1[3], 2)  # CHOOSE ROW FOR SBOX1
    s1_c = int(xr_s1[1] + xr_s1[2], 2)  # CHOOSE COLUMN FOR SBOX1
    sbo = sBOX1[s1_r][s1_c]  # TAKE RESULT FROM SBOX1
    sbOPuts = sbz + sbo  # Join S-BOX outputs
    f = pFOUR(sbOPuts)  # P4(joined S-BOX results)
    return f  # F(R,Key) Result


def encrypt(msg, key):
    permuted = ip(msg)
    k1, k2 = keyGeneration(key)
    ipR = permuted[4:]  # Right half nibble (R) of IP(Message)
    fK1 = f(ipR, k1)
    ipL = permuted[:4]  # Left half nibble (L) of IP(Message)
    lXf = bitXOR(ipL, fK1)  # L XOR F(R, K1)
    newIP = lXf + permuted[4:]
    print("Round 1 output: " + str(newIP))
    swH = sw(newIP)  # SW(fk1(IP(plaintext)))
    swR = swH[4:]  # Right half nibble of SW result
    fK2 = f(swR, k2)  # Result of F(R,K2)
    swL = swH[:4]  # Left half nibble of SW
    swLXf = bitXOR(swL, fK2)  # L XOR F(R, K2)
    final = swLXf + swR
    print("Round 2 output: " + str(final))
    cipher = ipInverse(final)  # IP^-1
    return cipher


def main():
    message = input("Enter 8 bit plain text: ")
    key = input("Enter 10 bit key: ")
    print("-" * 30)
    cipher = encrypt(message, key)
    print("Cipher text: " + cipher)


if __name__ == "__main__":
    main()
