from data.loader import (
    get_match_details,
    get_match_innings,
    get_match_deliveries,
    get_team_match_stats,
    get_player_match_stats,
    get_match_aura,
)


def get_match_context(season: str, match_name: str):
    """
    Build a unified match context by combining metadata
    from the CSV and analytics from the Excel workbook.
    """

    metadata = get_match_details(season, match_name)

    if metadata is None:
        return None

    match_id = metadata["match_id"]

    return {
        "metadata": metadata,
        "innings": get_match_innings(match_id),
        "deliveries": get_match_deliveries(match_id),
        "team_stats": get_team_match_stats(match_id),
        "player_stats": get_player_match_stats(match_id),
        "match_aura": get_match_aura(match_id),
    }