def oktet(num):
    return "0" * (8 - len(bin(num)[2:])) + bin(num)[2:]


def halozati_cim(cim, maszk):
    return cim[:maszk] + "0" * (32 - len(cim[:maszk]))


def broadcast_cim(cim, maszk):
    return cim[:maszk] + "1" * (32 - len(cim[:maszk]))


def utolso_interace_cim(bc_cim):
    eredmeny = bin(int(bc_cim, 2) - 1)[2:]
    return "0" * (32 - len(eredmeny)) + eredmeny


def olvashato_cim(cim):
    olvashato = ""
    for i in range(0, len(cim), 8):
        okt = cim[i:i+8]
        olvashato += str(int(okt, 2)) + "."
    return olvashato[:-1]


def add_binary(bin1, bin2):
    eredmeny = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return "0" * (32 - len(eredmeny)) + eredmeny


def main():
    inp = input("IP cím és maszkhossz (x.x.x.x/y): ").split("/")
    cim = "".join([oktet(int(okt)) for okt in inp[0].split(".")])
    maszk_hossz = int(inp[1])

    # Annak a hálózatnak a hálózati címe, amiben benne van
    halozati = halozati_cim(cim, maszk_hossz)
    print(f"Hálózati cím: {olvashato_cim(halozati)}")

    # Szintén csak broadcast címmel
    broadcast = broadcast_cim(cim, maszk_hossz)
    print(f"Broadcast cím: {olvashato_cim(broadcast)}")

    # Első interfésznek adható cím
    elso = add_binary(halozati, bin(1)[2:])
    print(f"Első interfésznek adható cím: {olvashato_cim(elso)}")

    # Utolsó
    utolso = utolso_interace_cim(broadcast)
    print(f"Utolsó interfésznek adható cím: {olvashato_cim(utolso)}")

    # Információközlés arról, hogyha az adott cím a fenti kettővel egyezik!
    print()
    if broadcast == cim:
        print("Ez a cím egy broadcast cím!!!")
    elif halozati == cim:
        print("Ez a cím egy hálózati cím!!!")


main()
