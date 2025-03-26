import os

# Fonction pour demander les valeurs des flags
def get_build_flags():
    v_etendard = input("Entrez la valeur pour V_ETENDARD : ")
    id_etendard = input("Entrez la valeur pour ID_ETENDARD : ")
    # Générer les flags sous forme de chaîne
    return f"-D V_ETENDARD={v_etendard} -D ID_ETENDARD={id_etendard}"

# Écrire les flags dans une variable d'environnement
os.environ["CUSTOM_BUILD_FLAGS"] = get_build_flags()