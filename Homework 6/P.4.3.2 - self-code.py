"""Self code session for ROT13 program"""

def cyclic_shift(alphabet):
    result_shift = ''
    """Error handling to only calculate for lowercase"""
    if 'a' <= alphabet <= 'z':
        """Transform alphabet to unicode"""
        uni_num = ord(alphabet)
        result_shift = ((uni_num - ord('a') + 13) % 26 ) + ord('a')
        shift_alphabet = chr(result_shift)
        return shift_alphabet
    else:
        result_shift = alphabet
        return result_shift

def word_shift(word_input):
    result_word = ''
    for alpha in word_input:
        result_word += cyclic_shift(alpha)
    return result_word

def sentence_shift(sentence_input):
    result_sentence = ''
    for words in sentence_input.split():
        result_sentence += word_shift(words) + ' '
    return result_sentence

word = "hello"
print("Encoded word: " + word_shift(word))

sentence = "hello world this is rot13"
print("Encoded sentence: " + sentence_shift(sentence))