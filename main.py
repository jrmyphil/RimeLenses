# Tuple containing a list of lens colors in ascending order.
C = ('W', 'Y', 'M', 'B', 'C', 'G')
# Tuple containing a list of lens colors in descending order.
C_REV = ('G', 'C', 'B', 'M', 'Y', 'W')

def create_valid_array():
    # Create list of all valid color combos
    # RULES:    1. No repeating colors.
    #           2. Colors can only ascend or descend through the combo.

    # Populate a list with all valid color combinations by running the algorithm on both ascending and descending
    # color tuples. Then, traverse and print all valid combinations.
    all_color_combos = []
    find_all_colors(C, all_color_combos)
    find_all_colors(C_REV, all_color_combos)

    print("==============================")
    print("All valid color combinations: ")
    for i in range(len(all_color_combos)):
        print(f'{(i+1):02d}\t' + all_color_combos[i])

    # Using the list of all valid color combos, create a new (much larger) list of all valid color combos with all
    # valid lens apertures.
    # RULES:    1. Top lens ([0]) aperture size is always 0.
    #           2. Adjacent lenses cannot have the same aperture size.
    all_aperture_combos = []
    find_all_apertures(all_color_combos, all_aperture_combos)

    print("==============================")
    print("All valid color/aperture combinations: ")
    for i in range(len(all_aperture_combos)):
        print(f'{(i+1):03d}\t' + all_aperture_combos[i])

    # Using the list of all valid aperture combos, create a new (even larger) list of all valid height settings for
    # all lens combinations.
    # RULES:    1. Lenses cannot go lower than 1 or higher than 20.
    #               Note: Element [0] is the TOP lens (farthest from the book) and cannot be higher than 20. Element
    #                     len - 1 is the BOTTOM lens (closest to the book) and cannot be lower than 1. Naturally,
    #                     all distances must be in descending order.
    #           2. Each lens takes up an additional 1 distance worth of space above and below it, so they cannot be
    #               within two spaces of each other. (e.g., lenses can be at 1 and 4, or 7 and 10. They cannot be at
    #               1 & 2, 1 & 3, 7 & 8, 7 & 9.)
    #           3. There must be 11 or fewer steps between the top lens (index 0) and the bottom lens (index 3).
    #           4. If a lens is between two lenses that both have the smallest aperture (2), the middle lens must
    #               be equidistant between them.
    all_height_combos = []
    find_all_heights(all_aperture_combos, all_height_combos)

    count = 0;

    print("==============================")
    print("All valid color/aperture/height combinations: ")
    for i in range(len(all_height_combos)):
        print(f'{(i+1):05d}\t' + all_height_combos[i])
        count += 1

    print(f'\nTotal number of valid lens lens contraption configurations: {count}')

# Iterate through color lists (both ascending and descending), create strings of valid lens color sequences, and
# append the strings to the passed list.
# Note: Instead of creating a reversed "C_REV" tuple and taking a color list as a parameter, it would make more sense
# to take a "descending" boolean parameter and switch the order programmatically.
def find_all_colors(colors, list):
    for i in range(3):
        combo_a = colors[i]
        for j in range(i+1, 4):
            combo_b = combo_a + colors[j]
            for k in range(j+1, 5):
                combo_c = combo_b + colors[k]
                for l in range(k+1, 6):
                    combo_d = combo_c + colors[l]
                    list.append(combo_d)


# Iterate through the color combos list, build new strings that include aperture sizes, and append the strings to the
# passed list.
def find_all_apertures(colors, list):
    for c in colors:
        combo_a = c[0] + '0-'
        for i in range(1, 3):
            combo_b = combo_a + c[1] + str(i) + '-'
            for j in range(3):
                if i != j:
                    combo_c = combo_b + c[2] + str(j) + '-'
                    for k in range(3):
                        if k != j:
                            combo_d = combo_c + c[3] + str(k)
                            list.append(combo_d)

# Iterate down from 20 to 1, build new strings that include heights, and append the strings to the passed list.
def find_all_heights(apertures, list):
    # If lens 3 & lens 1 both have small apertures (2), lens 2 must be equidistant between them.
    # For lens 3 & lens 1, higher height - lower height must be even, or there cannot be an equidistant lens.
    for lenses in apertures:
        small_apertures = lenses[4] == '2' and lenses[-1] == '2'
        for h1 in range(20,10,-1):
            lowest = max((h1 - 11), 0)
            combo_a = lenses[0:2] + '|' + str(h1) + '|' + '\t'
            for h2 in range((h1-3), (lowest+5), -1):
                combo_b = combo_a + lenses[3:5] + '|' + str(h2) + '|' + '\t'
                if small_apertures:
                    for h4 in range((h2-6), (lowest-1), -1):
                        if (h2 + h4) % 2 == 0:
                            mid = int((h2 + h4) / 2)
                            if (h2 - mid >= 3) and (mid - h4 >= 3):
                                combo_c = combo_b + lenses[6:8] + '|' + str(mid) + '|' + '\t'
                                combo_d = combo_c + lenses[-2:] + '|' + str(h4) + '|'
                                list.append(combo_d)
                else:
                    for h3 in range((h2-3), (lowest+2), -1):
                        combo_c = combo_b + lenses[6:8] + '|' + str(h3) + '|' + '\t'
                        for h4 in range((h3-3), (lowest-1), -1):
                            combo_d = combo_c + lenses[-2:] + '|' + str(h4) + '|'
                            list.append(combo_d)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_valid_array()
