# PIC Development Container

Ce devcontainer fournit un environnement de développement complet pour les microcontrôleurs PIC avec :

- **XC8 Compiler v2.50** : Compilateur C pour microcontrôleurs PIC
- **MPLAB X IDE v6.25** : Environnement de développement intégré de Microchip
- **xc8-wrapper** et **ipecmd-wrapper** : Wrappers Python modernes
- **Java 8** : Requis pour MPLAB X IDE
- **Extensions VS Code** : Support C/C++, Python, debugging, etc.

## 🚀 Démarrage rapide

### 1. Pré-requis

- **Docker Desktop** installé et fonctionnel
- **VS Code** avec l'extension "Dev Containers"
- **X11 forwarding** configuré pour l'interface graphique (Linux/macOS)

### 2. Lancement du devcontainer

1. Ouvrez ce projet dans VS Code
2. Appuyez sur `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur macOS)
3. Tapez "Dev Containers: Reopen in Container"
4. Attendez la construction et la configuration automatique

### 3. Première utilisation

Une fois le container démarré, tous les outils sont configurés et prêts :

```bash
# Vérifier l'installation
xc8-wrapper --version
ipecmd-wrapper --version

# Compiler le projet
python compile.py

# Programmer le microcontrôleur (avec programmateur connecté)
python upload.py
```

## 🛠️ Outils disponibles

### Compilateur XC8
```bash
# Utilisation directe
xc8-cc --version

# Via wrapper Python (recommandé)
xc8-wrapper --tool cc --cpu PIC16F877A --xc8-version 2.50
```

### MPLAB X IDE

#### Interface graphique (nécessite X11 forwarding)
```bash
# Lance MPLAB X IDE avec interface graphique
mplab-gui
```

#### Ligne de commande
```bash
# Commandes MPLAB en ligne de commande
mplab --help
```

### Programmation
```bash
# Avec ipecmd-wrapper
ipecmd-wrapper -P 16F877A -T PK3 -F build/main.hex

# Ou avec le script Python
python upload.py
```

## Utilisation

### 1. Ouvrir dans VS Code

1. Assurez-vous d'avoir VS Code avec l'extension "Dev Containers" installée
2. Ouvrez ce projet dans VS Code
3. Cliquez sur "Reopen in Container" quand VS Code le propose
4. Attendez que le container se construise (peut prendre plusieurs minutes)

### 2. Si la construction échoue

1. Vérifiez votre connexion internet
2. Essayez la version simple : renommez `devcontainer.simple.json` → `devcontainer.json`
3. Ou utilisez Docker manuellement (voir ci-dessus)

### 3. Tester l'installation

```bash
# Vérifier XC8 (après installation automatique)
xc8-cc --version

# Vérifier xc8-wrapper
xc8-wrapper --version

# Compiler l'exemple
cd examples/blink
xc8-wrapper --tool cc --xc8-version 3.00 --cpu PIC16F877A --source-dir . --main-c-file main.c
```

### 4. Développer

Le container inclut tous les outils nécessaires pour :
- Développer en C pour PIC
- Modifier et tester xc8-wrapper
- Utiliser les outils de debug et d'analyse

## Structure du projet

```
.devcontainer/
├── devcontainer.json        # Configuration principale
├── devcontainer.simple.json # Configuration simplifiée (fallback)
├── Dockerfile              # Image Docker avec installation XC8
├── Dockerfile.simple       # Image Docker simple (XC8 installé après)
├── post-create.sh          # Script de post-installation
└── README.md              # Ce fichier

examples/
└── blink/
    ├── main.c             # Code exemple LED blink
    └── README.md          # Instructions
```

## Microcontrôleurs supportés

Le compilateur XC8 supporte tous les PIC 8 bits, incluant :
- PIC10F, PIC12F, PIC16F, PIC18F
- Exemples populaires : PIC16F877A, PIC18F4520, PIC12F675

## Dépannage

### Container ne se construit pas
- **Problème réseau** : Vérifiez votre connexion internet (téléchargement XC8 ~500MB)
- **Espace disque** : Assurez-vous d'avoir suffisamment d'espace (~2GB)
- **Timeout** : Le téléchargement XC8 peut être lent, essayez plusieurs fois

**Solution rapide** : Utilisez la version simple
```bash
cp .devcontainer/devcontainer.simple.json .devcontainer/devcontainer.json
```

### XC8 non trouvé après installation
```bash
# Vérifier l'installation
ls -la /opt/microchip/xc8/v3.00/bin/

# Ajouter au PATH manuellement
export PATH="/opt/microchip/xc8/v3.00/bin:$PATH"

# Ou réinstaller avec le script
bash .devcontainer/post-create.sh
```

### Compilation échoue
- Vérifiez le nom exact du MCU (sensible à la casse)
- Utilisez `--verbose` pour plus de détails
- Consultez la documentation XC8

### Permissions Docker sur Windows
```bash
# Si problème de permissions sur Windows
docker run --rm -it -v ${PWD}:/workspace -w /workspace ubuntu:22.04 bash
```

## Alternatives

### Docker Compose
```bash
# Développement avec docker-compose
docker-compose up xc8-dev

# Tests
docker-compose run test

# Compilation d'exemple
docker-compose run compile
```

### Installation manuelle de XC8
Si l'installation automatique échoue :

1. Téléchargez manuellement depuis [Microchip](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
2. Copiez le fichier `.run` dans le container
3. Exécutez l'installation manuelle

```bash
# Dans le container
sudo ./xc8-v3.00-full-install-linux-x64-installer.run --mode unattended --prefix /opt/microchip
```

## Ressources

- [Documentation XC8](https://www.microchip.com/en-us/tools-resources/develop/mplab-xc-compilers)
- [xc8-wrapper GitHub](https://github.com/s-celles/xc8-wrapper)
- [Datasheets PIC](https://www.microchip.com/en-us/products/microcontrollers-and-microprocessors/8-bit-mcus)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/remote/containers)
