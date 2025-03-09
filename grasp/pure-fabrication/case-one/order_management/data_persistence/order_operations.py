from order_management.pure_fabrication.supabase_connection import SupabaseConnection
from supabase import  Client


class OrderOperations:

    @staticmethod
    def save_order_in_bd(order):
        supabase: Client = SupabaseConnection().get_connection()
        response = supabase.table("checkout-order").insert(order).execute()
        return response.data