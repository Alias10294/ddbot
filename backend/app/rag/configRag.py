from pathlib import Path

# Chemin vers le jsonl dans lequel est stocké le rag
BACKEND_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = BACKEND_DIR / "data" / "chunks.jsonl"

liens_RAG = [
    "https://numerique.uphf.fr/organisation/s%C3%A9curit%C3%A9%20des%20syst%C3%A8mes%20d%27information",
    "https://www.info.gouv.fr/risques",
    "https://cyber.gouv.fr/",

    # Wiki de l'uphf
    "https://www.uphf.fr/wiki/doku.php/Accueil%20",
    # Achat logiciel et matériel
    "https://www.uphf.fr/wiki/doku.php/outils/achat_logiciel_et_materiel/marches_informatiques/antivirus",
    "https://www.uphf.fr/wiki/doku.php/outils/achat_logiciel_et_materiel/marches_informatiques/redhat",
    "https://www.uphf.fr/wiki/doku.php/outils/achat_logiciel_et_materiel/marches_informatiques/vmware",
    # Assistance
    "https://www.uphf.fr/wiki/doku.php/outils/assistance/helpdesk/demande_interventions",
    # Enseignement
    "https://www.uphf.fr/wiki/doku.php/outils/enseignement/moodle",
    "https://www.uphf.fr/wiki/doku.php/outils/enseignement/salle_info",
    "https://www.uphf.fr/wiki/doku.php/outils/enseignement/wooclap/wooclap_pour_dynamiser_un_cours",
    # Identité Numérique
    "https://www.uphf.fr/wiki/doku.php/outils/identite_numerique/sesame",
    # Infrastructures, réseau et téléphonie
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/reseau/configurer_le_proxy",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/reseau/proxy_ftp",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/telephonie",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/telephonie_sur_pc/guide_cisco_jabber",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/vpn/eduvpn",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/vpn/vpn_installation_linux",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/vpn/vpn_installation_macos",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/vpn/vpn_installation_windows",
    "https://www.uphf.fr/wiki/doku.php/outils/infrastructures_reseau_et_telephonie/wifi",
    # Poste de travail
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/documentation_diverse/connecter_mes_espaces_professionnels_sur_mac",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/documentation_diverse/definir_imprimante_par_defaut",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/documentation_diverse/monter_lecteur_reseau_ad_uphf",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/documentation_diverse/monter_lecteur_reseau",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/documentation_diverse/mot_de_passe_adm",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/documentation_diverse/ouverturesessionadm",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/migration_ad",
    "https://www.uphf.fr/wiki/doku.php/outils/poste_de_travail/ent",
    # Sécurité et réglementation
    "https://www.uphf.fr/wiki/doku.php/outils/securite_et_reglementation/cybersecurite/hameconnage",
    "https://www.uphf.fr/wiki/doku.php/outils/securite_et_reglementation/esup_otp",
    "https://www.uphf.fr/wiki/doku.php/outils/securite_et_reglementation/gestionnaire_de_mots_de_passe",
    # Stockage des données
    "https://www.uphf.fr/wiki/doku.php/outils/stockage_des_donnees/cloud/installer_et_configurer_nextcloud",
    "https://www.uphf.fr/wiki/doku.php/outils/stockage_des_donnees/cloud/mettre_un_fichier_sur_le_cloud",
    "https://www.uphf.fr/wiki/doku.php/outils/stockage_des_donnees/cloud/partager_un_fichier_a_un_exterieur",
    "https://www.uphf.fr/wiki/doku.php/outils/stockage_des_donnees/cloud/partager_un_fichier_a_une_personne_de_l_uphf",
    "https://www.uphf.fr/wiki/doku.php/outils/stockage_des_donnees/dossiers_partages/accesdocuments"
]

# Paramètres pour les chunks
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150

# Paramètres pour le classement
NUMBER_OF_CHUNK_SELECTED = 3
LAMBDA = 0.7