# # entropy coding

# variable-width prefix-free codes
from .shannon import get_shannon_table
from .shannon_fano import get_shannon_fano_table
from .huffman import get_huffman_table

# variable-width prefix-free words
from .tunstall import get_tunstall_table

# codecs
from .variable_width_codecs import encode_var_code
from .variable_width_codecs import decode_var_code

from .variable_width_codecs import encode_var_word
from .variable_width_codecs import decode_var_word

# # dictionary/substitution coding
from .lempel_ziv_welch import lzw_compress
from .lempel_ziv_welch import lzw_decompress
