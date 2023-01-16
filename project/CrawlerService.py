from typing import Dict, Any
import time


class CrawlerService(object):
    def __init__(self, inputs):
        self.transformer = inputs["transformer"]
        self.provider = inputs["provider"]
        self.send_msg = inputs["send_msg"]
        self.setting = inputs["my_settings"]
        self.latest_send_time = time.time()

    def service(self):
        try:
            start_time = time.time()
            season_year = self.transformer.get_season_year()
            season_type = self.transformer.get_season_type("regular")
            player_info_content = self.provider.get_url_data("player_info", season_year, season_type)
            if player_info_content is None:
                self.send_msg("請求所有球員資料失敗!")
                return
            players_info = self.transformer.transform_player_info(player_info_content)
            for index, player_info in enumerate(players_info):
                self.player_service(player_info, season_year, season_type)
                time.sleep(5)
            print(f"球員共有{index+1}名, 花費時間:{time.time()-start_time:.2f}秒")
        except:
            self.send_msg()

    def player_service(self, player_info, season_year, season_type):
        player_id = str(player_info["PERSON_ID"])
        player_name = f'{player_info["PLAYER_FIRST_NAME"]} {player_info["PLAYER_LAST_NAME"]}'
        player_stats_content = self.provider.get_url_data("player_stats", player_id, season_year, season_type)
        if player_stats_content is not None:
            player_stats_datas = self.transformer.transform_player_stats(player_stats_content)
            for title, stats in player_stats_datas.items():
                for data in stats:
                    changed_match = self.transformer.get_match(player_id, player_name, data)
                    self.post_datas(title, changed_match)

    def post_datas(self, title: str, change_matches: Dict[str, Any]) -> None:
        try:
            print(title, change_matches)
            # TODO: Send or Write Datas here
            self.heartbeat_log()
        except:
            self.send_msg()

    def heartbeat_log(self) -> None:
        now = time.time()
        if now - self.latest_send_time >= 60:
            self.latest_send_time = now
            self.send_msg("傳送成功")
