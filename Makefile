.PHONY: image python_image
image:
	docker build -t udplugin_shell .
python_image:
	docker build -t python3_udplugin Python/
