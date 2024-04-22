import os
import logging
from collections import namedtuple
# Настройка логирования
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s',encoding='utf8')

# Определение namedtuple для хранения информации о файле или каталоге(вот ето загуглил)
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path):
    # Получение списка файлов и каталогов в указанной директории
    try:
        files = os.listdir(directory_path)
    except FileNotFoundError:
        logging.error(f"Директория {directory_path} не найдена")
        return None
    except Exception as e:
        logging.error(f"Ошибка при получении списка файлов: {e}")
        return None

    # Создание списка объектов FileInfo
    file_info_list = []
    for file in files:
        # Определение пути к файлу или каталогу
        file_path = os.path.join(directory_path, file)
        # Определение имени файла или каталога без расширения
        name, extension = os.path.splitext(file)
        # Определение флага каталога
        is_directory = os.path.isdir(file_path)
        # Определение названия родительского каталога
        parent_directory = os.path.basename(directory_path)
        # Создание объекта FileInfo
        file_info = FileInfo(name, extension, is_directory, parent_directory)
        # Добавление объекта в список
        file_info_list.append(file_info)
    return file_info_list

if __name__ == "__main__":
    directory_path = input("Введите путь до директории: ")
    directory_info = get_directory_info(directory_path)
    if directory_info:
        for i in directory_info:
            logging.info(i)