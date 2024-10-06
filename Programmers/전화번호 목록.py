def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        tmp1 = phone_book[i]
        tmp2 = phone_book[i + 1]
        if tmp1 == tmp2[:len(tmp1)]:
            return False

    return True
