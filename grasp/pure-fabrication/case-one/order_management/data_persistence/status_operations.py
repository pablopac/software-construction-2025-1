from order_management.pure_fabrication.supabase_connection import SupabaseConnection
from supabase import  Client


class StatusOperations:

    @staticmethod
    def update_order_status_in_bd(order_status):
        supabase: Client = SupabaseConnection().get_connection()
        response = supabase.table("order_statuses").upsert(order_status).execute()
        return response.data