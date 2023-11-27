def sətirlərin_minimalı(matrix):
    B = []

    # Hər bir sətrdəki minimal elementləri tap və B massivinə əlavə et
    for sətr in matrix:
        minimal_element = min(sətr)
        B.append(minimal_element)

    # B massivindəki maksimal elementi tap
    B_max = max(B)

    return B, B_max

# Nümunə bir matris
matrix = [
    [3, 7, 1],
    [8, 4, 2],
    [5, 9, 6]
]

# Funksiyanı çağır və nəticələri əldə et
netice_B, netice_B_max = sətirlərin_minimalı(matrix)

# Nəticələri ekrana çap et
print("Hər bir sətrdəki minimal elementlər (B massivi):", netice_B)
print("B massivinin maksimal elementi:", netice_B_max)