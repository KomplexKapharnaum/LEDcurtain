# Teensy KxKm Artnet Node
**Version: V1.0.0**
# Clément SAILLANT pour KomplexKapharnaüm

Ce projet est un nœud Artnet basé sur Teensy 4.1 pour contrôler jusqu'a 50 bandes LED. La Teensy 4.1 est un microcontrôleur puissant capable de piloter un grand nombre de LEDs. Ce projet utilise la bibliothèque FastLED et objectFLED pour contrôler les LEDs et la bibliothèque Artnet pour recevoir les données Artnet.

Utilisé avec les cartes suivante : 

https://github.com/KomplexKapharnaum/LEDcurtain_hardware


* Teensy Board 4.1: https://www.pjrc.com/store/teensy41.html 
* Ethernet Kit for Teensy 4.1: https://www.pjrc.com/store/ethernet_kit.html
* FastLED: https://github.com/FastLED/FastLED
* ObjectFLED: https://github.com/KurtMF/ObjectFLED
* Artnet Library: https://github.com/natcl/Artnet

Basé sur l'exemple original Artnet de la bibliothèque OctoWS2811 de Paul Stoffregen et inspiré par Studio Jordan Shaw // http://jordanshaw.com artnet node et la bibliothèque objectFLED de .

**Remarque:** pour Teensy 4.1, Teensyduino et la bibliothèque Artnet, le fichier artnet.h suivant doit être modifié pour fonctionner avec 4.1.
Modifiez ce fichier pour utiliser NativeEthernet `/Users/[USER]/Library/Arduino15/packages/teensy/hardware/avr/1.58.1/libraries/Artnet/Artnet.h`

Teensy 4.1 nécessite `NativeEthernet.h` et `NativeEthernetUdp.h`.
Pour éviter les conflits de bibliothèques, il est utilisé la bibliothèque Artnet modifiée incluse avec Teensyduino. Autour de la ligne ~30 dans Artnet.h
[le fil PJRC.](https://forum.pjrc.com/index.php?threads/does-the-artnet-library-work-with-the-native-ethernet-library.70064/)

```
#if defined(ARDUINO_SAMD_ZERO)
    #include <WiFi101.h>
    #include <WiFiUdp.h>
#else
    // #include <Ethernet.h>
    // #include <EthernetUdp.h>
    #include <NativeEthernet.h>
    #include <NativeEthernetUdp.h>
#endif
```

## Sources d'inspiration et de facilitation

Exemple original Artnet de la bibliothèque OctoWS2811 de Paul Stoffregen
https://github.com/PaulStoffregen/OctoWS2811/blob/master/examples/Artnet/Artnet.ino

Implémentation de la bibliothèque ObjectFLED pour utiliser jusqu'à 50 sortie pour strip LED
https://github.com/KurtMF/ObjectFLED


## Serveur Artnet / Application Processing
Vous pouvez utiliser une application Processing.org personnalisée pour générer les visuels LED.
Le problème avec cela est que la bibliothèque Artnet compatible avec la configuration Teensy/Octo n'est pas la bibliothèque du gestionnaire de bibliothèques Processing.
VOUS DEVEZ télécharger et installer manuellement depuis le dépôt de Florian [Artnet4j - Art-Net DMX over IP library for Java and Processing repo](https://github.com/cansik/artnet4j).

Ce projet a été testé avec MadMapper, et il fonctionne parfaitement. Vous pouvez également utiliser QLC+ ou tout autre logiciel compatible Artnet.
