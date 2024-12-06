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

# Fonction principale : Accueil avec navigation
def accueil():
    st.title("Bienvenue chez Santa Mamamia")
    
    # Initialisation de l'état pour la sélection du menu
    if "menu_selection" not in st.session_state:
        st.session_state["menu_selection"] = "Accueil"

    # Sidebar avec menu de navigation
    with st.sidebar:
        selection = option_menu(
            menu_title="Navigation",  # Titre de la barre
            options=["Accueil", "Photos"],  # Options dans la barre
            icons=["house", "camera"],  # Icônes associées
            menu_icon="menu-app",  # Icône pour le menu global
            default_index=["Accueil", "Photos"].index(st.session_state["menu_selection"])  # Synchronisation avec l'état
        )
        # Mettre à jour l'état avec la sélection actuelle
        st.session_state["menu_selection"] = selection

    # Contenu des pages
    if st.session_state["menu_selection"] == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif st.session_state["menu_selection"] == "Photos":
        st.write("Bienvenue sur mon album photo !")

if st.session_state.get("authentication_status"):
    accueil()
    # Ajout d'une clé unique au bouton de déconnexion
    authenticator.logout("Déconnexion", key="unique_logout_button")
    
elif st.session_state.get("authentication_status") is False:
    st.error("L'username ou le password est/sont incorrect(s)")
elif st.session_state.get("authentication_status") is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
