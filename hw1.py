import os
import shutil
import argparse

def copy_files(src_dir, dest_dir):
  """
  Рекурсивно копіює файли з вихідної директорії в директорію призначення, 
  сортуючи їх за розширенням.

  Args:
    src_dir: Шлях до вихідної директорії.
    dest_dir: Шлях до директорії призначення.
  """
  try:
    for item in os.listdir(src_dir):
      item_path = os.path.join(src_dir, item)
      if os.path.isdir(item_path):
        copy_files(item_path, dest_dir)
      elif os.path.isfile(item_path):
        file_name, file_ext = os.path.splitext(item)
        subdir = os.path.join(dest_dir, file_ext[1:])  # Видаляємо крапку з розширення
        os.makedirs(subdir, exist_ok=True)
        shutil.copy2(item_path, subdir)
  except OSError as e:
    print(f"Помилка: {e}")

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Копіювання файлів з сортуванням за розширенням.")
  parser.add_argument("src_dir", help="Шлях до вихідної директорії.")
  parser.add_argument("-d", "--dest_dir", default="dist", help="Шлях до директорії призначення (за замовчуванням: dist).")
  args = parser.parse_args()

  copy_files(args.src_dir, args.dest_dir)
  print("Копіювання файлів завершено.")
  