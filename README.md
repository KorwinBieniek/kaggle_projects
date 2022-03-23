# kaggle_projects
Repo for projects from Kaggle website
conda env create -f environment.yml

# TODO 23.03.2022 - simple base line model for object detection in keras - shape detection:
- [ ] **dodałem po lekcji - przeczytaj tę prezentacje: [Spatial Localization and
Detection - Fei-Fei Li & Andrej Karpathy & Justin Johnson- Stanford Universit](http://cs231n.stanford.edu/slides/2016/winter1516_lecture8.pdf)** 
- [ ] zamienić te metryki ious, dist, mse w notebooku `shape_detection.ipynb` na kerasowe metrki albo callbacki
- [ ] rozwiązać ten błąd: InternalError: Failed copying input tensor from /job:localhost/replica:0/task:0/device:CPU:0 to /job:localhost/replica:0/task:0/device:GPU:0 in order to run _EagerConst: Dst tensor is not initialized.
- [ ] przeczytać bloga https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491
- [ ] obczaj jak zrobić wykrwanie dowolnej liczby obiektów
- [ ] jak działać z obrazami o różnych rozmiarach
- [ ] run yolo demo
- [ ] znaleźć zbiór który ma takie same rozmiary i dwie klasy i małe obrazki 

# TODO 20.03.2022 - ogarniecie dota i yolo:
- [ ] Zdjęcia Satelitarne - yolo transfer learning + simple dataset
    - [ ] do którego folderu który zip trafił
    - [ ] sprytne wczytywanie (https://keras.io/api/preprocessing/image/)
    - [ ] na początek wybrać 1 kategorie (samochody) 
    - [ ] jak yolo rozwiązuje wykrywanie instancji i klasyfikacje instancji
    - [ ] YOLO 5 wersji - docztać czym się różnią (liczba parametrów, funkcjonalność, zmienny rozmiar obrazka?) 
    - [x] BASELINE MODEL FOR OBJECT DETECTION - byle by było
    - [ ] yolo in keras import transferlearning (wyślij mi linki)
    - [X] duże obrazki 20kx20k tnij na mniejsze (przygotować skrypt pythonowy) RESEARCH 
    - [ ] format - yolo ma swój format - musisz to sprawdzić czy tu zadziała na tych etykietach
- [X] jupyter fix
  - [X] zaktualizuj pycharm
- [X] Cifar do sprawdczenia
  - [x] Zmniejszyliśmy architekture i dziala szybciej i lepiej
  - [X] można by odpalić z data augmentation (https://www.tensorflow.org/tutorials/images/data_augmentation)
  - [X] dopisać ealy stopping
  - [X] callback z zapisywaniem modelu co 5 iteracji
- [X] ZANIM TO SPRAWDŹ GPU USAGE - Ctr Shift Esc - Install Tensowrlow (https://www.tensorflow.org/install/gpu)
  - [X] NVIDIA® GPU drivers — CUDA® 11.2 requires 450.80.02 or higher.
  - [X] CUDA® Toolkit — TensorFlow supports CUDA® 11.2 (TensorFlow >= 2.5.0)
  - [X] CUPTI ships with the CUDA® Toolkit.
  - [X] cuDNN SDK 8.1.0 cuDNN versions.


# Questions

# Projects
- [ ] Wykrywanie pojazdów, zczytywanie tablic rejestracyjnych i odczytywanie danych na tablicy rejestracyjnej
    - [ ] użyć gotowego modelu do wykrywania pojazdów
    - [ ] Yolo/OpenCV
    - [ ] wykrywanie tablic rejestracyjnych (sieć splotowa)
    - [ ] Rozpoznawanie znaków na tablicy rejestracyjnej
- [ ] MNIST data recognition
  - [ ] Stworzyć 100 danych do nauki (po 10 dla każdej z cyfr)
  - [ ] Użyć data augmentation aby manipulować danymi i stworzyć ich wariacje
