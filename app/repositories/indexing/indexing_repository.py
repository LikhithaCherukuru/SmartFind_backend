from app.core.database import supabase_admin


class IndexingRepository:

    def create_scan(self, data: dict):

        return (

            supabase_admin

            .table("scan_history")

            .insert(data)

            .execute()

            .data[0]

        )

    def finish_scan(

        self,

        scan_id,

        files_found,

        new_files,

        duplicates,

        failed

    ):

        return (

            supabase_admin

            .table("scan_history")

            .update({

                "status": "completed",

                "files_found": files_found,

                "new_files": new_files,

                "duplicates": duplicates,

                "failed": failed

            })

            .eq("id", scan_id)

            .execute()

        )

    def update_failed(self, scan_id):

        return (

            supabase_admin

            .table("scan_history")

            .update({

                "status": "failed"

            })

            .eq("id", scan_id)

            .execute()

        )