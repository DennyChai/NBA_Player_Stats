from dataclasses import dataclass


@dataclass
class Match(object):
    PlayerID: str = ""
    Name: str = ""
    Year: str = ""
    Team: str = ""
    GamePlayed: str = ""
    Win: str = ""
    Lose: str = ""
    WinRate: str = ""
    MinPlayed: str = ""
    FieldGoalsMade: str = ""
    FieldGoalsAttempted: str = ""
    FieldGoalsRate: str = ""
    FieldGoalsMade_3Point: str = ""
    FieldGoalsAttempted_3Point: str = ""
    FieldGoalsRate_3Point: str = ""
    FreeThrowsMade: str = ""
    FreeThrowsAttempted: str = ""
    FreeThrowsRate: str = ""
    OffensiveRebounds: str = ""
    DefensiveRebounds: str = ""
    Rebounds: str = ""
    Assists: str = ""
    Steals: str = ""
    Blocks: str = ""
    Turnovers: str = ""
    PersonalFouls: str = ""
    Points: str = ""
    PlusMinus: str = ""

    def change_match(self):
        match = {
            "Id": self.PlayerID,
            "Name": self.Name,
            "Year": self.Year,
            "Team": self.Team,
            "Record": {
                "GamePlayed": self.GamePlayed,
                "Win": self.Win,
                "Lose": self.Lose,
                "WinRate": self.WinRate,
                "MinutesPlayed": self.MinPlayed,
                "FieldGoalsMade": self.FieldGoalsMade,
                "FieldGoalsAttempted": self.FieldGoalsAttempted,
                "FieldGoalsRate": self.FieldGoalsRate,
                "FieldGoalsMade_3Point": self.FieldGoalsMade_3Point,
                "FieldGoalsAttempted_3Point": self.FieldGoalsAttempted_3Point,
                "FieldGoalsRate_3Point": self.FieldGoalsRate_3Point,
                "FreeThrowsMade": self.FreeThrowsMade,
                "FFreeThrowsAttemptedTA": self.FreeThrowsAttempted,
                "FreeThrowsRate": self.FreeThrowsRate,
                "OffensiveRebounds": self.OffensiveRebounds,
                "DefensiveRebounds": self.DefensiveRebounds,
                "Rebounds": self.Rebounds,
                "Assists": self.Assists,
                "Steals": self.Steals,
                "Blocks": self.Blocks,
                "Turnovers": self.Turnovers,
                "PersonalFouls": self.PersonalFouls,
                "Points": self.Points,
                "PlusMinus": self.PlusMinus,
            },
        }
        return match
