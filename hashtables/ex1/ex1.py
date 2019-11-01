#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # answer = [None, None]
    # 21
    # [4, 6, 10, 15, 16]
    # [(17,0), (15,1), (11, 2), (6,3), (5,4)]

    for i in range(length):
        weight_pair = hash_table_retrieve(ht, weights[i])

        if weight_pair is None:
            hash_table_insert(ht, limit - weights[i], i)
        else:
            print((i, weight_pair))
            return (i, weight_pair)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
