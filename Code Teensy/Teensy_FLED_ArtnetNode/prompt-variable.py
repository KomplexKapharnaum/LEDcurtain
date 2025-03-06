Import("env")

def prompt_for_variable(target, source, env):
    value = input("Entrez la valeur pour ID_ETENDARD : ")
    env.Append(CPPDEFINES=[("ID_ETENDARD", env.StringifyMacro(value))])

env.AddPreAction("buildprog", prompt_for_variable)

# from SCons.Script import Import
# 
# Import("env")
# 
# def generate_config_file(source, target, env):
#     with open("src/config.h", "w") as f:
#         f.write("#define WIFI_SSID \"MyNetwork\"\n")
#         f.write("#define WIFI_PASSWORD \"MyPassword\"\n")
#     print("Fichier config.h généré.")
# 
# env.AddPreAction("buildprog", generate_config_file)     