# kaggle_projects
Repo for projects from Kaggle website
conda env create -f environment.yml

# TODO:
- [ ] Zdjęcia Satelitarne - yolo transfer learning + simple dataset
    - [ ] do którego folderu który zip trafił
    - [ ] sprytne wczytywanie (https://keras.io/api/preprocessing/image/)
    - [ ] na początek wybrać 1 kategorie (samochody) 
    - [ ] jak yolo rozwiązuje wykrywanie instancji i klasyfikacje instancji
    - [ ] YOLO 5 wersji - docztać czym się różnią (liczba parametrów, funkcjonalność, zmienny rozmiar obrazka?) 
    - [ ] BASELINE MODEL FOR OBJECT DETECTION - byle by było
    - [ ] yolo in keras import transferlearning (wyślij mi linki)
    - [ ] duże obrazki 20kx20k tnij na mniejsze (przygotować skrypt pythonowy) RESEARCH 
    - [ ] format - yolo ma swój format - musisz to sprawdzić czy tu zadziała na tych etykietach
- [ ] jupyter fix
  - zaktualizuj pycharm
- [ ] Cifar do sprawdczenia
  - [x] Zmniejszyliśmy architekture i dziala szybciej i lepiej
  - [ ] można by odpalić z data augmentation (https://www.tensorflow.org/tutorials/images/data_augmentation)
  - [ ] dopisać ealy stopping
  - [ ] callback z zapisywaniem modelu co 5 iteracji
- [ ] ZANIM TO SPRAWDŹ GPU USAGE - Ctr Shift Esc - Install Tensowrlow (https://www.tensorflow.org/install/gpu)
  - [ ] NVIDIA® GPU drivers — CUDA® 11.2 requires 450.80.02 or higher.
  - [ ] CUDA® Toolkit — TensorFlow supports CUDA® 11.2 (TensorFlow >= 2.5.0)
  - [ ] CUPTI ships with the CUDA® Toolkit.
  - [ ] cuDNN SDK 8.1.0 cuDNN versions.


# Questions