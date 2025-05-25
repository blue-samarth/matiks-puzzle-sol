print(f"Enter {9} numbers separated by spaces:")
numbers: list[int] = list(map(int, input().split()))
if len(numbers) != 9: 
    print("You must enter exactly 9 numbers.")
    exit(1)

hashmap: dict[int, bool] = {i : False for i in numbers}

def solve(hashmap: dict[int,bool], sol1: int, sol2: int, sol3: int, sol4: int, sol5: int, sol6: int) -> dict[str, int]:
    for a1 in hashmap.keys():
        for a2 in hashmap.keys():
            if a1 == a2: continue
            for a3 in hashmap.keys():
                if a3 == a1 or a3 == a2: continue
                if (a1 + a2) * a3 != sol1: continue
                else: print(f"a1: {a1}, a2: {a2}, a3: {a3}")

                for b1 in hashmap.keys():
                    if b1 == a1 or b1 == a2 or b1 == a3: continue
                    for b2 in hashmap.keys():
                        if b2 == a1 or b2 == a2 or b2 == a3 or b2 == b1: continue
                        for b3 in hashmap.keys():
                            if b3 == a1 or b3 == a2 or b3 == a3 or b3 == b1 or b3 == b2: continue
                            if (b1 - b2) + b3 != sol2: continue
                            else: print(f"b1: {b1}, b2: {b2}, b3: {b3}")

                            for c1 in hashmap.keys():
                                if c1 == a1 or c1 == a2 or c1 == a3 or c1 == b1 or c1 == b2 or c1 == b3: continue
                                if (a1 // b1) - c1 != sol4: continue
                                else: print(f"a1: {a1}, b1: {b1}, c1: {c1}")
                                for c2 in hashmap.keys():
                                    if c2 == a1 or c2 == a2 or c2 == a3 or c2 == b1 or c2 == b2 or c2 == b3 or c2 == c1: continue
                                    if (a2 + b2) * c2 != sol5: continue
                                    else: print(f"a2: {a2}, b2: {b2}, c2: {c2}")
                                    for c3 in hashmap.keys():
                                        if c3 == a1 or c3 == a2 or c3 == a3 or c3 == b1 or c3 == b2 or c3 == b3 or c3 == c1 or c3 == c2: continue
                                        if c1 * c2 != sol3 * c3: continue
                                        if (a3 - b3) * c3 != sol6: continue
                                        else: 
                                            print(f"c1: {c1}, c2: {c2}, c3: {c3}")
                                            return {
                                                "a1": a1, "a2": a2, "a3": a3,
                                                "b1": b1, "b2": b2, "b3": b3,
                                                "c1": c1, "c2": c2, "c3": c3
                                            }


                        

    return {}

print(f"{solve(hashmap, 214, 10, 32, -1, 365, 17)}")
# print(f"{solve(hashmap, 15, 4, 6, 5, 25, 5)}")
# (a1 + a2) * a3 == 214
# (b1 - b2) + b3 == 10
# (c1 * c2) // c3 == 32 or c1 * c2 == 32 * c3
# a1 // b1 - c1 == -1
# (a2 + b2) * c2 == 365
# (a3 - b3) * c3 == 17
# a1, a2, a3, b1, b2, b3, c1, c2, c3 := {4, 5, 39, 13, 5, 72, 35, 9, 2}