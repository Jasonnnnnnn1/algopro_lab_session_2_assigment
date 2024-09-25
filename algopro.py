# Jason Franto Fong - 2802557791

# unify your stuffs
def unify_lists(A, B):
    return list(set(A).union(set(B)))

# modify your stuffs
def modify_string(tup, string):
    return ''.join([char * times for char, times in zip(string, tup)])

# yea the stuff thing "patient 0" yeah stuff whatever
a1, b1 = [1, 3, 5], [1, 2, 3]
a2, b2 = [2, 4, 6], [2, 4, 6]
a3, b3 = [1, 2, 3, 4], [4, 5, 6, 7]
a4, b4 = [1, 3, 4], [1, 3, 6]

# yea this thing "patient 2" or whatever here
tup1, str1 = (1, 2, 3, 4), 'This'
tup2, str2 = (1, 2, 1), 'Was'
tup3, str3 = (5, 1, 3, 4, 3, 2, 1, 4, 3, 2), 'Definitely'
tup4, str4 = (1, 2, 3), 'Not'
tup5, str5 = (1, 3, 1, 1, 2, 1, 1, 4, 1, 2 ,3), 'Plagiarized'

unify_results = [unify_lists(a1, b1), unify_lists(a2, b2), unify_lists(a3, b3), unify_lists(a4, b4)]
modify_results = [modify_string(tup1, str1), modify_string(tup2, str2), modify_string(tup3, str3), modify_string(tup4, str4), modify_string(tup5, str5)]

print(unify_results)
print(modify_results)