#Intro To Raspberry Pi: DIY Home Security System
This repository demonstrates how to stream live video to Youtube from a Raspberry Pi.

#Installation

**SSH Into Pi**
<pre>
ssh -X pi@192.168.1.yourIP
</pre>

**Enable Camera And Expand Filesystem**
<pre>
sudo raspi-config
</pre>

**Get git**
<pre>
sudo apt-get update
sudo apt-get install git
</pre>

**Clone git Repo**
<pre>
cd ~/
git clone https://github.com/devonmurphy/PIHomeSecurity
cd PIHomeSecurity/
</pre>

**Uncompress ffmpeg**
<pre>
tar -xvf arm.tar.gz
</pre>

**Add A Stream Key To "start-stream"**
Change the "YourStreamKeyHere" to the steam key provided to you on https://www.youtube.com/live_dashboard
<pre>
nano start-stream
</pre>

**Start A Stream**
<pre>
./start-stream
</pre>
