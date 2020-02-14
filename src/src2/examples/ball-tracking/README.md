# Ball Tracking Example take from from https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

## Locally Installed OpenCV

Right now, this program runs with the local installation of OpenCV. You can run Python programs directly
from the terminal, as specified in each  program. You must be inside the `src` directory.


## Docker 

If you would like to run this program from Docker, you must have `imutils` package installed
directly in the `src` directory. Then, once you have Docker Desktop running on your machine, 
you can use Docker to run given
Python programs that use OpenCV.  You must be inside `ball-tracking` directory.


### Building
First run:

`docker build -t opencv .`


### Running

To run the *ball tracking* program in a docker container, you must first download `imutils` package, then you can run the following command, where `video.mp4` 
is the video used for tracking.
   
`docker run --rm -v $(pwd)/src:/root opencv python ball_tracking.py --video video.mp4`


