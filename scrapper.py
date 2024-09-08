from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

# Configuration du dossier de téléchargement
download_folder = "3D models"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Configuration de Selenium et du navigateur (ici Chrome)
chrome_driver_path = "/Applications/chromedriver"  # Remplacez par le chemin correct

# Crée un service Chrome pour spécifier le chemin du driver
chrome_service = Service(executable_path=chrome_driver_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-notifications")

# Initialisation du navigateur Chrome avec le service
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Accès à Sketchfab et recherche du mot clé
search_keyword = "realistic car"
search_url = f"https://sketchfab.com/search?features=downloadable&q={search_keyword.replace(' ', '%20')}"

print("Visite de la page de recherche...")
driver.get(search_url)

# Attendre que la page se charge complètement
wait = WebDriverWait(driver, 10)
try:
    model_links = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='model-title-link']")))
    if not model_links:
        print("Aucun lien de modèle trouvé. Vérifiez le sélecteur XPath.")
    else:
        print(f"{len(model_links)} liens de modèles trouvés.")
except TimeoutException:
    print("Erreur : Temps d'attente dépassé pour trouver les éléments.")
    driver.quit()
    exit()

# Limite le nombre de téléchargements pour cet exemple
max_downloads = 5
download_count = 0

for link in model_links:
    if download_count >= max_downloads:
        break

    model_url = link.get_attribute('href')
    print(f"Traitement du lien: {model_url}")
    driver.get(model_url)

    time.sleep(5)

    try:
        # Ajustez le sélecteur XPath selon la structure actuelle du site
        download_button = driver.find_element(By.XPATH, "//a[contains(@class, 'download-button')]")
        download_button.click()
        download_count += 1

        time.sleep(5)  # Attendre le téléchargement, ajustez si nécessaire

    except Exception as e:
        print(f"Erreur lors du téléchargement de {model_url}: {e}")
        continue

driver.quit()

print(f"Téléchargement terminé : {download_count} modèles ont été téléchargés dans le dossier '{download_folder}'.")
