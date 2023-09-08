# ATIVIDADE ESQUENTA 2

Fazer uma busca do valor máximo usando dois algoritmos distintos.

## Instalação

Criar um ambiente virtual no python (venv)
* ```shell
    python -m venv env
  ```
* ```shell
    source env/bin/activate
  ```
* ```shell
    pip install -r requirements.txt
  ```

Gerar os arquivo executar o script `src/generateFiles.py`.

```shell
cd src && python generateFiles.py
```

Depois rodar o script `main.py`.

```shell
python main.py
```

Nessa parte do código, é possível selecionar apenas as funções que você deseja testar.
```python
def main():    
    directory = 'src/files/'
    getResults(directory, ['maxVal1', 'maxVal2'])
```