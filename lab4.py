import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Создание простейшей модели
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))  # Входной слой
model.add(Dense(1, activation='sigmoid'))  # Выходной слой

# Компиляция модели
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Пример данных
X_train = np.random.rand(100, 8)  # 100 примеров по 8 признаков
y_train = np.random.randint(2, size=(100, 1))  # 100 меток

# Обучение модели
model.fit(X_train, y_train, epochs=10)

# Оценка модели
scores = model.evaluate(X_train, y_train)
print(f"Accuracy: {scores[1] * 100}%")
