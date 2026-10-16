#exercise 1
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return True if len(zip_code) == 5 and zip_code.isnumeric() else False
    pass

# có thể dùng hàm isdigit

#exercise 2
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    list = []
    for word in doc_list: #lấy 1 đoạn
        a = word.split() #chia thành nhiều từ
        
        for b in a:
            if b.lower().strip('.,') == keyword:
                list.append(doc_list.index(word)) #nếu strip nó là casio thì lấy thứ tự của word
                break #phải break vì 1 đoạn có thể có nhiều từ casio, có 1 từ => auto qua luôn k in lại nữa
    return list

#or
def word_search(doc_list, keyword):
    # tạo 1 list rỗng
    indices = [] 
    # lập hàm gồm thứ tự (index) và đoạn 
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens] # tạo 1 hàm gồm toàn chữ lower case và k có .,
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
        # nếu keyword trong normalized => lấy i thêm vào indices
    return indices

#exercise 3
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    dics = {}
    for small_word in keywords:
        dics[small_word] = word_search(doc_list, small_word)
    return dics
        
print(multi_word_search(["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"], ['casino', 'they']))
