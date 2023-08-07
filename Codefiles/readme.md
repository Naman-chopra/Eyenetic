## Let's get the pre-requisites sorted
1. So the first step would be to clone the directory using 
```code
git clone https://github.com/Naman-chopra/Eyenetic.git
```
2. After cloning the repository, cd into the `Codefiles` folder by using 
```code
cd Eyenetic/Codefiles/
```
3. Now to get the prerequisite packages installed, run `pip install -r requirements.txt` and *Voila!!* requirements are installed.

## Running the program
It's very Easy. Just launch the terminal in the `Codefiles` directory, run
```code
python mouse_movement.py
```
and stare at the point of the screen you want your mouse to point to. `Make sure that your eyes are clearly visible in the videocapture device.` The program by default runs for **30 seconds**, which can be adjusted by modifying the `'t'` variable in [mouse_movement.py](mouse_movement.py)
### Optional files to play with
If you're not satisfied with the dataset and want to collect your own dataset for your device, go ahead and use [dataset_collection.py](dataset_collection.py)  
It will help you create your own dataset for your device which will in turn increase the model's accuracy.  
Here are the steps to collect the dataset:  
`Make sure your eyes are clearly visible in the videocapture device before running the code.`
1. Run [dataset_collection.py](dataset_collection.py) with your video capture device turned on.
2. Stare on your screen normally where the mouse pointer is and click any button of the mouse.
3. Change the location of the pointer, stare at it again and click any one of the buttons.
3. Keep doing this until your heart's desire.

### `NOTE: The performance of the program on your device will highly depend on it's resolution. The original model was trained on a 2560x1440 screen`