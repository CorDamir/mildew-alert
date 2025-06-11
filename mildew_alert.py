from app_pages.multipage import MultiPage
# MultiPage class and logic behind it is NOT my work
# This idea is copied from Code Institute's lesson project
# Link can be found in "multipage.py"
from app_pages._1_project_summary import project_summary_page

mildew_alert = MultiPage(app_name="Mildew Alert!")

mildew_alert.add_page("Project summary", project_summary_page)

mildew_alert.run()
