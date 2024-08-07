# Self-learning-platform

👨‍🎓 Self-learning-platform - API для платформы самообучения студентов. Платформа обеспечивает возможность
авторизации и аутентификации пользователей, предоставляет функционал для создания
и управления разделами(курсами) и их материалами, а также тестирования знаний. Функционал
платформы реализован с использованием Django Rest Framework (DRF).  

---

 /             | CRUD(create) | CRUD(read) | CRUD(update) | CRUD(delete) 
---------------|--------------|------------|--------------|--------------
 Course        | +            | +          | +            | +            
 Lesson        | +            | +          | +            | +            
 Test          | +            | +          | +            | +            
 AttemptAnswer | +            | -          | -            | -            
 Users         | +            | -          | -            | -            

___
🧩 Используемый стек:

- Django (для реализации проекта использован фреймворк Django)
- PostgreSQL (хранения и обработка данных)
- DRF (используется библиотека DRF)
- JWT (реализована авторизация для защиты и управления сеансами)
- Viewset/Generic (используются специальные базовые классы для создания контролеров)
- Permissions (реализовано разделение прав доступа)
- Test (написаны тесты для основного функционала)
- Readme (описана документация в Readme файле)
- PEP8 (код соответствует рекомендациям PEP8)
- ORM (работа с СУБД, без написания SQL запросов в ручную)
- Git (код хранится в удаленном репозитории)
- CORS (настроена работа с доверенными доменными именами или IP адресами)
- OpenAPI Docs (реализована авто-генерируемая документация)
- Serialiers (для обработки данных проектом, используется библиотека сериализаторов)

___
⚙️ Рекомендации по запуску:

- Клонируйте проект
- Установите библиотеки из requirements.txt
- Переименуйте файл .env_free в .env и заполните его своими данными
- Сделайте миграции
- Протестируйте проект командой - "python manage.py test"
- Воспользуйтесь фикстурами для тестового заполнения данными приложения в очередности:
    - loaddata fixtures/group.json - Создаст группу moderators
    - loaddata fixtures/users.json - Создаст 4-х пользователей:
        - admin@rambler .ru - Администратор. Доступ в админку (назначает модераторов в группу moderators)
        - alexandr@top .ru - Модератор. Доступ ко всем функциям платформы (назначает преподавателя на курс - курс так же
          может создать только модератор!)
        - sergo@top .ru - Преподаватель/Владелец курса. Доступ только к своему курсу (курс ему задастся следующей по
          счету фикстурой) - может работать по системе CRUD с уроками и тестами принадлежащими к заданному курсу.
        - test@top .ru - Студент. Доступ к просмотру Курсов, Уроков, Тестов + может давать ответы на тесты.
    - loaddata fixtures/materials.json - Создаст курс присвоенный 3-ому по "pk" пользователю - sergo@top .ru
- Так же вы можете создать тестовых пользователей командой python manage.py cpu (CreatePackUsers) / удалить - python
  manage.py cpu_none. Или зарегистрировать в ручную
- Запустите проект 🚀
