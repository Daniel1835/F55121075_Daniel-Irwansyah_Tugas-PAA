import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Membuat array acak
arr = random.sample(range(1, 1000), 100)

# Menggunakan Bubble Sort
start_time = time.time()
sorted_arr_bubble = arr.copy()
bubble_sort(sorted_arr_bubble)
bubble_sort_time = time.time() - start_time

# Menggunakan Insertion Sort
start_time = time.time()
sorted_arr_insertion = arr.copy()
insertion_sort(sorted_arr_insertion)
insertion_sort_time = time.time() - start_time

# Menampilkan hasil dan perbandingan waktu eksekusi
print("Array awal:", arr)
print("Hasil Bubble Sort:", sorted_arr_bubble)
print("Waktu eksekusi Bubble Sort:", bubble_sort_time)
print("Hasil Insertion Sort:", sorted_arr_insertion)
print("Waktu eksekusi Insertion Sort:", insertion_sort_time)

# Membandingkan keoptimalan algoritma
if bubble_sort_time < insertion_sort_time:
    print("Bubble Sort lebih optimal.")
elif insertion_sort_time < bubble_sort_time:
    print("Insertion Sort lebih optimal.")
else:
    print("Kedua algoritma memiliki kinerja yang sama.")
