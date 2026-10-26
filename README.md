# 👑 Tibia PilotNG 👑

lightxcvn+ruby@gmail.com
ajshdgsksgshdgff+leung@gmail.com

🤖 The most advanced 24/7 Full-Auto PixelBot for Tibia with Cavebot, Refiller, Depositer and more.

![Logo](docs/assets/images/logo.png)

## 📖 A brief history

I started working on this bot in December 2023, I added all the necessary features to make it operational 24/7, which was active until today when I decided to stop the operation and publish my work and tell the experience of what it was like to have a tibia bot farm in 2024, I had 7 chars and 3 pcs, each char farmed an average of 10-11kk a day resulting in an average turnover of 30kk a day, on servers I played I dominated the minocults spot, placing bots on all floors, players gave up farming and dominant guilds didn't care. I hope you make the most of this bot, it's still 100% functional until the day I publish this source.

Below I'll leave some images and videos of how it worked, prints of the bot's UI, and how to install and run it.

## 📷 Gallery

![UI](docs/assets/images/ui.png)

### [You can see videos of it working on my Youtube channel](https://www.youtube.com/channel/UC4uyI035S2h0z862wpYVqXA)

## 📝 CAVEBOT SCRIPTS (SEE SCRIPTS FOLDER)

- DRAKEN WALLS NORTH ✔️
- MINOTAUR CULT -1 AND -2 ✔️

## 🟢 Features

- WORKS ON TIBIA GLOBAL ✔️
- 100% FULL AUTO ✔️
- CAVEBOT WITH WAYPOINTS (COORDINATES NOT CLICKMAP) ✔️
- SAVE AND SHARE CAVEBOT SCRIPTS ✔️
- CONFIGURABLE HOTKEYS ✔️
- CAITING CREATURES OVER BOXES ✔️
- OPEN DOORS, TRAVEL, CLICK ON BOATS ✔️
- IGNORE CREATURES ✔️
- DROP LOOT ON THE GROUND ✔️
- REFILER ✔️
- DEPOSITER ✔️
- WALK OVER THE FIRE ✔️
- ALERTS ✔️
- AUTO AMULET/RING ✔️
- COMBO SPELLS ✔️
- DROP FLASKS ✔️
- DEPOSIT GOLD ✔️
- DEPOSIT ITEMS ✔️
- FOOD EATER ✔️
- TARGETING ✔️
- HEALING ✔️
- QUICK LOOTING ✔️
- DEFAULT MESSAGE WHEN SEE A PLAYER ON THE SCREEN ✔️
- AUTO HUR ✔️
- AUTO CURE POISON ✔️
- FOLLOW ENEMY OR GO TO BOX TO KILL MONSTERS (DEPENDS THE CHAR LEVEL) ✔️

## 🔴 HARDWARE REQUIREMENTS

This bot needs good processing power to work properly (fast) i tested it with weak machines and didn't succeed, of the 3 machines i had running bots they all had a ryzen 5 5600 (6 core/12 threads +- 3.5ghz), use an equal or superior processor (or you can also use a worse one but overclock it), in addition to less input detection I chose to use a leonardo arduino to simulate mouse and keyboard inputs, you need a leonardo arduino to use this bot, if you don't have one you can change the source manually to use pyautogui or derivatives, or use a driver, but note that this may result in easier detection, inside the source I will leave a . ino file with the arduino code, just send it to your arduino leonardo and it will work (remember to leave the arduino as the standard COM33 port, otherwise the bot will not work), I also recommend spoofing the arduino (it's not necessary to run the project) so that it doesn't have the id of the arduino board but that of some input device (mouse/keyboard), thus making detection more difficult.

![Arduino](docs/assets/images/arduino.png)

## 🔴 SOFTWARE REQUIREMENTS

THE BOT ONLY WORKS IN 1920X1080 RESOLUTION

### Windows

- [PYTHON 3.11.x](https://www.python.org/downloads/release/python-3117/)
- [POETRY](https://python-poetry.org/)
- [TESSERACT-WINDOWS](https://github.com/UB-Mannheim/tesseract/wiki)
- [VIRTUAL DISPLAY](https://www.amyuni.com/downloads/usbmmidd_v2.zip&v=ybHKFZjSkVY)
- [OBS](https://obsproject.com/pt-br/download)
- Arduino Leonardo (para simular inputs HID)

### 🐧 Linux (Linux Lite / Ubuntu-based)

> ✅ No Linux **não é necessário** OBS, Virtual Display nem Arduino.
> O bot captura a tela diretamente via `mss` (X11) e simula inputs via `pynput`.

**Dependências do sistema:**

```bash
# Python 3.11
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-dev python3.11-tk

# Dependências X11 para pynput e mss
sudo apt install -y python3-xlib xdotool libxtst6

# Tesseract OCR
sudo apt install -y tesseract-ocr

# Poetry
curl -sSL https://install.python-poetry.org | python3 -
```

**Tibia (cliente nativo Linux):**

```bash
# Baixe o AppImage no site oficial: https://www.tibia.com/news/?subtopic=newsarchive
chmod +x Tibia.AppImage
./Tibia.AppImage
```

> ⚠️ Configure o Tibia em resolução **1920x1080** conforme as imagens na seção de configuração abaixo.

## 🔴 TIBIA CONFIG REQUIREMENTS

YOU NEED TO USE THIS CONFIGS IN YOUR CLIENT, OTHERWISE WILL NOT WORK

![Controls](docs/assets/images/controls.png)
![General Hotkeys](docs/assets/images/generalHotkeys.png)
![Action Bar Hotkeys](docs/assets/images/actionBarHotkeys.png)
![Custom hotkeys](docs/assets/images/customHotkeys.png)
![Interface](docs/assets/images/interface.png)
![HUD](docs/assets/images/hud.png)
![Console](docs/assets/images/console.png)
![Game Window](docs/assets/images/gameWindow.png)
![Action Bars](docs/assets/images/actionBars.png)
![Graphics](docs/assets/images/graphics.png)
![Effects](docs/assets/images/effects.png)
![Misc](docs/assets/images/misc.png)
![Gameplay](docs/assets/images/gameplay.png)

## ⚙️ HOW TO SETUP

🔴 USE AT YOUR OWN RISK

### Windows

- Instale as dependências de software listadas acima
- Conecte o Arduino Leonardo (COM33)
- Clone/baixe o projeto
- Instale as dependências Python:

```bash
poetry install
```

- Execute o projeto:

```bash
poetry run python main.py
```

### 🐧 Linux (Linux Lite)

- Instale as dependências do sistema (veja seção acima)
- Clone/baixe o projeto
- Instale as dependências Python:

```bash
poetry install
```

- Execute o projeto:

```bash
poetry run python main.py
```

> 💡 O bot detecta automaticamente o SO e usa `mss` + `pynput` no Linux.
> Não é necessário nenhum hardware adicional.

## 🤝 Contributing

Contributions are always welcome! Create a pull request xD

## 💬 Lets talk

if you want to talk to me, add me on [**Linkedin**](https://br.linkedin.com/in/paulordyl) or [**Discord**](https://discord.gg/YzVhxzy4W6)

<a href="https://www.buymeacoffee.com/paulordyl" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


# ❤️ Acknowledgements

I started this project on the basis of the [**PyTibia**](https://github.com/lucasmonstrox/PyTibia) developed by [**lucasmonstrox**](https://github.com/lucasmonstrox), he did a great job, I was able to learn a lot from his project and the techniques he used, take a look at his project, he keeps updating it to this day.
