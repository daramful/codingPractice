def isOrderedOptimized(words, ordering):
    letter_index = 0
    for word_index, word in enumerate(words):
        if word.startswith(ordering[letter_index]):
            continue
        elif letter_index+1 < len(ordering) and word.startswith(ordering[letter_index+1]):
            letter_index += 1
            continue
        else:
            return False
    return True




print(isOrderedOptimized(['cc','cb','bb','ac'], ['c','b','a'])) # True
print(isOrderedOptimized(['cc','cb','bb','ac'], ['b','c','a'])) # False
print(isOrderedOptimized(['cc','cb','bb','ac','cat', 'aab'], ['c','b','a'])) # False

#Running time: O(n)
#The more optimized way which can be done is O(M) time is where you have two pointers 
#which point to the words list and the letters list respectively. 
# As soon as you encounter the first mismatch, return False immediately. 
# Else, if the traversal through the entire list is successful, then return True.


def check_order(words, ordering):
        order_dict = dict((ordering[i], i) for i in range(0, len(ordering)))
        max_len = _get_max_len(words)
        return _is_in_order([_convert(word, order_dict, max_len) for word in words])

def _convert(word, order_dict, max_digit):
        cur_digit = max_digit
        result = 0
        for c in word:
                result += order_dict[c] * 26 * cur_digit
                cur_digit -= 1
        return result

def _get_max_len(words):
        result = 0
        for word in words:
                if len(word) > result:
                        result = len(word)
        return result

def _is_in_order(converted):
        prev = 0
        for i in converted:
                if i < prev:
                        return False
                prev = i
        return True

print(check_order(['cc', 'cb', 'bb', 'ac'], ['c', 'b', 'a'])) # True
print(check_order(['cc', 'cb', 'bb', 'ac'], ['b', 'c', 'a'])) # False
#Running time: O(n)
