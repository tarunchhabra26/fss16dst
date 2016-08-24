### [Coding assignment for hw1] (https://github.com/txt/ase16/blob/master/doc/hw1.md)
1. Watch the great [Kent Beck video on how to write a test engine in just a few lines of code](https://www.youtube.com/watch?v=nIonZ6-4nuU). Note
that that example is in CoffeeScript. For the equivalent Python code, see
[utest.py](../src/utest.py).
2. Get the Python equivalent of the watch command used by Beck. Specifically, run the command
   `sudo pip install rerun`
3. Download the `utest.py`
4. Write a python file `main.py` that imports `utest.py` and code from `who1.py who2.py who3.py`;
   i.e. one file per member of your team.
4. Get two windows open:
	 + One editing main.py
	 + One in a shell
5. In the shell, type `rerun "python -B main.py"`
6. Add one more unittest to `main.py`.
     + Important... leave behind at least one failing test.
     + Save the file. Watch the code run.
### [Final Output]
1. Created `fib.py` which compute's nth fibonacci number.
2. Wrote `who1.py`, `who2.py` and `who3.py` which simply have names of team members.
3. Imported `utest.py`,`fib.py`,`who1.py`, `who2.py` and `who3.py` into main.py. Wrote some test cases on `fib.py`
4. `rerun "python -B main.py"` leads to following output :
![Output](https://s3-us-west-2.amazonaws.com/ase.assignments/Screen+Shot+2016-08-23+at+8.47.01+PM.png?X-Amz-Date=20160824T005024Z&X-Amz-Expires=300&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Signature=1828dd7913b43e5fe65af61ebe70965999ded0cca1e547b626b749cdf9dadbda&X-Amz-Credential=ASIAJ2Y2FXLNBHRY5AXQ/20160824/us-west-2/s3/aws4_request&X-Amz-SignedHeaders=Host&x-amz-security-token=FQoDYXdzEIL//////////wEaDEpIpedKYxMwGEQANSLHAacgepTFCr7zrGH8muWuZCAHnn9dSqorSUJDMY9BrUZxhmNQrOIEY4tx0QSfKbs3p81XeDSWTFUxg1EnBrj9Vgue8ntiy5wsVYj85libZf/vKDpZLcaKRjsoo9Mv8jLWs9BjkQxK141lrk8LGgL19CGLArFix5HC/7CxYby9aUNLsMysbYWHAuE%2BBQ2GKsdR8N6CXNCZSjvLECyh7TF4s8IzSPl5x/B4Q0heNXThi/ilwKsGY0M%2BPV3xjetATDL7YuG1md%2BFXhso0djzvQU%3D)
