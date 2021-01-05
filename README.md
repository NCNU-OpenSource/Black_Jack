# Black_Jack

<!-- A system to help you win the game -->

## Concept Development

Lots of people play blackjack with relatives during Chinese New Year, some even gamble much money away.  
Now, Chinese New Year is around the corner, in order to keep money in our pocket, we gonna develope a "cheat box" to help us raise the win rate.
In this "cheat box", we use camera to capture the point of cards, then through some compute, would give users some feedback.

## Implementation Resources

To implement this "cheat box", first, we need a raspberry pi and a camera, which is compatible with our pi.
We use raspberry pi 3 as our main device, as for the camera, here's the [link](https://m.momoshop.com.tw/goods.momo?i_code=5541576&cid=mobile&oid=BfM&recomd_id=rgc-f8m5_normal_1609184511_105161526).

There are two techniques in our project, one is object recognition, another is machine learning.
We use deep Q learning to compute the win rate of every possible movement, and send the recommend movement to users.

## Existing Library/Software

- Docker
- TensorFlow
- Keras

## Implementation Process

## Knowledge from Lecture

## Installation

Due to raspberry pi doesn't support the version of TensorFlow we use, we need to install docker first.

### Install h5py

```=shell
    sudo apt-get install libhdf5-dev
    sudo apt-get install libhdf5-serial-de
```

### Install pillow

```=shell
    sudo apt-get update
    sudo apt-get install libjpeg-dev -y
    sudo apt-get install zlib1g-dev -y
    sudo apt-get install libfreetype6-dev -y
    sudo apt-get install liblcms1-dev -y
    sudo apt-get install libopenjp2-7 -y
    sudo apt-get install libtiff5 -y
```

### Install pyttsx3 (Python Text to Speech)

```=shell
    pip3 install pyttsx3
```

### Install Docker

Unfortunately for Raspbian, installing using the repository is not yet supported. We must instead use the ***convenience script***.

```=
    $ curl -fsSL https://get.docker.com -o get-docker.sh
    $ sudo sh get-docker.sh

    <output truncated>
```

