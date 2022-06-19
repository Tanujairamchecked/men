if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BalamuruganDV/Luna-Filter.git /Luna-Filter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Luna-Filter
fi
cd /Luna-Filter
pip3 install -U -r requirements.txt
echo "𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 ᎡᏴ[𝙻𝚄𝙽𝙰]..."
python3 bot.py
