* abre o cmd *

pip install virtualenv

virtualenv .env

.env\Scripts\activate

* instale as dependências que vc quer ou pip install -r requirements.txt *

streamlit run main.py [-- script args]

* após terminar o projeto, crie um arquivo para salvar todas as dependências *
pip freeze > requirements.txt