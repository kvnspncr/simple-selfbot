#script for setting up the bot
#temporary fix for this issue on github 
#https://github.com/dolfies/discord.py-self/issues/597
#that above is the lib issue this is fixing you can check it out by yourself
echo "IMPORTANT!"
echo "If you have the original discord library uninstall it"
python3 -m pip install -U discord.py-self
current=$(pwd)
mv $current/utils.py ~/.local/lib/python3.11/site-packages/discord/ #this is moving the fixed utils.py to fix the temp broken package
echo "All done!"
