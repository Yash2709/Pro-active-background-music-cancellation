from .reader import BaseReader
import os
from pydub import AudioSegment
from pydub.utils import audioop
import numpy as np
from hashlib import sha1

class FileReader(BaseReader):
  def __init__(self, filename):
    self.filename = filename

  def parse_audio(self):
    limit = None

    songname, extension = os.path.splitext(os.path.basename(self.filename))

    try:
      audiofile = AudioSegment.from_file(self.filename)

      if limit:
        audiofile = audiofile[:limit * 1000]

      data = np.fromstring(audiofile._data, np.int16)

      channels = []
      for chn in range(audiofile.channels):
        channels.append(data[chn::audiofile.channels])

      fs = audiofile.frame_rate
    except audioop.error:
      print('audioop.error')
      pass
    return {
      "songname": songname,
      "extension": extension,
      "channels": channels,
      "Fs": audiofile.frame_rate,
      "file_hash": self.parse_file_hash()
    }

