import sys

n, m = map(int, sys.stdin.readline().split())

tile_list = list(map(int, sys.stdin.readline().split()))

fix_count = 1
tile_list.sort()
prev_tile = tile_list[0]
for tile in tile_list[1:]:
    if tile - prev_tile <= m - 1:
        continue
    else:
        fix_count += 1
        prev_tile = tile

print(fix_count)