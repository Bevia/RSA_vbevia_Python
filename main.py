def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    m0, x0, x1 = phi, 0, 1
    if phi == 1:
        return 0
    while e > 1:
        q = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def main():
    p = 2
    q = 7

    # Value of N
    n = p * q
    print("The value of N =", n)

    # Value of phi
    phi = (p - 1) * (q - 1)
    print("The value of phi =", phi)

    # Finding e
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    print("The value of e =", e)

    # Finding d
    d = mod_inverse(e, phi)
    print("The value of d =", d)

    msg = 2
    print("The message in clear =", msg)

    # Encryption: C = (msg ^ e) % n
    c = pow(msg, e, n)
    print("Encrypted message is:", c)

    # Decryption: msgback = (C ^ d) % n
    msgback = pow(c, d, n)
    print("Decrypted message is:", msgback)


if __name__ == "__main__":
    main()
