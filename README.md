# gifterhub-multilabel-classification
Reproduce the ML-functionality for the gifterhub.ru

Service for selecting the best gifts

This project is my diploma work on specialization Data Science in SkillFactory, in <a href="https://youtu.be/KMik1zZr-ro">this video</a> you may look my successful protection of the diploma and learn more about creating a service from scratch

## Install
Python 3.7.7

    git clone https://github.com/salih-ds/gifterhub-multilabel-classification.git
    pip install -r requirements.txt
    
## Usage
Run the file "main.py"

    python main.py
    
Answer the questions using the terminal and get a list of gifts with the probability of success in descending order

## History

<table>
  <tbody><tr>
    <th>Задача</th>
    <th>Описание</th>
    <th>Модель</th>
    <th>f1-score</th>
    <th>sum log_loss</th>
  </tr>
  <tr>
    <td>Определить признаки и подарки, сформировать первичный датасет</td>
    <td>Определил 28 бинарных признаков по полу, возрасту, интересам (x).
      <br>Определил 977 подарков (y).
      <br>Используя фрилансеров, составил датасет 300x1005, при этом нашел фрилансеров всех возрастов и передал на разметку данные в соответствии с возрастной категорией исполнителя - таким образом получил наиболее релевантные данные.</td>
    <td>-</td>
    <td>-</td>
      <td>-</td>
  </tr>
    <tr>
    <td>Обучить базовый multi-label классификатор</td>
    <td>Протестировал 7 различных классификаторов в sklearn, лучший результат показал SVC.</td>
    <td>SVC</td>
    <td>0.606</td>
      <td>169.9</td>
  </tr>
    <tr>
    <td>Custom Active learning</td>
    <td>Сгенерировал 700 персонажей, предсказал с помощью обученного SVC подарки с порогом выбора от 15% - таким образом очистил мусорные данные.
      <br>Передал фрилансерам результат предсказания на проверку.
      <br>Получил датасет 1000х1005, при этом сократил расходы на разметку в 4 раза. Переобучил классификаторы на объединенных данных, лучший результат показал MLPClassifier.</td>
    <td>MLPClassifier</td>
    <td>0.719</td>
      <td>127.4</td>
  </tr>
    <tr>
    <td>Feature engineering</td>
    <td>Протестировал двойную и тройную генерацию комбинаций признаков, переобучая классификатор с новыми фичами.
      <br>Двойная генерация сильно улучшила метрики качества модели.</td>
    <td>MLPClassifier</td>
    <td>0.927</td>
      <td>41.1</td>
  </tr>
    <tr>
    <td>Active Learning</td>
    <td>Определил список персонажей, для которых модель наименее уверена в предсказаниях.
      <br>Попробовал самостоятельно разметить персонажей, но мои ответы были не релевантны, качество упало, сохраняю предыдущий вариант.</td>
    <td>MLPClassifier</td>
    <td>0.919</td>
      <td>45.9</td>
  </tr>
</tbody></table>

Удалось достичь очень высоких показателей качества модели, при этом сохранив очень высокую скорость предсказания в 0.007 сек

