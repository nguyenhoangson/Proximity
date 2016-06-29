# Wave class, it is simple just a data class

class Wave:

    def __init__(self, frame_rate, data):
        self.data = data # 2D numpy array 
        self.nchannels = len(data[0])
        self.frame_rate = frame_rate
        self.sample_width = data[0].dtype.itemsize # in bytes
        self.nframes = len(data)
        
    def get_data(self):
        return self.data

    def get_nchannels(self):
        return self.nchannels

    def get_frame_rate(self):
        return self.frame_rate

    def get_sample_width(self):
        return self.sample_width

    def get_nframes(self):
        return self.nframes
