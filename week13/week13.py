# التكليف 01
# "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
# \w\s

# التكليف 02
# "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
# L\w\w\w\w\w\w

# التكليف 03
# +(0100) 600-1234
# +(0100) 60-1234
# (0100) 6000-1234
# 01006001234
# 0100 600 1234
# (0100) 600-1
# (0100) 600-12
# \W{1,2}\d{4}\W\s\d{2}...\d{2,4}

# التكليف 04
# http://www.elzero.org:8888/link.php
# https://elzero.org:8888/link.php
# http://www.elzero.com/link.py
# https://elzero.com/link.py
# http://www.elzero.net
# https://elzero.net
# [A-z]*\W*[A-z\.]*(com|org)\w*\W?[A-z0-9]*(\.|/)[a-z\.]*


# التكليف 05
# http
# https
# abcd
# abcd
# 1)    http.*
# 2)    [e-z]
# 3)    ...p(s)?
# 4)    [a-z]tt[a-z]*
# 5)    [a-z]*p[a-z]*
# 6)    https?
