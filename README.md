## User
To deploy this website locally use the steps below:
1. On Mac/Windows install docker desktop (pay attention to preferences/resources menu and give it as many CPUs as you can before you make your system unstable and at least 2-3 GB of RAM).  On linux install docker.
2. grab the appropriate docker image by executing `docker pull shanko07/vc-app:standalonedocker`
3. Setup a google app password for sending automated emails via the following [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
4. run the website by executing `docker run --env APP_ROOT_URL=http://localhost:5000 --env PORT=5000 --env GOOGLE_APP_PASSWORD=<your google app password> --env GOOGLE_APP_EMAIL=<your google app email> -d --rm -p 5000:5000 shanko07/vc-app:standalonedocker`
5. visit [http://localhost:5000](http://localhost:5000) in your web browser and follow instructions from there
6. grab a coffee, or do something else and wait for the email that says conversion is complete
7. open the link in the email on the same computer to download the file

To deploy for production, you must have a server and the appropriate domain name, certs, A records, firewall rules etc setup.  I typically use an nginx server to terminate the HTTPS connection and then proxy pass the requests to the docker container's address and port.

## Developer
To build the docker container and run your own version of the code, a few additional steps are necessary.
1. Clone the repo
2. Enter the root level of the app and execute `git submodule init` and `git submodule update` to pull in the submodules