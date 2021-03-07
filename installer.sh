if [ -d /venv/ ];
then
echo "venv folder exists"
else
python3 -m venv venv
fi
source venv/bin/activate;
pip install Flask
