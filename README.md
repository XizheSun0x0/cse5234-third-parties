# cse5234-third-parties
BOF is payment microsevice and 5PS is shipment microservice
# package requirements
make sure that fastapi is in 0.99.1 version
# upload to aws
in any root dir of any microservice run:
```bash
pip3 install -t denpendencies -r requirments.txt
(cd dependencies; zip ../aws_lambda.zip -r .)
zip aws_lambda.zip -u *.py
```