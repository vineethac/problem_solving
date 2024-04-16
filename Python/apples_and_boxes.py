'''
apples = [2, 1, 4, 3] - total 10 apples
boxes = [5, 1, 8] - 3 boxes can hold a max of 14 apples

how many minimum boxes will be required to store all the apples.

'''
import sys


def main():
    """
    Main function.
    """
    apples = [15, 2, 2] #Total number of apples
    boxes = [5, 1, 12] #Here 3 boxes are there, and can hold total 14 apples

    total_apples = sum(apples)
    print(f"Total apples: {total_apples}")

    #Sort boxes by size
    boxes.sort()
    boxes.reverse()
    total_box_capacity = sum(boxes)
    print(f"Total box capacity: {total_box_capacity}")
    print(f"Boxes sorted by size: {boxes}")

    if total_apples > total_box_capacity:
        print("There are more apples than the total box capacity!")
        sys.exit(0)

    min_box_count = 0
    for box in boxes:
        if total_apples > 0:
            if total_apples <= box:
                min_box_count += 1
                total_apples -= total_apples
            else:
                min_box_count += 1
                total_apples = total_apples - box

    print(f"Minimum boxes required: {min_box_count}")



if __name__ == "__main__":
    main()
