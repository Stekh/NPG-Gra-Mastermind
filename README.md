# Repozytorium projektu grupowego z NPG - Gra Mastermind  

## Instrukcja przygotowania lokalnego środowiska:  

1. Sklonuj repozytorium za pomocą komendy: `git clone https://github.com/Stekh/NPG-Gra-Mastermind.git`  
2. Wewnątrz powstałego folderu wywołaj następującą komendę: `python -m venv .\.venv`  
3. Ustaw swoje IDE by korzystało z powstałego wirtualnego środowiska  
4. Wywołaj wewnątrz wirtualnego środowiska komendę: `pip install .`
5. Aby zainstalować moduły potrzebne do testów, wywołaj komendę `pip install .[test]`  

## Instrukcja ustawienia wirtualnego środowiska w IDE PyCharm:  

1. Otwórz folder z repozytorium jako projekt PyCharm  
2. Wejdź w File>Settings>Project>Python Interpreter  
3. Naciśnij `Add Interpreter` następnie wybierz `Add Local Interpreter`  
4. Wybierz opcję `Existing` i naciśnij `Ok`  

## Instrukcja instalacji Pythona (w wersji 3.11)  

1. Wywołaj komendę `winget install -e --id Python.Python.3.11`
2. Zrestartuj komputer  
