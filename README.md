sudo apt install python3-pip
sudo apt-get install python-pyaudio python3-pyaudio sox
pip3 install -r requirements.txt
<!-- sudo apt-get install espeak -->
sudo apt-get install libsox-fmt-mp3

si pb avec pyaudio -> sudo apt install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg




From source

    If you don’t already have it, install setuptools for Python 3
    Clone this repository: git clone https://github.com/desbma/GoogleSpeech
    Install Google Speech: python3 setup.py install
    Install SoX, with MP3 support. On Ubuntu and other Debian derivatives: sudo apt-get install sox libsox-fmt-mp3. Windows users can download binaries on the SoX website, once installed you also need to copy libmad DLL in the directory where you have installed SoX, and to add this directory to your PATH environment variable.

Command line usage

Run google_speech -h to get full command line reference.
Examples

    Plane stall alarm:

    google_speech -l en stall -e delay 0.5 overdrive 20 repeat 5 speed 0.9 gain -5

    Female robot voice (idea from here):

    google_speech -l en "Hello, I am a stupid robot voice" -e speed 0.9 overdrive 10 echo 0.8 0.7 6 0.7 echo 0.8 0.7 10 0.7 echo 0.8 0.7 12 0.7 echo 0.8 0.88 12 0.7 echo 0.8 0.88 30 0.7 echo 0.6 0.6 60 0.7
