from order_management.pure_fabrication.supabase_connection import SupabaseConnection
from supabase import  Client


class PaymentOperations:

    @staticmethod
    def save_payment_in_bd(address_details):
        supabase: Client = SupabaseConnection().get_connection()
        response = supabase.table("payments").upsert(address_details).execute()
        return response.data

