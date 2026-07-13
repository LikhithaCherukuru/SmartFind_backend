from app.core.database import supabase


class UserRepository:

    def get_profile(self, user_id: str):

        return (
            supabase
            .table("profiles")
            .select("*")
            .eq("id", user_id)
            .single()
            .execute()
        )

    def update_profile(
        self,
        user_id: str,
        data: dict
    ):

        return (
            supabase
            .table("profiles")
            .update(data)
            .eq("id", user_id)
            .execute()
        )