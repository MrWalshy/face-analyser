# Notes
- Local conda env face-detection holds scikit files and opencv + dependencies
- Should take any picture of a face/s
- Makes use of the Viola-Jones Object Detection algorithm, this essentially makes passes over sub-images of an image deciding if they are a face or not(can also be used with other features).The description of the face is held in an xml file, the style is also known as a cascade(think cascade of information).

# How to run?
- Use venv or conda for the virtual environment
- Ensure scikit-learn and scikit-image are installed in a virtual environment
- Set up correct face-detection env, fullfill dependencies for opencv
- Run the following in the terminal:

        conda activate face-detection
        python main.py <image_path.format>
        
# How to deactivate a conda environment

        conda deactivate

# Resources
- https://pypi.org/project/opencv-python/#description
- https://realpython.com/traditional-face-detection-python/
- https://github.com/opencv/opencv/tree/master/data/haarcascades

# Possible Future
- The ability to detect faces in images is powerful. So much so that I would like to incorporate the following features of computer vision technology:
    - Face detection is a computer vision tech. that can identify faces within digital images.
    - Facial recognition is used for biometric purposes, i.e. identification
    - Facial analysis trys determining properties describing a face, such as age, gender, emotion...
    - Facial tracking is used in video anaylsis, tracking the face + features(eyes, nose, lips) across the screen.
- A project involving my R-Pi could be good for learning here, I would need a camera module for an R-Pi facial-recognition security cam project.
