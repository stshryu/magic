def number_needed(a, b):
    _a = {}
    _b = {}
    for i in a:
        if i in _a:
            _a[i] = _a[i] + 1
        else:
            _a[i] = 1

    for j in b:
        if j in _b:
            _b[j] = _b[j] + 1
        else:
            _b[j] = 1

    common = set(_b.keys()).intersection(set(_a.keys()))
    notcommon_a = set(_a.keys()) - set(_b.keys())
    notcommon_b = set(_b.keys()) - set(_a.keys())

    remove_count = 0

    for key in common:
        remove_count = remove_count + abs(_a[key] - _b[key])

    for key in notcommon_a:
        remove_count = remove_count + _a[key]

    for key in notcommon_b:
        remove_count = remove_count + _b[key]

    return remove_count

a = ['a', 'b', 'c']
b = ['c', 'd', 'e']

print(number_needed(a, b))
