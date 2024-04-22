Python script that takes youtube links and converts them into downloadadble mp3 files

# GETTING STARTED
1. Setup the Virtual Env
   
   ``` python -m venv venv```
   
2. Activate the virtual env with either
   
   Linux:
   
   ```source .\venv\Scripts\activate ```

   Windows:
   
   ``` .\venv\Scripts\Activate.ps1 ```
   
3. Install all dependencies:
   ```pip install -r requirements.txt ```

4. To run the script:

   ``` python main.py <youtube_url_link> ```

5. Options:

  - to pass in a list of links using a text file:

     ``` python main.py -f <path_to_file> ```

  - to save the mp3 file with a specific name

     ``` python main.py <youtube_link> -n <file_name> ``` 
