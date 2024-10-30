import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
      API_ID = int(os.environ.get("APP_ID", "28714959"))
      API_HASH = os.environ.get("API_HASH", "c0b9797634090ee3f4c1c56db6c051a7")
      CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "<b>{file_name} \n\n ⌬  Powered By ~ @Thefilimfactor</b>")
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "HikariTsuki")
