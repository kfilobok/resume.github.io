# Портфолио-резюме

Проект для создания персонального резюме с использованием HTML, CSS и Flask.

## Описание задания

Необходимо разработать веб-страницу с вашим резюме, включающую следующий функционал:

### 1. Базовое резюме (30% от общей оценки)
- Создание структурированного резюме с основными разделами:
  - Личная информация
  - Образование
  - Опыт работы (проекты)
  - Навыки
  - Контактная информация

### 2. Темная тема (30% от общей оценки)
- Реализация переключателя между светлой и темной темой
- Сохранение выбранной темы при перезагрузке страницы
- Дополнительные баллы (+2):
  - Автоматическое определение системных настроек темы пользователя
  - Автоматическое переключение в зависимости от времени суток

### 3. Мультиязычность (35% от общей оценки)
- Реализация переключателя между русской и английской версиями
- Полный перевод всего контента
- Сохранение выбранного языка при перезагрузке страницы
- Поддержка темной темы для обеих языковых версий

### 3. Хостинг (5% от общей оценки)
- Требуется захостить ваше резюме на любом бесплатном хостинге (наши рекомендации попробуйте github pages, например как тут https://buzaev-fedor.github.io/)

## Критерии оценки
- Качество верстки и отсутствие визуальных багов
- Работоспособность всех интерактивных элементов
- Полнота и качество представленной информации в резюме
- Корректная работа переключателей темы и языка
- Сохранение настроек пользователя

Ваше проект будет проверяться в ручном режиме, поэтому в anytask загружайте ссылку на ваш github репозиторий, а не архив с проектом. Также ссылку на сайт-резюме.

---
Оригинальные файлы
---

```html
<!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet", crossorigin="anonymous">
    <link rel="stylesheet" href="static/css/custom.css">
    <title> Верхняя строчка | Должность </title>
  </head>
  <body>
    <!-- Секция промо с темным фоном - шапка сайта -->
    <section class="promo dark-bg pt-2 pb-5">
      <div class="container">
        <!-- Навигационная панель с логотипом и кнопкой -->
        <nav class="navbar navbar-expand-lg mb-5 navbar-dark">
          <div class="container-fluid">
            <a href="#" class="navbar-brand logo d-flex align-items-center text-decoration-none">
              <div class="logo-left pe-2">
                <!-- Здесь вставьте ваш логотип/фотку, ее можно скруглять и увеличивать в размере-->
                <img src="../static/01_Logo_HSE_full_rus_PANTONE_for_dark_2.png" alt="" class="rounded-circle" width="70">
              </div>
              <div class="logo-right" style="margin-left: 6px;">
                <div class="logo-title link-purple">Верхняя строчка</div>
                <div class="logo-subtitle text-yellow">Должность</div>
              </div>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <!-- Меню навигации -->
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="nav m-auto">
                <li class="nav-item mx-3">
                  <a href="#story" class="nav-link link-purple link-border-bottom">Вкратце обо мне</a>
                </li>
                <li class="nav-item mx-3">
                  <a href="#projects" class="nav-link link-purple link-border-bottom">Мой опыт работы</a>
                </li>
                <li class="nav-item mx-3">
                  <a href="#contact" class="nav-link link-purple link-border-bottom">Сотрудничество</a>
                </li>
              </ul>
              <ul class="nav ml-auto">
                <li class="nav-item mx-3">
                  <a href="https://github.com" class="nav-link link-purple link-border-bottom">Github</a>
                </li>
                <li class="nav-item mx-3 mr-0">
                  <a href="#contact" class="nav-link link-purple link-border-bottom">Написать мне</a>
                </li>
              </ul>
            </div>
          </div>
        </nav>

         <!-- Блок приветствия с основной информацией -->
        <div class="row py-0 py-sm-5">
          <div class="col-12 col-lg-8 offset-lg-2 mb-0 mb-sm-5 py-5">
            <h1 class="h1 font-weight-bold font greeting-text text-blue">Привет! Здесь вы напишете о себе</h1>
            <p class="promo-text pb-3">Я&nbsp;&mdash; студент Высшей Школы Экономики, ФКН/ФЭН ВШЭ, <br> Учусь хорошо, мечтаю начать ходить на все лекции. </p>
            <a href="#contact" class="btn text-center" style="background-color: #DCFF05; color: #102D69">Написать мне</a>
          </div>
        </div>
      </div>
    </section>
     <!-- Секция "Обо мне" -->
    <section class="story container py-5 text-center" id="story">
      <h2 class="h1 font-weight-bold mt-4 mb-3 mb-sm-5 pb-3 navigo-font">Обо мне</h2>
      <div class="row">
        <div class="col-12 col-sm-8 offset-sm-2 px-2 pb-5">
          <p class="font-weight-bold pb-4">Я &mdash; обычный студент (здесь напишите о себе);
        </div>
      </div>
    </section>
     <!-- Секция опыта работы с темным фоном -->
    <section class="projects dark-bg pt-3 pt-sm-5 pb-3" id="projects">
      <div class="container">
        <h2 class="h1 font-weight-bold text-center mt-4 mt-sm-5 mb-0 mb-sm-4 pb-5 navigo-font">Мой опыт работы</h2>

        <div class="work-experience text-white">
          <div class="d-flex align-items-center mb-4">
            <img src="../static/01_Logo_HSE_full_rus_PANTONE_for_dark_2.png" alt="HSE Logo" class="me-3" style="height: 60px; margin-top: -6px;">
            <div class="d-flex flex-column justify-content-center">
              <h3 class="h4 mb-1">НИУ «ВШЭ»</h3>
              <p class="text-white-40 mb-0">Сентябрь 2022 – Настоящее время</p>
            </div>
          </div>

          <div class="position mb-4" style="margin-left: 20px;">
            <h4 class="h5 text-purple">Студент</h4>
            <p class="text-white" style="opacity: 0.4">Сентябрь 2022 – настоящее время</p>
            <p>Занимаюсь изучением математики и программирования.</p>
          </div>
      </div>
    </section>
 <!-- Секция личных целей -->
    <section class="goals container pt-3 pt-sm-5 pb-3">
      <h2 class="h2 font-weight-bold my-4">Мои цели</h2>
      <div class="row">
        <div class="col-12 col-sm-8 pb-1">
          <p class="pb-2">Добиться в Ровеснике скидку 20%.</p>
        </div>
      </div>
    </section>

     <!-- Секция сотрудничества -->
    <section class="goals container mb-5 pb-sm-5 pb-0" id="contact">
      <h2 class="h2 font-weight-bold my-4">Сотрудничество</h2>
      <div class="row">
        <div class="col-12 col-sm-8 pb-1">
          <p class="pb-1 mb-1">Если интересно, что я могу для вас сделать, пишите:</p>
          <!-- <ul class="list-unstyled mb-4">
            <li class="d-flex align-items-center align-content-start m-2" style="line-height: 24px;">
              <span class="pr-1">
                <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
              </span>
              <span>Найти интересную работу в хорошей компании с возможностью роста</span>
            </li>
            <li class="d-flex align-items-center align-content-start m-2" style="line-height: 24px;">
              <span class="pr-1">
                <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/><path d="M0 0h24v24H0z" fill="none"/></svg>
              </span>
              <span>Поучаствовать в олимпиаде как ml-developer</span>
            </li>
          </ul> -->
          <!-- Блок с кнопками для связи -->
          <div class="row">
            <div class="col-12 col-sm-9">
              <p class="d-flex justify-content-start gap-2 flex-wrap">
                <a href="https://t.me/durov" class="btn mb-3" style="background-color: #DCFF05; color: #102D69" target="_blank">Написать в Telegram</a>
                <a href="https://example.com/" class="btn mb-3" style="background-color: #DCFF05; color: #102D69" target="_blank">Посмотреть резюме</a>
                <a href="mailto:any@example.com" class="btn mb-3" style="background-color: #DCFF05; color: #102D69" target="_blank">Написать на почту</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Подвал сайта с темным фоном -->
    <footer class="footer dark-bg">
      <nav class="container navbar ">
        <ul class="nav m-auto py-2">
          <li class="nav-item mx-3">
            Cделано с любовью в 2024 году.
          </li>
        </ul>
      </nav>
    </footer>

    <!-- Подключение скриптов Bootstrap -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

```css
@font-face {
  font-family: 'Navigo';
  src: url('../fonts/Navigo-Regular-Desktop.otf') format('opentype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Roboto';
  src: url('../fonts/Roboto-Regular.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

html {
  scroll-behavior: smooth;
}

body {
  font-size: 18px;
  line-height: 1.6;
  font-family: 'Roboto', sans-serif;
}

.dark-bg {
  background-color: #102D69;
  color: #fff;
}

.dark-bg .navbar-toggler {
  border: 1px solid #fff;
  color: #fff;
}

.font-color-blue {
  color: #102D69;
}

.btn-blue {
  font-size: 1.15rem;
  padding-left: 1.5rem;
  padding-right: 1.5rem;
  background-color: #102D69;
  border-color: #102D69;
}

.promo-text {
  font-size: 24px;
  opacity: .75;
  font-family: 'Roboto', sans-serif;
}

.link-border-bottom {
  display: inline-block;
  padding:0;
  text-decoration: none;
  line-height: 1.3;
  border-bottom: 1px solid #6c757d;
  transition: .4s ease;
}

.text-white.link-border-bottom {
  border-bottom: 1px solid #fff;
}

.link-border-bottom:hover {
  border-color: transparent;
}

.link {
  color: rgba(255,255,255,.8);
  text-decoration: none;
  transition: .4s ease;
  border-bottom: 1px solid rgba(255,255,255,.8);
}

.link:hover {
  color: rgba(255,255,255,.8);
  text-decoration: none;
  border-color: transparent;
}

.link.link-blue {
  color: #102D69;
  border-color: #102D69;
}

.link.link-blue:hover {
  color: #102D69;
  border-color: transparent;
}

.link.link-purple {
  color: #DFC7F2;
  border-color: #DFC7F2;
}

.link.link-purple:hover {
  color: #DFC7F2;
  border-color: transparent;
}

.link.link-yellow {
  color: #DCFF05;
  border-color: #DCFF05;
}

.link.link-yellow:hover {
  color: #DCFF05;
  border-color: transparent;
}

.text-yellow {
  color: #DCFF05 !important;
}

.logo:hover {
  text-decoration: none;
  transition: .4s ease;
  opacity: .85;
}

.logo-title {
  font-size: 20px;
  line-height: 1.5;
}

.logo-subtitle {
  font-size: 17px;
  line-height: 1;
}

.story p {
  font-size: 24px;
  line-height: 35px;
}

.story-link {
  color: #102D69;
  text-decoration: none;
  transition: .4s ease;
  border-bottom: 2px solid #102D69;
}

.story-link:hover {
  color: #102D69;
  text-decoration: none;
  border-color: transparent;
}

.greeting-text {
  color: #DFC7F2;
  font-family: 'Navigo', sans-serif;
  font-weight: normal;
}

.navbar .nav-link.link-purple {
  color: #DFC7F2 !important;
}

.navbar .nav-link.link-purple:hover {
  color: #DFC7F2 !important;
}

.logo-right {
  margin-left: 6px;
}

.text-blue {
  color: #DFC7F2 !important;
}

h1.greeting-text {
  color: #DFC7F2;
}

.btn-yellow {
  background-color: #DCFF05;
  color: #102D69;
}

.btn-yellow:hover {
  background-color: #c4e004;  /* Немного темнее при наведении */
  color: #102D69;
}

.navigo-font {
  font-family: 'Navigo', sans-serif;
  font-weight: normal;
}

.text-purple {
  color: #DFC7F2 !important;
}

.text-white-40 {
  color: #fff !important;
  opacity: 0.4;
}

.position {
  margin-left: 20px;
}
```

```py
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.errorhandler(404)
def render_not_found(error):
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим"



if __name__ == '__main__':
    app.run(port=5002, debug=True)

```