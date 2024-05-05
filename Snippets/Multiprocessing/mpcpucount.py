import multiprocessing as mp

print(mp.cpu_count())
print(mp.active_children())

current = mp.current_process()
print(current)
print(mp.get_start_method())