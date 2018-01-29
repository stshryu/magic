def ransom_note(magazine, ransom):
    _m, _r = {}, {}
    for item in magazine:
        if item in _m:
            _m[item] = _m[item] + 1
        else:
            _m[item] = 1
    for item in ransom:
        if item in _r:
            _r[item] = _r[item] + 1
        else:
            _r[item] = 1

    for item in _r.keys():
        if item in _m:
            if _r[item] <= _m[item]:
                pass
            else:
                return False
        else:
            return False

    return True

m = 'give me one grand today night'
n = 'give one grand today'

answer = ransom_note(m.split(' '), n.split(' '))

if(answer):
    print("Yes")
else:
    print("No")