If you want to manage docker as a non-root user, see [here](https://docs.docker.com/engine/install/linux-postinstall/).

<!-- After installation, here are some steps we need to walk through:

0. Create the `docker` group

    ```=
        sudo groupadd docker
    ```

1. Add your user to the docker group

    ```=
        sudo usermod -aG docker $USER
    ``` -->

### Install TensorFlow

#### Download source code of TensorFlow

Download the source code of Tensorflow by using `git`:

```=
    $ git clone https://github.com/tensorflow/tensorflow.git
    $ cd tensorflow
```

The default storage is in the `master` branch

```=
    $ git checkout master
```

#### Start construct from the source code

Use the below command if you're using Python 2.7

```=
    $ tensorflow/tools/ci_build/ci_build.sh PI-PYTHON37 \
        tensorflow/tools/ci_build/pi/build_raspberry_pi.sh
```

Command of other Python version could be found in this [page](https://www.tensorflow.org/install/source_rpi?hl=zh-tw#python-3.7).

After the construction is finished, system will create a `.whl` package file in the output directory of the host source tree structure. Please copy the wheel file to Raspberry pi, and use `pip` to install:

```=
    $ pip install tensorflow-version-cp35-none-linux_armv7l.whl
```

Then the TensorFlow has been installed successfully.

<!-- ### 即時影像辨識 -->

### Install Camera of Raspberry pi 安裝樹莓派相機

<!-- :::success -->

- [Poker TensorFlow Object Detection API](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)
- [即時影像辨識環境建置](https://xianghu.pixnet.net/blog/post/155977403-raspberrypi%26webcamera)
- [影像辨識教學](https://www.youtube.com/watch?v=npZ-8Nj1YwY&ab_channel=EdjeElectronics)
<!-- ::: -->

#### 環境建置

- update apt
- 更新安裝軟體

```shell=
    sudo apt-get update
    sudo apt-get upgrade
```

- install relative package
- 安裝依賴包

```shell=
    sudo apt-get install subversion libjpeg62-turbo-dev imagemagick
```

- download source code
- 下載原始碼

```shell=
    svn co https://svn.code.sf.net/p/mjpg-streamer/code/
```

- switch to the path of makefile
- 切換到有 makefile 的路徑下

```shell=
    cd code/mjpg-streamer
```

- execute makefile
- 執行 makefile

```shell=
    make
```

#### 這邊會報錯

![這邊會報錯](https://i.imgur.com/PdrA7kf.png)

#### 解決方案

- edit `util.c` which is in the same directory as makefile
- 編輯和 makefile 同個資料夾中的 `utils.c`

```shell=
    sudo vim utils.c
```

- commit this two line
- 註解掉以下兩行

```shell=
    #include <linux/stat.h>
    #include <sys/stat.h>
```

#### Make

- make install

```shell=
    sudo make install
```

- drive mjpeg-streamer
- 驅動 mjpg-streamer

```shell=
    ./mjpg_streamer -i "./input_uvc.so -y" -o "./output_http.so -w ./www" 
```

- wait a minute, if the below image is seen, which means works successfully
- 這邊要等他跑一下，看到以下畫面代表成功

![](https://i.imgur.com/EidXj7j.png)

- Go to this link to see the instant image (Insert the ip of pi)
- 輸入以下網址來看到即時影像(IP填樹莓派的)

```shell=
    http://YourIP:8080/?action=stream
```

#### 影像辨識

- update pi
- 更新 pi

```shell=
    sudo apt-get update
    sudo apt-get dist-upgrade
```

- install TensorFlow
- 安裝 TensorFlow

```shell=
    mkdir tf
    cd tf
    wget ...
    sudo pip3 install tensorflow-1.8.0-cp35-none-linux_armv71.whl
    sudo apt-get install libatlas-base-dev
    sudo pip3 install pillow lxml jupyter matplotlib cython
```

![](https://i.imgur.com/6XswhLw.png)

![](https://i.imgur.com/SaWmP0L.png)

![](https://i.imgur.com/NuXdUEL.png)

```shell=
    sudo apt-get install python3-tk
```

![](https://i.imgur.com/i13v7QC.png)

- install OpenCV
- 安裝 OpenCV

```shell=
    # sudo apt-get install libjpeg-dev libjasper-dev libpng12-dev
    # sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    # sudo apt-get install libxvidcore-dev libx264-dev
    # sudo apt-get install qt4-dev-tools
    pip3 install opencv-python
```

- Compile and install Protobuf
- 編譯並安裝 Protobuf

```shell=
    sudo apt-get install autoconf automake libtool curl 
    wget https://github.com/protocolbuffers/protobuf/releases/download/v3.14.0/protobuf-all-3.14.0.tar.gz
    tar -zxvf protobuf-all-3.14.0.tar.gz
    cd protobuf-3.14.0
    ./configure
    make
    make check
    sudo make install

    cd python
    export LD_LIBRARY_PATH=../src/.libs

    python3 setup.py build --cpp_implementation
    python3 setup.py test --cpp_implementation
    sudo python3 setup.py install --cpp_implementation
    export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp
    export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION=3
    sudo ldconfig
    protoc
    sudo reboot now
```

- Setup TensorFlow Directory structure 
- 設定 TensorFlow 目錄結構

```shell=
    mkdir tensorflow1
    cd tensorflow1
    git clone --recurse-submodules https://github.com/tensorflow/models.git
```

```shell=
    sudo nano ~/.bashrc
    export PYTHONPATH=$PYTHONPATH:/home/pi/tensorflow1/models/research:/home/pi/tensorflow1/models/research/slim
```

- echo after close terminal
- 關掉終端機後，echo

```shell=
    echo $PYTHONPATH
```

```=shell
    cd tensorflow1/models/research/object_detection
    
    wget http://download.tensorflow.org/models/object_detection/ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
    tar -xzvf ssdlite_mobilenet_v2_coco_2018_05_09.tar.gz
```

```shell=
    cd tensorflow1/models/research
    protoc object_detection/protos/*.proto --python_out=.
```

```shell=
    cd tensorflow1/models/research/object_detection/
```

```shell=
    wget https://raw.githubusercontent.com/EdjeElectronics/TensorFlow-Object-Detection-on-the-Raspberry-Pi/master/Object_detection_picamera.py
```

```shell=
    python3 Object_detection_picamera.py
```

```shell=
    wget https://www.dropbox.com/s/27avwicywbq68tx/card_model.zip
```

```shell=
    unzip card_model.zip
```

```shell=
    mv card_labelmap.pbtxt data
```

```shell=
    sudo idle3 Object_detection_picamera.py

    MODEL_NAME = 'card_model'
    PATH_TOLABELS = os.path.join(CWD_PATH, 'data', 'card_labelmap.pbtxt')
    NUM_CLASSES = 13
```

```shell=
    python3 Object_detection_picamera.py
```

<！-- ## Usage -->

## Trouble Shooting

### Unexpected recovery

#### Situation

When reboot the pi, many package would be deleted, and data in directories be deleted unexpected, seemed to be recovered to older versions as before.

#### When

When a blue window jump out unexpectedly, with "Pending kernel update"

#### Why

It seems that packages ends with `dev` would need to change some settings of kernel, so the efforts would be deleted.
After searching lots of articles, the broken of SD card is the main problem.

#### Solution

Install all these kind of packages at the same time at first, maybe this works, we hope.

## Job Assignment

- Object Recognition: 陳靖、林詩涵
- Text to Voice: 李盛廉
- Model training: 謝博丞
- Compile Data, Docs: 林宥均
- Slides: Everyone

## Future Outlook

1. Combine current function with communication applications, like Telegram, Messenger or Line...

2. Reduce the size of whole device, make it harder to be noticed when using our device.

## References

- Docker Official docs: https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script
- TensorFlow installation: https://www.tensorflow.org/install/source_rpi?hl=zh-tw
- TensorFlow & Keras environments: https://docs.floydhub.com/guides/environments/
- pyttsx3 on pypi: https://pypi.org/project/pyttsx3/
