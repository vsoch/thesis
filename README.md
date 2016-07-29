Thesis HTML Generator
====================

This simple Dockerfile will take an Overleaf extracted thesis (a zip file with some main.tex file, images, etc.) and use [hdlatex](http://tug.org/tex4ht/) (and [docs](https://github.com/vsoch/thesis/raw/master/img/gurari.pdf)) to render a simple HTML view for reading the thesis. The installation of latex, etc. and the generation of the static files is done via Docker so the user does not need to worry about installing dependencies. The idea is that if you fork the repo, you can then push the files to your gh-pages branch and **wha-la** you have your thesis as a simple website for sharing!

### Instructions

First, fork the repo to your Github by clicking on the fork button. Then clone the repo.

      git clone https://www.github.com/{{username}}/thesis
      cd thesis
      
Next, you need to download your thesis in zip format from Overleaf. They have a nice button to do this:

![overleaf](https://github.com/vsoch/thesis/raw/master/img/overleaf.png)

You should plop it in this folder, making sure to delete mine (if I've included it in the repo, I maybe haven't until I properly submit it!). The script will find your thesis based on it having the `.zip` extension. If you don't have a zip file, it's going to get angry at you.

Then, you need to run the Docker image. You can either build it locally, or run the version from Dockerhub. I would suggest building locally, but it's up to you. Here is how to build it if needed:

      docker build -t vanessa/thesis .

Now we are going to run the docker image, and map the local folder to it so that the generated files pop up in our present working directory. You can just run the script [generate.sh](generate.sh) to start the container, map the the present working directory, generate the site, and stop the container. To make life easier, if you plan to put the thesis on the gh-pages associated with the repo, I'd check out that branch first:

      git checkout -b gh-pages
      chmod u+x generate.sh
      bash generate.sh

You will see the following:


      LOTS OF LATEX OUTPUT...

      ...

      ...

      ight -x 1400 -D 72 -bg Transparent -pp 41:41 main.idv -o main36x.png
      System return: 0
      Entering main.css
      Entering main.tmp
      @@@@@@@@@@@@@@@@@@@*#?.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@,::,,::***:,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@::::*********?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@.:::***********%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@.:::************@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@*:::************..?@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@*.::**********...*@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@*:::::::::::::**.....S@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@+*:::::::::::::***.......@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@..?.%?:*:::::*#???........@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@..*.**********?....#?.......@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@.*.S...S.....S*.........*....@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@*.#...SSSSSSSSSSSSSSSS...*....S@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@........SSSSS?.++.+.%S?....*...*@@@@@@@@@@@@@@
      @@@@@@@@@@@@@S....%*..?SS++.++...+++....?*....@@@@@@@@@@@@@@
      @@@@@@@@@++.*.....@@....+.**::::::+......*.....@@@@@@@@@@@@@
      %****............?@@@@@S.+.#::*%.......@@*.....@@@@@@@@@@@@@
      @%****...........@@@@@@@@@.......SS...@@@+.....*@@@@@@@@@@@@
      @@@***.......?@@@@@@@@@@:**...........*@@,*.....@@@@@@@@@@@@
      @@@@@..%@@@@@@@@@@@@@@@.***.............*@*......@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@:*****..............:*......@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@*******.............+?.......,.%%S@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@...*?.....+..+.%%%%.+....?@@@@@@@*.%
      @@@@@@@@@@@@@@@@@@@@@@@@@......#.......,@@S%%%%%%%%%%%...%%%

      Welcome to the Thesis Site Generator!
      Found HTLATEX at /usr/bin/htlatex

      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+,@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*@@@@@%%?.@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%?@@@#%?#@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@:??#@???+@@@@*?@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@??:??*.#?%%??#@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?#?#???#S@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@.%,,::::,::::::.%@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@::::%,::::,::::::::::::::::,.@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@S**?,::,,,::::::::::::::::::::::+*@@@@@@@@@@@@@@
      @@@@@@@@@@?***::,,,:::::::::::::::::::::::::.,?.?,+@@@@@@@@@
      @@@@@@@@.***.*@@@@@@:,,,,:::::::*?S.+%::::S#::::::S@@@@@@@@@
      @@@@@@@.****:.@@@@@@@*::::::::S@@@@@@@@@.:S::::*:*:%@@@@@@@@
      @@@@@@%.***.:::*@@@@,:::::::::.@@@@@@@@@%:*.*:::::::S:@@@@@@
      @@@@@:.****.::::::::#@:::%::::*.,@@@@@@#****.:::::::::%@@@@@
      @@@@@#......#:%@@@,@,,::::::,+.%#%:*********%:::::::::*%@@@@
      @@@@@?.......+,@@,,,,:.,:,,,,,,,,,:.********?:::::::::::.@@@
      @@@@@,*..?@@,@,@@@@,,,,,,,,,,,,,:,.*********?:::::::::::::@@
      @@@@@@.,@@,,@@@@,@,,,,,,,,,,,,,:,**********?.*::::::::::::?@
      @@@@%@@,@,,,,@@@@,,,,,,,,,,,,,,:*******+?:****:::::::::::*.@
      @@@S@,@@@@@@,@@,,,,,,,,,,,,,,,,:.**************::::::::::**@
      @@@@,,@@@@,,,,,,,,,,,,,,,,,,,,,:.**********S********:*:::*.@
      @@@@@::,,,,,,,,,,,,,,,,,,,,,,::,***********::*************S@
      @@@@@@*,:::,,,,,,,,,,,,,,,,::,#*************#************?@@
      @@@@@@@@@@*.:,::::::::::,:%::::::*************%********#@@@@
      @@@@@@@@@@@+::::::::::::::::::::::::::::*****************@@@
      @@@@@@@@@@@::::::::::::::::::::::::::::::***************.@@@
      @@@@@@@@@@+:::::::::::::::::::::::::::::::***************,@@
      @@@@@@@@@@%::::::::::::::::::::::::::::::::**************.@@
      S:::S%?.SSS::::::::::::::::::::::::::::::****************%@@
      @@........?*::::::::::::::::::::::::::::**************..**@@
      @@@%......S******::::::::::::::::::***********.,,+*?@:*:+@@@
      @@@@@.......*********************************.,:**:*****%+,@
      @@@@@@@S...*:*******************************S,:***********:@
      @@@@@@@@@:S..#*****************************?,:***********?@@
      @@@@@@@@@@@@@#*#:**************************:,***********@@@@
      @@@@@@@@@@@@@@@@@+.**********************:.:,:*******:.@@@@@
      @@@@@@@@@@@@@@@@@:+..S?.********S?+@@@@@@@@@*,****.S@@@@@@@@
      @@@@@@@@@@@@@@@#::,,,,,,::***...@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@?,,,,,,,:***%@@@@@@@@@@@@@@@@@@@@@@@@@@@

      Generating HTML, please wait!
      Site generation complete. Push to gh-pages for finished site.
      7e642e3285f7
      Thesis generation finished, look in site folder for output, and add index.html and site folder to github pages!


What is really happening? Here are the basic commands. In a nutshell, we are starting the container and directing output to `/dev/null` to keep it running, then getting the ID for it (something like `7e642e3285f7`) programatically, and then sending a command, `python /code/generate.py` directly to the container.

      CONTAINER_MD5=`docker run -v $PWD:/code -d vanessa/thesis tail -f /dev/null`
      CONTAINER_ID=`echo ${CONTAINER_MD5} | cut -c1-12`
      docker exec $CONTAINER_ID python /code/generate.py

This means that the entire generation of the site (and all the software needed to do it) is installed and run in the container, and we get to see and keep the output. Pretty neat!

### Output
You will see new files in your present working directory, namely an `index.html` that redirects to the main content of your thesis in the `site` folder. In the `site` folder is a simple version of your thesis, in html form, with all the images and links as they should be. Then you simple need to add these files to a github pages branch. If you haven't yet, checkout a new gh-pages branch

      git checkout -b gh-pages

If you're already on it, skip the above, and just add the site files to the gh-pages branch:

      git add site/
      git add index.html
      git push origin gh-pages

Then, your site should be available at `{{username}}.github.io/thesis`. 


### Debugging
You may need to connect to the container interactively if you run into some issue, and there is an easy way to do that. First, we will use some of the commands that are in [generate.sh](generate.sh) to get the container running, and get it's container ID:

      CONTAINER_MD5=`docker run -v $PWD:/code -d vanessa/thesis tail -f /dev/null`
      CONTAINER_ID=`echo ${CONTAINER_MD5} | cut -c1-12`
      
Now you can connect to it:

      docker exec -it $CONTAINER_ID bash


### Anticipated Issues
I would imagine that University / Institution templates are different. My zipped up thesis only contains a bibliography (thesis.bib), one main `.tex` file (main.tex), a folder of images (`/images`) and a style file (`suthesis-2e.sty`). Thus, my program makes a few assumptions that might need tweaking if your zip is different:

By default, the first .tex file found via `glob` is assumed to be the main thesis to render. If you have something like supplementary material or else, the fix to this would be to modify the [generate.py](generate.py) script to take the name of this file as first argument instead of finding programatically. Then you would modify the command in the [generate.sh](generate.sh) before running:

      docker exec $CONTAINER_ID python /code/generate.py mainfile.tex
 
In the same way, if you have more than one zip file in your folder, it will select the first. This could also be an argument added to the two generate scripts.

Finally, in my tests I am seeing some of the early sections get generated more than once (eg, a duplicate "Abstract" section). I haven't looked into this yet, and will in the future.

### Coming Soon
I am going to add some custom style files to give the thesis a bit of branding, and a bit of... say... style? :) Once mine is submit, I'll add it to the github pages for this repo! Until then.... 

### Help and Features

If you want me to add or change something, please don't hesitate to post on the [issues board](https://github.com/vsoch/thesis/issues).


### License
[MIT](LICENSE)
