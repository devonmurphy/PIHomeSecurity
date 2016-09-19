#Intro To Raspberry Pi: DIY Home Security System


#Installation

**Get git**
<pre>
sudo apt-get update
sudo apt-get install git
</pre>

**Clone Repo**
<pre>
git clone https://github.com/devonmurphy/PIHomeSecurity
</pre>

**Enable Camera and Expand Filesystem**
<pre>
sudo raspi-config
</pre>

**Uncompress ffmpeg**
<pre>
tar -xvf arm.tar.gz
</pre>

**Add A Stream Key to "start-stream"**


Change the "YourStreamKeyHere" to the steam key provided to you on https://www.youtube.com/live_dashboard
<pre>
nano start-stream
</pre>

**Start A Stream**
<pre>
./start-stream
</pre>
