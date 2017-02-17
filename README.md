# KS_LI-for-Raspberry-Pi

## Устанока пакетов (из  [статьи](http://raspberrypi.ru/blog/readblog/578.html))

1. Скачиваем исходники библиотеки из репозитория `git clone git://git.drogon.net/wiringPi`

2. Заходим в дирректорию 'cd wiringPi' м выполняем './build'.

## Компиляция и запуск

1. Для компиляции скрипта выполняем 'gcc -Wall -o KsLiRunner KsLiRunner.c -lwiringPi'

2. И запускаем командой `sudo ./example`
