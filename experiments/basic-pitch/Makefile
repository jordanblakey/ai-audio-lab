install:
	sudo apt install fluidsynth
	uv venv --python=python3.11
	. .venv/bin/activate
	uv pip install -r requirements.txt


basic-pitch:
	. .venv/bin/activate
	basic-pitch . $(FILE)

inference:
	. .venv/bin/activate
	python basic_pitch_inference.py $(FILE)

play-midi:
	. .venv/bin/activate
	python play_midi.py $(FILE)