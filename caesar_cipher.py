import argparse


def write_file(output_file, data):
    print("Written output to: {}".format(output_file))

    f = open(output_file, "w")
    f.write(data)
    f.close()


def encrypt(shift):
    print("Encrypting file...")
    f = open("Example.txt", "r")
    original_message = f.read()
    f.close()

    encrypted_message = ""
    for x in [x for x in original_message]:
        if x.isupper():
            encrypted_message += chr((ord(x) + shift - 65) % 26 + 65)
        elif not x.isalpha():
            encrypted_message += x
        else:
            encrypted_message += chr((ord(x) + shift - 97) % 26 + 97)

    return encrypted_message


def decrypt(shift):
    print("Decrypting file...")

    f = open("Encrypted.txt", "r")
    encrypted_message = f.read()
    f.close()

    decrypted_message = ""
    for x in [x for x in encrypted_message]:
        if x.isupper():
            decrypted_message += chr((ord(x) - shift - 65) % 26 + 65)
        elif not x.isalpha():
            decrypted_message += x
        else:
            decrypted_message += chr((ord(x) - shift - 97) % 26 + 97)

    return decrypted_message


def main(shift, mode):
    if mode == "encrypt":
        encrypted_message = encrypt(shift)
        write_file("Encrypted.txt", encrypted_message)
    elif mode == "decrypt":
        decrypted_message = decrypt(shift)
        write_file("Decrypted.txt", decrypted_message)
    else:
        raise Exception("Invalid commands")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", help="The mode (e = encrypt or d = decrypt)", required=True)
    parser.add_argument("-s", help="The shift value (1-26)", required=True)
    args = parser.parse_args()

    main(int(args.s), args.m)
