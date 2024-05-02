# Многостраничный сайт в рамках Мегахакатона по лендингам для ГБУ «Доринвест»
![not images!!!](static/images/icons/dorinvest_logo.ico)
## Техническое задание
<details>
<summary>

### Описание
</summary>

***Необходимо создать веб-страницу для размещения анонса выставки-пристройства животных из приютов.
Шаблон планируется использовать для анонса каждой выставки, проводимой ГБУ «Доринвест».
На базе шаблона для каждой выставки будет создаваться отдельная страница в доменной зоне dorinvest.ru (например vistavka.dorinvest.ru).***
</details>

<details>
<summary>

### Требования
</summary>

***Шаблон должен иметь административную панель, где работники ГРУ «Доринвест» смогут самостоятельно редактировать весь контент, 
который будет на веб-странице.***

***Дизайнер веб-страницы должны быть в стиле официального сайта ГБУ «Доринвест» https://dorinvest.ru.***
На веб-страницу должны быть размещены:
+ ***Логотип ГБУ «Доринвест»;***
+ ***Баннер в виде картинки или слайдера;***
+ ***Название выставки;***
+ ***Сетка из фотографий животных с кратким описанием, 
которые будут участвовать в выставке (с разбивкой по категориям: кошки, собаки);***
+ ***Сетка фотографий — подборка с прошлых выставок;***
+ ***Информация о дате и месте проведения выставки;***
+ ***Логотипы партнеров выставки;***
+ ***Дополнительный блок, который отображается только после проведения выставки, где будет размещена информация
по итогам выставки и галерея фотографий с мероприятия;***
+ ***Ссылка на соц. сети ГБУ «Доринвест»;***
+ ***Контакты администраторов сайта с формой обратной связи.***
</details>

<details>
<summary>

### Целевая аудитория

</summary>

___
***ЦА, которую бренд хочет привлечь***

*Люди, которые хотят завести домашнее животное, но не знает о том, что можно забрать животное из приюта.*
___
***Текущая ЦА бренда***

*Люди, которые думают о том, чтобы забрать животное из приюта, волонтеры, люди занимающиеся благотворительностью.*

</details>

___
<details>
<summary>

## Команда «Крёстный кОтец»
</summary>

№ | ФИО                           | Должность                    | Никнейм в телеграмме | Ссылка на проекты                 |
--|-------------------------------|------------------------------|----------------------|-----------------------------------
1 | Зайцев Антон Александрович    | Тимлид и Backend разработчик | @BlackMarvel         | https://github.com/Hashtagich     |
2 | Назаров Ринат                 | Backend разработчик          | @NazRinRus           | https://github.com/NazRinRus      |
3 | Зайдигалов Артур              | Frontend разработчик         | @ArthZai             | https://github.com/Zaidigalov     |
4 | Наталия	                      | UX/UI дизайнер               | @goncearova_natalia  |                                   |
5 | Дмитриева Алина Анатольевна   | UX/UI дизайнер               | @LinneAya            |                                   |
6 | Мусаткина Анжела Вячеславовна | Графический дизайнер         | @avantello           | https://www.behance.net/avantello |
7 | Сергеева Оксана Юрьевна       | Графический дизайнер         | @Obl30               | https://www.behance.net/9510434b  |

</details>

___
<details>
<summary>

## Реализация проекта

</summary>

***Проект выполнен согласно требованиям Заказчика, полностью адаптирован под все устройства, удобен и прост в использовании.***

***Использованы следующие цвета:***
+ *#FFFFFF*
+ *#207B44*
+ *#79BD9A*
+ *#000000*
+ *#6E8877*
+ *#9DE1BE* и *#649B79*

***И шрифты:***
+ *Montserrat - Геометрический шрифт был выбран для заголовков на сайте;*
+ *Arial - Базовый шрифт, который идеально подходит для набора основного текста;*
+ *ARCO CYRILLIC - Геометрический шрифт на кириллице, который характеризуется четкими линиями и симметричными формами.*

***Backend разработка выполнена на Django с возможностью поддержки БД SQL и PostgreSQL.***

***Frontend разработка выполнена на JavaScript.***

