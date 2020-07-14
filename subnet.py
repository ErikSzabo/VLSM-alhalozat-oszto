import sys
import math


def oktet(num):
    return "0" * (8 - len(bin(num)[2:])) + bin(num)[2:]


def add_binary(bin1, bin2):
    eredmeny = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return "0" * (32 - len(eredmeny)) + eredmeny


def nagyobb_ketto_hatvany(num):
    hatvany = 0
    while 2**hatvany < num:
        hatvany += 1
    return hatvany


def maszk_bit(gep_szam):
    return 32 - nagyobb_ketto_hatvany(gep_szam)


def olvashato_cim(cim):
    olvashato = ""
    for i in range(0, len(cim), 8):
        okt = cim[i:i+8]
        olvashato += str(int(okt, 2)) + "."
    return olvashato[:-1]


def halozat_beolvas():
    halozatok = []
    mennyiseg = int(input("Hány hálózat lesz? "))
    for i in range(mennyiseg):
        inp = input("Név Gépszám: ").split(" ")
        halozatok.append((inp[0], int(inp[1])))
    halozatok.sort(key=lambda x: x[1], reverse=True)
    return halozatok


def get_minimum_meret(halozatok):
    osszeg = 0
    for nev, db in halozatok:
        osszeg += 2**nagyobb_ketto_hatvany(db+3)
    return osszeg


def get_halozat_meret(cim, maszk_hossz):
    utolso_cim = cim[:maszk_hossz] + "1" * (32-maszk_hossz)
    return int(utolso_cim, 2) - int(cim, 2)


def main():
    # Bináris formátumó stringé alakítjuk a kezdő címet
    kezdo_cim = "".join([oktet(int(okt)) for okt in sys.argv[1].split(".")])

    # Bináris formátumú stringé alakítjuk a kezdő maszkot
    kezdo_maszk = "1" * int(sys.argv[2]) + "0" * (32 - int(sys.argv[2]))

    # szám listává alakítjuk a gépeket, és csökkenő sorrendbe rendezzük őket
    halozatok = halozat_beolvas()
    print(end="\n\n")

    if get_minimum_meret(halozatok) > get_halozat_meret(kezdo_cim, int(sys.argv[2])):
        print("Nincs elég cím a megadott tartományban!")
        return

    for halozat in halozatok:
        print(f"{halozat[0]} ({halozat[1]}) hálózat:", end="\n\n")

        # Jöjjünk rá, hány bites maszk kell.
        maszk_hossz = maszk_bit(halozat[1] + 3)
        if maszk_hossz < kezdo_maszk.count("1"):
            print("Lehetetlen művelet!")
            return

        halozati_cim = kezdo_cim
        broadcast_cim = add_binary(
            kezdo_cim,
            bin(2**nagyobb_ketto_hatvany(halozat[1]+3) - 1)[2:]
        )

        router_cim = add_binary(
            kezdo_cim,
            bin(2**nagyobb_ketto_hatvany(halozat[1]+3) - 2)[2:]
        )

        elso_interface_cim = add_binary(
            kezdo_cim,
            bin(1)[2:]
        )

        utolso_interface_cim = router_cim

        maszk = "1" * maszk_hossz + "0" * (32 - maszk_hossz)

        print(f"\t{olvashato_cim(kezdo_cim)}/{maszk_hossz}")
        print(f"\tHálózati cím: {olvashato_cim(halozati_cim)}")
        print(f"\tBroadcast cím: {olvashato_cim(broadcast_cim)}")
        print(f"\tRouter cím: {olvashato_cim(router_cim)}")
        print(
            f"\tcím tartomány: {olvashato_cim(elso_interface_cim)} - {olvashato_cim(utolso_interface_cim)}")
        print(f"\tmaszk: {olvashato_cim(maszk)}", end="\n\n\n")

        kezdo_cim = add_binary(
            broadcast_cim,
            bin(1)[2:]
        )


main()
