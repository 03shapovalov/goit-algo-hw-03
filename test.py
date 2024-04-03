ETAGEY = 5
KVARTIR_NA_ETAGE = 4

nomer_kvartiry = int(input('Input your number: '))
kvartir_v_padike = ETAGEY * KVARTIR_NA_ETAGE
kakaya_kvartira = (nomer_kvartiry - 1) // kvartir_v_padike + 1

print(kakaya_kvartira)