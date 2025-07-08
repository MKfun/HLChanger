# HLChanger
## Создавался для возможности одним скриптом менять вид халф лайф.

# Установка
## Клонируйте репозиторий и создайте виртуальное окружение
```
вы чё долбаёбы? Сами не додумаетесь?
```
## Установите зависимости
```
pip install -r requirements.txt
```
## Скрипт готов к работе!

# Примеры
## Заменить skybox на нужное вам изображение
```
python main.py ~/Downloads/torvalds.png --skybox all
```
![замена skybox](https://files.catbox.moe/4kz2kw.jpg)

### all значит все skybox`ы. Если хотите по одному - вместо all указывайте название без расширения и пути, типа "neb1bk"

## Заменить фон меню на нужное вам изображение
```
python main.py ~/Downloads/torvalds.png --background y
```
![замена фона](https://files.catbox.moe/1qq5tc.jpg)

## Заметьте, что некоторые аргументы можно комбинировать, например
```
python main.py ~/Downloads/torvalds.png --skybox all --background y
```

## Если вам хочется сделать аддон для игры (например чтоб скидывать его друзьям), укажите --addon y
```
python main.py ~/Downloads/torvalds.png --skybox all --background y --addon y
```
### Все файлы будут записаны в valve_addon а не valve

## Также если вы по какой-то причине хотите изменить директорию вывода, можете указать --output (работает только при указании --addon)
```
python main.py ~/Downloads/torvalds.png --skybox all --background y --addon y --output addon
```

## Также есть не показанные тут аргументы, они меняют файлы игры но в самой игре эффект почему-то не наблюдается. Если кто-то знает решение или нашел баг / всё подобное - пишите @botaner_1987 (telegram)
