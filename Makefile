.PHONY: image python_image
image:
	docker build -t udplugin_shell .
test: image
	docker run udplugin_shell python3 setup.py pytest
python_image:
	docker build -t python3_udplugin Python/
