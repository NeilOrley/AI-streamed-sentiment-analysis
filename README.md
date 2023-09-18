# AI-Streamed-Sentiment-Analysis

Le projet "AI-Streamed-Sentiment-Analysis" est une solution intégrée d'analyse en temps réel destinée à décortiquer et évaluer les sentiments des messages dans un flux Kafka. Utilisant des modèles avancés d'intelligence artificielle basés sur BERT, ce système extrait et analyse le sentiment de chaque message, offrant une compréhension instantanée des tendances émotionnelles des données streamées.

## Caractéristiques

- Analyse en temps réel des messages Kafka
- Utilisation du modèle BERT pour une précision optimale
- Extraction des tendances sentimentales pour une compréhension immédiate
- Configurable pour différents topics Kafka et modèles BERT

## Prérequis

- Python 3.7 ou ultérieur
- Confluent Kafka
- Bibliothèques Python : `confluent_kafka`, `transformers`

## Installation

Tout d'abord, clonez ce dépôt :

```bash
git clone https://github.com/NeilOrley/AI-streamed-sentiment-analysis.git
cd AI-Streamed-Sentiment-Analysis
```

### Utilisation des environnements virtuels (venvs)

L'utilisation d'un environnement virtuel est recommandée pour isoler les dépendances du projet.

Créez un environnement virtuel :

```bash
python -m venv venv
```

Activez l'environnement virtuel :

- Sur macOS et Linux :
  
  ```bash
  source venv/bin/activate
  ```

- Sur Windows :

  ```bash
  .\venv\Scripts\activate
  ```

Installez les dépendances nécessaires :

```bash
pip install -r app/requirements.txt
```

## Configuration

Modifiez le fichier `config.ini` avec vos paramètres Kafka et les chemins de vos modèles BERT.

## Utilisation

Exécutez le script principal :

```bash
python sentiment-analysis.py
```

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Contribution

Les contributions sont les bienvenues ! Assurez-vous de tester vos modifications avant de soumettre une pull request.
Si vous souhaitez contribuer à ce projet, veuillez suivre les étapes suivantes :

1. **Fork** le projet.
2. Créez votre **Feature Branch** (`git checkout -b feature/AmazingFeature`).
3. Commitez vos changements (`git commit -m 'Add some AmazingFeature'`).
4. Poussez dans la **Branch** (`git push origin feature/AmazingFeature`).
5. Ouvrez une **Pull Request**.

## Contact

Pour toute question ou feedback, n'hésitez pas à contacter [Neil Orley](https://github.com/NeilOrley) ou à ouvrir une issue sur ce dépôt.


> ---
>
> _Note : Ce texte a été généré avec l'aide de ChatGPT, un modèle linguistique développé par OpenAI._