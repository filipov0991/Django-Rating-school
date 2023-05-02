// Получаем кнопку по ее ID
var button = document.getElementById('signup');


var input = document.getElementById("floatingInput1");
var password = document.getElementById("floatingPassword1");

// Привязываем обработчик события клика к кнопке
button.addEventListener('click', function() {
    // Создаем новый объект XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Указываем метод и адрес запроса
    xhr.open('POST', '/users/registration/' , true);

    // Устанавливаем заголовок Content-Type для указания типа отправляемых данных
    xhr.setRequestHeader('Content-Type', 'application/json');

    // Создаем объект с данными, которые будут отправлены на сервер
    var value = input.value;
    var value_password = password.value;

    var data = {
        "email": value,
        "password": value_password
    };
    
    // Конвертируем объект данных в формат JSON
    var jsonData = JSON.stringify(data);

    // Назначаем обработчик событий для ответа от сервера
    xhr.onload = function () {
        // Обрабатываем ответ от сервера
        if (xhr.status === 200) {
            // Действия при успешной отправке запроса
            window.location.replace(window.location.protocol+'//'+window.location.host);
        } else {
            // Действия при неудачной отправке запроса
            console.log('Произошла ошибка при отправке запроса')
            console.log(xhr.response);
            console.log(jsonData)
        }
    };

    // Отправляем запрос на сервер с данными в формате JSON
    xhr.send(jsonData);
});
