def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length *2 ):
        for j in range(lock_length, lock_length *2 ):
            if new_lock[i][j] != 1:
                return False
    return True


