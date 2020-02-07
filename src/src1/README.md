# lab 02: part 1

## Locally Installed OpenCV

If you have OpenCV installed locally on your machine, you can run Python programs directly
from the terminal, as specified in each program.


## Docker 

Once you have Docker Desktop running on your machine, you can use Docker to run given
Python programs that use OpenCV. These commands should be run from the `src` directory,
one level up from the directory containing the source code. 

### Building
First run:

`docker build -t opencv .`

### Running

To run each program in a docker container, run the following command, where `program.py` 
is the name of the program.
   
`docker run --rm -v $(pwd)/src1:/root opencv python program.py`

Or, if the program requires some image input (say, `image.png`), you can run the following command.

`docker run --rm -v $(pwd)/src1:/root opencv python program.py --image image.png`

### Output

The output of each program is stored in the directory corresponding to the program name. See the source
code for more information.