import re

tokenizer = re.compile(r'''
    (int|float|bool|set|list|tuple) | # types
    ([0-9\.]+) | # number include int and float
    (False|True) | # Bool 
    (\'\w+\'|\"\w+\") | # String
    (\s+) | # whitespaces
    (\:) | # colon
    (\() | (\)) | # L,R Paren
    ([a-zA-Z_]\w*) | # etc Name
    (None|and|as|assert|async|await|break|class|continue
    |def|del|elif|else|except|finally|for|from|global|if|
    import|in|is|lambda|nonlocal|not|or|pass|raise|return|
    try|while|with|yield) # Keyword tag
''', re.VERBOSE)

token_tag_list = ['TYPE', 'NUM', 'BOOL', 'STRING', 'WHITESPACE', 
                'COLON', 'L_PAREN', 'R_PAREN', 'NAME', 'KEYWORD']

