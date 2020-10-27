def word_mod_steps(start, goal, limit):

    def add_letter(word, goal, string_index):
        try:
            new_word = word[:string_index] + goal[string_index] + word[string_index:]
        except IndexError:
            new_word = word + goal[len(goal) - 1]

        return new_word

    def delete_letter(word, string_index):
        new_word = word[:string_index] + word[string_index + 1:]
        return new_word

    def change_letter(word, goal, string_index):
        try:
            new_word = word[:string_index] + goal[string_index] + word[string_index + 1:]
        except IndexError:
            new_word = word[:string_index] + goal[len(goal) - 1] + word[string_index + 1:]
        return new_word

    def permutation_number(n):
        if n == 0:
            return '0'
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return ''.join(reversed(nums))

    def helper(start, goal, limit, index=0, lim_index=0, permutation=permutation_number(0), verbose=False):
        if limit > len(permutation):
            permutation = '0'*(limit - len(permutation)) + permutation

        if verbose:
            print(start, end=' ')

        if start == goal:
            if verbose:
                print('SUCCESS\tLimit Index:', lim_index)
            return lim_index
        elif lim_index == limit:
            limit += 1
            if verbose:
                print('LIMIT EXCEEDED\tLimit Index:', limit)
            return limit

        else:
            try:
                if start[index] == goal[index]:

                    if verbose:
                        print('==>', end=' ')

                    return helper(start, goal, limit, index=index+1, lim_index=lim_index, permutation=permutation,
                                  verbose=verbose)
            except IndexError:
                None

            digit = int(permutation[-(index+1)])

            if digit == 0:
                if verbose:
                    print('-->', end=' ')

                new_word = add_letter(start, goal, index)
                # print('-->', new_word, end='\r')

                return helper(new_word, goal, limit, index=index, lim_index=lim_index+1, permutation=permutation,
                              verbose=verbose)

            elif digit == 1:
                if verbose:
                    print('-->', end=' ')
                new_word = change_letter(start, goal, index)
                # print('-->', new_word, end='\r')

                return helper(new_word, goal, limit, index=index, lim_index=lim_index+1, permutation=permutation,
                              verbose=verbose)

            elif digit == 2:
                if verbose:
                    print('-->', end=' ')
                new_word = delete_letter(start, index)
                # print('-->', new_word, end='\r')

                return helper(new_word, goal, limit, index=index, lim_index=lim_index+1, permutation=permutation,
                              verbose=verbose)

    if len(goal) > len(start):
        lim_indices = [

            helper(start, goal, limit,
                   permutation=permutation_number(n)) for n in range(3**(len(goal)+1))

                        ]
    else:
        lim_indices = [

            helper(start, goal, limit,
                   permutation=permutation_number(n)) for n in range(3**(len(start)+1))

                        ]

    minimum_limit = min([i for i in lim_indices if i is not None])

    helper(start, goal, limit, permutation=permutation_number(lim_indices.index(minimum_limit)), verbose=True)

    return minimum_limit


limit = 10
print()
ash = word_mod_steps('hash', 'ash', limit)
print()
scat = word_mod_steps('cats', 'scat', limit)
print()
purring = word_mod_steps('purng', 'purring', limit)
print()
kittens = word_mod_steps('ckiteus', 'kittens', limit)
print()
gestate = word_mod_steps('gest', 'gestate', limit)
print()
okee = word_mod_steps('pray', 'okee', limit)
print()
btfi = sum([word_mod_steps('baffy', 'btfi', k) > k for k in range(5)])
print()
wopd = word_mod_steps('shop', 'wopd', 100)
print()
dance = word_mod_steps('pridy', 'dance', 100)
print()
wiry = word_mod_steps('wird', 'wiry', 100)
print()
logical = word_mod_steps("rlogcul", "logical", limit)
print()
ziinx = sum([word_mod_steps('chine', 'ziinx', k) > k for k in range(5)])
print()
grad = word_mod_steps('fluid', 'grad', 100)
print()
tskhteur = word_mod_steps('titer', 'tskhteur', 100)
print()
qualm = word_mod_steps('dayal', 'qualm', 100)
print()
jzgon = word_mod_steps('zygon', 'jzon', 5)
print()
zbk = word_mod_steps('dekko', 'zbk', 100)
print()
xdhe = word_mod_steps('sher', 'xdhe', 100)
print()
mdiye = word_mod_steps('mikie', 'mdiye', 100)

print()
print(ash, scat, purring, kittens, gestate, okee, btfi, wopd, dance, wiry, logical, ziinx, grad, tskhteur, qualm, jzgon,
      zbk, xdhe, mdiye)
