Import("env")
import sys

def prompt_for_variable(target, source, env):
    sys.stdout.write("Entrez la valeur pour ID_ETENDARD : ")
    sys.stdout.flush()
    value = input()
    env.Append(CPPDEFINES=[("ID_ETENDARD", env.StringifyMacro(value))])

env.AddPreAction("$BUILD_DIR/${PROGNAME}.elf", prompt_for_variable)

# env.AddPreAction("buildprog", prompt_for_variable)  # END


#env.AddPostAction("$BUILD_DIR/src/main.cpp.o", prompt_for_variable)
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