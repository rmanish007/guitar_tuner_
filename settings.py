
class Settings:
    """ GuitarTuner global app configuration """

    COMPILED_APP_MODE = False

    """ general settings """
    APP_NAME = "GuitarTuner"
    VERSION = ""
    AUTHOR = "Manish Kumar"
    YEAR = ""

    GITHUB_API_URL = "https://github.com/rmanish007/guitar-tuner"
    GITHUB_URL = "https://github.com/rmanish007/guitar-tuner"
    GITHUB_URL_README = "#"

    STATISTICS_AGREEMENT = f"{APP_NAME} tracks how often the app is being opened.\n\n" + \
                           "Do you agree on sending this anonymous data?"

    USER_SETTINGS_PATH = "/assets/user_settings/user_settings.json"

    ABOUT_TEXT = "{} Version {}  © {} {}".format(APP_NAME, VERSION, YEAR, AUTHOR)
    CF_BUNDLE_IDENTIFIER = "com.{}.{}".format(AUTHOR, APP_NAME)

    WIDTH = 450  # window size when starting the app
    HEIGHT = 440

    MAX_WIDTH = 600  # max window size
    MAX_HEIGHT = 500

    FPS = 60  # canvas update rate
    CANVAS_SIZE = 300  # size of the audio-display

    NEEDLE_BUFFER_LENGTH = 30
    HITS_TILL_NOTE_NUMBER_UPDATE = 15
