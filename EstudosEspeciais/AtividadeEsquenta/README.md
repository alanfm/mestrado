# Instalação

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

Depois rodar o script `openFiles.py`.

```shell
python openFiles.py
```

Nessa parte do código, é possível selecionar apenas as funções que você deseja testar.
```python
if __name__ == "__main__":
    directory = 'src/files/sorted/'
    iterationFiles(directory, ['quadratic', 'cubic', 'binary', 'ternary', 'sequentialV1', 'sequentialV1'], True)
    directory = 'src/files/unsorted/'
    iterationFiles(directory, ['quadratic', 'cubic', 'sequentialV1', 'sequentialV1'], False)
```