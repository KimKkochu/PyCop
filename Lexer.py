import re
import keyword

token = {
    "KEYWORD": "|".join(keyword.kwlist),
    "TYPE": "int|bool|float|str|list|set|tuple",
    "INT" : r'\d+',
    "FLOAT" : r'\d+[.]\d+',
    "STRING" : r'\'\w+\'|\"\w+\"',
    "LIST" : r'\[w+\]'
}

token_list = [f"({i})" for i in token.values()]
tokenizer = re.compile('|'.join(token_list))

print(tokenizer.findall('False int bool 121.21 "33231" [1, 2]'))
