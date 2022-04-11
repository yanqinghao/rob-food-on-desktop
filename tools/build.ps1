python -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements.txt -i https://pypi.org/simple
.venv\Scripts\python -m pip install pyinstaller

.venv\Scripts\pyinstaller --additional-hooks-dir tools/hooks --clean --noconfirm -D run.py -n rob

Compress-Archive "./dist/*" -DestinationPath 'rob.zip'