***Взаимодействие Backend и Frontend осуществляется путём запроса API (использовали rest_framework) через JavaScript.***

</details>

___
### API
***Метод:***
<details>
<summary><code>GET/api/exhibition/</code></summary>

*Получение списка всех выставок*
```
[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "bunner": "string",
    "date_begin": "2024-05-02",
    "date_end": "2024-05-02",
    "time_event": "string",
    "location": "string",
    "venue": "string",
    "participants": [
      {
        "id": 0,
        "participant_foto": [
          {
            "foto": "string"
          }
        ],
        "breed": {
          "code": "str",
          "name": "string",
          "sort": 9223372036854776000,
          "is_active": true
        },
        "type_p": {
          "code": "string",
          "name": "string",
          "sort": 9223372036854776000,
          "is_active": true
        },
        "talent": {
          "code": "str",
          "name": "string",
          "sort": 9223372036854776000,
          "is_active": true
        },
        "name": "string",
        "color": "string",
        "age": "string",
        "gender": "boy",
        "other": "string",
        "found_home": true,
        "avatar_id": "string"
      }
    ],
    "partners": [
      {
        "id": 0,
        "name": "string",
        "logo": "string",
        "info": "string",
        "website": "string"
      }
    ],
    "about": "string",
    "exhibition_foto": [
      {
        "foto": "string"
      }
    ],
    "results": "string"
  }
]
```
</details>

***Метод:***
<details>
<summary><code>GET/api/exhibition/{id}/</code></summary>

*Получение одной записи (выставки) по её id*
```
{
  "id": 0,
  "name": "string",
  "description": "string",
  "bunner": "string",
  "date_begin": "2024-05-02",
  "date_end": "2024-05-02",
  "time_event": "string",
  "location": "string",
  "venue": "string",
  "participants": [
    {
      "id": 0,
      "participant_foto": [
        {
          "foto": "string"
        }
      ],
      "breed": {
        "code": "str",
        "name": "string",
        "sort": 9223372036854776000,
        "is_active": true
      },
      "type_p": {
        "code": "string",
        "name": "string",
        "sort": 9223372036854776000,
        "is_active": true
      },
      "talent": {
        "code": "str",
        "name": "string",
        "sort": 9223372036854776000,
        "is_active": true
      },
      "name": "string",
      "color": "string",
      "age": "string",
      "gender": "boy",
      "other": "string",
      "found_home": true,
      "avatar_id": "string"
    }
  ],
  "partners": [
    {
      "id": 0,
      "name": "string",
      "logo": "string",
      "info": "string",
      "website": "string"
    }
  ],
  "about": "string",
  "exhibition_foto": [
    {
      "foto": "string"
    }
  ],
  "results": "string"
}
```

</details>

***Метод:***
<details>
<summary><code>GET/api/exhibition/now/</code></summary>

*Получение одной записи (выставки). Выставка чья дата ближе всего к текущей. 
JSON аналогичен запросу <code>GET/api/exhibition/{id}/</code>*
</details>

***Метод:***
<details>
<summary><code>GET/api/exhibition/previous/</code></summary>

*Получение списка 6 последний выставок. JSON аналогичен запросу <code>GET/api/exhibition/</code>*
</details>

***Метод:***
<details>
<summary><code>POST/api/feedback/</code></summary>

*Метод предаёт информацию о пользователе, который желает приобрести питомца. 
После этого отправляется эл. письмо на почту сотрудников организации.*
```
{
  "name": "string",
  "phone": "string",
  "email": "user@example.com",
  "participant": "string"
}
```
</details>

***Метод:***
<details>
<summary><code>GET/api/faq/</code></summary>

*Получение списка часто задаваемых вопросов и ответов на них.*

```
[
  {
    "question": "string",
    "answer": "string"
  }
]
```
</details>

___
<details>
<summary>

## Дополнительная информация
</summary>

+ ***Сайт Заказчика (ГБУ «Доринвест») — https://dorinvest.ru/***
+ ***Подробная видеоинструкция сайта — https://cloud.mail.ru/public/tS2A/vtzQchok7***
</details>

![not images!!!](static/images/icons/logo.svg)