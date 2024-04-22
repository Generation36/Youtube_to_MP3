Python script that takes youtube links and converts them into downloadadble mp3 files

# GETTING STARTED
1. Install all dependencies:
   ```pip install -r requirements.txt ```
2. Activate the virtual env with either
   
   Linux:
   
   ```source ./scripts/activate ```

   Windows:
   
   ``` Activate.ps1 ```

3. To run the script:

   ``` python main.py <youtube_url_link> ```

4. Options:

  - to pass in a list of links using a text file:

     ``` python main.py -f <path_to_file> ```

  - to save the mp3 file with a specific name

     ``` python main.py <youtube_link> -n <file_name> ``` 
