row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]

map = [row1, row2, row3]
print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")

position = input(f"Where do you want to put the treasure?\nFirst type the number of row then the number of column.\n")
position1 = int(position[0]) - 1
position2 = int(position[1]) - 1

map[position1][position2] = "x"

print(f"    1    2    3\n1 {row1}\n2 {row2}\n3 {row3}")
