// Получаем кнопку по ее ID
var button1 = document.getElementById('login');

var csrf = document.getElementsByTagName('csrfmiddlewaretoken');
var input1 = document.getElementById("floatingInput");
var password1 = document.getElementById("floatingPassword");

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

function encodeFormData(data) {
    var encodedString = '';
    for (var key in data) {
        if (encodedString.length > 0) {
            encodedString += '&';
        }
        encodedString += encodeURIComponent(key) + '=' + encodeURIComponent(data[key]);
    }
    return encodedString;
}

// Привязываем обработчик события клика к кнопке
button1.addEventListener('click', function() {
    // Создаем новый объект XMLHttpRequest
    var xhr = new XMLHttpRequest();

    // Указываем метод и адрес запроса
    xhr.open('POST', '/users/login2/' , true);

    // Устанавливаем заголовок Content-Type для указания типа отправляемых данных
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded;charset=UTF-8");
    // Создаем объект с данными, которые будут отправлены на сервер
    var value1 = input1.value;
    var value_password1 = password1.value;
    const csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader('X-CSRFToken', csrftoken);
    var data = {
        "username": value1,
        "password": value_password1
    };
    
    // Конвертируем объект данных в формат JSON
    var jsonData = JSON.stringify(data);

    // Назначаем обработчик событий для ответа от сервера
    xhr.onload = function () {
        // Обрабатываем ответ от сервера
        if (xhr.status === 200) {
            // Действия при успешной отправке запроса
            console.log(xhr.response);
            window.location.replace(window.location.protocol+'//'+window.location.host);
        } else {
            // Действия при неудачной отправке запроса
            console.log('Произошла ошибка при отправке запроса')
            console.log(xhr.response);
            console.log(jsonData)
        }
    };

    // Отправляем запрос на сервер с данными в формате JSON
    xhr.send(encodeFormData(data));
});
