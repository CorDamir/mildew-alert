from app_pages.__multipage import MultiPage
# MultiPage class and logic behind it is NOT my work
# This idea is copied from Code Institute's lesson project
# Link can be found in "multipage.py"
from app_pages._1_project_summary import project_summary_page
from app_pages._2_data_study import data_study_page
from app_pages._3_mildew_alerter import mildew_alerter_page
from app_pages._4_hypothesis import hypothesis_page
from app_pages._5_technical_information import technical_informatio_page

mildew_alert = MultiPage(app_name="Project: Mildew Alert!")

mildew_alert.add_page("Project summary", project_summary_page)
mildew_alert.add_page("Data study", data_study_page)
mildew_alert.add_page("Mildew alerter", mildew_alerter_page)
mildew_alert.add_page("Hypothesis", hypothesis_page)
mildew_alert.add_page("Technical information", technical_informatio_page)

mildew_alert.run()
