from dotenv import load_dotenv
from dotenv import dotenv_values
import time

load_dotenv()
env_vars = dotenv_values()

import google.generativeai as genai

genai.configure(api_key=env_vars.get("GEMINI_API_KEY"))

def upload_to_gemini(path, mime_type=None):
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
  print("Waiting for file processing...")
  for name in (file.name for file in files):
    file = genai.get_file(name)
    while file.state.name == "PROCESSING":
      print(".", end="", flush=True)
      time.sleep(10)
      file = genai.get_file(name)
    if file.state.name != "ACTIVE":
      raise Exception(f"File {file.name} failed to process")
  print("...all files ready")
  print()

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
#   "max_output_tokens": 8192,
    "max_output_tokens": 5000,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# TODO Make these files available on the local file system
# You may need to update the file paths
files = [
  # upload_to_gemini("dem_sla.pdf", mime_type="application/pdf"),
  upload_to_gemini("./data/demon_slayer.pdf", mime_type="application/pdf"),
]

# Some files have a processing delay. Wait for them to be ready.
wait_for_files_active(files)

# chat_session = model.start_chat(
#   history=[
#     {
#       "role": "user",
#       "parts": [
#         files[0],
#         "I have a demon slayer pdf. analyse the pdf and answer my questions based on your understanding of the pdf contents.",
#       ],
#     },
#     {
#       "role": "model",
#       "parts": [
#         "Please provide me with the PDF file. I will read through it and then I can answer your questions about the Demon Slayer series based on the information contained in the PDF. \n",
#       ],
#     },
#     {
#       "role": "user",
#       "parts": [
#         files[1],
#       ],
#     },
#     {
#       "role": "model",
#       "parts": [
#         "I am a text-based AI and thus I cannot process any files, including PDFs. \n\nTo help me answer your questions, please type out the questions you have about the Demon Slayer series.  I will do my best to answer them based on the information provided in your summary of the PDF. \n",
#       ],
#     },
#     {
#       "role": "user",
#       "parts": [
#         "who is the main character in demon slayer?\nwhat is demon slayer?\nwho is tanjiro's sister?\nhow did nezuko become a demon?",
#       ],
#     },
#     {
#       "role": "model",
#       "parts": [
#         "Here are the answers to your questions based on the provided text:\n\n* **The main character in Demon Slayer is Tanjiro Kamado.** He is a kind and determined young man who becomes a Demon Slayer after his family is slaughtered by a demon, and his sister Nezuko is turned into a demon. \n* **Demon Slayer is a Japanese manga and anime series created by Koyoharu Gotouge.**  The story follows Tanjiro as he strives to become a Demon Slayer to protect his sister, Nezuko, and avenge his family's death. \n* **Tanjiro's sister is Nezuko Kamado.** \n* **Nezuko was turned into a demon by Muzan Kibutsuji, the main antagonist in the series.** Muzan attacked Tanjiro's family, killing all but Tanjiro and Nezuko. He then turned Nezuko into a demon in an attempt to turn her into one of his \"Twelve Kizuki\". \n\nLet me know if you have any other questions about the series. \n",
#       ],
#     },
#   ]
# )


chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "I have a demon slayer pdf. analyse the pdf and answer my questions based on your understanding of the pdf contents.",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please provide me with the pdf file, and I will be happy to analyze it and answer your questions based on its contents. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[0],
      ],
    },
    {
      "role": "model",
      "parts": [
        "The provided text is a summary of the Demon Slayer: Kimetsu no Yaiba manga and its adaptations. Here is an analysis of the information provided:\n\n**Summary**\n\n* **Premise:** Tanjiro Kamado, a young boy, strives to become a Demon Slayer after his family is slaughtered and his sister Nezuko is transformed into a demon.\n* **Setting:** Taisho era Japan, a secret organization known as the Demon Slayer Corps wages war against demons, supernatural beings with enhanced abilities.\n* **Plot:** Tanjiro trains to become a Demon Slayer, learns the Water Breathing style, and faces numerous challenges in his quest to cure Nezuko and defeat the ultimate demon, Muzan Kibutsuji.\n* **Themes:** Family, sacrifice, determination, fighting for justice, overcoming adversity.\n* **Key characters:**\n    * Tanjiro Kamado: The protagonist, a kind-hearted and determined boy.\n    * Nezuko Kamado: Tanjiro's younger sister, transformed into a demon, but retains her humanity.\n    * Giyu Tomioka: A skilled Demon Slayer who serves as Tanjiro's mentor.\n    * Kyojuro Rengoku: The Flame Hashira, a powerful and inspiring Demon Slayer.\n    * Muzan Kibutsuji: The ultimate evil, the progenitor of all demons.\n* **Adaptations:**\n    * Anime television series: Aired from April to September 2019.\n    * Film: Demon Slayer: Kimetsu no Yaiba – The Movie: Mugen Train (2020)\n    * Second season: Aired from October 2021 to February 2022.\n    * Third season: Aired from April to June 2023.\n    * Fourth season: Aired from May to June 2024.\n    * Video game: Demon Slayer: Kimetsu no Yaiba - The Hinokami Chronicles (2021)\n    * Stage play: Premiered in January 2020.\n    * Light novels: Several light novels expanding on the world of Demon Slayer have been released.\n\n**Popularity and Cultural Impact**\n\n* The manga series has been a massive success, selling over 150 million copies worldwide, making it one of the best-selling manga series of all time.\n* Its popularity has translated into huge success for its anime adaptations, particularly the Mugen Train film.\n* The series has been praised for its art, storytelling, and characters, and has had a significant cultural impact in Japan and around the world.\n\n**Production**\n\n* The manga was serialized in Shueisha's Weekly Shōnen Jump from February 2016 to May 2020.\n* It was written and illustrated by Koyoharu Gotouge.\n* The anime series was produced by Ufotable, a studio known for its high-quality animation.\n\n**Please provide me with the specific questions you have about the Demon Slayer pdf, and I will do my best to answer them based on my understanding of its contents.** \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Who is Muzan?\nWHo is Nezuko?\nHow did nezuko become a demon?\nWho is the leader of the demon slayer corps?\nhow to kill the demons?\nWHo is the main character?\nWHo is a hashira?\nWHo is the strongest hashira?\nWho is the flame hashira?",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Here are the answers to your questions about Demon Slayer:\n\n* **Who is Muzan?** Muzan Kibutsuji is the ultimate evil in the Demon Slayer universe. He is the progenitor of all demons, responsible for the massacre of Tanjiro's family and the suffering of countless humans. He is a powerful and ruthless demon who seeks immortality and to rule the world.\n\n* **Who is Nezuko?** Nezuko Kamado is Tanjiro's younger sister, who was transformed into a demon by Muzan. Despite her transformation, Nezuko retains some of her humanity and has an unwavering bond with Tanjiro. She is a powerful ally in his fight against demons.\n\n* **How did Nezuko become a demon?**  Muzan attacked Tanjiro's family, killing all but Nezuko. In a desperate attempt to save her, Muzan bit Nezuko, transforming her into a demon.\n\n* **Who is the leader of the Demon Slayer Corps?** The current leader of the Demon Slayer Corps is Kagaya Ubuyashiki, a wise and compassionate man. He is a blind man who possesses a strong sense of justice and a deep understanding of the demon threat. \n\n* **How to kill demons?** There are several methods to kill demons:\n    * **Direct sunlight:** Demons are vulnerable to direct sunlight and will disintegrate in its presence.\n    * **Decapitation with a Nichirin sword:** These special swords, forged from an alloy called Nichirin, are the primary weapons of the Demon Slayers and are effective against demons. \n    * **Wisteria poison:** Poison extracted from wisteria flowers is also effective in killing demons. \n\n* **Who is the main character?** The main character of Demon Slayer is Tanjiro Kamado, a kind-hearted and determined young man who becomes a Demon Slayer to save his sister and avenge his family.\n\n* **Who is a Hashira?** The Hashira are the most elite and powerful Demon Slayers in the Corps. They have earned this title through years of intense training and a record of successfully slaying many demons. They are considered the strongest warriors within the organization.\n\n* **Who is the strongest Hashira?**  While the strength of the Hashira is debated, Gyomei Himejima, the Stone Hashira, is often considered the most powerful. He is a giant man with superhuman strength and possesses the Stone Breathing style. \n\n* **Who is the Flame Hashira?** Kyojuro Rengoku was the Flame Hashira, a powerful and inspiring Demon Slayer who fought fiercely against demons and served as a mentor to Tanjiro. He was tragically killed during a battle against Akaza, the Upper Three demon. \n",
      ],
    },
  ]
)


# response = chat_session.send_message("Who is Tanjiro?")

# print(response.text)