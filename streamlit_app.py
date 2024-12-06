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
name, authentication_status, username = authenticator.login("Connexion", "main")

# Définir la page d'accueil
def accueil():
    st.title("Bienvenue chez Santa Mamamia")

# Vérifier l'état d'authentification
if authentication_status:
    accueil()
    authenticator.logout("Déconnexion", "main")
    
    # Menu de navigation avec streamlit_option_menu
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"],
        icons=["house", "camera"],  # Optionnel : Ajoutez des icônes
        menu_icon="cast",  # Optionnel : Icône du menu principal
        default_index=0,  # L'onglet par défaut
    )

    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos":
        st.write("Bienvenue sur mon album photo")
        # Ajoutez des photos ici si nécessaire
        st.image(["image1.jpg", "image2.jpg"], caption=["Photo 1", "Photo 2"], width=300)

elif authentication_status is False:
    st.error("L'username ou le password est/sont incorrect(s)")

elif authentication_status is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
