"""
A useful list of words for a naive model for flagging text that indicates disasters are taking place.

This is not a complicated or extensive model.
"""

# A set of keywords that indicate a fire
FIRE_KEYWORDS = {'fire'}

# A set of keywords that indicate a flood
FLOOD_KEYWORDS = {'flood', 'flooded', 'flooding',
                  'landslide', 'mudslide'}

# All disaster keywords.
ALL_KEYWORDS = set.union(FIRE_KEYWORDS) \
    .union(FLOOD_KEYWORDS)
