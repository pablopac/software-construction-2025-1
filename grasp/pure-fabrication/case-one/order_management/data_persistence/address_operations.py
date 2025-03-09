from order_management.pure_fabrication.supabase_connection import SupabaseConnection
from supabase import  Client


class AddressOperations:

    @staticmethod
    def save_address_in_bd(address_details):
        supabase: Client = SupabaseConnection().get_connection()
        response = supabase.table("address_details").upsert(address_details).execute()
        return response.data

