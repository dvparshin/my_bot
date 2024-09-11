# Телеграм бот
В письме предлагают использовать библиотеку python-telegram-bot версии `13.15`. На данный момент актуальная версия `21.5`. Переделал бота с использованием последней версии библиотеки по статье из официальной документации [Extensions Your first Bot](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot).  

## Локальный запуск
1) Скачать текущий репозиторий  
```bash
git clone git@github.com:dvparshin/my_bot.git
```
2) Перейти в каталог репозитория  
```bash
cd my_bot
```
3) Установить библиотеку python-telegram-bot  
```bash
pip install -r requirements.txt
```
4) Запустить бот  
```bash
python3 bot.py
```

## Запуск в docker  
Сборка образа телеграм бота для платформ **linux/amd64, linux/arm64/v8**  
1) Создать сборщик  
```bash
docker buildx create \
--name container-builder \
--driver docker-container \
--use --bootstrap
```

2) Запустить сборку образов  
```bash
docker buildx build --platform linux/amd64,linux/arm64/v8 .
docker buildx build --load -t telegram-bot .
```
3) Запустить docker образ, заменив токен доступа к боту `API_KEY` на необходимый  
```bash
docker run --env API_KEY="======= telegram bot token=======" telegram-bot
```