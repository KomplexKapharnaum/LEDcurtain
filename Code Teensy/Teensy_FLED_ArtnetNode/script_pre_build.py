Import("env")

if env.IsIntegrationDump():
    # Arrêter l'exécution du script
    Return()
    
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

v_etendard = input(f"Entrez la valeur pour V_ETENDARD [{config['build_flags']['V_ETENDARD']}]: ") or config['build_flags']['V_ETENDARD']
id_etendard = input(f"Entrez la valeur pour ID_ETENDARD [{config['build_flags']['ID_ETENDARD']}]: ") or config['build_flags']['ID_ETENDARD']

config['build_flags']['V_ETENDARD'] = v_etendard
config['build_flags']['ID_ETENDARD'] = id_etendard

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print(f"-D V_ETENDARD={v_etendard} -D ID_ETENDARD=\"{id_etendard}\"")