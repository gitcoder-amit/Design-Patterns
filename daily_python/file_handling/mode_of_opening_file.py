'''
Mode of opening file :-
    when we open a file  for operations, you have to specify mode. mode specifies the purpose of opening file.There are two type of modes
    1. Text modes
    2. Binary Modes

    Text Mode -> when we open a file  in text modes, python treats it's  content as str type
                when we get data  from a text mode file, python first decodes the raw bytes using either a platform dependent encoding or specified encoding

    Binary Mode -> when we open a file in binary mode, python uses the data without any encoding. Binary mode file    reflects the raw data directly in the file
        Python treats file content  as bytes type. These modes are used  while dealing  with nontext file like images, audios, videos etc
'''