# -*- coding: utf-8 -*-
import googlemaps


class GoogleMapHandler:
    """ Google Map API
    Geocode Service
    Map service """

    def __init__(self, api_key):
        """ Initialisation.
        """
        self.place_name = None
        self.lat = None
        self.lng = None
        self.address = None
        self.g_maps = googlemaps.Client(key=api_key)

    def provide_geocode(self):
        """ Provide latitude & longitude from a place name.
        """

        # Geocode an address
        geocode_data = self.g_maps.geocode(self.place_name)

        # Grab the lat lng
        self.lat = geocode_data[0]['geometry']['location']['lat']
        self.lng = geocode_data[0]['geometry']['location']['lng']

        # Grab the address
        self.address = geocode_data[0]['formatted_address']