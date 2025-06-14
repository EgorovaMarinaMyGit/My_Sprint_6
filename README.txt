ТЕСТОВЫЕ СЦЕНАРИИ:

1. Выпадающий список в разделе «Вопросы о важном». 
Нужно проверить: когда нажимаешь на стрелочку, открывается соответствующий текст. 
Важно написать отдельный тест на каждый вопрос.

2. Заказ самоката. 
Нужно проверить весь флоу позитивного сценария с двумя наборами данных. 
Проверить точки входа в сценарий, их две: кнопка «Заказать» вверху страницы и внизу.

Из чего состоит позитивный сценарий:
- Нажать кнопку «Заказать». На странице две кнопки заказа.
- Заполнить форму заказа.
- Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
- Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
- Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная 
страница Дзена.

Нужно написать тесты с разными данными: минимум два набора. 
Сценарий общий, несмотря на разные точки входа: не нужно дважды тестировать каждую из них.


НАПИСАТЬ ТЕСТЫ:
- Описать необходимые локаторы с помощью Page Object.
- Создать отдельный пакет для Page Object.
- Для каждой страницы нужно создать отдельный класс с Page Object.
- Тесты на Selenium:
    - Разделить по тематике или функциональности
    - Обратить внимание: не нужно создавать отдельный класс для каждого теста
    - Добавить тесты на одну функциональность в один класс
    - Все тесты должны лежать в директории test
    - Проверить, что тесты запускаются
    - Использовать параметризацию

СДЕЛАТЬ ОТЧЁТ В Allure:
- Сгенерировать Allure-отчёт и запушить его в репозиторий.