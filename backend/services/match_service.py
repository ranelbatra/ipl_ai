from data.match_context import get_match_context


def load_match(season, match_name):
    """
    Returns a complete match context
    for all AI features.
    """
    return get_match_context(season, match_name)