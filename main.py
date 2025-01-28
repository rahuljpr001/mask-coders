import streamlit as st
import streamlit_option_menu
import about, account,home,projects,about,contact_us
st.set_page_config(
    page_title="MASK CODERS"
    )
class Multipp:
    def __init__(self):
        self.apps =[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "fuction":function
            })

    def run():
        with st.sidebar:
            app=option_menu(
                menu_title="MASK CODERS",
                options=["HOME","ACCOUNT","PROJECTS","ABOUT","CONTACT_US"],
                icons=["house-fill","person-circle","trophy-fill","question mark","phone"],
                default_index=1,
                )
        if app == "HOME":
            home.app()
        if app == "ACCOUNT":
            account.app()
        if app == "PROJECTS":
            projects.app()

        if app == "ABOUT":
            about.app()
        if app == "CONTACT_US":
            contact_us.app()

    run()
                
