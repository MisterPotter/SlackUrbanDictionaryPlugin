.PHONY: shell
shell:
	docker build -t udplugin_shell .
python:
	docker build -t python3_udplugin Python/
