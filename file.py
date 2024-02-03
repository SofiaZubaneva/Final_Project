import tkinter as tk
from tkinter import messagebox
import time


#Функция пузырьковой сортировки.
def bubble_sort(arr):
   num = len(arr)
   for i in range(num):
       for j in range(0, num-i-1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]


#Функция сортировки выбором
def selection_sort(arr):
    num = len(arr)
    for i in range(num):
        min_idx = i
        for j in range(i+1, num):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


#Функция быстрой сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


#Функция отвечающая за: проверку корректности ввода, ввод чисел, выбора вида сортировки и вычисления затраченного времени
def start_sort():
    # Проверка наличия введенных чисел
    if len(input_entry.get().strip()) == 0:
        messagebox.showerror("Ошибка", "Введите, пожалуйста, числа.")
        return

    input_numbers = input_entry.get()
    # Проверка на корректность введенных чисел
    try:
        numbers = [int(x) for x in input_numbers.split(",")]
    except ValueError:
        messagebox.showerror("Ошибка", "Числа введены некорректно")
        return

    sort_method = sort_choice.get()

    if sort_method == 'пузырьковая сортировка':
        bubble_sort(numbers)
    elif sort_method == 'сортировка выбором':
        selection_sort(numbers)
    elif sort_method == 'быстрая сортировка':
        quick_sort(numbers)

    timing(numbers)


#Функция вычисления затраченного времени.
def timing(num):
    # Засекаем начальное время
    start_time = time.time()
    # Засекаем конечное время
    end_time = time.time()
    # Вычисляем затраченное время
    all_time = end_time - start_time

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, ', '.join(map(str, num)))
    output_text.insert(tk.END, f"\nВремя сортировки: {round(all_time, 6)} сек")


#Создание окна
root = tk.Tk()
root.title('Программа сортировки')

input_label = tk.Label(root, text='Введите числа через запятую: ')
input_entry = tk.Entry(root)

sort_label = tk.Label(root, text='Выберете метод сортировки: ')

choice = ['Пузырьковая сортировка', 'Сортировка выбором', 'Быстрая сортировка']

sort_choice = tk.StringVar(root)
sort_choice.set(choice[0])

sort_menu = tk.OptionMenu(root, sort_choice, *choice)

btm = tk.Button(root, text='Start', command=start_sort)

output_label = tk.Label(root, text='Вывод')

output_text = tk.Text(root, height=4)

input_label.pack()
input_entry.pack()
sort_label.pack()
sort_menu.pack()
btm.pack()
output_label.pack()
output_text.pack()


root.mainloop()




