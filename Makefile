help:
	@echo "Makefile commands"
	@echo " install - Установка зависимостей"
	@echo " test - Запуск всех тестов"

install:
	pip install -r requirements.txt

run_test:
	python3 -m pytest