git lfs install
git lfs pull
source ./.venv/bin/activate
pip3 install -r requirements.txt --force-reinstall --no-cache-dir
python -m spacy download it_core_news_lg
python -m spacy download es_dep_news_trf
