from . models import user_dashboard_table      
from . serializers import user_dashboard_table_serializer
class UserDataUpdate:
    @staticmethod
    def update_user_dashboard(user_email, problems_solved_increment=0, total_submissions_increment=0):
        try:
            dashboard_data = user_dashboard_table.objects.get(user_EmailD=user_email)
            dashboard_data.problems_solved += problems_solved_increment
            dashboard_data.total_submissions += total_submissions_increment
            dashboard_data.save()
            serializer = user_dashboard_table_serializer(dashboard_data)
            return serializer.data
        except user_dashboard_table.DoesNotExist:
            return None