# # entropy coding

# variable-size prefix-free encoding
from .shannon import get_shannon_table
from .shannon_fano import get_shannon_fano_table
from .huffman import get_huffman_table

from .tunstall import tunstall

from .variable_width_codecs import encode
from .variable_width_codecs import decode

# # dictionary/substitution coding


from .lempel_ziv import lzw_compress
from .lempel_ziv import lzw_decompress
