import string

class Music_Bot:

    def __init__(self):
        self.__prev = ""
        self.__next = ""
        self.__curr = ""
        self.__songs = []
        self.__shuffle_on = False

    '''
    Return the name of the current song playing
    '''
    def get_current_song(self) -> string:
        return self.__curr
    

    '''
    Return the name of the next song to be played
    '''
    def get_next_song(self) -> string:
        return self.__next
    
    '''
    Return the name of the prev song played
    '''
    def get_prev_song(self) -> string:
        return self.__prev
    
    '''
    TODO: implement to handle adding new songs to queue
    '''
    def add_song(self):
        pass

    '''
    TODO: implement to remove song from queue
    '''
    def remove_song(self):
        pass

    '''
    TODO: implement shuffle
    '''
    def shuffle(self):
        pass

    '''
    TODO: implement shuffle_off
    '''
    def shuffle_off(self):
        pass

    '''
    TODO: download requested song
    '''
    def __get_song__(self, name):
        pass
