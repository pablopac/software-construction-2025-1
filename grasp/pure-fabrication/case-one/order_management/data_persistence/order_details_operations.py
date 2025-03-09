from order_management.pure_fabrication.supabase_connection import SupabaseConnection
from supabase import  Client


class OrderDetailsOperations:

    @staticmethod
    def save_order_details_in_bd(order_details):
        supabase: Client = SupabaseConnection().get_connection()
        response = supabase.table("order-details").insert(order_details).execute()
        return response.data