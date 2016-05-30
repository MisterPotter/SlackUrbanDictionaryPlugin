.PHONY: image python_image
image:
	docker build -t udplugin_shell .
server: image
	docker run -d -p 127.0.0.1:5127:5127 udplugin_shell
test: image
	docker run udplugin_shell python3 setup.py pytest
python_image:
	docker build -t python3_udplugin Python/
