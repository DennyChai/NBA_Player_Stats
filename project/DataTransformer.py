from typing import List, Dict, Any
from datetime import datetime
from Match import Match


class DataTransformer:
    def __init__(self, send_msg, my_settings):
        self.send_msg = send_msg
        self.setting = my_settings

    def get_season_type(self, type: str) -> str:
        return self.setting["season_type"][type]

    def get_season_year(self) -> str:
        year_now = datetime.now().year
        return f"{year_now-1}-{str(year_now)[2:]}"

    def convert_percentage(self, data: float):
        return f"{data*100:.1f}%"

    def transform_player_info(self, players_info_content: Dict[str, Any]) -> List[Dict[str, Any]]:
        result = []
        try:
            if "resultSets" not in players_info_content:
                self.send_msg(f"resultSets沒有資料, Data:{players_info_content}")
                return []
            for player_info in players_info_content["resultSets"]:
                if "rowSet" not in player_info:
                    self.send_msg(f"rowSet沒有資料, Data:{player_info}")
                    return []
                data_headers = player_info["headers"]
                for player_data in player_info["rowSet"]:
                    result.append(dict(zip(data_headers, player_data)))
        except:
            self.send_msg()
        return result

    def transform_player_stats(self, players_stats_content: Dict[str, Any]) -> Dict[str, List[Any]]:
        players_stats = {}
        try:
            if "resultSets" not in players_stats_content:
                self.send_msg(f"resultSets沒有資料, Data:{players_stats_content}")
                return {}
            for player_stats in players_stats_content["resultSets"]:
                if "rowSet" not in player_stats:
                    self.send_msg(f"rowSet沒有資料, Data:{player_stats}")
                    return {}
                stats_title = player_stats["name"]
                data_headers = player_stats["headers"]
                for player_stat in player_stats["rowSet"]:
                    if stats_title not in self.setting["req_categories"]:
                        continue
                    if stats_title not in players_stats:
                        players_stats[stats_title] = []
                    players_stats[stats_title].append(dict(zip(data_headers, player_stat)))
        except:
            self.send_msg()
        return players_stats

    def get_match(self, player_id: str, player_name: str, player_stats: Dict[str, Any]) -> Match:
        try:
            return Match(
                PlayerID=player_id,
                Name=player_name,
                Year=player_stats["GROUP_VALUE"],
                Team=player_stats["TEAM_ABBREVIATION"],
                GamePlayed=player_stats["GP"],
                Win=player_stats["W"],
                Lose=player_stats["L"],
                WinRate=self.convert_percentage(player_stats["W_PCT"]),
                MinPlayed=str(player_stats["MIN"]),
                FieldGoalsMade=str(player_stats["FGM"]),
                FieldGoalsAttempted=str(player_stats["FGA"]),
                FieldGoalsRate=self.convert_percentage(player_stats["FG_PCT"]),
                FieldGoalsMade_3Point=str(player_stats["FG3M"]),
                FieldGoalsAttempted_3Point=str(player_stats["FG3A"]),
                FieldGoalsRate_3Point=self.convert_percentage(player_stats["FG3_PCT"]),
                FreeThrowsMade=str(player_stats["FTM"]),
                FreeThrowsAttempted=str(player_stats["FTA"]),
                FreeThrowsRate=self.convert_percentage(player_stats["FT_PCT"]),
                OffensiveRebounds=str(player_stats["OREB"]),
                DefensiveRebounds=str(player_stats["DREB"]),
                Rebounds=str(player_stats["REB"]),
                Assists=str(player_stats["AST"]),
                Steals=str(player_stats["STL"]),
                Blocks=str(player_stats["BLK"]),
                Turnovers=str(player_stats["TOV"]),
                PersonalFouls=str(player_stats["PF"]),
                Points=str(player_stats["PTS"]),
                PlusMinus=str(player_stats["PLUS_MINUS"]),
            ).change_match()
        except:
            self.send_msg(f"ID:{player_id}, Name:{player_name}, Data:{player_stats}")
