# SKI challenge
Repo that have the solution for ski challenge

## Steps to run:
* clone the repository

    ```
    git clone https://github.com/santiagomd11/ski.git
    ```
* open the folder in which the repository was cloned
    ```
    cd ski
    ```
* And finally placed on ski folder in order to run the the program on the 4x4 map and the 1000x1000 map, simply run on command line:

    ```
    python3 -m unittest discover -s tests -p "test*"
    ```

    or 

    ```
    python -m unittest discover -s tests -p "test*"
    ```

    This could take a bit (∼20 seconds on 12 GB RAM computer).  At the end of the execution you will get a result like this on the console:

    ![results](/images/TestResults.png)
