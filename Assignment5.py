import sys
from collections import defaultdict
import heapq



#first question
def top_two_bands():

    first_line = sys.stdin.readline()
    try:
        line_count = int(first_line.strip())
    except ValueError:
        print("Invalid input for number of lines.")
        return

    band_counts = defaultdict(int)


    for _ in range(line_count):
        line = sys.stdin.readline().strip()
        if not line or ':' not in line:
            continue
        _, bands_string = line.split(':', 1)
        bands = [band.strip() for band in bands_string.split(',') if band.strip()]
        for band in bands:
            band_counts[band] += 1

    if not band_counts:
        return


    two_largest = heapq.nlargest(2, set(band_counts.values()))
    if len(two_largest) == 1:
        second_highest = two_largest[0]
    else:
        second_highest = two_largest[1]

    top_bands = [band for band, count in band_counts.items() if count >= second_highest]

    for band in top_bands:
        print(band)

#second question
#____________________________________________________________________________________


def bands_to_colleagues():
    first_line = sys.stdin.readline()
    try:
        line_count = int(first_line.strip())
    except ValueError:
        print("Invalid input for the number of lines.")
        return

    band_to_colleagues = defaultdict(list)


    for _ in range(line_count):
        line = sys.stdin.readline().strip()
        if not line or ':' not in line:
            continue  # Skip invalid lines
        name, bands_string = line.split(':', 1)
        name = name.strip()
        bands = [band.strip() for band in bands_string.split(',') if band.strip()]
        for band in bands:
            band_to_colleagues[band].append(name)


    for band in sorted(band_to_colleagues.keys()):

        colleagues = sorted(set(band_to_colleagues[band]))
        colleagues_str = ', '.join(colleagues)
        print(f"{band}: {colleagues_str}")



if __name__ == "__main__":
    top_two_bands()
    bands_to_colleagues()
