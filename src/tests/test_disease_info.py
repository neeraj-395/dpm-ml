"""
Test module of disease info class
"""
from src.utils.disease_info import DiseaseInfo

disease_info = DiseaseInfo()

summary = disease_info.short_summary('Fungal infection')

precations = disease_info.precautions('Fungal infection')

doctor_info = disease_info.doctor_info('Fungal infection')

image_link = disease_info.image_link('Fungal infection')

print(summary)
print(doctor_info)
print(image_link)
print(precations)
