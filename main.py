# 1
# import os
# import multiprocessing

# def count_words_in_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         return len(f.read().split())

# def main():
#     txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
#     with multiprocessing.Pool() as pool:
#         word_counts = pool.map(count_words_in_file, txt_files)
    
#     total_word_count = sum(word_counts)
#     print(f" Barcha .txt fayllaridagi so'zlarning umumiy soni : {total_word_count}")

# if __name__ == "__main__":
#     main()



# 2
# import os
# import multiprocessing
# import re

# def count_digits_in_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#         return len(re.findall(r'\d', content))

# def main():
#     txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
#     with multiprocessing.Pool() as pool:
#         digit_counts = pool.map(count_digits_in_file, txt_files)
    
#     total_digit_count = sum(digit_counts)
#     print(f"Barcha .txt fayllaridagi raqamlarning umumiy soni: {total_digit_count}")

# if __name__ == "__main__":
#     main()



# 3
# import os
# import multiprocessing
# import re

# def count_sentences_in_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#         sentences = re.split(r'[.!?]+', content)
#         return len([s for s in sentences if s.strip()])

# def main():
#     txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
#     with multiprocessing.Pool() as pool:
#         sentence_counts = pool.map(count_sentences_in_file, txt_files)
    
#     total_sentence_count = sum(sentence_counts)
#     print(f"Barcha .txt faylidagi jumlalarning umumiy soni: {total_sentence_count}")

# if __name__ == "__main__":
#     main()





# 4
# import os
# import multiprocessing
# import re

# def find_longest_sentence_in_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
#         sentences = re.split(r'(?<=[.!?]) +', content)
#         longest_sentence = max(sentences, key=len).strip() if sentences else ''
#         return longest_sentence

# def main():
#     txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
#     with multiprocessing.Pool() as pool:
#         longest_sentences = pool.map(find_longest_sentence_in_file, txt_files)
    
#     overall_longest_sentence = max(longest_sentences, key=len).strip() if longest_sentences else ''
#     print(f"Eng uzun jumla: {overall_longest_sentence}")

# if __name__ == "__main__":
#     main()




# 5
# import os
# import string
# import multiprocessing

# def remove_punctuation_from_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         content = f.read()
        
#     translator = str.maketrans('', '', string.punctuation)
#     cleaned_content = content.translate(translator)
    
#     with open(file_path, 'w', encoding='utf-8') as f:
#         f.write(cleaned_content)

# def main():
#     txt_files = [f for f in os.listdir() if f.endswith('.txt')]
    
#     with multiprocessing.Pool() as pool:
#         pool.map(remove_punctuation_from_file, txt_files)

# if __name__ == "__main__":
#     main()



# 6
# import os
# import requests
# import multiprocessing
# from urllib.parse import urlparse

# def download_image(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()

#         parsed_url = urlparse(url)
#         image_name = os.path.basename(parsed_url.path)

#         with open(image_name, 'wb') as f:
#             f.write(response.content)
#         print(f"Downloaded {image_name} from {url}")
#     except requests.exceptions.RequestException as e:
#         print(f"Failed to download {url}: {e}")

# def main():
#     image_urls = [
#         "https://example.com/image1.jpg",
#         "https://example.com/image2.jpg",
#         "https://example.com/image3.jpg"
#     ]
    
#     with multiprocessing.Pool(processes=len(image_urls)) as pool:
#         pool.map(download_image, image_urls)

# if __name__ == "__main__":
#     main()

