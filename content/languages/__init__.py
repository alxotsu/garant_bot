from models.models import User
from .russian import ru
from .english import en

__all__ = ['get_strings']


def get_strings(language: User.Language):
    return languages[language]


languages = {None: ru, User.Language.ru: ru, User.Language.en: en}
