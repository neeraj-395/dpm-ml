"""
This module provides functionality to visualize the predicted disease probabilities
from a disease prediction model using pie charts. It includes functions for generating
a pie chart and filtering disease probabilities, aggregating diseases with low probabilities
into an 'Other' category.
"""
import io
from typing import Iterable
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
from src.models.dp_model import DiseasePredictModel

matplotlib.use('Agg')


def disease_piechart(__labels: list[str], __probs: list[float]) -> io.BytesIO:
    """
    Return a pie chart ByteIO image to visualize the predicted probabilities of diseases.
    """
    _, ax = plt.subplots()
    explode = [0.1 if x == max(__probs) else 0 for x in __probs]
    ax.pie(__probs, explode=explode, autopct='%1.1f%%',
           shadow=True, startangle=90, textprops={'fontsize': 20})

    plt.axis('equal')
    plt.tight_layout(pad=0)
    plt.legend(__labels, loc='upper left', fontsize=16)
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)
    plt.close()
    return image

def filter_proba(__labels: tuple[str], __probs: Iterable[float],
                 threshold: float) -> tuple[list[str], list[float]]:
    """
    Filters probabilities below a certain threshold into an 'Other' category.
    
    Parameters:
        labels: A list of label names.
        probs: A list of probs corresponding to each labels.
        threshold: The minimum probs required for a disease to remain as a separate category.
    """
    large_probs = [prob for prob in __probs if prob >= threshold]
    large_labels = [__labels[i] for i, val in enumerate(__probs) if val >= threshold]
    large_probs.append(sum(prob for prob in __probs if prob < threshold))
    large_labels.append('Others')

    return large_labels, large_probs

if __name__ == "__main__":
    dpm = DiseasePredictModel()
    probas = dpm.predict_proba(['chills', 'itching', 'skin_rash'])
    if probas is not None and dpm.diseases is not None:
        labels, probs = filter_proba(dpm.diseases, probas, 0.05)
        img_data = disease_piechart(labels, probs)
        Image.open(img_data).show()
