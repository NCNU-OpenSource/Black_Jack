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

Due to raspberry pi doesn't support the version of TensorFlow we use, we need to install docker first.

### Install Docker

Unfortunately for Raspbian, installing using the repository is not yet supported. We must instead use the ***convenience script***.

```=
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sudo sh get-docker.sh

<output truncated>
```

If you want to manage docker as a non-root user, see [here](https://docs.docker.com/engine/install/linux-postinstall/).

<!-- After installation, here are some steps we need to walk through:

1. Create the `docker` group

    ```=
        sudo groupadd docker
    ```

2. Add your user to the docker group

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

Use the below command if you're using Python 3.7

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

## Knowledge from Lecture

## Installation

## Usage

## Job Assignment



## Future Outlook

1. Combine current function with communication applications, like Telegram, Messenger or Line...

2. Reduce the size of whole device, make it harder to be noticed when using our device. 

## References

- Docker's Offical docs: https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script
- Tensorflow installation: https://www.tensorflow.org/install/source_rpi?hl=zh-tw