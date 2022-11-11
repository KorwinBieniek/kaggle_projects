# kaggle_projects
Repo for projects from Kaggle website
conda env create -f environment.yml

# TODO 23.03.2022 - simple base line model for object detection in keras - shape detection:
- [X] **przeczytaj tę prezentacje: [Spatial Localization and
Detection - Fei-Fei Li & Andrej Karpathy & Justin Johnson- Stanford Universit](http://cs231n.stanford.edu/slides/2016/winter1516_lecture8.pdf)** 
- [X] zamienić te metryki ious, dist, mse w notebooku `shape_detection.ipynb` na kerasowe metrki albo callbacki
- [X] rozwiązać ten błąd: InternalError: Failed copying input tensor from /job:localhost/replica:0/task:0/device:CPU:0 to /job:localhost/replica:0/task:0/device:GPU:0 in order to run _EagerConst: Dst tensor is not initialized.
- [X] przeczytać bloga https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491
- [X] obczaj jak zrobić wykrwanie dowolnej liczby obiektów
- [X] jak działać z obrazami o różnych rozmiarach
- [x] run yolo demo
- [X] znaleźć zbiór który ma takie same rozmiary i dwie klasy i małe obrazki 

# TODO 20.03.2022 - ogarniecie dota i yolo:
- [X] Zdjęcia Satelitarne - yolo transfer learning + simple dataset
    - [X] do którego folderu który zip trafił
    - [X] sprytne wczytywanie (https://keras.io/api/preprocessing/image/)
    - [X] na początek wybrać 1 kategorie (samochody) 
    - [X] jak yolo rozwiązuje wykrywanie instancji i klasyfikacje instancji
    - [X] YOLO 5 wersji - doczytać czym się różnią (liczba parametrów, funkcjonalność, zmienny rozmiar obrazka?) 
    - [x] BASELINE MODEL FOR OBJECT DETECTION
    - [X] yolo in keras import transferlearning
    - [X] duże obrazki 20kx20k tnij na mniejsze (przygotować skrypt pythonowy) RESEARCH 
    - [X] format - yolo ma swój format - musisz to sprawdzić czy zadziała na tych etykietach
- [X] jupyter fix
  - [X] zaktualizuj pycharm
- [X] Cifar do sprawdczenia
  - [x] Zmniejszyliśmy architekture i dziala szybciej i lepiej
  - [X] można by odpalić z data augmentation (https://www.tensorflow.org/tutorials/images/data_augmentation)
  - [X] dopisać early stopping
  - [X] callback z zapisywaniem modelu co 5 iteracji
- [X] ZANIM TO SPRAWDŹ GPU USAGE - Ctr Shift Esc - Install Tensowrlow (https://www.tensorflow.org/install/gpu)
  - [X] NVIDIA® GPU drivers — CUDA® 11.2 requires 450.80.02 or higher.
  - [X] CUDA® Toolkit — TensorFlow supports CUDA® 11.2 (TensorFlow >= 2.5.0)
  - [X] CUPTI ships with the CUDA® Toolkit.
  - [X] cuDNN SDK 8.1.0 cuDNN versions.


# Questions

# Projects
- [X] Wykrywanie pojazdów, zczytywanie tablic rejestracyjnych i odczytywanie danych na tablicy rejestracyjnej
    - [X] użyć gotowego modelu do wykrywania pojazdów
    - [X] Yolo/OpenCV
    - [X] wykrywanie tablic rejestracyjnych (sieć splotowa)
    - [X] Rozpoznawanie znaków na tablicy rejestracyjnej
- [X] MNIST data recognition
  - [X] Stworzyć 100 danych do nauki (po 10 dla każdej z cyfr)
  - [X] Użyć data augmentation aby manipulować danymi i stworzyć ich wariacje
