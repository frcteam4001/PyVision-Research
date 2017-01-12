import cv2
import numpy
import math
#from enum import Enum

class steamworks_rail:
    """This is a generated class from GRIP.
    To use the pipeline first create a steamworks_rail instance and set the sources,
    next call the process method,
    finally get and use the outputs.
    """
    
    def __init__(self):
        """initializes all values to presets or None if need to be set
        """
        self.__source0 = None
        self.__cv_resize_src = self.__source0
        self.__cv_resize_dsize = (0, 0)
        self.__cv_resize_fx = 1.0
        self.__cv_resize_fy = 1.0
        self.__cv_resize_interpolation = cv2.INTER_LINEAR
        self.cv_resize_output = None

        self.__hsl_threshold_input = self.cv_resize_output
        self.__hsl_threshold_hue = [0.0, 180.0]
        self.__hsl_threshold_saturation = [0.0, 255.0]
        self.__hsl_threshold_luminance = [204.09172661870502, 255.0]
        self.hsl_threshold_output = None

        self.__find_contours_input = self.hsl_threshold_output
        self.__find_contours_external_only = False
        self.find_contours_output = None


    
    def process(self):
        """Runs the pipeline.
        Sets outputs to new values.
        Requires all sources to be set.
        """
        #Step CV_resize0:
        self.__cv_resize_src = self.__source0
        (self.cv_resize_output ) = self.__cv_resize(self.__cv_resize_src, self.__cv_resize_dsize, self.__cv_resize_fx, self.__cv_resize_fy, self.__cv_resize_interpolation)

        #Step HSL_Threshold0:
        self.__hsl_threshold_input = self.cv_resize_output
        (self.hsl_threshold_output ) = self.__hsl_threshold(self.__hsl_threshold_input, self.__hsl_threshold_hue, self.__hsl_threshold_saturation, self.__hsl_threshold_luminance)

        #Step Find_Contours0:
        self.__find_contours_input = self.hsl_threshold_output
        (self.find_contours_output ) = self.__find_contours(self.__find_contours_input, self.__find_contours_external_only)

    def set_source0(self, value):
        """Sets source0 to given value checking for correct type.
        """
        assert isinstance(value, numpy.ndarray) , "Source must be of type numpy.ndarray"
        self.__source0 = value
    


    @staticmethod
    def __cv_resize(src, d_size, fx, fy, interpolation):
        """Resizes an Image.
        Args:
            src: A numpy.ndarray.
            d_size: Size to set the image.
            fx: The scale factor for the x.
            fy: The scale factor for the y.
            interpolation: Opencv enum for the type of interpolation.
        Returns:
            A resized numpy.ndarray.
        """
        return cv2.resize(src, d_size, fx=fx, fy=fy, interpolation=interpolation)

    @staticmethod
    def __hsl_threshold(input, hue, sat, lum):
        """Segment an image based on hue, saturation, and luminance ranges.
        Args:
            input: A BGR numpy.ndarray.
            hue: A list of two numbers the are the min and max hue.
            sat: A list of two numbers the are the min and max saturation.
            lum: A list of two numbers the are the min and max luminance.
        Returns:
            A black and white numpy.ndarray.
        """
        out = cv2.cvtColor(input, cv2.COLOR_BGR2HLS)
        return cv2.inRange(out, (hue[0], lum[0], sat[0]),  (hue[1], lum[1], sat[1]))

    @staticmethod
    def __find_contours(input, external_only):
        """Sets the values of pixels in a binary image to their distance to the nearest black pixel.
        Args:
            input: A numpy.ndarray.
            external_only: A boolean. If true only external contours are found.
        Return:
            A list of numpy.ndarray where each one represents a contour.
        """
        if(external_only):
            mode = cv2.RETR_EXTERNAL
        else:
            mode = cv2.RETR_LIST
        method = cv2.CHAIN_APPROX_SIMPLE
        #im2, contours, hierarchy =cv2.findContours(input, mode=mode, method=method)
        contours, hierarchy =cv2.findContours(input, mode=mode, method=method)
        return contours


