if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/BalamuruganDV/LUNA-XTRA-FEATURE.git /LUNA-XTRA-FEATURE
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LUNA-XTRA-FEATURE
fi
cd /LUNA-XTRA-FEATURE
pip3 install -U -r requirements.txt
echo "𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 ᎡᏴ[𝙻𝚄𝙽𝙰]..."
python3 bot.py
