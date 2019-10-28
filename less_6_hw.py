import sys
from collections import Counter
from math import log

def tf_idf(term, doc: list, corpus):
    tf = doc.count(term) / len(doc)
    amount_docs_with_term = len([d for d in corpus if term in d])
    idf = log(len(corpus) / amount_docs_with_term)
    print(*[f'Object name: {obj[0]} size: {sys.getsizeof(obj)} bytes\n' for obj in locals().items()], '\n')
    return tf * idf


doc_1 = ['bbb', 'ccc']
doc_2 = ['aaa', 'bbb', 'ccc', 'ddd','aaa', 'bbb', 'ccc', 'ddd','aaa', 'bbb', 'ccc', 'ddd','aaa', 'bbb', 'ccc', 'ddd','aaa', 'bbb', 'ccc', 'ddd','aaa', 'bbb', 'ccc', 'ddd','aaa', 'bbb', 'ccc', 'ddd']
doc_3 = ['aaa', 'bbb', 'ddd']
corpus = [doc_1, doc_2, doc_3]

tf_idf('aaa', doc_2, corpus)

def control_bytes(foo):
    import inspect, sys
    local_string = """    print(*[f'Object name: {obj[0]} size: {sys.getsizeof(obj)} bytes\n' for obj
    in locals().items()], '\n')\n
    """
    foo_lines = inspect.getsourcelines(tf_idf)
    if foo_lines[-1].__str__().startswith('return'):
        foo_lines.insert(-1, local_string)
    print(*foo_lines)
    eval(''.join(foo_lines))

control_bytes(tf_idf)
