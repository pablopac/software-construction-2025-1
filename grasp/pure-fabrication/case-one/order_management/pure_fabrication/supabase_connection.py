from supabase import create_client

from order_management.helpers.config_loader import ConfigLoader


class SupabaseConnection:
    _instance = None
    def __init__(self):
        pass

    def __new__(cls):
        if cls._instance is None:
            cls.instance = super().__new__(cls)
            user, password = ConfigLoader.load_credentials("SUPABASE")
            cls._instance.__connection = create_client(user, password)
        return cls._instance

    def get_connection(self):
        return  self.__connection




