from random import seed, shuffle
#Encoder Function
def Encoder(user_input,SEED):
    user_input = user_input.lower()
    letter = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Letter_code = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    code = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    n = []
    seed(SEED)
    shuffle(code)
    for letter in user_input:
        for let in letter:
            if letter != " ":
                if letter == let:
                    first = Letter_code[let]
                    n.append(code[first])
            else:
                n.append("~")
    return ''.join(n)

# Decoder Function
def Decoder(user_input,SEED):
    user_input = user_input.lower
    key_list = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    final = ["a","b","c","d","e","f","g","h","i","j","k",'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    seed(SEED)
    shuffle(key_list)
    key_code = {}
    z = 0
    n = []
    for key in key_list:
        key_code[key] = z
        z += 1
    for let in user_input:
        if let != "~":
            for Ke in key_list:
                if let == Ke:
                    a = key_code[Ke]
                    n.append(final[a])
        else:
            n.append(" ")
    return ''.join(n)

# Prompt
encode_decode = str(input("Would you like to encode or decode a message?(encode/decode): "))
encode_decode = encode_decode.lower()
if encode_decode == "encode":
    message =input("Message to encode (no puncuation):")
    SEED = input("Key:")
    print (Encoder(message,SEED))
elif encode_decode == "decode":
    message = input("Message to decode:")
    SEED = input("Key:")
    print(Decoder(message,SEED))
else:
    print("!!!INVALID RESPONSE!!!")

# === Output === #

# Would you like to encode or decode a message?(encode/decode): encode
# Message to encode (no puncuation):Hello Abrar
# Key:a
# gbjjo~xkdxd