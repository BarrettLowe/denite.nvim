# ============================================================================
# FILE: sorter/cpph.py
# AUTHOR: Barrett Lowe <barrett.lowe at gmail.com>
# DESCRIPTION: Simple sorter to show .c, .cpp, and .h files before other files
# License: MIT license
# ============================================================================
from ..base import Base
from itertools import compress


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'sorter/cpph'
        self.description = 'show .c, .cpp, and .h files before others'

    def filter(self, context):

        types=['.cpp', '.c','.h']

        return sorted(context['candidates'], key=lambda x: any([x['word'].endswith(y) for y in types]), reverse=True)
