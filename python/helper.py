import numpy as np


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

