# scream.py
A simple tool for creating a five second `.wav` file for sampling. This script is used during [Messica Arson](https://messicaarson.bandcamp.com) performances for recording screams.

## Prerequisites
To use this tool, you'll need:

- A microphone.
- A method to connect your microphone to your computer.

My current setup includes:
- [Motu M4](https://motu.com/en-us/products/m-series/m4/)
- [Shure SM-58](https://www.shure.com/en-US/products/microphones/sm58?variant=SM58S)

## Usage
1. Install the required packages:
```bash
pip install numpy scipy sounddevice
```

2. You will need to update the path on line 20 as well.
```python
wav.write('/path/to/your/scream.wav', fs, myrecording)
```

3. Ensure that your computer's sound output is configured to use your audio interface or the method through which your microphone is connected to your computer.

4. Run the file:
```
python scream.py
```

5. Scream! 

## Contributions
Contributions to improve this tool are welcome! If you have any suggestions, feature requests, or find any issues, please feel free to open an issue or submit a pull request.
