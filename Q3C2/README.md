# Q3 - Challenge 2: Local Web Application Monitoring

Add text here!
 
## Instructions

* Create a virtual environment:
```console
python3 -m venv venv
source venv/bin/activate
pip3 install requests
```

* Build and start db and web containers, expose port 5000 in web container:
```console
docker-compose up --build
```

* Run monitoring script:
```console
python monitor.py
```

* Tail log file, then stop/start the db and web containers and check the live logs outputs:
```console
tail -f alert.txt
```


* Cleanup:
```console
docker-compose down
```