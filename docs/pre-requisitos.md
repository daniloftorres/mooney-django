## Pré-requisitos

- [Git](#instalacao-e-configuracao-do-git)
- [python](#instalacao-do-python)
- [Pip](#instalacao-do-pip)
- [Docker](#instalacao-e-configuracao-docker)
- [Docker Compose](#instalacao-e-configuracao-docker)

## Instalação e Configuração do Git

    -   Configuração inicial para uso de ssh para conexão

    ```bash

        git init
        git config --local user.name "Danilo Torres"
        git config --local user.email daniloftorres@gmail.com
        git remote -v
        git remote set-url origin git@github-daniloftorres:daniloftorres/mooney.github.io.git
    ```

    -   Arquivo `config`

    ```bash
        # Configuração para a conta daniloftorres
        Host github-daniloftorres
        HostName github.com
        User git
        IdentityFile ~/.ssh/id_rsa
        IdentitiesOnly yes
    ```

    Check permissão e dono do arquivo config
    - As permissões devem ser -rw-------
    - O config precisa estar como dono o usuario local
    ```bash
        ls -lha
        -rw-------  1 danilo danilo 1,2K mar  6 12:00 config
        drwxrwxr-x  2 danilo danilo 4,0K mar 13  2023 danilo
        -rw-------  1 danilo danilo 2,6K dez  4  2020 danilotorres3030
        -rw-rw-r--  1 danilo danilo  577 dez  4  2020 danilotorres3030.pub
    ```

    Ajustando caso necessário
    ```bash
    sudo chown danilo:danilo ~/.ssh/config
    ```

    Mudando permissão caso necessario:

    ```bash
    chmod 600 ~/.ssh/config
    ```

    Teste a conexão

    ```bash
        ssh -T git@github-daniloftorres
    ```

## Instalação do Python

Se o Python 3 não estiver instalado, você pode instalá-lo usando:

```bash
sudo apt update
sudo apt install python3
```

## Instalação do Pip

```bash
pip3 --version
```

### Instalação do Pip para Python

O Pip normalmente é instalado com o Python 3 no Ubuntu, mas se não estiver, você pode instalar usando:

```bash
sudo apt install python3-pip
pip3 --version
```

## Instalação e Configuração do Docker

Instalação do Docker e Docker Compose no Ubuntu 20.04.3 LTS
Aqui está um guia passo a passo para instalar o Docker e o Docker Compose em um sistema Ubuntu 20.04.3 LTS.

1.  Atualize o banco de dados de pacotes e instale dependências pré-requisitadas:

    ```bash
    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```

2.  Adicione a chave GPG oficial do Docker:

    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ```

3.  Adicione a chave GPG oficial do Docker:

    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    ```

4.  Adicione o repositório estável do Docker:

    ```bash
    echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

5.  Atualize o banco de dados de pacotes novamente e instale o Docker Engine:

    ```bash
    sudo apt update
    sudo apt install docker-ce docker-ce-cli containerd.io
    ```

6.  Adicione seu usuário ao grupo docker para executar comandos Docker sem precisar de sudo:

    ```bash
    sudo usermod -aG docker $USER
    Nota: É necessário fazer logout e login novamente ou reiniciar o sistema para aplicar as alterações.
    ```

7.  Verifique se o Docker está instalado corretamente:

    ```bash
    docker --version
    ```

## Instalação e Configuração do Docker Compose

8. Baixe a versão mais recente do Docker Compose:

   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   ```

9. Dê permissão de execução ao Docker Compose:

   ```bash
   sudo chmod +x /usr/local/bin/docker-compose
   ```

10. Verifique se o Docker Compose está instalado corretamente:

    ```bash
    docker-compose --version
    ```

    Agora, você deve ter o Docker e o Docker Compose instalados em seu sistema Ubuntu 20.04.3 LTS. Certifique-se de seguir todos os passos corretamente e verificar as versões para garantir uma instalação bem-sucedida.
