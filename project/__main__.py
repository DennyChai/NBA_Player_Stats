import DataTransformer
import CrawlerService
import DataProvider
import AppSettings
import traceback
import socket


def send_msg(msg=""):
    sys_log = traceback.format_exc()
    print("開發測試:", sys_log + msg)


def main():
    try:
        MACHINE_NAME = socket.gethostname()
        PROJECT_NAME = "NBAPlayerInfo"
        VERSION = "V1"
        my_settings = AppSettings.settings
        provider = DataProvider.DataProvider(send_msg, my_settings)
        transformer = DataTransformer.DataTransformer(send_msg, my_settings)
        service_inputs = {
            "machine_name": MACHINE_NAME,
            "transformer": transformer,
            "provider": provider,
            "send_msg": send_msg,
            "my_settings": my_settings,
        }
        print(f"{PROJECT_NAME} Start! Version:{VERSION}!")
        CrawlerService.CrawlerService(service_inputs).service()
    except:
        print(f"Main Error: {traceback.format_exc()}")


if __name__ == "__main__":
    main()
