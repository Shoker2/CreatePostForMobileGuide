# CreatePostForMobileGuide

Данная прога нужна, чтобы легко добавлять посты для приложения "MobileGuide" https://github.com/Shoker2/MobileGuide/

Но тут есть один ньюанс. Эта прога с помощью request отправляет json файл с нужными данными на сервер с php.

Там просто нужно декодировать json. Вот так я это делаю у себя:

$postData = file_get_contents('php://input');

$Post = json_decode($postData, true);

И дальше просто получаю данные:

$city = $Post['City'];
