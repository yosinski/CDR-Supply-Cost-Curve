import numpy as np
from math import floor, ceil
from prettytable import PrettyTable


class DuckStruct(object):
    '''Use to store anything!'''

    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        rep = ['%s=%s' % (k, repr(v)) for k,v in self.__dict__.items()]
        return 'DuckStruct(%s)' % ', '.join(rep)


# Tags in order in which tags will be plot
# Colors are those used on https://carbonplan.org/research/cdr-database
# The order below is the order in which data are plotted, matching CarbonPlan's plot order:
_colors = {
    'forests': (49.0, 70.0, 42.0),
    'soil': (92.0, 59.0, 33.0),
    'biomass': (83.0, 75.0, 37.0),
    'ocean': (39.0, 73.0, 77.0),
    'mineralization': (66.0, 71.0, 77.0),
    'dac': (74.0, 52.0, 85.0),
}
colors = {k: np.array(v)/100.0 for k, v in _colors.items()}
# ['forests', 'soil', 'biomass', 'ocean', 'mineralization', 'dac']
primary_tags = list(colors.keys())
primary_tag_set = set(primary_tags)

primary_tags_carbonplan_pt_order = ['forests', 'soil', 'biomass', 'dac', 'mineralization', 'ocean']


def get_pt(tags):
    '''Returns a single primary tag (first tag from primary_tags found), or 'none' if project has no primary tags.'''
    for pt in primary_tags_carbonplan_pt_order:
        if pt in tags:
            #print('For tags', tags, 'returning', pt)
            return pt
    else:
        return 'none'


def get_clr(tags, default_clr=(.7, .7, .7)):
    '''Returns the color of the first tag found, if any, or a default color if not.'''
    pt = get_pt(tags)
    return default_clr if pt == 'none' else colors[pt]


def lsprint(lst, max_width=90, return_str=False, align='l'):
    '''Print a list in columns like ls, where each column is as narrow as
    possible and items are printed in column-major order.

    If return_str then return string instead of printing.

    A bit hacky. Assumes that the n_cols -> width function is
    monotonic, which it might not be.
    '''
    
    min_n_cols = 1  # This will succeed or, if it fails, just print it anyway.
    max_n_cols = int(floor(max_width / 2)) + 1   # Two spaces padding + zero characters width. This should fail.

    def get_table_string_with_n_cols(lst, n_cols, align=align):
        xx = PrettyTable(border=False, header=False)
        n_rows = int(ceil(len(lst)/n_cols))
        for jj in range(n_cols):
            col = lst[n_rows*jj:n_rows*(jj+1)]
            col.extend([''] * (n_rows - len(col)))
            xx.add_column('', col)
        xx.align = align
        return xx.get_string()

    # First try with 1 col.
    largest_working = get_table_string_with_n_cols(lst, min_n_cols, align=align)
    if len(largest_working.split('\n', 1)[0]) <= max_width:
        # If this worked, proceed with binary seach. Else just return.
        while min_n_cols + 1 < max_n_cols:
            try_n_cols = (min_n_cols + max_n_cols) // 2
            assert try_n_cols != min_n_cols, 'logic error'

            st = get_table_string_with_n_cols(lst, try_n_cols, align=align)        
            if len(st.split('\n', 1)[0]) > max_width:
                # Too wide, decrease max
                max_n_cols = try_n_cols
            else:
                # It worked, increase min
                min_n_cols = try_n_cols
                largest_working = st

    if return_str:
        return largest_working
    else:
        print(largest_working)
