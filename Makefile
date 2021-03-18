
run: 
	export FLASK_APP=src/api.py
	python -m flask run --host=0.0.0.0 --port=5000
	

scp :
	scp -r ./  root@test:/home/works/zhouyi/guangdongzaixian