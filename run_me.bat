@echo off
call "C:\Users\Fr. Alam\miniconda3\condabin\activate.bat"
call activate base
python ./script.py
call conda deactivate
Rename transcription.txt transcription.doc
pause
