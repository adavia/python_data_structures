def string_permutations(string):

    def sub_routine(used, left):

        combos = []

        for i in range(0, len(left)):
            ch = left.pop(i)
            used.append(ch)

            combos.append(''.join(used))

            # Append the results of the 
            # recursive call to our combos list
            combos = combos + sub_routine(used, left)


            # Remove ch from used
            used.pop(-1)
            # Splice ch back into left at its original index
            left[i:0] = [ch]

        return combos

    return sub_routine([], list(string))


print(string_permutations('abc'))
