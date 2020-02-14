# Pitch Tracking Example
# Completed as a part of a senior thesis by Dan Bonnet

## Locally Installed OpenCV

Right now, this program runs with the local installation of OpenCV. You can run Python programs directly
from the terminal, as specified in a  program. You must be inside the `src` directory.


## Docker 

If you would like to run this program from Docker, you must have `imutils` package installed
directly in the `src` directory. Then, once you have Docker Desktop running on your machine, 
you can use Docker to run given
Python programs that use OpenCV.  You must be inside `pitch-tracking` directory.


### Building
First run:

`docker build -t opencv .`


### Running

To run the *ball tracking* program in a docker container, you must first download `imutils` package, then you can run the following command.
   
`docker run --rm -v $(pwd)/src:/root opencv python pitch_tracking.py

