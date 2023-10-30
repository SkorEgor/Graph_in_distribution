<!---------------------------------------------------------------------------------->
<div align="left">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" height=24> 
<img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" height=24>
<img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white" height=24>
<img src="https://img.shields.io/badge/Qt-41CD52?style=for-the-badge&logo=Qt&logoColor=white" height=24>
</div>

<h1 align="center"> Antenna Directive / Направленность Антенн </h1>

Программа демонстрирует вызов модального окна с последующим возвратом значения.
Во всплывающем окне реализован кастомный lable, на заднем фоне сетка, на переднем можно рисовать график.
lable имеет функцию перевода графика в массив. 

Для проверки корректности перевода, в модальном окне предусмотрено отображение массива в виде графика 

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> Содержание </h2>

1. [ Описание задачи и демонстрация работы ](https://github.com/SkorEgor/Antenna_Directivity_version2#-1-описание-задачи-и-демонстрация-работы-)
2. [ Входные и выходные данные ](https://github.com/SkorEgor/Antenna_Directivity_version2#-2-входные-и-выходные-данные-)
3. [ Описание логической структуры - Алгоритм программы ](https://github.com/SkorEgor/Antenna_Directivity_version2#-3-описание-логической-структуры---алгоритм-программы-)
4. [ Структура программы - Классы и их описание](https://github.com/SkorEgor/Antenna_Directivity_version2#-4-структура-программы---классы-и-их-описание-)

<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 1. Описание задачи и демонстрация работы </h2>

1. Открытие главного окна
2. Вызов модального окна
3. Рисуем
   1. В случае ошибки - можно все стереть
   2. Для проверки - график
4. Кнопки Ок и Cancel закрывают окно передавая статус


<div align="center">
<!--- Демонстрация работы -->
<img src="" >
</div>
<!---------------------------------------------------------------------------------->

---

<h2 align="left"> 2. Добавление в свой проект </h2>

1. В корень проекта добавляем папки "label_drawing_to_array" и "modal_dialog"
2. В программе с вызовом окна
   1. Импортируем модальное окно
```C
from modal_dialog.schedule_to_distribution import DateDialog
```
   2. Вызываем и ждем значение
```C
    def open_and_get_data(self):
        print(DateDialog.get_array())
```
