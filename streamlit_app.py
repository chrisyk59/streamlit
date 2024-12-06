import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données des comptes utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {'name': 'utilisateur', 'password': 'utilisateurMDP', 'email': 'utilisateur@gmail.com', 'failed_login_attemps': 0, 'logged_in': False, 'role': 'utilisateur'},
        'root': {'name': 'root', 'password': 'rootMDP', 'email': 'admin@gmail.com', 'failed_login_attemps': 0, 'logged_in': False, 'role': 'administrateur'}
    }
}

# Initialisation de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",  # Nom du cookie
    "cookie_key",  # Clé du cookie
    30  # Durée du cookie en jours
)

# Gérer la connexion
authenticator.login()

def accueil():
    st.title("Bienvenue chez Santa Mamamia")

if st.session_state.get("authentication_status"):
    accueil()
    authenticator.logout("Déconnexion")
    
    # Menu de navigation avec streamlit_option_menu
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"]
    )
if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
elif st.session_state.get("authentication_status") is False:
    st.error("L'username ou le password est/sont incorrect(s)")
elif st.session_state.get("authentication_status") is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
