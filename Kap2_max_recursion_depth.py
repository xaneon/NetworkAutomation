def recursive(i):
    try:
        i = i + 1
        recursive(i)
    except RuntimeError as exc:
        print ('max depth == %d' % i)
        try:
            exit(0)
        except RuntimeError:
            print ('RuntimeError in exit')

recursive(0)
