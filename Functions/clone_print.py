def clone_print(str = None, end = '\n') :
    out = ''

    if type(str) != None:
        out = '{str}{end}'.format(str = str, end = end)
    else :
        out = 'You should enter some text'
    return out

out = clone_print('Ventsi is here', end="!")
print(out)