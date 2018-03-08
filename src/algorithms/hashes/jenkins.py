"""
jenkins_one_at_a_time_hash

Properties:
- non cryptographic

- output is distributed uniformly
- good avalanche effect / butterfly effect in hashing
- good time constant / fewer operations needed
"""


def jenkins(plaintext):
    code = 0
    for char in plaintext:
        code += ord(char)
        code += (code << 10)
        code ^= (code >> 6)

    code += (code << 3)
    code ^= (code >> 11)
    code += (code << 15)
    return code
