from order_management.pure_fabrication.supabase_connection import SupabaseConnection
from supabase import  Client


class ClientOperations:

    @staticmethod
    def save_client_in_bd(address_details):
        supabase: Client = SupabaseConnection().get_connection()
        response = supabase.table("clients").upsert(address_details).execute()
        return response.data

