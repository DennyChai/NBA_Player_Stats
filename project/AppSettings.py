settings = {
    "req_categories": ["ByYearBasePlayerDashboard"],  # 需要爬的數據種類
    "req_url": {
        "player_info": "https://stats.nba.com/stats/playerindex?College=&Country=&DraftPick=&DraftRound=&DraftYear=&Height=&Historical=0&LeagueID=00&Season={}&SeasonType={}&TeamID=0&Weight=",
        "player_stats": "https://stats.nba.com/stats/playerdashboardbyyearoveryearcombined?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerID={}&PlusMinus=N&Rank=N&Season={}&SeasonSegment=&SeasonType={}&ShotClockRange=&VsConference=&VsDivision=",
    },
    "headers": {
        "referer": "https://www.nba.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76",
    },
    "season_type": {
        "regular": "Regular%20Season",
        "preseason": "Pre%20Season",
        "playoffs": "Playoffs",
        "playin": "PlayIn",
    },
}
